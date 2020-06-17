## THIS SCRIPT MAY NOT WORK  
(mainly due to upstream dependencies changing regularly)  
Consider using deadsix27's at https://github.com/DeadSix27/python_cross_compile_script ... although that has ceased active maintenance.  
Or, maybe use MABS https://github.com/m-ab-s/media-autobuild_suite if you don't mind installing stuff in your nice Win10 PC.  

### A Linux to Windows x64 cross-compile script to build ffmpeg with dependencies  

A fork of DeadSix27's fantastic work to build a 64-bit STATIC ffmpeg.exe with lots of ffmpeg dependencies and have the ffmpeg.exe run in a Windows 10 64-bit o/s.  
... based on deadsix27 fine work at https://github.com/DeadSix27/python_cross_compile_script  

NOTE: attempt to build everything wherever possible with safety settings
```
          -O3  -fstack-protector-all  -D_FORTIFY_SOURCE=2
```

This script attempts to build 
```
ffmpeg.exe (64-bit, static) with and Vapoursynth input and OpenCL (eg to use with nvidia) and multibit h264/h265
ffprobe.exe (64-bit, static)
mediainfo.exe
x264.exe (multibit) with extra input/outout media container types eg mpg
x265.exe (multibit)
mp4box.exe
vpx encoder/decoder
aom-av1 encoder/decoder
dav1d av1 video decoder
sox audio processor
libaacs.dll (with dependent its libgcrypt*.dll and libgpg_error.dll) (never tried to run it though)
```

**Now with ```docker``` (perhaps it'd work).**  

Athough - I got sick of docker and haven't tried to use it in ages.  

Perhaps instead use the above with Ubuntu in HyperV (it has some issues) or in VMWare etc.  

The below will probably not work, now.  

In the folder ```/docker/app``` are instructions for attempting to build and use a docker image,
so that ffmpeg can be repeatably built easily in a disposable/re-usable docker container.  
It's a tad convoluted, mainly because the standard ```docker build``` command 
using a ```Dockerfile``` doesn't accept tty input which some of the dependency 
installs depend on, thus we use another way (```commit```) to build basic docker images.   

