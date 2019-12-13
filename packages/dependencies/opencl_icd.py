{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'needs_make_install' : False,
	'source_subfolder': '_build', # 2019.12.13 ??? this may not work and need to be commented out ???
	'conf_system' : 'cmake',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=ON -DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF',
	'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF', # 2019.12.13
	'depends_on' : [ 'opencl_headers' ],	
	'run_post_build' : [
		#'if [ ! -f "already_ran_make_install" ] ; then cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a" ; fi', # 2019.12.13 always copy it
        'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2019.12.13 always copy it
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'patches' : [
		('opencl/0001-OpenCL-git-prefix.patch', '-p1', '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
		('opencl/0002-OpenCL-git-header.patch', '-p1', '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
	],
		'run_post_patch' : [ # 2019.12.13
			#'sed -i.bak \'s/Windows.h/windows.h/\' ./loader/windows/icd_windows_envvars.c', # 2019.12.13 use this is not working in _build - as specified above
			'sed -i.bak \'s/Windows.h/windows.h/\' ../loader/windows/icd_windows_envvars.c', # 2019.12.13 attempt to look one folder level up if working in a _build subfolder !!!
		],
	'_info' : { 'version' : None, 'fancy_name' : 'OpenCL-ICD-Loader' }, # 2019.12.13 clarity with the fancy name
}
