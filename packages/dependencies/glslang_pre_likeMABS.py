{
	'repo_type' : 'git',
	'rename_folder' : 'glslang',
	'url' : 'https://github.com/KhronosGroup/glslang.git',
	'depth_git': 0,
	'recursive_git' : True,
	'conf_system' : 'cmake', # from MABS 2020.10.10
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DBUILD_SHARED_LIBS=OFF '
		'-DUNIX=OFF ' # 2020.10.12 comment out
		'-DSKIP_GLSLANG_INSTALL=OFF '
		'-DENABLE_GLSLANG_INSTALL=ON '
		'-DENABLE_GLSLANG_BINARIES=OFF '
		'-DENABLE_CTEST=OFF '
		'-DENABLE_GLSLANG_WEBMIN=OFF '
		'-DUSE_CCACHE=OFF '
		'-DCMAKE_BUILD_TYPE=Release ' #	 # from MABS 2020.10.10 -DENABLE_SPVREMAPPER=OFF
	,
	'run_post_patch' : [ 
		'rm -vf "./compile_commands.json"'
	],
	#'run_post_install' : [ 
	#	'cp -vf "{target_prefix}/lib/libglslangd.a" "{target_prefix}/lib/libglslang.a"' # 2020.10.10 only needed if CMAKE_BUILD_TYPE not defined or is "Debug"
	#],
	'depends_on' : [  'spirv-cross', 'spirv-tools', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'glslang' },
}
