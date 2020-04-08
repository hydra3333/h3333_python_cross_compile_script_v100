{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/dav1d.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
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
    'run_post_regexreplace' : [
		# 'sed -i.bak \'s/sdl2_dependency.found()/false/\' ../tools/meson.build' # 2019.12.13 # 2020.03.19 commented out
	],
	'configure_options' : ''
		'--prefix={output_prefix}/dav1d.installed  '    # 2019.12.13 old '--prefix={product_prefix}/dav1d.installed  '
		'--libdir={output_prefix}/dav1d.installed/lib ' # 2019.12.13 old '--libdir={product_prefix}/dav1d.installed/lib '
		'--default-library=static '
		'--backend=ninja '
		'-Denable_tests=true '
		'-Denable_tools=true '
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
	,
	'_info' : { 'version' : None, 'fancy_name' : 'dav1d' },
}
# 2019.12.13 old:
#	'dav1d' : { # https://code.videolan.org/explore/projects # https://code.videolan.org/videolan/dav1d
#		'repo_type' : 'git',
#		#'url' : 'https://git.videolan.org/videolan/dav1d.git',
#		'url' : 'https://code.videolan.org/videolan/dav1d.git',
#		'conf_system' : 'meson',
#		'build_system' : 'ninja',
#		'source_subfolder' : 'build',
#		'run_post_regexreplace' : [
#			'sed -i.bak \'s/sdl2_dependency.found()/false/\' ../tools/meson.build'  # 2019.08.07 turn off building of tool dav1dplay.exe since it won't link. A Nod to JB MABS.
#		],
#		'configure_options': ''
#			'--prefix={product_prefix}/dav1d.installed  '
#			'--libdir={product_prefix}/dav1d.installed/lib '
#			'--default-library=static '
#			'-Denable_tests=true ' # '-Dbuild_tests=true ' # 2019.07.09
#			'-Denable_tools=true ' # '-Dbuild_tools=true ' # 2019.07.09
#			'--backend=ninja '
#			'--buildtype=release '
#			'--cross-file={meson_env_file} ./ ..'
#      ,
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'dav1d' },
#	},