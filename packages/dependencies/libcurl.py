{
	'repo_type' : 'git',
	'url' : 'https://github.com/curl/curl',
	'rename_folder' : 'curl_git',
	'configure_options': '--enable-static --disable-shared --target={bit_name2}-{bit_name_win}-gcc --host={target_host} --build=x86_64-linux-gnu --with-libssh2 --with-gnutls --with-ca-fallback --without-winssl --prefix={target_prefix} --exec-prefix={target_prefix}', # 2019.12.13
	'depends_on': (
		'zlib','libssh2',
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