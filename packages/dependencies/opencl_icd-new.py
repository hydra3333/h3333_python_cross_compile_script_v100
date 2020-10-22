{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'depth_git' : 0,
	'needs_make_install' : True,
	'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options': '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} ' # note '..' sinxce we're in a subfolder
		'-DCMAKE_BUILD_TYPE=Release '
		'-DBUILD_SHARED_LIBS=ON '
		'-DBUILD_TESTING=OFF '
		'-DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF '
		'-DOPENCL_ICD_LOADER_DISABLE_OPENCLON12=ON', # build only symbols per https://github.com/KhronosGroup/OpenCL-ICD-Loader/commit/bb98ad9a9c264d63ad2204c1eeee0a3a1e724e20 
	'run_post_install' : [
		'cp -vf "{target_prefix}/lib/libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"',
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'patches' : [
		#('opencl/0002-OpenCL-git-header.patch', '-p1'), # this is from deadsix27 # if source_subfolder then use '..'), # 2020.10.23 remember, no header patch for Alexpux
		('opencl/01-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
		('opencl/02-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
		('opencl/03-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
		('opencl/04-mingw-build-Alexpux-updated-2020.10.23.patch', '-p1', '..'), # 2020.10.23 Alexpux patch updated Part 1
	],
	'run_post_patch' : [ # 2020.10.15 was 'run_post_regexreplace'
		#'cp -fv "CMakeLists.txt" "CMakeLists.txt.orig"',
		#'sed -i.bak \'s/project (OpenCL-ICD-Loader VERSION 1.2)/project (OpenCL-ICD-Loader)/g\' "CMakeLists.txt"', # 2020.06.27 added since CMakeLists.txt changed
		#'sed -i.bak \'s/set_target_properties (OpenCL PROPERTIES VERSION "1.2" SOVERSION "1")/set_target_properties (OpenCL PROPERTIES PREFIX "")/g\' "CMakeLists.txt"', # 2020.06.27 moved here from deadsix27 patch 0001
		## 2020.10.15 commit https://github.com/KhronosGroup/OpenCL-Headers/commit/9fac4e9866a961f66bdd72fa2bff50145512f972 changed default header version to 3.0 if CL_TARGET_OPENCL_VERSION is not defined
		##'sed -i.bak \'s/-DCL_TARGET_OPENCL_VERSION=300/-DCL_TARGET_OPENCL_VERSION=200/g\' "CMakeLists.txt"', # 2020.10.15 they changed it to version 3.0 headers, so put it back to v2.0 (perhaps even 1.2)
		#'diff -U 5 "CMakeLists.txt.orig" "CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"',
		'cp -fv "../CMakeLists.txt" "../CMakeLists.txt.orig"',
		# some sed editing right here
		'diff -U 5 "../CMakeLists.txt.orig" "../CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"',
	],
	'depends_on' : [ 'opencl_headers' ],
	'update_check' : { 'type' : 'git', },	
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' },
}
