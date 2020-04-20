{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
	'depth_git' : 0,
	'branch' : '6d0b214b9cc303cdb0b05b3c0dc9afb0c39998c5', # 2020.04.20 icd_loader broke upstream
	'needs_make_install' : False,
	#'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF', # 2019.12.13
	'run_post_build' : [
		'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2019.12.13 always copy it
		'cp -vf "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.a"', # 2020.03.27 required for mpv to link
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'patches' : [
		('opencl/0001-OpenCL-git-prefix.patch', '-p1'), # '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
		('opencl/0002-OpenCL-git-header.patch', '-p1'), # '..'), # 2019.12.13 when working in subfolder _build, use  ", '..'"  otherwise leave it off
	],
	'run_post_regexreplace' : [ # 2019.12.13
		'sed -i.bak \'s/Windows.h/windows.h/\' ./loader/windows/icd_windows_envvars.c',
	],
	'depends_on' : [ 'opencl_headers' ],	
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' }, # 2019.12.13 clarity with the fancy name
}
# 2019.12.13 old:
#	'opencl_icd' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/KhronosGroup/OpenCL-ICD-Loader.git',
#		#'source_subfolder': '_build', # per deadsix27 but does not work :( so undo related chnages below
#		'needs_make_install' : False,
#		'conf_system' : 'cmake',
#		'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DOPENCL_ICD_LOADER_REQUIRE_WDK=OFF', # was -DBUILD_SHARED_LIBS=OFF -DOPENCL_ICD_LOADER_REQUIRE_WDK=false
#		# -DBUILD_SHARED_LIBS=ON due to explanation here https://github.com/DeadSix27/python_cross_compile_script/commit/0218b4b80830563c7aab2b1e6d561d20977f5fd4#commitcomment-33472895
#		# i.e. Shared means it will use the system provided opencl.dll, which is supplied by AMD or Intel for example. (the right way). Needed, to create the .dll.a file.
#		'depends_on' : [ 'opencl_headers' ],
#		#'run_post_regexreplace' : [
#		#	'sed -i.bak \'s/Devpkey.h/devpkey.h/\' icd_windows_hkr.c',
#		#],
#		'run_post_build' : [
#			#'if [ ! -f "already_ran_make_install" ] ; then cp -fv "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a" ; fi',
#			'cp -fv "libOpenCL.dll.a" "{target_prefix}/lib/libOpenCL.dll.a"',
#			'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
#		],
#		'patches' : [
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/opencl/0001-OpenCL-git-prefix-2019.10.31.patch', '-p1'), #, '..'),
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/opencl/0002-OpenCL-git-header-2019.10.31.patch', '-p1'), #, '..'),
#		],
#		'run_post_regexreplace' : [
#			'sed -i.bak \'s/Windows.h/windows.h/\' ./loader/windows/icd_windows_envvars.c',
#			#### 'sed -i.bak \'s/set_target_properties (OpenCL PROPERTIES VERSION "1.2" SOVERSION "1")/#set_target_properties (OpenCL PROPERTIES VERSION "1.2" SOVERSION "1")\\nset_target_properties (OpenCL PROPERTIES PREFIX "")/\' CMakeLists.txt', # 2019.10.11 ??????????
#		],
#		'depends_on' : [ 'opencl_headers' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL-ICD-Loader' },
#	},
