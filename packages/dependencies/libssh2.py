{
	'repo_type' : 'git',
	'url' : 'https://github.com/libssh2/libssh2.git',
	'configure_options' : '{autoconf_prefix_options} --disable-examples-build --disable-shared --enable-static --disable-examples-build --with-crypto=openssl ', # 2019.12.13
	'env_exports' : {
		'LIBS' : '-lcrypt32' # Otherwise: libcrypto.a(e_capi.o):e_capi.c:(.text+0x476d): undefined reference to `__imp_CertFreeCertificateContext'
	},
	'depends_on' : [
		'zlib', 'libressl', # 2019.12.13
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libssh2' },
}