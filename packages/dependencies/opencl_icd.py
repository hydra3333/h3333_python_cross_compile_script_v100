{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'depth_git' : 0,
	'needs_make_install' : True, #False,
	#'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF -DOPENCL_ICD_LOADER_DISABLE_OPENCLON12=ON', # build only symbols https://github.com/KhronosGroup/OpenCL-ICD-Loader/commit/bb98ad9a9c264d63ad2204c1eeee0a3a1e724e20 
	'run_post_install' : [
	#	'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2019.12.13 always copy it
	#	'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2020.03.27 required for mpv to link
		'cp -vf "{target_prefix}/lib/libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2019.12.13 always copy it
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'patches' : [
		#('opencl/0001-OpenCL-git-prefix.patch', '-p1'), # '..'), # 2020.06.27 moved change to the "sed" below
		('opencl/0002-OpenCL-git-header.patch', '-p1'), # '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
	],
	'run_post_patch' : [ # 2020.10.15 was 'run_post_regexreplace' : [ # 2019.12.13
		'cp -fv "CMakeLists.txt" "CMakeLists.txt.orig"',
		#'sed -i.bak \'s/Windows.h/windows.h/\' ./loader/windows/icd_windows_envvars.c',
		'sed -i.bak \'s/project (OpenCL-ICD-Loader VERSION 1.2)/project (OpenCL-ICD-Loader)/g\' "CMakeLists.txt"', # 2020.06.27 added since CMakeLists.txt changed
		'sed -i.bak \'s/set_target_properties (OpenCL PROPERTIES VERSION "1.2" SOVERSION "1")/set_target_properties (OpenCL PROPERTIES PREFIX "")/g\' "CMakeLists.txt"', # 2020.06.27 moved here from patch 0001
		# 2020.10.15 commit https://github.com/KhronosGroup/OpenCL-Headers/commit/9fac4e9866a961f66bdd72fa2bff50145512f972 changed default header version to 3.0 if CL_TARGET_OPENCL_VERSION is not defined
		#'sed -i.bak \'s/-DCL_TARGET_OPENCL_VERSION=300/-DCL_TARGET_OPENCL_VERSION=200/g\' "CMakeLists.txt"', # 2020.10.15 they changed it to version 3.0 headers, so put it back to v2.0 (perhaps even 1.2)
		'diff -U 5 "CMakeLists.txt.orig" "CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"', # 2020.10.15 nope, comment this out or it fails to build.
	],
	'depends_on' : [ 'opencl_headers' ],
	'update_check' : { 'type' : 'git', },	
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' }, # 2019.12.13 clarity with the fancy name
}
