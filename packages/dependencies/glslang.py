{
	'repo_type' : 'git',
	'rename_folder' : 'glslang',
	'url' : 'https://github.com/KhronosGroup/glslang.git',
	'depth_git': 0,
	'recursive_git' : True,
	'conf_system' : 'cmake', # from MABS 2020.10.10
	#'run_post_patch' : [ 
	#	'./update_glslang_sources.py'
	#],
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} ', # -DUNIX=OFF # from MABS 2020.10.10
	'patches' : [ 
		('glslang/glslang-0001-fix-gcc-10.1-error-from-shinchiro.patch', '-p1'), # 2020.05.31 only when using gcc 10.1
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'glslang' },
}
#{
#	'repo_type' : 'git',
#	'rename_folder' : 'glslang',
#	'url' : 'https://github.com/KhronosGroup/glslang.git',
#	'depth_git': 0,
#	#'branch': '3ed344dd784ecbbc5855e613786f3a1238823e56', # 2020.04.20 COMMENTED OUT
#	'patches' : [ 
#		('glslang/glslang-0001-fix-gcc-10.1-error-from-shinchiro.patch', '-p1'), # 2020.05.31 only when using gcc 10.1
#	],
#	'needs_make' : False,
#	'needs_make_install' : False,
#	'needs_configure' : False,
#	'recursive_git' : True,
#	'update_check' : { 'type' : 'git', },
#	#'_info' : { 'version' : 'git (3ed344dd784ecbbc5855e613786f3a1238823e56)', 'fancy_name' : 'glslang' },
#	'_info' : { 'version' : 'git', 'fancy_name' : 'glslang' },
#}