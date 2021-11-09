{
	'repo_type' : 'git',
	'url' : 'https://github.com/MediaArea/MediaInfoLib.git',    # https://github.com/MediaArea/MediaInfoLib
	'depth_git' : 0,
	#'branch' : 'tags/v21.09', # 2021.10.31 A RELEASE
	'recursive_git' : True,
	'source_subfolder' : 'Project/GNU/Library',
	#
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://github.com/MediaArea/MediaInfoLib/archive/refs/tags/v21.09.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6db61bef0ad5b126d17bb59210c240f33fafb3450946e7b114d7884abf6e99fb' }, ], }, # https://github.com/MediaArea/MediaInfoLib/releases
	#],
	#'folder_name' : 'MediaInfoLib-21.09',
	#'source_subfolder' : 'Project/GNU/Library',
	#
	'configure_options' : '--host={target_host} --prefix={target_prefix} --enable-shared --enable-static --with-libcurl --with-libmms --with-libmediainfo-name=MediaInfo.dll', # --enable-static --disable-shared --enable-shared=no
	'custom_cflag' : '-D__USE_MINGW_ANSI_STDIO=1 {original_cflags}', # 2019.12.13
    #'patches' : [ # 2021.11.09 see if latest upstream commit resolves it
    #    ('mediainfolib/mediainfolib-patch-per-mabs-commit-2b8ffd6034953cae46765c4e50380f03d508f24a.patch', '-p1', "../../.."), # see https://github.com/MediaArea/MediaInfoLib/issues/1449 
	#],
	'run_post_regexreplace' : [
		#'sed -i.bak \'s/Windows.h/windows.h/g\' ../../../Source/MediaInfo/Reader/Reader_File.h',	# no longer needed
		#'sed -i.bak \'s/Windows.h/windows.h/g\' ../../../Source/MediaInfo/Reader/Reader_File.cpp', # no longer needed
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
