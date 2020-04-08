{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/dav1d.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'rename_folder' : 'libdav1d_git',
	'source_subfolder' : 'build',
	'regex_replace': { #hacky but works, so who cares, for some reason libdav1d thinks we have POSIX_MEMALIGN.. maybe mingw or gcc bug, .. so we'll just force it to not define that we have it so it doesn't use it.
		'post_patch': [
			{
				0: r'cdata.set\(\'HAVE_POSIX_MEMALIGN\', 1\)',
				1: 'cdata.set(\'HAVE_ALIGNED_MALLOC\', 1)',
				'in_file': '../meson.build'
			},
			{
				0: r'cdata.set\(\'HAVE_ALIGNED_MALLOC\', 1\)',
				1: 'cdata.set(\'HAVE_ALIGNED_MALLOC\', 1)',
				'in_file': '../meson.build'
			},
		],
	},
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
  	'run_post_regexreplace' : [ # 2019.12.13
		# 'sed -i.bak \'s/sdl2_dependency.found()/false/\' ../tools/meson.build'   # 2020.03.19 commented out
	],  # 2019.12.13
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'dav1d (library)' },
}
# 2019.12.13 old:
#	'libdav1d' : { # https://code.videolan.org/explore/projects # https://code.videolan.org/videolan/dav1d
#		'repo_type' : 'git',
#		'url' : 'https://code.videolan.org/videolan/dav1d.git',
#		'conf_system' : 'meson',
#		'build_system' : 'ninja',
#		'rename_folder' : 'libdav1d_git',
#		'source_subfolder' : 'build',
#		'run_post_regexreplace' : [
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