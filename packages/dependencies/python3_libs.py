#{
#	'repo_type' : 'git',
#	'url' : 'https://github.com/DeadSix27/python_mingw_libs.git',
#	'needs_configure' : False,
#	'needs_make_install' : False,
#	# python 3.7.5
#	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool PYTHON_VERSION=3.7.5',
#	'_info' : { 'version' : '3.7.5', 'fancy_name' : 'Python (library-only)' },
#}
{
	'repo_type' : 'git',
	'url' : 'https://github.com/DeadSix27/python_mingw_libs.git',
	'needs_configure' : False,
	'needs_make_install' : False,
	# python 3.8.2
	'run_post_patch' : [
		'cp -fv Makefile Makefile.orig',
		'sed -i.bak "s;3.7.5;3.8.2;g" "Makefile"',
		'diff -U 5 Makefile.orig Makefile && echo "NO difference" || echo "YES differences!"',
		'cp -fv install_python_libs.py install_python_libs.py.orig',
		'sed -i.bak "s;_DEBUG = False;_DEBUG = True;g" "install_python_libs.py"',
		'sed -i.bak "s;\'3.7.5\';\'3.7.5\',\'3.8.2\';g" "install_python_libs.py"',
		'sed -i.bak "s; 3.7.5 ; 3.8.2 ;g" "install_python_libs.py"',
		'diff -U 5 install_python_libs.py.orig install_python_libs.py && echo "NO difference" || echo "YES differences!"',
	],
	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool PYTHON_VERSION=3.8.2',
}
