{
	'repo_type' : 'git',
	'url' : 'https://git.ffmpeg.org/rtmpdump.git',
	'needs_configure' : False,
	#'install_options' : 'SYS=mingw CRYPTO=GNUTLS LIB_GNUTLS="-L{target_prefix}/lib -lpthread -lgnutls -lhogweed -lnettle -lgmp -lcrypt32 -lws2_32 -lintl -liconv -lz -lpthread " OPT=-O3 CROSS_COMPILE={cross_prefix_bare} SHARED=no prefix={target_prefix}', # 2019.12.13
	'install_options' : 'SYS=mingw CRYPTO=GNUTLS LIB_GNUTLS="-L{target_prefix}/lib -lpthread -lgnutls -lhogweed -lnettle -lgmp -lcrypt32 -lws2_32 -lwinmm -lz -liconv -lintl -liconv -lssp" OPT="{original_cflags}" CROSS_COMPILE={cross_prefix_bare} SHARED=no prefix={target_prefix}', # 2019.12.13

	#'build_options' : 'SYS=mingw CRYPTO=GNUTLS LIB_GNUTLS="-L{target_prefix}/lib -lpthread -lgnutls -lhogweed -lnettle -lgmp -lcrypt32 -lws2_32 -lintl -liconv -lz  -lpthread " OPT=-O3 CROSS_COMPILE={cross_prefix_bare} SHARED=no prefix={target_prefix}', # 2019.12.13
	'build_options' : 'SYS=mingw CRYPTO=GNUTLS LIB_GNUTLS="-L{target_prefix}/lib -lgnutls -lhogweed -lnettle -lgmp -lcrypt32 -lws2_32 -lwinmm -lz -liconv -lintl -liconv -lssp"	OPT="{original_cflags}" CROSS_COMPILE={cross_prefix_bare} SHARED=no prefix={target_prefix}',  # 2019.12.13
		'env_exports' : {
			'CFLAGS'   : ' {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'CXXFLAGS' : ' {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'CPPFLAGS' : ' {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'LDFLAGS'  : ' {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		},
    'run_post_install' :( # 2019.12.13
	#	'sed -i.bak \'s/-lrtmp -lz/-lrtmp -lwinmm -lz/\' "{pkg_config_path}/librtmp.pc"',
        'sed -i.bak \'s/-lrtmp -lz/-lrtmp -lwinmm -lz -lintl -liconv -lssp/\' "{pkg_config_path}/librtmp.pc"', # 2019.12.13
	),
	'depends_on' : [
		#'gnutls', 'zlib', # 2019.12.13
        'iconv', 'gnutls', 'zlib', 'gettext', 'libgcrypt', # 2019.12.13
	],
	'_info' : { 'version' : None, 'fancy_name' : 'rtmpdump' },
}