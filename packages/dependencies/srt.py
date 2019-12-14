{
	'repo_type' : 'git',
	'url' : 'https://github.com/Haivision/srt.git',
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
	'depends_on' : [ 'gettext', 'gnutls' ],
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_ENCLIB=gnutls -DENABLE_SHARED=0', # 2019.12.13
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_ENCLIB=gnutls -DUSE_GNUTLS=1 -DHAICRYPT_USE_OPENSSL_EVP=0 -DHAICRYPT_USE_OPENSSL_AES=0 -DENABLE_SUFLIP=0 -DENABLE_EXAMPLES=0 -DENABLE_SHARED=0', # 2019.12.13
	'_info' : { 'version' : None, 'fancy_name' : 'srt' }, # it is actually srt 
}