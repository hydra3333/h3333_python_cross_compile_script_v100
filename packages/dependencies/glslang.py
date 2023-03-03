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
	'branch' : '!CMD(cat "{inTreePrefix}/shaderc_commit_dependencies/glslang_revision.commit")CMD!',  # 2023.02.04
	#'rename_folder' : 'glslang_static_git', # CAREFUL changing this - it is referenced in shaderc
	'rename_folder' : 'glslang', # CAREFUL changing this - it is referenced in shaderc
	'recursive_git' : True,
	'conf_system' : 'cmake', # from MABS 2020.10.10
	'custom_ldflag' : ' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -L{target_prefix}/lib',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DUNIX=OFF ' # 2020.10.12 comment out
		'-DBUILD_SHARED_LIBS=OFF '
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
	'run_post_patch' : [ 
		#'rm -vf "./compile_commands.json"'
		'./update_glslang_sources.py',
	],
	'run_post_install' : [ 
		#'cp -vf "{target_prefix}/lib/libglslangd.a" "{target_prefix}/lib/libglslang.a"' # 2020.10.10 only needed if CMAKE_BUILD_TYPE not defined or is "Debug"
		#'if [ ! -f "{target_prefix}/include/glslang/Public/ResourceLimits.h" ] ; then cp -vf "./glslang/Public/ResourceLimits.h" "{target_prefix}/include/glslang/Public/" ; fi',
		'cp -vf "./glslang/Public/ResourceLimits.h" "{target_prefix}/include/glslang/Public/"', # force overwrite in case a new version which doesn't install properly which is why this line exists
	],
	'depends_on' : [ 'shaderc_commit_dependencies', 'spirv-cross', 'spirv-tools', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'glslang' },
}