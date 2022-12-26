{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/
		#{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.7/gnutls-3.7.7.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'be9143d0d58eab64dba9b77114aaafac529b6c0d7e81de6bdf1c9b59027d2106' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.7.7.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'be9143d0d58eab64dba9b77114aaafac529b6c0d7e81de6bdf1c9b59027d2106' }, ], },
		{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.7/gnutls-3.7.8.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c58ad39af0670efe6a8aee5e3a8b2331a1200418b64b7c51977fb396d4617114' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.7.8.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c58ad39af0670efe6a8aee5e3a8b2331a1200418b64b7c51977fb396d4617114' }, ], },
	],
    'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -D_POSIX_C_SOURCE {original_cflags}',
		'CXXFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}',
		'CPPFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}',
		'LDFLAGS'  : ' -D_POSIX_C_SOURCE {original_cflags}',
	},
	'configure_options' :
		'--host={target_host} --prefix={target_prefix} --disable-shared --enable-static '
		'--enable-threads=posix ' # 2022.12.18
		#'--disable-srp-authentication ' # 2022.12.18 per DEADSIX27 comment out
		#'--disable-non-suiteb-curves ' # 2022.12.18 per DEADSIX27 comment out
		'--enable-cxx '
		#'--enable-nls ' # 2020.03.19 comment out
        '--enable-openssl-compatibility '
		'--disable-rpath '
		'--disable-gtk-doc '
		'--disable-guile '
		'--disable-doc '
		'--enable-local-libopts '
		'--disable-tools '
		'--disable-tests '
		'--disable-bash-tests ' # 2022.12.18
		'--disable-full-test-suite ' # 2022.12.18
		'--disable-valgrind-tests ' # 2022.12.18
		'--enable-strict-x509 ' # 2022.12.18
		'--with-zlib '
		'--with-included-libtasn1 '
		'--with-included-unistring '
		'--with-default-trust-store-file '
		'--with-default-blacklist-file '
		#'--without-tpm '  # 2022.12.18 per DEADSIX27 comment out
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
				1: r'\1 -lnettle -lhogweed -lgmp -lcrypt32 -lws2_32 -liconv -lssp\2', # iconv is required by gettext, but gettext has no .pc file, so... # 2019.12.13 added -lssp # 2021.04.11 removed -lintl 
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
		#'gettext',  # 2021.02.03
		'iconv',
		'libnettle',
		'zlib',
        'gmp', # 2019.12.13
	],
	'update_check' : { 'url' : 'ftp://ftp.gnutls.org/gcrypt/gnutls/v3.6', 'type' : 'ftpindex', 'regex' : r'gnutls-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '3.7.8', 'fancy_name' : 'gnutls_3333' },
}
