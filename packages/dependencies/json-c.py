{
	'repo_type' : 'git',
	'url' : 'https://github.com/json-c/json-c.git',
	'depth_git': 0,
	'conf_system' : 'cmake',
	#
	'branch': '2327b23d8e9111ad7d0df7452546c611c0e7ad7e', # fails 'f2e991a3419ee4078e8915e840b1a0d9003b349e', #works '2327b23d8e9111ad7d0df7452546c611c0e7ad7e', #'json-c-0.14-20200419', # 2020.05.11 per deadsix27 https://github.com/DeadSix27/python_cross_compile_script/commit/133965456b7fdbc82cbfe97e4612f5d4a319a34f
	'source_subfolder' : 'json-c-build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_RDRAND=ON -DENABLE_THREADING=ON -DDISABLE_WERROR=ON',
	#
	#'branch': 'json-c-0.14-20200419',
	#'source_subfolder' : 'json-c-build',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_STATIC_LIBS=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_RDRAND=ON -DENABLE_THREADING=ON -DDISABLE_WERROR=ON',
	#
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'json-c' },
}
