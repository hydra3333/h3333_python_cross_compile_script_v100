{
	'repo_type' : 'git',
	'url' : 'https://github.com/libssh2/libssh2.git',
	'depth_git' : 0,
	#'branch' : '35695772d0b93a50a1de79ced596be39062a48f1',  #'b853d7a86e1648c00386790e91cefcfd701bd17b' aborts mediainfo build per https://github.com/libssh2/libssh2/issues/596
    'branch' : '7efb44abf854669eb254c9cb7290e557d0c5ab3c', #try this experimental branch/commit
	# OK !!! The latest git objected to --with-sysroot="{target_sub_prefix}" ... doesn't handle it correctly,
	#        which is contained in {autoconf_prefix_options} 
	# 	     so remove that and do the configure the hard way
    'run_post_regexreplace' : [ # 'run_post_patch' : [ # 2020.04.08
		'autoreconf -fiv',
	],
	'configure_options' : ' --host="{target_host}" --prefix="{target_prefix}" --disable-examples-build --disable-shared --enable-static --disable-examples-build --with-crypto=openssl ', # 2019.12.13
	'env_exports' : {
		'LIBS' : '-lcrypt32' # Otherwise: libcrypto.a(e_capi.o):e_capi.c:(.text+0x476d): undefined reference to `__imp_CertFreeCertificateContext'
	},
	'depends_on' : [
		'zlib', 'libressl', # 2019.12.13
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (35695772d0b93a50a1de79ced596be39062a48f1)', 'fancy_name' : 'libssh2' },
}
