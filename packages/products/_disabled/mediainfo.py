{ 
	'repo_type' : 'git',
	#'branch' : 'v0.7.94', # 2019.12.13 
	'recursive_git' : True,
	'url' : 'https://github.com/MediaArea/MediaInfo.git',
	'source_subfolder' : 'Project/GNU/CLI',
	'rename_folder' : 'mediainfo_git', # 2019.12.13
    'run_post_patch' : [ # 2019.12.13
		'rm -fv ./configure',
		'./autogen.sh NOCONFIGURE=1',
		'autoreconf -fiv',
	],
	'configure_options': '--host={target_host} --prefix={product_prefix}/mediainfo_git.installed --disable-shared --disable-static-libs',
    'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.12.13
	'depends_on': [
		'zenlib', 'libmediainfo', # 2019.12.13
	],
	'run_post_configure' : [
		'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'MediaInfo' },
	'_disabled' : True, # 2019.12.13 ?????
}