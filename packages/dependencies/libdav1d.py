{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/dav1d.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'rename_folder' : 'libdav1d_git',
	'source_subfolder' : 'build',
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--backend=ninja '
		'-Denable_tests=false '
		'-Denable_tools=false '
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
    ,
  	'run_post_patch' : [ # 2019.12.13
		'sed -i.bak \'s/sdl2_dependency.found()/false/\' ../tools/meson.build'   # 2019.12.13 # 2019.08.07 turn off building of tool dav1dplay.exe since it won't link. A Nod to JB MABS. 
	],  # 2019.12.13
	'_info' : { 'version' : None, 'fancy_name' : 'dav1d (library)' },
}
# 2019.12.13 old:
#	'libdav1d' : { # https://code.videolan.org/explore/projects # https://code.videolan.org/videolan/dav1d
#		'repo_type' : 'git',
#		'url' : 'https://code.videolan.org/videolan/dav1d.git',
#		'conf_system' : 'meson',
#		'build_system' : 'ninja',
#		'rename_folder' : 'libdav1d_git',
#		'source_subfolder' : 'build',
#		'run_post_patch' : [
#			'sed -i.bak \'s/sdl2_dependency.found()/false/\' ../tools/meson.build'  # 2019.08.07 turn off building of tool dav1dplay.exe since it won't link. A Nod to JB MABS.
#		],
#		'configure_options':
#			'--prefix={target_prefix} '
#			'--libdir={target_prefix}/lib '
#			'--default-library=static '
#			'--backend=ninja '
#			'-Denable_tests=false ' # '-Dbuild_tests=true ' # 2019.07.09
#			'-Denable_tools=false ' # '-Dbuild_tools=true ' # 2019.07.09
#			'--buildtype=release '
#			'--cross-file={meson_env_file} ./ ..'
#      ,
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'dav1d (library)' },
#	},