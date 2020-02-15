{ # 2019.12.13 version 3.6.11.1 is later than mine
	'repo_type' : 'archive',
	'download_locations' : [ # 3.6.11.1 is newer than my 3.6.10
		{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.12.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'bfacf16e342949ffd977a9232556092c47164bd26e166736cf3459a870506c4b' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.12.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'bfacf16e342949ffd977a9232556092c47164bd26e166736cf3459a870506c4b' }, ], },
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
		'run_post_patch': [ # 2019.12.13
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
	'_info' : { 'version' : '3.6.12', 'fancy_name' : 'gnutls' },
}
# 2019.12.13 old:
#	'gnutls' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/
#			{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.10.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b1f3ca67673b05b746a961acf2243eaae0ffe658b6a6494265c648e7c7812293' }, ], }, # 2019.05.29
#			{ 'url' : 'https://fossies.org/linux/misc/gnutls-3.6.10.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b1f3ca67673b05b746a961acf2243eaae0ffe658b6a6494265c648e7c7812293' }, ], }, # 2019.05.29
#		],
#		'folder_name' : 'gnutls-3.6.10',
#		'run_post_patch': [   
#			'autoreconf -fiv -I M4', # 2019.05.29 try to get rid of error: 'automake-1.16' is missing on your system.
#		],
#		'configure_options':
#			'--host={target_host} --prefix={target_prefix} --disable-shared --enable-static '
#			'--disable-srp-authentication '
#			'--disable-non-suiteb-curves '
#			'--enable-cxx '
#			'--enable-nls '
#			'--disable-rpath '
#			'--disable-gtk-doc '
#			'--disable-guile '
#			'--disable-doc '
#			'--enable-local-libopts '
#			# '--disable-guile '
#			# '--disable-libdane '
#			'--disable-tools ' # 2018.11.23
#			'--disable-tests ' # 2018.11.23
#			'--with-zlib ' # 2018.11.23
#			'--with-included-libtasn1 '
#			'--with-included-unistring '
#			'--with-default-trust-store-file '
#			'--with-default-blacklist-file '
#			'--with-libiconv-prefix={target_prefix} ' # 2018.11.23
#			'--without-tpm '
#			'--without-p11-kit'
#		,
#		'env_exports' : {
#			'CFLAGS'   : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CXXFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CPPFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'LDFLAGS' : ' -D_POSIX_C_SOURCE {original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		},
#		# 'configure_options':
#			# '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --with-included-unistring '
#			# '--disable-rpath --disable-nls --disable-guile --disable-doc --disable-tests --enable-local-libopts --with-included-libtasn1 --with-libregex-libs="-lgnurx" --without-p11-kit --disable-silent-rules '
#			# 'CPPFLAGS="-DWINVER=0x0501 -DAI_ADDRCONFIG=0x0400 -DIPV6_V6ONLY=27" LIBS="-lws2_32" ac_cv_prog_AR="{cross_prefix_full}ar"'
#		# ,
#		'run_post_install': [
#			"sed -i.bak 's/-lgnutls *$/-lgnutls -lnettle -lhogweed -lgmp -lcrypt32 -lws2_32 -lintl -liconv -lssp/' \"{pkg_config_path}/gnutls.pc\"", #TODO -lintl
#		],
#		# 2018.12.05 comment out patches per deadsix27
#		# 2019.04.13 add patch rename-inet_pton_for_srt.diff per deadsix27
#		'patches' : [
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/gnutls-from-Alexpux/rename-inet_pton_for_srt.diff', '-p1'),
#			#('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/gnutls-from-Alexpux/0001-add-missing-define.patch', '-p1'), # un-commented per alexpux 2018.05.29
#			#('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/gnutls-from-Alexpux/0003-gnutls-fix-external-libtasn1-detection.patch', '-p1'), # un-commented per alexpux 2018.05.29
#			#('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/gnutls-from-Alexpux/0004-disable-broken-examples.patch', '-p1'), # un-commented per alexpux 2018.05.29
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/gnutls-from-Alexpux/0005-remove-coverage-rules.patch', '-p1'), # new patch per alexpux 2018.05.29
#		],
#		'depends_on' : [ 
#			'iconv', 
#			'zlib', 
#			'gmp', 
#			'libnettle',
#		],
#		'_info' : { 'version' : '3.6.10', 'fancy_name' : 'gnutls' },
#	},