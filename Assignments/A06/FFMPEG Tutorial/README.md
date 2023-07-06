
FFmpeg is a powerful command-line tool for manipulating and converting audio and video files. In this tutorial, we will explore various commands and options to perform common tasks using FFmpeg.

To get basic help, you can use the following commands:
```
ffmpeg -? or ffmpeg -h
```

For more specific help on a particular topic, such as decoding FLV files, you can use:
```
ffmpeg -h decoder=flv
```

Here are some commonly used commands for different tasks:

**1. Available Codecs:**
To view the available codecs, use the command:
```
ffmpeg -codecs
```

**2. Available Decoders:**
To list the available decoders, use the command:
```
ffmpeg -decoders
```

**3. Available Filters:**
To see the available filters, use the command:
```
ffmpeg -filters
```

**4. Available Formats:**
To get a list of available formats, use the command:
```
ffmpeg -formats
```

**5. Available Pixel Formats:**
To view the available pixel formats, use the command:
```
ffmpeg -pix_fmts
```

**6. Available Protocols:**
To list the available protocols, use the command:
```
ffmpeg -protocols
```

**7. Setting FPS (Frames Per Second):**
To set the frame rate of a video, use the following command:
```
ffmpeg -i input -r fps output
ffmpeg -i clip.mpg -vf fps=fps=25 clip.webm
```

**8. Setting Bitrate:**
To set the bitrate of a video, use the following command:
```
ffmpeg -i film.avi -b 1.5M film.mp4
```

**9. Setting Maximum Size of Output File:**
To limit the output file size, use the command:
```
ffmpeg -i input.avi -fs 10MB output.mp4
```

**10. Resizing Video:**
To resize a video, use the command:
```
ffmpeg -i input_file -s 320x240 output_file
```

**11. Special Enlarging Filter:**
To apply a special enlarging filter, use the command:
```
ffmpeg -i phone_video.3gp -vf super2xsai output.mp4
```

**12. Cropping Frame Center:**
To crop the center of a video frame, use the command:
```
ffmpeg -i input.avi -vf crop=iw/2:ih/2 output.avi
```

**13. Padding Video/Image:**
To add padding to a video or image, use the command:
```
ffmpeg -i photo.jpg -vf pad=860:660:30:30:pink framed_photo.jpg
```

**14. Flipping and Rotating Video:**
To flip or rotate a video, use the following commands:
```
Flip:
ffmpeg -i input -vf vflip output

Rotate:
ffmpeg -i input -vf transpose=0 output
```

**15. Overlaying Images or Videos:**
To overlay an image or video onto another, use the command:
```
ffmpeg -i pair.mp4 -i logo.png -filter_complex overlay pair1.mp4
```
You can also specify the position of the overlay using `overlay=x:y` or `overlay=W-w:H-h`.

**16. Adding Text:**
To add text to a video, use the command:
```
ffmpeg -i input -vf drawtext=fontfile=arial.ttf:text=Welcome:fontcolor=green:fontsize=30 output
```

**17. Converting Videos:**
To

convert a video from one format to another, specify the video and audio codecs using the following command:
```
ffmpeg -i input.mp4 -c:v video_codec -c:a audio_codec output.mp4
```
For example:
```
ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4
```

**18. Cropping a Particular Time Range:**
To extract a specific time range from a video, use the command:
```
ffmpeg -i video.mpg -ss start_time -t duration output.mpg
```
For example:
```
ffmpeg -i myvid.mp4 -ss 480 -t 180 -c copy -map 0 finalvid.mp4
```

**19. Converting Video to Frames:**
To extract frames from a video, use the command:
```
ffmpeg -i input.mp4 output_%03d.jpg
```

**20. Converting Frames to Video:**
To convert frames to a video, use the command:
```
ffmpeg -framerate 30 -i input_%03d.jpg -c:v libx264 -r 30 output.mp4
```
You can also add audio to the video using the `-i audio.mp3` option.

These are just a few examples of what you can do with FFmpeg. It is a versatile tool with numerous options and capabilities for audio and video manipulation. Experiment with different commands and explore the FFmpeg documentation for more advanced usage.

---

I hope this improved version of the FFmpeg tutorial helps you better understand and utilize the various commands and options available.
