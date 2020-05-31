{
	'repo_type' : 'git',
	'rename_folder' : 'glslang',
	'url' : 'https://github.com/KhronosGroup/glslang.git',
	'depth_git': 0,
	#'branch': '3ed344dd784ecbbc5855e613786f3a1238823e56', # 2020.04.20 COMMENTED OUT
	'patches' : [ 
		('glslang/glslang-0001-fix-gcc-10.1-error-from-shinchiro.patch', '-p1'), # 2020.05.31 only when using gcc 10.1
	],
	'needs_make' : False,
	'needs_make_install' : False,
	'needs_configure' : False,
	'recursive_git' : True,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (3ed344dd784ecbbc5855e613786f3a1238823e56)', 'fancy_name' : 'glslang' },
}
