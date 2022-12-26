{
	'repo_type' : 'git',
	'url' : 'https://github.com/hoene/libmysofa',
	'branch' : 'main',
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS:bool=off -DBUILD_TESTS=no -DENABLE_STATIC=1 -DUSE_STATIC_LIBSTDCXX=1 -DUSE_GNUTLS=1 -DENABLE_SHARED=0', # 2019.12.13
    'depends_on' : [ 'gnutls_3333' ], # 2021.02.03 'gettext', 
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmysofa_3333' },
}
