{
	'repo_type' : 'git', 
	'url' : 'https://github.com/xiph/speex.git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
		'CFLAGS'   : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CXXFLAGS' : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CPPFLAGS' : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'LDFLAGS'  : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
	},
    'depends_on' : [ 'libogg', 'libspeexdsp', ],
	'_info' : { 'version' : None, 'fancy_name' : 'speex' },
}