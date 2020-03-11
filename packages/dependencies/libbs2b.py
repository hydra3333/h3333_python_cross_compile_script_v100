{
	'repo_type' : 'archive',
	'do_not_bootstrap' : True,
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/bs2b/files/libbs2b/3.1.0/libbs2b-3.1.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6aaafd81aae3898ee40148dd1349aab348db9bfae9767d0e66e0b07ddd4b2528' }, ], },
		{ 'url' : 'http://sourceforge.mirrorservice.org/b/bs/bs2b/libbs2b/3.1.0/libbs2b-3.1.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6aaafd81aae3898ee40148dd1349aab348db9bfae9767d0e66e0b07ddd4b2528' }, ], },
	],
	'env_exports' : {
		'ac_cv_func_malloc_0_nonnull' : 'yes', # fixes undefined reference to `rpl_malloc'
	},
	'run_post_patch' : [
		'autoreconf -fiv',
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r' dist-lzma',
				1: r'',
				'in_file': 'configure.ac' # configure.ac:7: error: support for lzma-compressed distribution archives has been removed
			},
			{
				0: r'\t-lsndfile',
				'in_file': 'src/Makefile.am'
			},
			{
				0: r'bs2bconvert_LDFLAGS = \\',
				1: r'bs2bconvert_LDFLAGS = !CMD(pkg-config sndfile --libs-only-l)CMD!\n',
				'in_file': 'src/Makefile.am'
			},
		],
	},

	'depends_on' : ['libflac', 'libsndfile', ], # 2019.12.13 'libspeex',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
	'update_check' : { 'url' : 'https://sourceforge.net/projects/bs2b/files/libbs2b/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '3.1.0', 'fancy_name' : 'libbs2b' },
}
# 2019.12.13 old:
#	'libbs2b' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://sourceforge.net/projects/bs2b/files/libbs2b/
#			{ "url" : "https://sourceforge.net/projects/bs2b/files/libbs2b/3.1.0/libbs2b-3.1.0.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6aaafd81aae3898ee40148dd1349aab348db9bfae9767d0e66e0b07ddd4b2528" }, ], },
#			{ "url" : "http://sourceforge.mirrorservice.org/b/bs/bs2b/libbs2b/3.1.0/libbs2b-3.1.0.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6aaafd81aae3898ee40148dd1349aab348db9bfae9767d0e66e0b07ddd4b2528" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'custom_cflag' : '{original_cflags}', # 2019.10.19 D_FORTIFY_SOURCE=0' # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		'env_exports' : {
#			"ac_cv_func_malloc_0_nonnull" : "yes", # fixes undefined reference to `rpl_malloc'
#			'PKGCONFIG' : 'pkg-config',
#			'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		},
#		'depends_on': [ 'libflac', 'libsndfile' ],
#		'_info' : { 'version' : '3.1.0', 'fancy_name' : 'libbs2b' },
#	},
