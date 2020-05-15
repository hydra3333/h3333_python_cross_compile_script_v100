{ # NOTE: now we MUST add --legacy to the mediainfo.exe commandline at runtime to get the "old" fields !!!!! 
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'https://github.com/MediaArea/MediaInfo.git',
	'source_subfolder' : 'Project/GNU/CLI',
	'rename_folder' : 'mediainfo_git', # 2019.12.13
    'run_post_regexreplace' : [ # 2019.12.13
		'rm -fv ./configure',
		'./autogen.sh NOCONFIGURE=1',
		'autoreconf -fiv',
	],
	'configure_options': '--host={target_host} --prefix={output_prefix}/mediainfo_git.installed --disable-shared --disable-static-libs',
    'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.12.13
	'depends_on': [
		'zenlib', 'libmediainfo', # 2019.12.13
	],
	'run_post_configure' : [
		'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'MediaInfo' },
}
