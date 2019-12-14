{ # 2019.12.13  used by liblsw and in turn product x264
		'repo_type' : 'git',
		'url' : 'https://github.com/hydra3333/l-smash', # 2019.12.13 mine is patched #'https://github.com/l-smash/l-smash.git',
		'env_exports' : {
			'PKGCONFIG' : 'pkg-config',
			'CFLAGS'   : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'CXXFLAGS' : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'CPPFLAGS' : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'LDFLAGS'  : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		},
		'configure_options':
			'--prefix={target_prefix} '
			'--cross-prefix={cross_prefix_bare} '
			'--extra-libs="-lssp" ' 
		,
		'build_options': 'install-lib',
		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libl-smash' },
}