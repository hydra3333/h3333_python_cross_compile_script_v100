{
	'repo_type' : 'git',
	'url' : 'https://github.com/dekkers/libilbc.git',
	'branch' : 'main',  # 2020.12.19 they've changed the trunk from master to main (a US political race thing against the word, apparently)
    'recursive_git': True,
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	#{ 'url' : 'https://github.com/TimothyGu/libilbc/releases/download/v3.0.3/libilbc-3.0.3.tar.gz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '47c57deb26a36da11cbf7d51e76894c7b909ab007664f736319267bde57c73d0' },	], }, # sha256sum filename
	#	{ 'url' : 'https://github.com/TimothyGu/libilbc/releases/download/v3.0.4/libilbc-3.0.4.tar.gz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '6820081a5fc58f86c119890f62cac53f957adb40d580761947a0871cea5e728f' },	], }, # sha256sum filename
	#],	
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libilbc' },
	#'update_check' : { 'url' : 'https://github.com/TimothyGu/libilbc/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	#'_info' : { 'version' : '3.0.4', 'fancy_name' : 'libilbc' },
}
