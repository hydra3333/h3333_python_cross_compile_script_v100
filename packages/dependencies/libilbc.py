{
	'repo_type' : 'git',
	'url' : 'https://github.com/dekkers/libilbc.git',
	'branch' : 'main',  # 2020.12.19 they've changed the trunk from master to main (a US political race thing against the word, apparently)
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libilbc' },
}
