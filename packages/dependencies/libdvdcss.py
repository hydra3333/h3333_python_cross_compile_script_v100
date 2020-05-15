{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/libdvdcss.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-doc',
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libdvdcss' },
}