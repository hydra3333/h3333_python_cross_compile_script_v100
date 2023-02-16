#### DO NOT RELY ON THIS GIT CONTENT TO SATISFY ANY AND/OR ALL OF YOUR PERCEIVED OR ACTUAL NEEDS.

### THIS SCRIPT WILL PROBABLY NOT WORK !   

#### EXPRESSLY: DO NOT RELY ON NOR USE ANY OF THE CONTENTS OF THIS GIT

IN ADDITION TO ANY OTHER LICENSE CONDITIONS AND AT THE SAME TIME SPECIFICALLY 
NOT NEGATING NOR REDUCING IN ANY WAY WHATSOEVERY ANY OTHER LICENCE 
CONDITIONS WHICH MAY LIMIT INCREASE IN LIABILITY BY ME AND/OR REDUCE
INDEMNIFICATION OF ME:    
THERE IS ZERO LIABILITY BY ME EXPRESS OR IMPLIED, UNDER ANY THEORY, 
ARISING FROM ANY AND ALL MATTERS IN RELATION THIS GIT CONTENTS AND
ANY THING OR EVENT OR FEELING OR OUTCOME IN RELATION TO THIS GIT CONTENTS
EITHER IN THE PAST OR AT PRESENT OR IN THE FUTURE;    
ZERO WARRANTY AND/OR SUPPORT IS PROVIDED AT ANY TIME MEANING THAT
YOU HAVE ZERO ENTITLEMENT TO WARRANTY AND/OR SUPPORT EITHER EXPLICIT AND/OR IMPLIED;    
IF YOU DO USE ANY OF THE CONTENTS OF THIS GIT IN ANY WAY THEN YOU AGREE
THAT IT IS ENTIRELY AND COMPLETELY AT YOUR OWN RISK IN EVERY 
CIRCUMSTANCE AND IN EVERY JURISDICTION AND UNDER ANY THEORY;    
IF YOU DO USE ANY OF THE CONTENTS OF THIS GIT IN ANY WAY THEN YOU AGREE
TO INDEMNIFY ALL PERSONS ASSOCIATED WITH THIS GIT CONTENTS AGAINST ANY EVENT
AND/OR LOSS AND/OR ACTION IN ANY AND/OR EVERY WAY WHICH MAY BE ASSOCIATED 
WITH THIS GIT CONTENTS AND/OR ITS USE WHETHER BY YOU AND/OR 
ANY AND/OR ALL PARTIES WHICH MAY USE DERIVATIVES OF
OF THE CONTENTS OF THIS GIT IN ANY AND/OR ALL WAYS AND THAT SUCH 
INDEMNIFICATION SHALL BE WITHOUT LIMIT.    

YOU EXPLICITLY AGREE THAT SHOULD THE WORDING OF CONDITIONS STATED HERE
AND/OR IN THE LICENSE AND/OR ANYWHERE IN THIS GIT BE AMBIGUOUS AND/OR
INDICATE OR IMPLY OR BE FOUND THAT MY LIABILITY IS INCREASED ABOVE ZERO
AND/OR CLAUSES BENEFICIAL TO ME BECOME WITHOUT EFFECT AND/OR
INDEMNIFICATION OF ME BY YOU IS REDUCED IN ANY AND/OR ALL WAYS THEN
IN ANY AND ALL CIRCUMSTANCES ANY AND ALL LIABILITY BY ME SHALL
BE ZERO AND INDEMNIFICATION OF ME BY YOU SHALL BE WITHOUT LIMIT IN 
EVERY JURISDICTION AND UNDER ANY THEORY.    

YOU ALSO AGREE THAT AT ALL TIMES AND IN ALL CIRCUMSTANCES IN EVERY JURISDICTION AND 
UNDER ANY THEORY THE LICENSE FILE SHALL BE IN EFFECT AND
THE LICENSE FILE SHALL BE A MINIMUM POSITION BEYOND WHICH LIABILITY BY ME
CAN NEVER BE INCREASED AND INDEMNIFICATION OF ME CANNOT BE REDUCED;    
FURTHER, ALL LIABILITY BY ME CAN NEVER BE ABOVE ZERO AND YOUR INDEMNIFICATION OF ME
CANNOT BE REDUCED REGARDLESS OF ANY MATERIAL EXPLICIT OR IMPLIED IN THIS GIT CONTENTS.

Consider using deadsix27's at https://github.com/DeadSix27/python_cross_compile_script ... although that has ceased active maintenance.  

Or, preferably use MABS https://github.com/m-ab-s/media-autobuild_suite   
... update: MABS works really well under Windows Sandbox and doesn't leave stuff on your PC - you can copy results from the Sandbox to your PC before closing the sandbox.   
... perhaps see https://github.com/m-ab-s/media-autobuild_suite/issues/2227 for draft-only sample .wsb and whatnot

Or, use rdp's loverly build system https://github.com/rdp/ffmpeg-windows-build-helpers


### A Linux to Windows x64 cross-compile script to build ffmpeg with dependencies   
#### i.e. NVidia's NVENC encoder, OpenCL filters, and Vapoursynth input

NOTE: You may attempt to build everything wherever possible with safety settings
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

0. Probably fork your own `https://github.com/hydra3333/h3333_python_cross_compile_script_v100.git` and then change a small number of things in .py files to point to your fork   
1. Create an Ubuntu VM (tested with 20.04+)   
2. login into ubuntu and start a Terminal window   
```
sudo apt -y install git
cd ~/Desktop
sudo chmod +777 -R ./*
sudo rm -vfR ./h3333_python_cross_compile_script_v100
git clone https://github.com/hydra3333/h3333_python_cross_compile_script_v100.git # or your fork
cp -fv ./h3333_python_cross_compile_script_v100/*.sh ./
sudo chmod +777 -R ./*
./h3333_v100.setup.sh # (once-off, before the first build)
```
then to build just ffmpeg:    
3. `./h3333_v100.003_ff.sh`    
or to build everything:    
4. `./h3333_v100.003.sh`    
5. To create your own new static `libOpenCL.a` wrapper after a new nvidia driver with OpenCL.dll is installed on a Win10x64 PC,
and a new `libvulkan-1.a` wrapper after microsoft updates install a new vulkan dll, so you can upload these into in your own fork, please see:  
`https://github.com/hydra3333/h3333_python_cross_compile_script_v100/tree/master/sources`   
since this method is used here, rather than building those OpenCL and vulkan_loader from source.   
NOTE: we do it this way because khronos frequently updated stuff which then frequently broke building ffmpeg; Nvidia and Microsoft keep these updated reasonably frequently.   


Good luck.

