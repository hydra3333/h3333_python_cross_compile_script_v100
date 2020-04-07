{
	'repo_type' : 'git',
	'url' : 'https://github.com/libass/libass.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-silent-rules',
    'run_post_install': [
		'sed -i.bak \'s/-lass -lm/-lass -lfribidi -lfreetype -lexpat -lm/\' "{pkg_config_path}/libass.pc"', #-lfontconfig # 2018.12.13
	],
	#'depends_on' : [ 'expat', 'fontconfig',  'harfbuzz', 'freetype', 'iconv', 'libfribidi'],
	'depends_on' : [ 'expat', 'fontconfig',  'freetype', 'iconv', 'libfribidi'], # 'freetype' depends on depends on 'freetype_lib', 'harfbuzz_lib-with-freetype' so it gets the order right !
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libass' },
}
# 2019.12.13 old:
#	'libass' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/libass/libass.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-silent-rules',
#		'run_post_install': (
#			'sed -i.bak \'s/-lass -lm/-lass -lfribidi -lfreetype -lexpat -lm/\' "{pkg_config_path}/libass.pc"', #-lfontconfig
#		),
#		'depends_on' : [ 'fontconfig', 'harfbuzz', 'libfribidi', 'freetype', 'iconv', ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libass' },
#	},