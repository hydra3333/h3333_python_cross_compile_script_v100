@ECHO ON
copy /B /V /Z /Y "C:\Windows\System32\OpenCL.dll" "./"
copy /B /V /Z /Y "C:\Windows\System32\vulkan-1.dll" "./"
dir 
PAUSE
EXIT

REM After copying the .dll files to Linux:

/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef OpenCL.dll
/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libOpenCL.a -d OpenCL.def -k -A
#
cp -fv vulkan-1.dll vulkan.dll
/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef vulkan-1.dll
/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libvulkan-1.a -d vulkan-1.def -k -A
/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef vulkan.dll
/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libvulkan.a -d vulkan.def -k -A
