{
	'repo_type' : 'git',
	'run_post_patch' : [
		'autoreconf -fiv',
	],
	'url' : 'https://github.com/mstorsjo/fdk-aac.git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	'_info' : { 'version' : None, 'fancy_name' : 'fdk-aac' },
}