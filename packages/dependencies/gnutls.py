{
	'repo_type' : 'archive',
	'download_locations' : [ # 3.6.14 crashes rtmpdump 
		#{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.14.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5630751adec7025b8ef955af4d141d00d252a985769f51b4059e5affa3d39d63' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.14.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5630751adec7025b8ef955af4d141d00d252a985769f51b4059e5affa3d39d63' }, ], },
		#{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.15.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0ea8c3283de8d8335d7ae338ef27c53a916f15f382753b174c18b45ffd481558' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.15.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0ea8c3283de8d8335d7ae338ef27c53a916f15f382753b174c18b45ffd481558' }, ], },
		{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.16.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1b79b381ac283d8b054368b335c408fedcb9b7144e0c07f531e3537d4328f3b3' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.16.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1b79b381ac283d8b054368b335c408fedcb9b7144e0c07f531e3537d4328f3b3' }, ], },
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
        '--with-libiconv-prefix={target_prefix} ' # 2019.12.13 added this from https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gnutls/PKGBUILD
		'--with-libregex-libs=-lsystre ' # 2020.06.09 from https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gnutls/PKGBUILD
		'--disable-libdane ' # 2020.06.09 from https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gnutls/PKGBUILD
		'gl_cv_double_slash_root=yes ' # 2020.06.09 from https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gnutls/PKGBUILD
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
	# 2020.09.05 up to v2.6.15 and patch "0006-fix-ncrypt-bcrypt-linking.patch" fails, so see if can do without patches
	#'patches' : [ # 3.6.13 built OK without patches, however 3.6.14 does not ... try these patches from https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gnutls/PKGBUILD
    #    ('gnutls/0001-add-missing-define.patch', '-p1'), # 2020.06.09 for 3.6.14
    #    ('gnutls/0003-gnutls-fix-external-libtasn1-detection.patch', '-p1'), # 2020.06.09 for 3.6.14
    #    ('gnutls/0004-disable-broken-examples.patch', '-p1'), # 2020.06.09 for 3.6.14
    #    ('gnutls/0005-remove-coverage-rules.patch', '-p1'), # 2020.06.09 for 3.6.14
    #    ('gnutls/0006-fix-ncrypt-bcrypt-linking.patch', '-p1'), # 2020.06.09 for 3.6.14
	#],
	'run_post_regexreplace': [
		'autoreconf -fiv -I M4',
	],
	'depends_on' : [
		'gettext',
		'iconv',
		'libnettle',
		'zlib',
        'gmp', # 2019.12.13
	],
	'update_check' : { 'url' : 'ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6', 'type' : 'ftpindex', 'regex' : r'gnutls-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '3.6.16', 'fancy_name' : 'gnutls' },
}
