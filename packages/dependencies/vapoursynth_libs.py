{
	'repo_type' : 'git',
	'url' : 'https://github.com/DeadSix27/vapoursynth_mingw_libs.git',
	'needs_configure' : False,
	'needs_make_install' : False,
	'depends_on' : [ 'python3_libs' ],
	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool VAPOURSYNTH_VERSION=R48 PYTHON_VERSION=3.7.5', # 2019.12.13 added PYTHON_VERSION=3.7.5
	'packages' : {
		'arch' : [ '7za' ],
	},
	'_info' : { 'version' : 'R48', 'fancy_name' : 'VapourSynth (library-only)' },
}
# 2019.12.13 old:
#	'vapoursynth_libs': {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/DeadSix27/vapoursynth_mingw_libs.git',
#		'needs_configure' : False,
#		'needs_make_install' : False,
#		'build_options': 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool VAPOURSYNTH_VERSION=R48',
#		'packages': {
#			'arch' : [ '7za' ],
#		},
#		'depends_on': [ 'python3_libs' ], 
#		'_info' : { 'version' : 'R48', 'fancy_name' : 'VapourSynth (library-only)' },
#	},