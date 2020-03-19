{ # NOTE: now we MUST add --legacy to the mediainfo.exe commandline at runtime to get the "old" fields !!!!! 
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'https://github.com/MediaArea/MediaInfo.git',
	'source_subfolder' : 'Project/GNU/CLI',
	'rename_folder' : 'mediainfo_git', # 2019.12.13
    'run_post_patch' : [ # 2019.12.13
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
	'_info' : { 'version' : 'git master', 'fancy_name' : 'MediaInfo' },
}
# 2019.12.13 old:
#	'mediainfo' : { # 2018.11.23 - NOTE: now have to add --legacy to the mediainfo.exe commandline to get the "old" fields !!!!! :( :( :(
#		'repo_type' : 'git',
#		'recursive_git' : True,
#		'url' : 'https://github.com/MediaArea/MediaInfo.git',
#		#'branch' : 'tags/v18.12', # 2019.02.02
#		'source_subfolder' : 'Project/GNU/CLI',
#		'rename_folder' : 'mediainfo_git',
#		'run_post_patch' : [
#			'rm -fv ./configure',
#			'./autogen.sh NOCONFIGURE=1',
#			'autoreconf -fiv',
#		],
#		'configure_options': '--host={target_host} --prefix={product_prefix}/mediainfo_git.installed --disable-shared --disable-static-libs ', 
#		'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.10.19 D_FORTIFY_SOURCE=0 # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		#'env_exports' : {
#		#	'CFLAGS'   : '-DLIBXML_STATIC -DGLIB_STATIC_COMPILATION',
#		#	'CXXFLAGS' : '-DLIBXML_STATIC -DGLIB_STATIC_COMPILATION',
#		#	'CPPFLAGS' : '-DLIBXML_STATIC -DGLIB_STATIC_COMPILATION',
#		#},
#		'depends_on': [
#			'zenlib', 'libmediainfo',
#		],
#		'run_post_configure' : [
#			'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'MediaInfo' },
#		'_disabled' : True,
#	},