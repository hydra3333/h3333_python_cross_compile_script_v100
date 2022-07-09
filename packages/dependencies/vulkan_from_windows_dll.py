{
	'repo_type' : 'none',
	'folder_name' : 'vulkan_from_windows_dll',
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	#'run_pre_depends_on' : [
	'run_post_regexreplace' : [
		#'echo ""',
		#'ls -al',
		#'rm -fv "./OpenCL.dll ./libOpenCL.a ./OpenCL.def ./already_ran_make_install"',
		#'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/OpenCL.dll?raw=true" --retry 50 -L --output "./OpenCL.dll"',
		#'ls -al',
		#'echo "1. cross_prefix_full={cross_prefix_full}"',
		#'echo "2. cross_prefix_bare={cross_prefix_bare}"',
		#'echo "3. mingw_binpath={mingw_binpath}"',
		#'ls -al "{mingw_binpath}"',
		#'echo ""',
		#'ls -al "{cross_prefix_full}dlltool"',
		#'ls -al "{mingw_binpath}/gendef"',
		#'echo ""',
		#'{mingw_binpath}/gendef OpenCL.dll',
		#'echo ""',
		#'{cross_prefix_full}dlltool -l libOpenCL.a -d OpenCL.def -k -A',
		#'echo ""',
		#'ls -al',
		'echo ""',
		'rm -fv "./already_ran_make_install"',
		#'rm -fv "{target_prefix}/lib/pkgconfig/OpenCL.pc "',
		#'rm -fv "{target_prefix}/lib/pkgconfig/vulkan-1.pc "',
		#'rm -fv "{target_prefix}/lib/pkgconfig/vulkan.pc "',
		'echo ""',
		'rm -fv "./OpenCL.dll ./libOpenCL.a ./OpenCL.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/OpenCL.def?raw=true" --retry 50 -L --output "./OpenCL.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/libOpenCL.a?raw=true" --retry 50 -L --output "./libOpenCL.a"',
		'cp -fv "libOpenCL.a" "{target_prefix}/lib/libOpenCL.a"',     # 2020.04.28
		'cp -fv "libOpenCL.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2020.04.28
		'echo ""',
		'rm -fv "./vulkan-1.dll ./libvulkan-1.a ./vulkan-1.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/vulkan-1.def?raw=true" --retry 50 -L --output "./vulkan-1.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/libvulkan-1.a?raw=true" --retry 50 -L --output "./libvulkan-1.a"',
		'cp -fv "libvulkan-1.a" "{target_prefix}/lib/libvulkan-1.a"',     # 2022.07.09
		'cp -fv "libvulkan-1.a" "{target_prefix}/lib/libvulkan-1.dll.a"', # 2022.07.09
		'echo ""',
		'rm -fv "./vulkan.dll ./libvulkan.a ./vulkan.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/vulkan.def?raw=true" --retry 50 -L --output "./vulkan.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/libvulkan.a?raw=true" --retry 50 -L --output "./libvulkan.a"',
		'cp -fv "libvulkan.a" "{target_prefix}/lib/libvulkan.a"',     # 2022.07.09
		'cp -fv "libvulkan.a" "{target_prefix}/lib/libvulkan.dll.a"', # 2022.07.09
		'echo ""',
		'echo ""',
		'echo "To create a new libOpenCL.a and libvulkan.a etc after a new nvidia driver is installed or windows is updated on a Win10x64 PC,"',
		'echo "refer the readme in https://github.com/hydra3333/h3333_python_cross_compile_script_v100/tree/master/sources"',
		'echo ""',
		'echo ""',
		'touch already_ran_make_install',
	],
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', ], # MABS/DEADSIX27 - VULKAN depends only on these
	'_info' : { 'version' : 'windows/system32/vulkan-1.dll', 'fancy_name' : 'vulkan_from_windows_dll' }, # 2020.04.28
}
