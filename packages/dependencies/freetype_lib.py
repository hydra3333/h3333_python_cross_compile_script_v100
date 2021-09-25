{ # http://git.savannah.gnu.org/cgit/freetype/freetype2.git/
	#'repo_type' : 'git',
	#'url': 'git://git.savannah.gnu.org/freetype/freetype2.git', # http://savannah.nongnu.org/projects/freetype
	#'depth_git' : 0,
	#'branch' : '13c0df80dca59ce2ef3ec125b08c5b6ea485535c', # 2020.04.10 to get ffmpeg to build http://savannah.nongnu.org/bugs/index.php
	# 2020.05.13 back down to a fixed soutce so it doesn;t keet building when the git changes
	#            since when that happens, it rebuilds with harfbuzz out-of-order :( and that causes link fails later (eg ffmpeg blaming libbluray when it isn't that)
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1543d61025d2e6312e0a1c563652555f17378a204a61e99928c9fcef030a2d8b' }, ], },
		#{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.2/freetype-2.10.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1543d61025d2e6312e0a1c563652555f17378a204a61e99928c9fcef030a2d8b' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784' }, ], }, # 2020.11.05
		#{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.4/freetype-2.10.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784' }, ], }, # 2020.11.05
		{ 'url' : 'https://fossies.org/linux/misc/freetype-2.11.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.11.0/freetype-2.11.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7' }, ], },

	],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DBUILD_SHARED_LIBS=OFF ' # was commented out 2021.09.25
		'-DFT_WITH_HARFBUZZ=OFF '
		'-DFT_WITH_ZLIB=ON '
		'-DFT_WITH_BZIP2=ON '
		'-DFT_WITH_PNG=ON '
	,
	#'patches' : [
	#	('freetype2/freetype_cmake.patch', '-p1', '..') # 2021.09.25 patch no longer required ?
	#],
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
	'run_post_regexreplace': ( # 2021.09.25
		'sed -i.bak "s/find_package(BZip2)/find_package(BZip2 REQUIRED)/" "../CMakeLists.txt"',
	),
	'depends_on': [
		'zlib', 'bzip2', 'libpng',
	],
	#'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', 'regex' : r'(?P<version_num>[\d.]+)'},
	'_info' : { 'version' : '2.11.0', 'fancy_name' : 'freetype2' },
}
