{
	'repo_type' : 'git',
	'url' : 'https://github.com/hoene/libmysofa',
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
    'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS:bool=off -DBUILD_TESTS=no -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_GNUTLS=1 -DENABLE_SHARED=0', # 2019.12.13
    'depends_on' : [ 'gettext', 'gnutls' ], # 2019.12.13
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmysofa' },
}
# 2019.12.13 old:
#	'libmysofa' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/hoene/libmysofa',
#		#'branch' : '16d77ad6b4249c3ba3b812d26c4cbb356300f908',
#		'source_subfolder' : '_build',
#		'conf_system' : 'cmake',
#		#'configure_options': '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS:bool=off -DBUILD_TESTS=no',
#		'configure_options': '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS:bool=off -DBUILD_TESTS=no -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_GNUTLS=1 -DENABLE_SHARED=0',
#		'depends_on' : [ 'gettext', 'gnutls' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmysofa' },
#	},