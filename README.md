## THIS SCRIPT MAY NOT WORK  
(mainly due to upstream dependencies changing regularly)  
Consider using deadsix27's at https://github.com/DeadSix27/python_cross_compile_script ... although that has ceased active maintenance.  
Or, maybe use MABS https://github.com/m-ab-s/media-autobuild_suite if you don't mind installing stuff in your nice Win10 PC.  

### A Linux to Windows x64 cross-compile script to build ffmpeg with dependencies   
#### i.e. NVidia's NVENC encoder, OpenCL filters, and Vapoursynth input

A fork of DeadSix27's fantastic work to build a 64-bit STATIC ffmpeg.exe with lots of ffmpeg dependencies and have the ffmpeg.exe run in a Windows 10 64-bit o/s.  
... based on deadsix27 fine work at https://github.com/DeadSix27/python_cross_compile_script  

NOTE: attempt to build everything wherever possible with safety settings
```
          -O3  -fstack-protector-all  -D_FORTIFY_SOURCE=2
```

This script attempts to build (eveything 64 bit) ffmpeg, primarily in order to utilise eg NVidia's NVENC encoder, optionally some OpenCL filters, and optional Vapoursynth input.

```
ffmpeg.exe (64-bit, static) with and Vapoursynth input and OpenCL (eg to use with nvidia) and multibit h264/h265
ffprobe.exe (64-bit, static)
mediainfo.exe (64-bit, static)
x264.exe (multibit) with extra input/output media container types eg mpg (64-bit, static)
x265.exe (multibit) (64-bit, static)
mp4box.exe (64-bit, static)
vpx encoder/decoder (64-bit, static)
aom-av1 encoder/decoder (64-bit, static)
dav1d av1 video decoder (64-bit, static)
sox audio processor (64-bit, static)
fftw*.dll 3.3.8 (64-bit)
libaacs.dll (64-bit)(with its libgcrypt*.dll and libgpg_error.dll) (never tried to run it though)
```

### How to build ?

1. Create an Ubuntu VM (tested with 20.04)   
2. login into ubuntu and start a Terminal window   
```
sudo apt -y install git
cd ~/Desktop
sudo rm -vfR ./h3333_python_cross_compile_script_v100
git clone https://github.com/hydra3333/h3333_python_cross_compile_script_v100.git
cp -fv ./h3333_python_cross_compile_script_v100/*.sh ./
chmod +777 *.sh
./h3333_v100.setup.sh # (once-off, before the first build)
```
then to build just ffmpeg:    
3. `./h3333_v100.001_ff.sh
or to build everything:    
4. `./h3333_v100.001.sh 

Good luck.

**Now with ```docker``` (perhaps it'd work).**  

Athough - I got sick of docker and haven't tried to use it in ages.  

Perhaps instead use the above with Ubuntu in HyperV (it has some issues) or in VMWare etc.  

The below will probably not work, now.  

In the folder ```/docker/app``` are instructions for attempting to build and use a docker image,
so that ffmpeg can be repeatably built easily in a disposable/re-usable docker container.  
It's a tad convoluted, mainly because the standard ```docker build``` command 
using a ```Dockerfile``` doesn't accept tty input which some of the dependency 
installs depend on, thus we use another way (```commit```) to build basic docker images.   

