{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_4_1/expat-2.4.1.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : 'cf032d0dba9b928636548e32b327a2d66b1aab63c4f4a13dd132c2d1d2f2fb6a' },	], },
		#{ 'url' : 'https://fossies.org/linux/www/expat-2.4.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cf032d0dba9b928636548e32b327a2d66b1aab63c4f4a13dd132c2d1d2f2fb6a' }, ],	},
		{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_4_2/expat-2.4.2.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : 'bc2ff58f49c29aac7bff705a6c167a821f26c512079ff08ac432fd0fdc9bb199' },	], },
		{ 'url' : 'https://fossies.org/linux/www/expat-2.4.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'bc2ff58f49c29aac7bff705a6c167a821f26c512079ff08ac432fd0fdc9bb199' }, ],	},
	],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'custom_cflag' : '{original_cflags} -DXML_LARGE_SIZE',
	#'run_post_regexreplace': ( # 2020.03.19 comment out
	#	'sed -i.bak "s/SUBDIRS += xmlwf doc/SUBDIRS += xmlwf/" "./Makefile.am"',
	#), 
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release -DEXPAT_BUILD_EXAMPLES=OFF -DEXPAT_SHARED_LIBS=OFF -DEXPAT_BUILD_DOCS=OFF -DEXPAT_BUILD_TESTS=OFF -DEXPAT_BUILD_TOOLS=OFF -DEXPAT_LARGE_SIZE=ON',
	'update_check' : { 'url' : 'https://github.com/libexpat/libexpat/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	'_info' : { 'version' : '2.4.2', 'fancy_name' : 'expat' },
}
