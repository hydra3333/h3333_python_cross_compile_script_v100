{
	'repo_type' : 'git',
	'url' : 'https://github.com/curl/curl',
	'depth_git' : 0,
	#'branch' : '3735107d62ad28d6e25bd94109ab9f2454c22116', # https://github.com/curl/curl/issues/5219#ref-pullrequest-599156369 # works: '3735107d62ad28d6e25bd94109ab9f2454c22116', # fails: '1fc0617dccc3fa138235f219e2eaa7b405d1162e' under gcc10,
	'rename_folder' : 'curl_git',
	'configure_options': '--prefix={target_prefix} --exec-prefix={target_prefix} --enable-static --disable-shared --target={bit_name2}-{bit_name_win}-gcc --host={target_host} --build=x86_64-linux-gnu '
		'--with-libssh2 --with-gnutls --with-ca-fallback --without-winssl --enable-pthreads --enable-symbol-hiding ',
	'depends_on': (
		'zlib', 'gnutls', 'libssh2',
	),
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcurl' },
}
#


