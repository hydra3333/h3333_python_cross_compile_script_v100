{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'depth_git' : 0,
	#'branch' : '6d0b214b9cc303cdb0b05b3c0dc9afb0c39998c5', # 2020.04.20 icd_loader broke upstream
	'needs_make_install' : True, #False,
	#'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF -DOPENCL_ICD_LOADER_DISABLE_OPENCLON12=ON', # build only symbols https://github.com/KhronosGroup/OpenCL-ICD-Loader/commit/bb98ad9a9c264d63ad2204c1eeee0a3a1e724e20 
	'run_post_build' : [
	#	'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2019.12.13 always copy it
	#	'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2020.03.27 required for mpv to link
		'cp -vf "{target_prefix}/lib/libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2019.12.13 always copy it
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'patches' : [
		('opencl/0001-OpenCL-git-prefix.patch', '-p1'), # '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
		('opencl/0002-OpenCL-git-header.patch', '-p1'), # '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
	],
	#'run_post_regexreplace' : [ # 2019.12.13
	#	'sed -i.bak \'s/Windows.h/windows.h/\' ./loader/windows/icd_windows_envvars.c',
	#],
	'depends_on' : [ 'opencl_headers' ],	
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' }, # 2019.12.13 clarity with the fancy name
}
