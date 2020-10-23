{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'depth_git' : 0,
	'needs_make_install' : True,
	'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options': 
		'.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} ' # note '..' sinxce we're in a subfolder
		'-DOPENCL_ICD_LOADER_HEADERS_DIR={target_prefix}/lib ' # 2020.10.23
		'-DCMAKE_BUILD_TYPE=Release '
		'-DBUILD_SHARED_LIBS=ON '
		'-DBUILD_TESTING=OFF '
		'-DOPENCL_ICD_LOADER_DISABLE_OPENCLON12=ON ' # build only symbols per https://github.com/KhronosGroup/OpenCL-ICD-Loader/commit/bb98ad9a9c264d63ad2204c1eeee0a3a1e724e20 
		'-DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF '
	,
	'run_pre_patch' : [ # this runs before descending into 'source_subfolder'
		'cp -fv "CMakeLists.txt" "CMakeLists.txt.orig"',
		# Config.cmake.in does not already exist
		'cp -fv "loader/windows/icd_windows_hkr.c" "loader/windows/icd_windows_hkr.c.orig"',
		'cp -fv "test/loader_test/test_create_calls.c" "test/loader_test/test_create_calls.c.orig"',
		'cp -fv "test/loader_test/test_program_objects.c" "test/loader_test/test_program_objects.c.orig"',
	],	
	'patches' : [
		#('opencl/0002-OpenCL-git-header.patch', '-p1'), # this is from deadsix27 # if source_subfolder then use '..'), # 2020.10.23 remember, no header patch for Alexpux
		('opencl/01-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1 make default to version 1.2
		('opencl/01a-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
		('opencl/02-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
		('opencl/03-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
		('opencl/04-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
	],
	'run_post_patch' : [ # 2020.10.15 was 'run_post_regexreplace'
		# PATCH OPENCL DEFAULT HEADERS VERSION TO 1.2
		'cp -fv "{target_prefix}/include/CL/cl_version.h" "{target_prefix}/include/CL/cl_version.h.orig"',
		'sed -i.bak "s/define CL_TARGET_OPENCL_VERSION 300/define CL_TARGET_OPENCL_VERSION 120/g" "{target_prefix}/include/CL/cl_version.h"',
		'sed -i.bak "s/Defaulting to 300 (OpenCL 3.0)/Defaulting to 120 (OpenCL 1.2)/g" "{target_prefix}/include/CL/cl_version.h"',
		'diff -U 5 "{target_prefix}/include/CL/cl_version.h.orig" "{target_prefix}/include/CL/cl_version.h"  && echo "NO difference" || echo "YES differences!"',
		#
		'diff -U 5 "../CMakeLists.txt.orig" "../CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"',
		'cat "../Config.cmake.in" # newly created file',
		'diff -U 5 "../loader/windows/icd_windows_hkr.c.orig" "../loader/windows/icd_windows_hkr.c"  && echo "NO difference" || echo "YES differences!"',
		'diff -U 5 "../test/loader_test/test_create_calls.c.orig" "../test/loader_test/test_create_calls.c"  && echo "NO difference" || echo "YES differences!"',
		'diff -U 5 "../test/loader_test/test_program_objects.c.orig" "../test/loader_test/test_program_objects.c"  && echo "NO difference" || echo "YES differences!"',
	],
	'run_post_install' : [
		'cp -vf "{target_prefix}/lib/libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"',
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'depends_on' : [ 'opencl_headers' ],
	'update_check' : { 'type' : 'git', },	
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' },
}
