{
	'repo_type' : 'git',
	'url' : 'https://github.com/OpenMPT/openmpt.git',
	#'depth_git' : 0,
	'needs_configure' : False,
	#'build_options' : '{make_prefix_options} VERBOSE=1 TEST=0 SHARED_LIB=0 SHARED_SONAME=0 DYNLINK=0 STATIC_LIB=1 EXAMPLES=0 MODERN=1',
	'build_options' : '{make_prefix_options} CONFIG=mingw-w64 OPTIMIZE=vectorize OPENMPT123=0 VERBOSE=1 TEST=0 SHARED_LIB=0 SHARED_SONAME=0 DYNLINK=0 STATIC_LIB=1 EXAMPLES=0 MODERN=1',
	#'install_options' : '{make_prefix_options} VERBOSE=1 TEST=0 SHARED_LIB=0 SHARED_SONAME=0 DYNLINK=0 STATIC_LIB=1 EXAMPLES=0 MODERN=1 PREFIX={target_prefix}', # was uVERBOSE=1
	'install_options' : '{make_prefix_options} CONFIG=mingw-w64 OPTIMIZE=vectorize OPENMPT123=0 VERBOSE=1 TEST=0 SHARED_LIB=0 SHARED_SONAME=0 DYNLINK=0 STATIC_LIB=1 EXAMPLES=0 MODERN=1 PREFIX={target_prefix}', # was uVERBOSE=1
	'run_post_patch' : [
		'cp -fv {cross_prefix_full}ld {mingw_binpath}/ld',
	],
	'run_post_install' : [
		'rm -v {mingw_binpath}/ld',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'openmpt' },
}
