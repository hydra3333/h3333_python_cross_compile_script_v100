{
	'repo_type' : 'git',
	'rename_folder' : 'glslang',
	'url' : 'https://github.com/KhronosGroup/glslang.git',
	'depth_git': 0,
	'recursive_git' : True,
	'conf_system' : 'cmake', # from MABS 2020.10.10
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DUNIX=OFF '
		'-DBUILD_SHARED_LIBS=OFF '
		'-DBUILD_EXTERNAL=ON '
		'-DSKIP_GLSLANG_INSTALL=OFF '
		'-DENABLE_GLSLANG_BINARIES=OFF '
		'-DENABLE_GLSLANG_JS=OFF '
		'-DENABLE_OPT=ON '
		'-DENABLE_CTEST=OFF '
	,
	'run_post_patch' : [ 
		'rm -vf "./compile_commands.json"',
		'if [ -d "../external/googletest" ] ; then rm -fvR   "External/googletest" ; fi',
		'git clone https://github.com/google/googletest.git  External/googletest',
		#' echo "TEMPORARY NOTICE: additionally perform the following to avoid a current breakage in googletest:"',
		#'cd External/googletest'
		#'git checkout 0c400f67fcf305869c5fb113dd296eca266c9725',
		#'cd ../..',
	],
	#'run_post_install' : [ 
	#	'cp -vf "{target_prefix}/lib/libglslangd.a" "{target_prefix}/lib/libglslang.a"' # 2020.10.10 only needed if CMAKE_BUILD_TYPE not defined or is "Debug"
	#],
	'depends_on' : [  'spirv-cross_likeMABS', 'spirv-tools_likeMABS', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'glslang' },
}
