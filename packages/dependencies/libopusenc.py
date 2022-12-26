{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/libopusenc.git',
	'depth_git': 0,
	'configure_options' : '{autoconf_prefix_options}',
	'depends_on' : [
		'libopus',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libopusenc' },
}