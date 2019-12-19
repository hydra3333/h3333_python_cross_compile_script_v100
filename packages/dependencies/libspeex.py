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
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'speex' },
}
# 2019.12.13 old:
#	'libspeex' : {
#		'repo_type' : 'git', #"LDFLAGS=-lwinmm"
#		'url' : 'https://github.com/xiph/speex.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'env_exports' : {
#			'PKGCONFIG' : 'pkg-config',
#			'CFLAGS'   : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CXXFLAGS' : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CPPFLAGS' : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'LDFLAGS'  : '{original_cflags} -D_FORTIFY_VA_ARG=0', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		},
#		'depends_on' : [ 'libogg', 'libspeexdsp', ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'speex' },
#	},