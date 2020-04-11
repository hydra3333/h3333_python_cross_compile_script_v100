{
	'repo_type' : 'git',
	'url' : 'https://github.com/libssh2/libssh2.git',
	'depth_git' : 0,
	#'branch' : '',
	# OK !!! The latest git objected to --with-sysroot="{target_sub_prefix}" ... doesn't handle it correctly,
	#        which is contained in {autoconf_prefix_options} 
	# 	     so remove that and do the configure the hard way
	'configure_options' : ' --host="{target_host}" --prefix="{target_prefix}" --disable-examples-build --disable-shared --enable-static --disable-examples-build --with-crypto=openssl ', # 2019.12.13
	'env_exports' : {
		'LIBS' : '-lcrypt32' # Otherwise: libcrypto.a(e_capi.o):e_capi.c:(.text+0x476d): undefined reference to `__imp_CertFreeCertificateContext'
	},
	'depends_on' : [
		'zlib', 'libressl', # 2019.12.13
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libssh2' },
}
# 2019.12.13 old:
#	'libssh2' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/libssh2/libssh2.git',
#		'configure_options':
#			'--host={target_host} '
#			'--prefix={target_prefix} '
#			'--disable-shared '
#			'--enable-static '
#			'--disable-examples-build '
#			'--with-crypto=openssl' # 2018.11.23
#		,
#		'depends_on': (
#			'zlib', 'libressl', # 2018.11.23 add 'libressl'
#		),
#		'env_exports' : {
#			'LIBS' : '-lcrypt32' # Otherwise: libcrypto.a(e_capi.o):e_capi.c:(.text+0x476d): undefined reference to `__imp_CertFreeCertificateContext'
#		},
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libssh2' },
#	},