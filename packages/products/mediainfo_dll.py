{ # NOTE: now we MUST add --legacy to the mediainfo.exe commandline at runtime to get the "old" fields !!!!! 
	'repo_type' : 'git',
	'url' : 'https://github.com/MediaArea/MediaInfo.git', # 2021.08.12 https://github.com/MediaArea/MediaInfo/issues/551
	'depth_git' : 0,
	#'branch' : 'tags/v21.09', # 2021.10.31 A RELEASE
	'recursive_git' : True,
	'source_subfolder' : 'Project/GNU/CLI',
	#
	'rename_folder' : 'mediainfo_dll_git', # 2019.12.13
	'run_post_regexreplace' : [ # 2019.12.13
		'rm -fv ./configure',
		'./autogen.sh NOCONFIGURE=1',
		'autoreconf -fiv',
	],
	'configure_options': '--host={target_host} --prefix={output_prefix}/mediainfo_dll_git.installed --enable-shared --enable-static-libs',
	'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.12.13
	'depends_on': [
		'zenlib', 'libmediainfo_dll', # 2019.12.13
	],
	'run_post_configure' : [
		'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'MediaInfo_dll' },
}
