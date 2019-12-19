{
	'repo_type' : 'git',
	'source_subfolder' : 'Project/GNU/Library',
	'url' : 'https://github.com/MediaArea/ZenLib.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --enable-static --disable-shared --enable-shared=no',
	'run_post_configure' : [
		'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile', # 2019.12.13
	],

	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zenlib' },
}