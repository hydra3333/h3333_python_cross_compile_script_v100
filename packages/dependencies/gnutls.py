{
	'repo_type' : 'archive',
	'download_locations' : [ # 3.6.14 crashes rtmpdump 
		{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.13.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '32041df447d9f4644570cf573c9f60358e865637d69b7e59d1159b7240b52f38' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.13.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '32041df447d9f4644570cf573c9f60358e865637d69b7e59d1159b7240b52f38' }, ], },
		#{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.14.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5630751adec7025b8ef955af4d141d00d252a985769f51b4059e5affa3d39d63' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.14.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5630751adec7025b8ef955af4d141d00d252a985769f51b4059e5affa3d39d63' }, ], },
	],
    'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -D_POSIX_C_SOURCE {original_cflags}',
		'CXXFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}',
		'CPPFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}',
		'LDFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}',
	},
	'configure_options' :
		'--host={target_host} --prefix={target_prefix} --disable-shared --enable-static '
		'--disable-srp-authentication '
		'--disable-non-suiteb-curves '
		'--enable-cxx '
		#'--enable-nls ' # 2020.03.19 comment out
		'--disable-rpath '
		'--disable-gtk-doc '
		'--disable-guile '
		'--disable-doc '
		'--enable-local-libopts '
		'--disable-tools '
		'--disable-tests '
		'--with-zlib '
		'--with-included-libtasn1 '
		'--with-included-unistring '
		'--with-default-trust-store-file '
		'--with-default-blacklist-file '
		'--without-tpm '
		'--without-p11-kit '
        '--with-libiconv-prefix={target_prefix} ' # 2019.12.13 added this
	,
	'regex_replace': {
		'post_install': [
			{
				0: r'^(Libs: -L\${{libdir}} -lgnutls)([\n\r\s]+)?$',
				1: r'\1 -lnettle -lhogweed -lgmp -lcrypt32 -lws2_32 -lintl -liconv -lssp\2', # iconv is required by gettext, but gettext has no .pc file, so... # 2019.12.13 added -lssp
				'in_file': '{pkg_config_path}/gnutls.pc'
			},
		],
	},
	# 'patches' : [
		#('gnutls/rename-inet_pton_for_srt.diff', '-p1'), # 2019.12.13 hmm, i wonder why this patch was not applied ? Leave it out for now
        #('gnutls/0005-remove-coverage-rules.patch', '-p1'), # 2019.12.13 hmm, i wonder why this patch was not applied ? Leave it out for now
	# ],
	'run_post_regexreplace': [ # 2019.12.13
		'autoreconf -fiv -I M4', # 2019.12.13
	], # 2019.12.13
	'depends_on' : [
		'gettext',
		'iconv',
		'libnettle',
		'zlib',
        'gmp', # 2019.12.13
	],
	'update_check' : { 'url' : 'ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6', 'type' : 'ftpindex', 'regex' : r'gnutls-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '3.6.13', 'fancy_name' : 'gnutls' },
}
