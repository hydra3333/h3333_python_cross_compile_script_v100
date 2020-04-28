## To create a new libOpenCL.a after a new nvidia driver is installed on a Win10x64 PC,  

###1. Copy `C:\Windows\System32\OpenCL.dll` to a `vm` with `mingw` etc installed into folder `~/Desktop/OpenCL/`  
###2. `/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef OpenCL.dll`  
###3. `/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libOpenCL.a -d OpenCL.def -k -A`  
###4. Copy/upload/commit resulting `libOpenCL.a` and `libOpenCL.def` into `sources` folder in the git  
		
