{
	'repo_type' : 'git',
	'url' : 'https://github.com/hydra3333/python_mingw_libs.git',
	'needs_configure' : False,
	'needs_make_install' : False,
	'run_post_regexreplace' : [
		#'cp -fv Makefile Makefile.orig',
		#'sed -i.bak "s;;;g" "Makefile"',
		#'diff -U 5 Makefile.orig Makefile && echo "NO difference" || echo "YES differences!"',
		'cp -fv install_python_libs.py install_python_libs.py.orig',
		'sed -i.bak "s;_DEBUG = False;_DEBUG = True;g" "install_python_libs.py"',
		'diff -U 5 install_python_libs.py.orig install_python_libs.py && echo "NO difference" || echo "YES differences!"',
	],
	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool VAPOURSYNTH_VERSION=R62 PYTHON_VERSION=3.11.2', # for vapoursynth R62
	## eg 
	## make -j 4 PREFIX=/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32 GENDEF=/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef DLLTOOL=/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool PYTHON_VERSION=3.8.5
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : '3.11.2', 'fancy_name' : 'Python (library-only)' },
}
