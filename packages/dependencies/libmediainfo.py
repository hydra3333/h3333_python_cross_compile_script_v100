{
	'repo_type' : 'git',
	'source_subfolder' : 'Project/GNU/Library',
	'url' : 'https://github.com/MediaArea/MediaInfoLib.git',
	'recursive_git' : True,
	'configure_options' : '--host={target_host} --prefix={target_prefix} --enable-shared --enable-static --with-libcurl --with-libmms --with-libmediainfo-name=MediaInfo.dll', # --enable-static --disable-shared --enable-shared=no
	'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.12.13
	'run_post_regexreplace' : [
		'sed -i.bak \'s/Windows.h/windows.h/\' ../../../Source/MediaInfo/Reader/Reader_File.h',
		'sed -i.bak \'s/Windows.h/windows.h/\' ../../../Source/MediaInfo/Reader/Reader_File.cpp',
        './autogen.sh NOCONFIGURE=1',
        'autoreconf -fiv',
	],
	'run_post_configure' : [
		'sed -i.bak \'s/ -DSIZE_T_IS_LONG//g\' Makefile',
	],
	'depends_on': [
		'zenlib', 'libcurl',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmediainfo' },
}
