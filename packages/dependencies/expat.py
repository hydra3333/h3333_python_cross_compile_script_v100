{
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_4_8/expat-2.4.8.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : 'f79b8f904b749e3e0d20afeadecf8249c55b2e32d4ebb089ae378df479dcaf25' },	], },
	#	{ 'url' : 'https://fossies.org/linux/www/expat-2.4.8.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f79b8f904b749e3e0d20afeadecf8249c55b2e32d4ebb089ae378df479dcaf25' }, ],	},
	#	# Ugn, version 2.4.9 produces a .dll and not a .a ... reported in https://github.com/libexpat/libexpat/issues/662
	#	#{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_4_9/expat-2.4.9.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '6e8c0728fe5c7cd3f93a6acce43046c5e4736c7b4b68e032e9350daa0efc0354' },	], },
	#	#{ 'url' : 'https://fossies.org/linux/www/expat-2.4.9.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6e8c0728fe5c7cd3f93a6acce43046c5e4736c7b4b68e032e9350daa0efc0354' }, ],	},
	#],
	
	'repo_type' : 'git',
	'url' : 'https://github.com/libexpat/libexpat',
	#'recursive_git' : True,
	'depth_git' : 0,
	#'branch' : '',
	'source_subfolder' : 'expat/_build', # 2022.10.16 folder changed from _build once we went to using git :(
	'conf_system' : 'cmake',
	'custom_cflag' : '{original_cflags} -DXML_LARGE_SIZE',
	#'run_post_regexreplace': ( # 2020.03.19 comment out
	#	'sed -i.bak "s/SUBDIRS += xmlwf doc/SUBDIRS += xmlwf/" "./Makefile.am"',
	#), 
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release -DEXPAT_BUILD_EXAMPLES=OFF -DEXPAT_SHARED_LIBS=OFF -DEXPAT_BUILD_DOCS=OFF -DEXPAT_BUILD_TESTS=OFF -DEXPAT_BUILD_TOOLS=OFF -DEXPAT_LARGE_SIZE=ON',
	#'update_check' : { 'url' : 'https://github.com/libexpat/libexpat/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	'update_check' : { 'type' : 'git', },
	#'_info' : { 'version' : '2.4.8', 'fancy_name' : 'expat' },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'expat' },
}
