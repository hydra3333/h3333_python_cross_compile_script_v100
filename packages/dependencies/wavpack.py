{
	'repo_type' : 'git',
	'url' : 'https://github.com/dbry/WavPack.git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'wavpack' },
}
# 2019.12.13 old:
#	'wavpack' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/dbry/WavPack.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'wavpack' },
#	},