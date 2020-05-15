{
	'repo_type' : 'git',
	'url' : 'https://git.ffmpeg.org/rtmpdump.git',
	'needs_configure' : False,
	'install_options' : 'SYS=mingw CRYPTO=GNUTLS LIB_GNUTLS="-L{target_prefix}/lib -lpthread -lgnutls -lhogweed -lnettle -lgmp -lcrypt32 -lwinmm -lz -liconv -lintl -liconv -lssp" OPT="{original_cflags}" CROSS_COMPILE={cross_prefix_bare} SHARED=no prefix={target_prefix}', # 2019.12.13
	'build_options'   : 'SYS=mingw CRYPTO=GNUTLS LIB_GNUTLS="-L{target_prefix}/lib -lpthread -lgnutls -lhogweed -lnettle -lgmp -lcrypt32 -lwinmm -lz -liconv -lintl -liconv -lssp" OPT="{original_cflags}" CROSS_COMPILE={cross_prefix_bare} SHARED=no prefix={target_prefix}',  # 2019.12.13
	'run_post_install' :( # 2019.12.13
        'sed -i.bak \'s/-lrtmp -lz/-lrtmp -lwinmm -lz -lintl -liconv -lssp/\' "{pkg_config_path}/librtmp.pc"', # 2019.12.13
	),
	'depends_on' : [
        'iconv', 'gnutls', 'zlib', 'gettext', 'libgcrypt', # 2019.12.13
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'rtmpdump' },
}
