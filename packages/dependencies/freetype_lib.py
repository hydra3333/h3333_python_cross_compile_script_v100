{ # http://git.savannah.gnu.org/cgit/freetype/freetype2.git/
	'repo_type' : 'git',
	'url': 'git://git.savannah.gnu.org/freetype/freetype2.git', # http://savannah.nongnu.org/projects/freetype
	'depth_git' : 0,
	'branch' : '13c0df80dca59ce2ef3ec125b08c5b6ea485535c', # 2020.04.10 to get ffmpeg to build
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f' }, ], },
	#],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		#'-DBUILD_SHARED_LIBS=OFF '
		'-DFT_WITH_HARFBUZZ=OFF '
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
#	'configure_options' : '{autoconf_prefix_options} --build=x86_64-linux-gnu --disable-shared --enable-static --with-zlib={target_prefix} --with-zlib={target_prefix} --without-png --with-harfbuzz=no', # TODO get rid of hardcoded build variable ## 2019.12.15 ensured static # 2019.12.13
#    'depends_on': [
#		'zlib', 'bzip2', 'libpng',
#	],
#	'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', },
#	'_info' : { 'version' : '2.10.1', 'fancy_name' : 'freetype2 lib' },
#}
# 2019.12.13 old:
#	'freetype_lib' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://sourceforge.net/projects/freetype/files/freetype2/
#			{ "url" : "https://fossies.org/linux/misc/freetype-2.10.1.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f" }, ], },
#			{ "url" : "https://sourceforge.net/projects/freetype/files/freetype2/2.10.1/freetype-2.10.1.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f" }, ], },
#			{ "url" : "https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f" }, ], },
#		],
#		'configure_options': '--host={target_host} --build=x86_64-linux-gnu --prefix={target_prefix} --disable-shared --enable-static --with-zlib={target_prefix} --without-png --with-harfbuzz=no',
#		'_info' : { 'version' : '2.10.1', 'fancy_name' : 'freetype2' },
#	},
