{
	'repo_type' : 'git',
	'url' : 'https://github.com/curl/curl',
	'depth_git' : 0,
	#'branch' : '70d010d285315e5f1cad6bdb4953e167b069b692', # works: '70d010d285315e5f1cad6bdb4953e167b069b692', # breaks: '576e507c78bdd2ec88da442a5354f9dd661b9a8a', 
	'rename_folder' : 'libcurl_git',
    #'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://github.com/curl/curl/releases/download/curl-7_85_0/curl-7.85.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '88b54a6d4b9a48cb4d873c7056dcba997ddd5b7be5a2d537a4acb55c20b04be6' }, ], }, # https://github.com/curl/curl/releases
	#	{ 'url' : 'https://fossies.org/linux/www/curl-7.85.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '88b54a6d4b9a48cb4d873c7056dcba997ddd5b7be5a2d537a4acb55c20b04be6' }, ], }, # https://fossies.org/linux/misc/
    #],
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'configure_options': '--prefix={target_prefix} --exec-prefix={target_prefix} --enable-static --disable-shared --target={bit_name2}-{bit_name_win}-gcc --host={target_host} --build=x86_64-linux-gnu '
		#'--with-libssh2 --with-gnutls --with-ca-fallback --without-winssl --enable-pthreads --enable-symbol-hiding ',
		'--without-libssh2 --without-ssl --with-gnutls --with-ca-fallback --without-winssl --enable-pthreads --enable-symbol-hiding ',
	'depends_on': (
		'zlib', 'gnutls', # 'libssh2',
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcurl' },
}
