{
	'repo_type' : 'git',
	'url' : 'https://github.com/dekkers/libilbc.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release',
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libilbc' },
}
# 2019.12.13 old:
#	'libilbc' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/dekkers/libilbc.git',
#		'run_post_regexreplace': [
#			'autoreconf -fiv',
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libilbc' },
#	},