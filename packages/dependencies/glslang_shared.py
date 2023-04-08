{
	'repo_type' : 'git',
	'rename_folder' : 'glslang',
	'url' : 'https://github.com/KhronosGroup/glslang.git',
	'depth_git': 0,
	#
	# 2022.09.05 SHADERC depends on GLSLANG ... GLSLANG is "ahead" of SHADERC 
	#            and there is a mismatch, so we affix GLSLANG to a KNOWN GOOD COMMIT
	#            both here in glslang.py and in shaderc.py at 'glslang_revision'
	#
	#'branch' : '1fb2f1d7896627d62a289439a2c3e750e551a7ab',
	'branch' : '!CMD(cat "{inTreePrefix}/shaderc_commit_dependencies/glslang_revision.commit")CMD!',  # 2023.02.04
	'rename_folder' : 'glslang_shared_git',
	'recursive_git' : True,
	'conf_system' : 'cmake', # from MABS 2020.10.10
	'custom_ldflag' : ' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -L{target_prefix}/lib',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DUNIX=OFF ' # 2020.10.12 comment out
		'-DBUILD_SHARED_LIBS=ON '
		'-DBUILD_EXTERNAL=OFF '
		'-DSKIP_GLSLANG_INSTALL=OFF '
		'-DENABLE_GLSLANG_INSTALL=ON '
		'-DENABLE_GLSLANG_BINARIES=OFF '
		'-DENABLE_GLSLANG_JS=OFF '
		'-DENABLE_OPT=ON '
		'-DENABLE_CTEST=OFF '
		'-DENABLE_GLSLANG_WEBMIN=OFF '
		'-DENABLE_SPVREMAPPER=ON '
		'-DUSE_CCACHE=OFF '
	,
	'patches' : [	# deadsix27 2023.04.08
		( 'https://github.com/KhronosGroup/glslang/pull/3144.patch', '-p1', '..' ), # Include <cstdint> header in Common.h #3144 
	],
	'run_post_patch' : [ 
		#'rm -vf "./compile_commands.json"'
		'./update_glslang_sources.py',
	],
	#'run_post_install' : [ 
	#	'cp -vf "{target_prefix}/lib/libglslangd.a" "{target_prefix}/lib/libglslang.a"' # 2020.10.10 only needed if CMAKE_BUILD_TYPE not defined or is "Debug"
	#],
	'depends_on' : [  'shaderc_commit_dependencies', 'spirv-cross', 'spirv-tools', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'glslang' },
}