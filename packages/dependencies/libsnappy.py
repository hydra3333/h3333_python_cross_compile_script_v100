{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/snappy.git',
	#'branch' : 'main',
	'branch' : 'f603a020086da1115118eef206ce28a4a5829438',	# 2023.04.02 the commit immediately after this one breaks cross-compilation
	'depth_git' : 0,
	'rename_folder' : 'libsnappy',
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_BINARY=OFF -DSNAPPY_BUILD_BENCHMARKS=OFF -DSNAPPY_REQUIRE_AVX2=ON -DSNAPPY_REQUIRE_AVX=ON -DSNAPPY_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release',
	'run_post_install' : [
		'rm -vf {target_prefix}/lib/libsnappy.dll.a',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libsnappy' },
}
