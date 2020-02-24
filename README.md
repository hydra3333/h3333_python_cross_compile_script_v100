# DO NOT USE THIS PROJECT - IT USUALLY DOES NOT WORK
# Instead, use deadsix27's at 
https://github.com/DeadSix27/python_cross_compile_script

A v100 fork of DeadSix27's work to build 64-bit STATIC ffmpeg.exe with lots of ffmpeg dependencies and have the ffmpeg.exe run in a Windows 10 64-bit o/s

based on deadsix27 fine work at https://github.com/DeadSix27/python_cross_compile_script

NOTE: attempt to build everything wherever possible with safety settings
```
          -O3  -fstack-protector-all  -D_FORTIFY_SOURCE=2
```

** Now with ```docker```.**  
In the folder ```/docker/app``` are instructions for attempting to build and use a docker image,
so that ffmpeg can be repeatably built easily in a disposable/re-usable docker container.  
It's a tad convoluted, mainly because the standard ```docker build``` command 
using a ```Dockerfile``` doesn't accept tty input which some of the dependency 
installs depend on, thus we use another way (```commit```) to build basic docker images.   


Some day this script will build 
```
ffmpeg.exe (64-bit, static) with OpenCL (eg to use with nvidia) and multibit h264/h265
ffprobe.exe (64-bit, static)
mediainfo.exe
x264.exe (multibit) with extra input/outout media container types eg mpg
x265.exe (multibit)
mp4box.exe
vpx encoder/decoder
aom-av1 encoder/decoder
dav1d av1 video decoder
sox audio processor
```

