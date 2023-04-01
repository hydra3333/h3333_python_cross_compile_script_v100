{
	'repo_type' : 'git',
	'url' : 'https://github.com/hydra3333/vapoursynth_mingw_libs.git',
	'needs_configure' : False,
	'needs_make_install' : False,
	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool VAPOURSYNTH_VERSION=R62 PYTHON_VERSION=3.11.2', # for vapoursynth R62
	'run_post_regexreplace' : [
		#'cp -fv Makefile Makefile.orig',
		#'sed -i.bak "s;;;g" "Makefile"',
		#'diff -U 5 Makefile.orig Makefile && echo "NO difference" || echo "YES differences!"',
		'cp -fv install_vapoursynth_libs.py install_vapoursynth_libs.py.orig',
		'sed -i.bak "s;_DEBUG = False;_DEBUG = True;g" "install_vapoursynth_libs.py"',
		'diff -U 5 install_vapoursynth_libs.py.orig install_vapoursynth_libs.py && echo "NO difference" || echo "YES differences!"',
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
	'depends_on' : [ 'python3_libs' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'R62', 'fancy_name' : 'VapourSynth (library-only)' },
}
