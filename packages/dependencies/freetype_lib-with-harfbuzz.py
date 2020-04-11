{ # http://git.savannah.gnu.org/cgit/freetype/freetype2.git/
	'repo_type' : 'git',
	'url': 'git://git.savannah.gnu.org/freetype/freetype2.git', # http://savannah.nongnu.org/projects/freetype
	'depth_git' : 0,
	#'branch' : '7a019a63ed9753772e758beec3cad7c0b74ee2aa', # 2020.04.10 to get ffmpeg to build http://savannah.nongnu.org/bugs/index.php
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f' }, ], },
	#],
	'folder_name' : 'freetype-with-harfbuzz',
	'rename_folder' : 'freetype-with-harfbuzz',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		#'-DBUILD_SHARED_LIBS=OFF '
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
