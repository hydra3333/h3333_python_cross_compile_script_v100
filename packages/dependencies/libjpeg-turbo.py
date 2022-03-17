{
	'repo_type' : 'git',
	'url' : 'https://github.com/libjpeg-turbo/libjpeg-turbo.git',
    'branch' : 'main',  # they've changed the trunk from master to main (a US political race thing against the word, apparently)
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_STATIC=ON -DENABLE_SHARED=OFF -DREQUIRE_SIMD=ON -DWITH_SIMD=ON -DWITH_JAVA=OFF -DCMAKE_BUILD_TYPE=Release',
	'patches' : [
		('libjpeg-turbo/0001-libjpeg-turbo-git-mingw-compat.patch', '-p1'),
		('libjpeg-turbo/0002-libjpeg-turbo-git-libmng-compat.patch', '-p1'),
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libjpeg-turbo' },
}
