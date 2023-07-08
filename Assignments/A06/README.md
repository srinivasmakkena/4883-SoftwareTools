# FFmpeg Presentation

## Srinivas Makkena

## Introduction

FFmpeg is a powerful command-line tool used for manipulating and converting audio and video files. In this tutorial, we will explore various commands and options to perform common tasks using FFmpeg.

| File/Folder                                                     | Description                                          |
| --------------------------------------------------------------- | ---------------------------------------------------- |
| [YTDownloader](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/tree/main/Assignments/A06/ytdownloader)         | Contains YouTube Downloader Django Project           |
| [FFMPEG Tutorial](https://github.com/srinivasmakkena/4883-SoftwareTools-Makkena/tree/main/Assignments/A06/FFMPEG%20Tutorial) | Contains Examples of FFmpeg Commands and Tutorials   |

## Prerequisites

Before you begin, make sure you have FFmpeg installed on your system. If you don't have it installed, you can follow these instructions to download and install it:

1. Visit the FFmpeg website at [ffmpeg.org](https://ffmpeg.org/) and navigate to the download section.

2. Choose the appropriate version of FFmpeg for your operating system.

3. Download the FFmpeg package and extract it to a directory on your computer.

4. Add the FFmpeg directory to your system's PATH environment variable. This step is important to be able to run FFmpeg from any location in the command prompt or terminal.

   - **Windows:** Open the system's **Environment Variables** settings. Under **System Variables**, find the **Path** variable and click **Edit**. Add the path to the FFmpeg directory (e.g., `C:\ffmpeg\bin`) to the list of paths. Click **OK** to save the changes.

   - **Linux/macOS:** Open a terminal window and navigate to your home directory. Open the `.bashrc` or `.bash_profile` file using a text editor. Add the following line at the end of the file, replacing `/path/to/ffmpeg` with the actual path to the FFmpeg directory:

     ```shell
     export PATH="/path/to/ffmpeg:$PATH"
     ```

     Save the file and run the following command in the terminal to apply the changes:

     ```shell
     source ~/.bashrc
     ```

     or

     ```shell
     source ~/.bash_profile
     ```

## Getting Started

To verify that FFmpeg is installed correctly and accessible from the command line, open a new terminal or command prompt window and run the following command:

```shell
ffmpeg -version
```

If FFmpeg is properly installed and added to your system's PATH, you should see the version information displayed in the terminal.

By following these instructions, you will be able to download and install FFmpeg on your system, add it to your system's PATH, and verify its installation. Once set up, you can proceed with using the FFmpeg commands to manipulate and convert audio and video files.# FFmpeg Presentation

To start using FFmpeg, you can execute the following command to get basic help:

```shell
ffmpeg -h
```

For more specific help on a particular topic, such as decoding FLV files, you can use:

```shell
ffmpeg -h decoder=flv
```

## Commonly Used Commands

Here are some commonly used commands for different tasks:

**1. Available Codecs:**

To view the available codecs, use the command:

```shell
ffmpeg -codecs
```

**2. Available Decoders:**

To list the available decoders, use the command:

```shell
ffmpeg -decoders
```

**3. Available Filters:**

To see the available filters, use the command:

```shell
ffmpeg -filters
```

**4. Available Formats:**

To get a list of available formats, use the command:

```shell
ffmpeg -formats
```

**5. Available Pixel Formats:**

To view the available pixel formats, use the command:

```shell
ffmpeg -pix_fmts
```

**6. Available Protocols:**

To list the available protocols, use the command:

```shell
ffmpeg -protocols
```

**7. Setting FPS (Frames Per Second):**

To set the frame rate of a video, use the following command:

```shell
ffmpeg -i input -r fps output
```

For example:

```shell
ffmpeg -i clip.mpg -vf fps=fps=25 clip.webm
```

**8. Setting Bitrate:**

To set the bitrate of a video, use the following command:

```shell
ffmpeg -i film.avi -b 1.5M film.mp4
```

**9. Setting Maximum Size of Output File:**

To limit the output file size, use the command:

```shell
ffmpeg -i input.avi -fs 10MB output.mp4
```

**10. Resizing Video:**

To resize a video, use the command:

```shell
ffmpeg -i input_file -s 320x240 output_file
```

**11. Special Enlarging Filter:**

To apply a special enlarging filter, use the command:

```shell
ffmpeg -i phone_video.3gp -vf super2xsai output.mp4
```

**12. Cropping Frame Center:**

To crop the center of a video frame, use the command:

```shell
ffmpeg -i input.avi -vf crop=iw/2:ih/2 output.avi
```

**13. Padding Video/Image:**

To add padding to a video or image, use the command:

```shell
ffmpeg -i photo.jpg -vf pad=860:660:30:30:pink framed_photo.jpg
```

**14. Flipping and Rotating Video:**

To flip or rotate a video, use the following commands:

Flip:

```shell
ffmpeg -i input -vf vflip output
```

Rotate:

```shell
ffmpeg -i input -vf transpose=0 output
```

**15. Overlaying Images or Videos:**

To overlay an image or video onto another, use the command:

```shell
ffmpeg -i pair.mp4 -i logo.png -filter_complex overlay pair1.mp4
```

You can also specify the position of the overlay using `overlay=x:y` or `overlay=W-w:H-h`.

**16. Adding Text:**

To add text to a video, use the command:

```shell
ffmpeg -i input -vf drawtext=fontfile=arial.ttf:text=Welcome:fontcolor=green:fontsize=30 output
```

**17. Converting Videos:**

To convert a video from one format to another, specify the video and audio codecs using the following command:

```shell
ffmpeg -i input.mp4 -c:v video_codec -c:a audio_codec output.mp4
```

For example:

```shell
ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4
```

**18. Cropping a Particular Time Range:**

To extract a specific time range from a video, use the command:

```shell
ffmpeg -i video.mpg -ss start_time -t duration output.mpg
```

For example:

```shell
ffmpeg -i myvid.mp4 -ss 480 -t 180 -c copy -map 0 finalvid.mp4
```

**19. Converting Video to Frames:**

To extract frames from a video, use the command:

```shell
ffmpeg -i input.mp4 output_%03d.jpg
```

**20. Converting Frames to Video:**

To convert frames to a video, use the command:

```shell
ffmpeg -framerate 30 -i input_%03d.jpg -c:v libx264 -r 30 output.mp4
```

You can also add audio to the video using the `-i audio.mp3` option.

## Additional Resources

For more advanced usage and a comprehensive list of FFmpeg options, refer to the official FFmpeg documentation. If you need more commands or examples, they are available inside the FFmpeg tutorial folder. Additionally, the YouTube downloader used in this presentation was developed using the Django framework, and the requirements file is attached for your reference.

Explore and experiment with different commands to unlock the full potential of FFmpeg for audio and video manipulation.

