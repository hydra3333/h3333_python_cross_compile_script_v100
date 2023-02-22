{ # http://git.savannah.gnu.org/cgit/freetype/freetype2.git/
	'repo_type' : 'archive',
	'download_locations' : [
		# HUH no: freetype 2.12.1 fails to build, with lots of link errors about duplicate definitions
		#{ 'url' : 'https://download.savannah.gnu.org/releases/freetype/freetype-2.12.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4766f20157cc4cf0cd292f80bf917f92d1c439b243ac3018debf6b9140c41a7f' }, ], },
		#{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.12.1/freetype-2.12.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4766f20157cc4cf0cd292f80bf917f92d1c439b243ac3018debf6b9140c41a7f' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/freetype-2.12.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4766f20157cc4cf0cd292f80bf917f92d1c439b243ac3018debf6b9140c41a7f' }, ], },
		{ 'url' : 'https://download.savannah.gnu.org/releases/freetype/freetype-2.13.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5ee23abd047636c24b2d43c6625dcafc66661d1aca64dec9e0d05df29592624c' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.13.0/freetype-2.13.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5ee23abd047636c24b2d43c6625dcafc66661d1aca64dec9e0d05df29592624c' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/freetype-2.13.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5ee23abd047636c24b2d43c6625dcafc66661d1aca64dec9e0d05df29592624c' }, ], },
	],
	'folder_name' : 'freetype-with-harfbuzz',
	'rename_folder' : 'freetype-with-harfbuzz',
	#'conf_system' : 'cmake',
	#'source_subfolder' : '_build',
	#'configure_options' : 
	#	'.. {cmake_prefix_options} '
	#	'-DCMAKE_INSTALL_PREFIX={target_prefix} '
	#	#'-DBUILD_SHARED_LIBS=OFF '
	#	'-DFT_WITH_HARFBUZZ=ON '
	#	'-DFT_WITH_ZLIB=ON '
	#	'-DFT_WITH_BZIP2=ON '
	#	'-DFT_WITH_PNG=ON '
	#,
	#'patches' : [
	#	('freetype2/freetype_cmake.patch', '-p1', '..')
	#],
	#'regex_replace': {
	#	'post_install': [
	#		{
	#			0: r'^Requires:(?:.+)?',
	#			'in_file': '{pkg_config_path}/freetype2.pc'
	#		},
	#		{
	#			0: r'Requires\.private:(.*)',
	#			1: r'Requires:\1',
	#			'in_file': '{pkg_config_path}/freetype2.pc'
	#		},
	#	],
	#},
    'configure_options' : '{autoconf_prefix_options} --build=x86_64-linux-gnu --with-zlib=yes --with-harfbuzz=yes ', # --without-png 
	'run_post_install' : [
		'sed -i.bak \'s/Libs: -L${{libdir}} -lfreetype.*/Libs: -L${{libdir}} -lfreetype -lbz2 -lharfbuzz/\' "{pkg_config_path}/freetype2.pc"',
    ],
	'run_post_regexreplace' : [
		'pwd ; sh ./autogen.sh ; pwd',
	],
	'depends_on': [
		'zlib', 'bzip2', 'libpng',
	],
	#'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', 'regex' : r'(?P<version_num>[\d.]+)'},
    'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '2.13.0', 'fancy_name' : 'freetype2-lib-with_harfbuzz' },
}
