{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'branch' : 'main',
	'depth_git' : 0,
	#'branch' : '98ca71fb9f8484f1cd1999f55224bf9e8d18693b', # 2020.11.01 so it works pre-meson, pre-opencl v3 patches
	'needs_make_install' : True, #False,
	#'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options': '. {cmake_prefix_options} -DOPENCL_ICD_LOADER_HEADERS_DIR={target_prefix}/include -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DBUILD_SHARED_LIBS=ON '
		'-DCMAKE_STATIC_LIBRARY_PREFIX="" ' # 2022.12.18 from deadsix27
		'-DBUILD_TESTING=OFF '
		'-DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF '
		'-DOPENCL_ICD_LOADER_DISABLE_OPENCLON12=ON', # build only symbols https://github.com/KhronosGroup/OpenCL-ICD-Loader/commit/bb98ad9a9c264d63ad2204c1eeee0a3a1e724e20 
	'run_post_install' : [
	#	'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2019.12.13 always copy it
	#	'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2020.03.27 required for mpv to link
		'cp -vf "{target_prefix}/lib/libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2019.12.13 always copy it
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	#'patches' : [
	#	('opencl/1.patch', '-p1'), # '..'),  # 2022.12.18 from deadsix27
	#	('opencl/0002-OpenCL-git-header-for-mingw64-8plus.patch', '-p1'), # 2020.10.23 for use with Mingw64 8plus
	#],
	'run_post_patch' : [ # 2020.10.15 was 'run_post_regexreplace' : [ # 2019.12.13
		'cp -fv "CMakeLists.txt" "CMakeLists.txt.orig"',
		#'sed -i.bak \'s/project (OpenCL-ICD-Loader VERSION 1.2)/project (OpenCL-ICD-Loader)/g\' "CMakeLists.txt"',
		'sed -i.bak \'s/project (OpenCL-ICD-Loader/project (OpenCL-ICD-Loader)/g\' "CMakeLists.txt"',
		'sed -i.bak \'s/VERSION 1.2/#VERSION 1.2/g\' "CMakeLists.txt"',
		'sed -i.bak \'s/LANGUAGES C)/#LANGUAGES C)/g\' "CMakeLists.txt"',
		#
		'sed -i.bak \'s/set_target_properties (OpenCL PROPERTIES VERSION "1.2" SOVERSION "1")/set_target_properties (OpenCL PROPERTIES PREFIX "")/g\' "CMakeLists.txt"', # 2020.06.27 moved here from patch 0001
		'diff -U 5 "CMakeLists.txt.orig" "CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"', 
	],
	'depends_on' : [ 'opencl_headers' ],
	'update_check' : { 'type' : 'git', },	
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' },
}
