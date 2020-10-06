{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_2_9/expat-2.2.9.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '1ea6965b15c2106b6bbe883397271c80dfa0331cdf821b2c319591b55eadc0a4' },	], },
		#{ 'url' : 'https://fossies.org/linux/www/expat-2.2.9.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1ea6965b15c2106b6bbe883397271c80dfa0331cdf821b2c319591b55eadc0a4' }, ],	},
		{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_2_10/expat-2.2.10.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '5dfe538f8b5b63f03e98edac520d7d9a6a4d22e482e5c96d4d06fcc5485c25f2' },	], },
		{ 'url' : 'https://fossies.org/linux/www/expat-2.2.10.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5dfe538f8b5b63f03e98edac520d7d9a6a4d22e482e5c96d4d06fcc5485c25f2' }, ],	},
	],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'custom_cflag' : '{original_cflags} -DXML_LARGE_SIZE',
	#'run_post_regexreplace': ( # 2020.03.19 comment out
	#	'sed -i.bak "s/SUBDIRS += xmlwf doc/SUBDIRS += xmlwf/" "./Makefile.am"',
	#), 
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release -DEXPAT_BUILD_EXAMPLES=OFF -DEXPAT_SHARED_LIBS=OFF -DEXPAT_BUILD_DOCS=OFF -DEXPAT_BUILD_TESTS=OFF -DEXPAT_BUILD_TOOLS=OFF -DEXPAT_LARGE_SIZE=ON',
	'update_check' : { 'url' : 'https://github.com/libexpat/libexpat/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	'_info' : { 'version' : '2.2.10', 'fancy_name' : 'expat' },
}
