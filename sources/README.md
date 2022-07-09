## To create a new libOpenCL.a and libvulkan-1.a and libvulkan.a   

To create your own new static `libOpenCL.a` wrapper after a new nvidia driver with OpenCL.dll is installed on a Win10x64 PC,
and a new `libvulkan.a` wrapper after microsoft updates install a new vulkan dll, which you can upload into in your own fork, please see below   
since this method is used in this git, rather than building those OpenCL and vulkan_loader from source.   

NOTE 1: we do it this way because khronos frequently updated stuff which then frequently broke building ffmpeg; Nvidia and Microsoft keep these updated reasonably frequently.   

Note 2: the static ffmpeg built with these will rely on OpenCL.dll and vulkan-1.dll being installed in `C:\Windows\System32\` 
on the target Win10x64 PC ... which they will be, automatically by Nvidia and Microsoft provided that 
you regularly install the latest Nvidia drivers and regularly do Microsoft `Check for Updates`.

So,   

Ensure the Ubuntu VM has `mingw64` etc installed and its bin is perhaps `/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/`.   

In Win10x64, copy `C:\Windows\System32\OpenCL.dll` to the Ubuntu VM into folder `~/Desktop`   
Then in a terminal window the Ubuntu VM,    
`cd ~/Desktop`    
`rm -fv OpenCL.def`    
`rm -fv libOpenCL.a`    
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef OpenCL.dll`  
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libOpenCL.a -d OpenCL.def -k -A`  
Finally, copy/upload/commit the resulting `libOpenCL.a` and `OpenCL.def` into `sources` folder in your forked git   
		

In Win10, copy `C:\Windows\System32\vulkan-1.dll` to the Ubuntu VM into folder `~/Desktop`   
Then in the Ubuntu machine,    
`cd ~/Desktop`    
`rm -fv vulkan-1.def vulkan.def`    
`rm -fv libvulkan-1.a libvulkan.a`    
`rm -fv vulkan.dll`    
`cp -fv vulkan-1.dll vulkan.dll`   
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef vulkan-1.dll`   
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libvulkan-1.a -d vulkan-1.def -k -A`   
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef vulkan.dll`   
`/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libvulkan.a -d vulkan.def -k -A`   
Finally,   
Copy/upload/commit resulting `libvulkan-1.a` and `vulkan-1.def` into `sources` folder in your forked git   
Copy/upload/commit resulting `libvulkan.a` and `vulkan.def` into `sources` folder in your forked git   