{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/snappy.git',
	'depth_git' : 0,
	#'branch' : '0793e2ae2d51640ae569b75ffb42fc444afafb32', # 2020.12.19 it broke after this
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_BINARY=OFF -DSNAPPY_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release',
	'run_post_install' : [
		'rm -vf {target_prefix}/lib/libsnappy.dll.a',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libsnappy' },
}
