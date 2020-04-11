{
	'repo_type' : 'git',
	'url' : 'https://github.com/curl/curl',
	'depth_git' : 0,
	'branch' : '2cfac302fbeec68f1727cba3d1705e16f02220ad', # fails: 'd4afa0fc2076ee0184cf8120d83ac997e8c57692',
	'rename_folder' : 'curl_git',
	'configure_options': '--enable-static --disable-shared --target={bit_name2}-{bit_name_win}-gcc --host={target_host} --build=x86_64-linux-gnu --with-libssh2 --with-gnutls --with-ca-fallback --without-winssl --prefix={target_prefix} --exec-prefix={target_prefix}', # 2019.12.13
	'depends_on': (
		'zlib', 'gnutls', 'libssh2',
	),
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcurl' },
}
# 2019.12.13 old:
#	'libcurl' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/curl/curl',
#		'rename_folder' : 'curl_git',
#		'configure_options': '--enable-static --disable-shared --target={bit_name2}-{bit_name_win}-gcc --host={target_host} --build=x86_64-linux-gnu --with-libssh2 --with-gnutls --with-ca-fallback --without-winssl --prefix={target_prefix} --exec-prefix={target_prefix}',
#		'depends_on': (
#			'zlib', 'libssh2',
#		),
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcurl' },
#	},