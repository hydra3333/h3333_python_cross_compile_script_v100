{ # http://git.savannah.gnu.org/cgit/freetype/freetype2.git/
	#'repo_type' : 'git',
	#'url': 'git://git.savannah.gnu.org/freetype/freetype2.git', # http://savannah.nongnu.org/projects/freetype
	#'depth_git' : 0,
	#'branch' : '7a019a63ed9753772e758beec3cad7c0b74ee2aa', # 2020.04.10 to get ffmpeg to build http://savannah.nongnu.org/bugs/index.php
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1543d61025d2e6312e0a1c563652555f17378a204a61e99928c9fcef030a2d8b' }, ], },
		#{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.2/freetype-2.10.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1543d61025d2e6312e0a1c563652555f17378a204a61e99928c9fcef030a2d8b' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.4/freetype-2.10.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784' }, ], }, # 2020.11.05
		{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784' }, ], }, # 2020.11.05
	],
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
	#'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', 'regex' : r'(?P<version_num>[\d.]+)'},
	'_info' : { 'version' : '2.10.4', 'fancy_name' : 'freetype2' },
}
