{
	'repo_type' : 'git',
	'run_post_patch' : [
		'autoreconf -fiv',
	],
	'url' : 'https://github.com/mstorsjo/fdk-aac.git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	'_info' : { 'version' : 'git (master), 'fancy_name' : 'fdk-aac' },
}
# 2019.12.13 old:
#	'fdk_aac' : {
#		'repo_type' : 'git',
#		'run_post_patch': [
#			'autoreconf -fiv',
#		],
#		'url' : 'https://github.com/mstorsjo/fdk-aac.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'fdk-aac' },
#	},