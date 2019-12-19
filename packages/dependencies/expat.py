{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://github.com/libexpat/libexpat/releases/download/R_2_2_9/expat-2.2.9.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '1ea6965b15c2106b6bbe883397271c80dfa0331cdf821b2c319591b55eadc0a4' },	], },
		{ 'url' : 'https://fossies.org/linux/www/expat-2.2.9.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1ea6965b15c2106b6bbe883397271c80dfa0331cdf821b2c319591b55eadc0a4' }, ],	},
	],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'custom_cflag' : '{original_cflags} -DXML_LARGE_SIZE',
	'run_post_patch': ( # 2019.12.13
		'sed -i.bak "s/SUBDIRS += xmlwf doc/SUBDIRS += xmlwf/" ."./Makefile.am"',
	), 
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release -DEXPAT_BUILD_EXAMPLES=OFF -DEXPAT_SHARED_LIBS=OFF -DEXPAT_BUILD_DOCS=OFF -DEXPAT_BUILD_TESTS=OFF -DEXPAT_BUILD_TOOLS=OFF -DEXPAT_LARGE_SIZE=ON',
	'update_check' : { 'url' : 'https://github.com/libexpat/libexpat/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	'_info' : { 'version' : '2.2.9', 'fancy_name' : 'expat' },
}
# 2019.12.13 old:
#	'expat' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://github.com/libexpat/libexpat/releases
#			{ "url" : "https://github.com/libexpat/libexpat/releases/download/R_2_2_9/expat-2.2.9.tar.xz",	"hashes" : [ { "type" : "sha256", "sum" : "1ea6965b15c2106b6bbe883397271c80dfa0331cdf821b2c319591b55eadc0a4" },	], },
#			{ "url" : "https://fossies.org/linux/www/expat-2.2.9.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "1ea6965b15c2106b6bbe883397271c80dfa0331cdf821b2c319591b55eadc0a4" }, ],	},
#		],
#		'env_exports' : {
#			'CPPFLAGS' : '-DXML_LARGE_SIZE',
#		},
#		'run_post_patch': (
#			'sed -i.bak "s/SUBDIRS += xmlwf doc/SUBDIRS += xmlwf/" Makefile.am',
#			'aclocal',
#			'automake',
#		),
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --without-docbook',
#		'_info' : { 'version' : '2.2.9', 'fancy_name' : 'expat' },
#	},
