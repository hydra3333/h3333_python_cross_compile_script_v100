{
	'repo_type' : 'git',
	'url' : 'https://github.com/Haivision/srt.git',
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_ENCLIB=gnutls -DENABLE_SHARED=0', # 2019.12.13
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -D_WIN32_WINNT=0x600 -DENABLE_SHARED=0 -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_ENCLIB=gnutls -DUSE_GNUTLS=1 -DHAICRYPT_USE_OPENSSL_EVP=0 -DHAICRYPT_USE_OPENSSL_AES=0 -DENABLE_SUFLIP=0 -DENABLE_EXAMPLES=0 ', # 2019.12.13
	'depends_on' : [ 'gettext', 'gnutls' ],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'srt' }, # it is actually srt 
}
# 2019.12.13 old:
#	'libsrt' : { # 2019.05.10
#		'repo_type' : 'git',
#		'url' : 'https://github.com/Haivision/srt.git',
#		'source_subfolder' : '_build',
#		'conf_system' : 'cmake',
#		'patches' : (
#		),
#		'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -D_WIN32_WINNT=0x600 -DENABLE_SHARED=off -DENABLE_STATIC=on -DUSE_STATIC_LIBSTDCXX=on -DUSE_GNUTLS=on -DENABLE_SUFLIP=off -DENABLE_EXAMPLES=off -DHAICRYPT_USE_OPENSSL_EVP=off -DHAICRYPT_USE_OPENSSL_AES=off',
#		'depends_on' : [ 'gettext', 'gnutls' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libsrt' },
#	},