{
	#'repo_type' : 'git',
	#'url' : 'https://github.com/dekkers/libilbc.git',
	#'branch' : 'main',  # 2020.12.19 they've changed the trunk from master to main (a US political race thing against the word, apparently)
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/TimothyGu/libilbc/releases/download/v3.0.1/libilbc-3.0.1.tar.gz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '033e5b5d311b5c5e688e23f9877a8cbf4f82a69f8e82cdc758e3c1085f7e91ae' },	], }, # sha256sum filename
		#{ 'url' : 'https://github.com/TimothyGu/libilbc/releases/download/v3.0.2/libilbc-3.0.2.tar.gz',	'hashes' : [ { 'type' : 'sha256', 'sum' : 'e82cbc41c8c84c0828af869a9c6bbb62e06dece0d17d069c8b9db95082f0a4ce' },	], }, # sha256sum filename
		{ 'url' : 'https://github.com/TimothyGu/libilbc/releases/download/v3.0.3/libilbc-3.0.3.tar.gz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '47c57deb26a36da11cbf7d51e76894c7b909ab007664f736319267bde57c73d0' },	], }, # sha256sum filename
	],	
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release',
	'update_check' : { 'type' : 'git', },
	'update_check' : { 'url' : 'https://github.com/TimothyGu/libilbc/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	#'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libilbc' },
	'_info' : { 'version' : '3.0.1', 'fancy_name' : 'libilbc' },
}
