{
	'repo_type' : 'git', 
	'url' : 'https://github.com/xiph/speex.git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	'env_exports' : { # 2019.12.13 -D_FORTIFY_VA_ARG=0
		'PKGCONFIG' : 'pkg-config',
		'CFLAGS'   : '{original_cflags} -D_FORTIFY_VA_ARG=0',
		'CXXFLAGS' : '{original_cflags} -D_FORTIFY_VA_ARG=0',
		'CPPFLAGS' : '{original_cflags} -D_FORTIFY_VA_ARG=0',
		'LDFLAGS'  : '{original_cflags} -D_FORTIFY_VA_ARG=0',
	},
	'depends_on' : [ 'libogg', 'libspeexdsp', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'speex' },
}
