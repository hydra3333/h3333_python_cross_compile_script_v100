{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/libdvdread.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --with-libdvdcss',
	'depends_on' : [
		'libdvdcss',
	],
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'run_post_install' : [
		'sed -i.bak \'s/-ldvdread/-ldvdread -ldvdcss/\' "{pkg_config_path}/dvdread.pc"', # fix undefined reference to `dvdcss_close'
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libdvdread' },
}