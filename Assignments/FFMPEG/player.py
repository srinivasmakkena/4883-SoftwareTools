import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel
from PyQt5.QtCore import Qt, QProcess, QUrl
from PyQt5.QtGui import QIcon

class VideoPlayerWindow(QMainWindow):
    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.setWindowTitle('Video Player')

        self.play_button = QPushButton(self)
        self.play_button.setIcon(QIcon('play.png'))
        self.play_button.clicked.connect(self.toggle_playback)

        self.seek_slider = QSlider(Qt.Horizontal, self)
        self.seek_slider.sliderMoved.connect(self.seek)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.play_button)
        layout.addWidget(self.seek_slider)
        layout.addWidget(self.time_label)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.process_output)
        self.process.start('ffplay', ['-i', self.video_path, '-noborder', '-window_title', 'Video Player'])

    def toggle_playback(self):
        self.process.write('p'.encode())

    def seek(self, position):
        duration = self.get_video_duration()
        seek_time = int((position / 100) * duration)
        self.process.write(f'{seek_time}\n'.encode())

    def process_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        if 'time=' in output:
            time_index = output.index('time=')
            time_str = output[time_index+5:time_index+13].strip()
            self.time_label.setText(time_str)

    def get_video_duration(self):
        self.process.write('q'.encode())
        self.process.waitForFinished()
        output = self.process.readAllStandardOutput().data().decode()
        duration_index = output.index('Duration:')
        duration_str = output[duration_index+10:duration_index+21].strip()
        hh, mm, ss = map(float, duration_str.split(':'))
        duration = int(hh * 3600 + mm * 60 + ss)
        self.process.start('ffplay', ['-i', self.video_path, '-noborder', '-window_title', 'Video Player'])
        return duration

    def closeEvent(self, event):
        self.process.kill()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    video_path = "D://Movies//Awtel embed source openload  Embed Streaming Videos.mp4"
    window = VideoPlayerWindow(video_path)
    window.show()
    sys.exit(app.exec_())
