{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_4_3/expat-2.4.3.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : 'b1f9f1b1a5ebb0acaa88c9ff79bfa4e145823b78aa5185e5c5d85f060824778a' },	], },
		#{ 'url' : 'https://fossies.org/linux/www/expat-2.4.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b1f9f1b1a5ebb0acaa88c9ff79bfa4e145823b78aa5185e5c5d85f060824778a' }, ],	},
		{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_4_8/expat-2.4.8.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : 'f79b8f904b749e3e0d20afeadecf8249c55b2e32d4ebb089ae378df479dcaf25' },	], },
		{ 'url' : 'https://fossies.org/linux/www/expat-2.4.8.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f79b8f904b749e3e0d20afeadecf8249c55b2e32d4ebb089ae378df479dcaf25' }, ],	},
	],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'custom_cflag' : '{original_cflags} -DXML_LARGE_SIZE',
	#'run_post_regexreplace': ( # 2020.03.19 comment out
	#	'sed -i.bak "s/SUBDIRS += xmlwf doc/SUBDIRS += xmlwf/" "./Makefile.am"',
	#), 
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release -DEXPAT_BUILD_EXAMPLES=OFF -DEXPAT_SHARED_LIBS=OFF -DEXPAT_BUILD_DOCS=OFF -DEXPAT_BUILD_TESTS=OFF -DEXPAT_BUILD_TOOLS=OFF -DEXPAT_LARGE_SIZE=ON',
	'update_check' : { 'url' : 'https://github.com/libexpat/libexpat/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	'_info' : { 'version' : '2.4.8', 'fancy_name' : 'expat' },
}
