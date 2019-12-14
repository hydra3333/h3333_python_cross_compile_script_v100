{
	'repo_type' : 'git',
	'url' : 'https://github.com/libass/libass.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-silent-rules',
    'run_post_install': [
		'sed -i.bak \'s/-lass -lm/-lass -lfribidi -lfreetype -lexpat -lm/\' "{pkg_config_path}/libass.pc"', #-lfontconfig # 2018.12.13 # 2019.12.13
	],
	'depends_on' : [ 'expat', 'fontconfig', 'freetype', 'iconv', 'libfribidi'],
	'_info' : { 'version' : None, 'fancy_name' : 'libass' },
}