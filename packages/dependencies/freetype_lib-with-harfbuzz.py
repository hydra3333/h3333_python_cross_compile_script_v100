{
	'repo_type' : 'git',
	'url': 'git://git.savannah.gnu.org/freetype/freetype2.git',
	'folder_name' : 'freetype-with-harfbuzz',
	'rename_folder' : 'freetype-with-harfbuzz',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release '
		'-DFT_WITH_HARFBUZZ=ON '
		'-DFT_WITH_ZLIB=ON '
		'-DFT_WITH_BZIP2=ON '
		'-DFT_WITH_PNG=ON '
	,
	'patches' : [
		('freetype2/freetype_cmake.patch', '-p1', '..')
	],
	'regex_replace': {
		'post_install': [
			{
				0: r'^Requires:(?:.+)?',
				'in_file': '{pkg_config_path}/freetype2.pc'
			},
			{
				0: r'Requires\.private:(.*)',
				1: r'Requires:\1',
				'in_file': '{pkg_config_path}/freetype2.pc'
			},
		],
	},
	'depends_on': [
		'zlib', 'bzip2', 'libpng',
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'freetype2' },
}
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f' }, ], },
#		{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.1/freetype-2.10.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f' }, ], },
#		{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f' }, ], },
#	],
#	'folder_name' : 'freetype-with-harfbuzz',
#	'rename_folder' : 'freetype-with-harfbuzz',
#	'configure_options' : '{autoconf_prefix_options} --build=x86_64-linux-gnu --with-zlib={target_prefix} --without-png --with-harfbuzz=yes',
#	'run_post_install' : [
#		'sed -i.bak \'s/Libs: -L${{libdir}} -lfreetype.*/Libs: -L${{libdir}} -lfreetype -lbz2 -lharfbuzz/\' "{pkg_config_path}/freetype2.pc"',
#	],
#	'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', },
#	'_info' : { 'version' : '2.10.1', 'fancy_name' : 'freetype2' },
#}

