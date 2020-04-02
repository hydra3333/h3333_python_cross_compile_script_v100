{
	'repo_type' : 'git',
	'url' : 'https://github.com/DeadSix27/vapoursynth_mingw_libs.git',
	'needs_configure' : False,
	'needs_make_install' : False,
	'depends_on' : [ 'python3_libs' ],
	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool VAPOURSYNTH_VERSION=R49 PYTHON_VERSION=3.8.2',
	'run_post_patch' : [
		'sed "s;R48;R49;g" "Makefile"',
		'sed "s;R48;R49;g" "install_vapoursynth_libs.py"',
	],
	'run_post_build' : [
		'cp -fv "{target_prefix}/include/vapoursynth/VapourSynth.h" "{target_prefix}/include/VapourSynth.h" ',
	],
	'run_post_install' : [
		'cp -fv "{target_prefix}/include/vapoursynth/VapourSynth.h" "{target_prefix}/include/VapourSynth.h" ',
	],
	'packages' : {
		'arch' : [ '7za' ],
	},
	'_info' : { 'version' : 'R49', 'fancy_name' : 'VapourSynth (library-only)' },
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