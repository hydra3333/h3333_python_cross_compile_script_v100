{
	'repo_type' : 'git',
	'source_subfolder' : 'Project/GNU/Library',
	'url' : 'https://github.com/MediaArea/MediaInfoLib.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --enable-shared --enable-static --with-libcurl --with-libmms --with-libmediainfo-name=MediaInfo.dll', # --enable-static --disable-shared --enable-shared=no
    'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.12.13
	'run_post_regexreplace' : [
		'sed -i.bak \'s/Windows.h/windows.h/\' ../../../Source/MediaInfo/Reader/Reader_File.h',
		'sed -i.bak \'s/Windows.h/windows.h/\' ../../../Source/MediaInfo/Reader/Reader_File.cpp',
	],
	'run_post_configure' : [
		'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
	],
	'depends_on': [
		'zenlib', 'libcurl',
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmediainfo' },
}
# 2019.12.13 old:
#	'libmediainfo' : { # 2018.11.23 - now have to add --legacy to the mediainfo.exe commandline to get the "old" fields !!!!! :( :( :(
#		'repo_type' : 'git',
#		'rename_folder' : 'libmediainfo_git',
#		'source_subfolder' : 'Project/GNU/Library',
#		'url' : 'https://github.com/MediaArea/MediaInfoLib.git',
#		#'branch' : 'tags/v18.12', # 2019.02.02
#		'configure_options' : '--host={target_host} --prefix={target_prefix} --enable-shared --enable-static --with-libcurl --with-libmms --with-libmediainfo-name=MediaInfo.dll ',
#		'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}',  # 2019.10.19 D_FORTIFY_SOURCE=0 # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		'run_post_regexreplace' : [
#			'sed -i.bak \'s/Windows.h/windows.h/\' ../../../Source/MediaInfo/Reader/Reader_File.h',
#			'sed -i.bak \'s/Windows.h/windows.h/\' ../../../Source/MediaInfo/Reader/Reader_File.cpp',
#		],
#		'run_post_configure' : [
#			'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
#		],
#		'depends_on': [
#			'zenlib', 'libcurl',
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmediainfo' },
#	},