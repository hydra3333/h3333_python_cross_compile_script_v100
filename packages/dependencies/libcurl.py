{
	'repo_type' : 'git',
	'url' : 'https://github.com/curl/curl',
	'depth_git' : 0,
	##'branch' : '8e701cc978430d638517d025fade2b0dc1ae9b73',
	'rename_folder' : 'curl_git',
    #'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://github.com/curl/curl/releases/download/curl-7_79_1/curl-7.79.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0606f74b1182ab732a17c11613cbbaf7084f2e6cca432642d0e3ad7c224c3689' }, ], }, # https://github.com/curl/curl/releases
	#	{ 'url' : 'https://fossies.org/linux/www/curl-7.79.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0606f74b1182ab732a17c11613cbbaf7084f2e6cca432642d0e3ad7c224c3689' }, ], }, # https://fossies.org/linux/misc/
    #],
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'configure_options': '--prefix={target_prefix} --exec-prefix={target_prefix} --enable-static --disable-shared --target={bit_name2}-{bit_name_win}-gcc --host={target_host} --build=x86_64-linux-gnu '
		'--with-libssh2 --with-gnutls --with-ca-fallback --without-winssl --enable-pthreads --enable-symbol-hiding ',
	'depends_on': (
		'zlib', 'gnutls', 'libssh2',
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcurl' },
}
#


