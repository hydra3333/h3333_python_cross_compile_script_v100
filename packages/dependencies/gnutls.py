{
	'repo_type' : 'archive',
	'download_locations' : [ # 3.6.11.1 is newer than my 3.6.10
		{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.11.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fbba12f3db9a55dbf027e14111755817ec44b57eabec3e8089aac8ac6f533cf8' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.11.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fbba12f3db9a55dbf027e14111755817ec44b57eabec3e8089aac8ac6f533cf8' }, ], },
	],
	'run_post_patch': [ # 2019.12.13 added this
		'autoreconf -fiv -I M4', # 2019.05.29 try to get rid of error: 'automake-1.16' is missing on your system.  # 2019.12.13 added this
	],
    'env_exports' : {
		'CFLAGS'   : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CXXFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CPPFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'LDFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
	},
	'configure_options' :
		'--host={target_host} --prefix={target_prefix} --disable-shared --enable-static '
		'--disable-srp-authentication '
		'--disable-non-suiteb-curves '
		'--enable-cxx '
		'--enable-nls '
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
		'--without-p11-kit'
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
		#('gnutls/rename-inet_pton_for_srt.diff', '-p1'), # 2019.12.13 hmm, i wonder why this patch was not applied ?
        #('gnutls/0005-remove-coverage-rules.patch', '-p1'), # 2019.12.13 hmm, i wonder why this patch was not applied ?
	# ],
	'depends_on' : [
		'gettext',
		'iconv',
		'libnettle',
		'zlib',
        'gmp', # 2019.12.13
	],
	'update_check' : { 'url' : 'ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6', 'type' : 'ftpindex', 'regex' : r'gnutls-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '3.6.11.1', 'fancy_name' : 'gnutls' },
}