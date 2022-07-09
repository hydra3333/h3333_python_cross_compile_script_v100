## To create a new libOpenCL.a after a new nvidia driver is installed on a Win10x64 PC,  

Do  

In Win10, copy `C:\Windows\System32\OpenCL.dll` to a `vm` (with `mingw` etc installed) into folder `~/Desktop/`  
Then in the Ubuntu machine,    
`cd ~/Desktop`    
`rm -fv OpenCL.def`    
`rm -fv libOpenCL.a`    
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef OpenCL.dll`  
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libOpenCL.a -d OpenCL.def -k -A`  
Copy/upload/commit resulting `libOpenCL.a` and `OpenCL.def` into `sources` folder in the git  
		

In Win10, copy `C:\Windows\System32\vulkan-1.dll` to a `vm` (with `mingw` etc installed) into folder `~/Desktop/`  
Then in the Ubuntu machine,    
`cd ~/Desktop`    
`rm -fv vulkan-1.def`    
`rm -fv libvulkan-1.a`    
`cp -fv vulkan-1.dll vulkan.dll`
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef vulkan-1.dll`
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libvulkan-1.a -d vulkan-1.def -k -A`
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef vulkan.dll`
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libvulkan.a -d vulkan.def -k -A`
Copy/upload/commit resulting `libvulkan-1.a` and `vulkan-1.def` into `sources` folder in the git  
Copy/upload/commit resulting `libvulkan.a` and `vulkan.def` into `sources` folder in the git  