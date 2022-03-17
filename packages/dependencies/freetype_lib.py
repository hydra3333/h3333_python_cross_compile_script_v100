{ # http://git.savannah.gnu.org/cgit/freetype/freetype2.git/
	'repo_type' : 'archive',
	'download_locations' : [
        # freetype 2.11.0 kills mp4box building, so keep freetype 2.10.4 ? mp4box fails anyway so just keep going
		#{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.4/freetype-2.10.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784' }, ], }, # 2020.11.05
		#{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784' }, ], }, # 2020.11.05
        #{ 'url' : 'https://download.savannah.gnu.org/releases/freetype/freetype-2.11.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7' }, ], },
		#{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.11.0/freetype-2.11.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/freetype-2.11.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8bee39bd3968c4804b70614a0a3ad597299ad0e824bc8aad5ce8aaf48067bde7' }, ], },
        { 'url' : 'https://download.savannah.gnu.org/releases/freetype/freetype-2.11.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3333ae7cfda88429c97a7ae63b7d01ab398076c3b67182e960e5684050f2c5c8' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.11.1/freetype-2.11.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3333ae7cfda88429c97a7ae63b7d01ab398076c3b67182e960e5684050f2c5c8' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/freetype-2.11.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3333ae7cfda88429c97a7ae63b7d01ab398076c3b67182e960e5684050f2c5c8' }, ], },
	],
	#'conf_system' : 'cmake',
	#'source_subfolder' : '_build',
	#'configure_options' : 
	#	'.. {cmake_prefix_options} '
	#	'-DCMAKE_INSTALL_PREFIX={target_prefix} '
	#	#'-DBUILD_SHARED_LIBS=OFF '
	#	'-DFT_WITH_HARFBUZZ=OFF '
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
    'configure_options' : '{autoconf_prefix_options} --build=x86_64-linux-gnu --with-zlib={target_prefix} --with-harfbuzz=no ', # --without-png 
	#'run_post_install' : [
	#	'sed -i.bak \'s/Libs: -L${{libdir}} -lfreetype.*/Libs: -L${{libdir}} -lfreetype -lbz2 -lharfbuzz/\' "{pkg_config_path}/freetype2.pc"',
    #],
	'run_post_regexreplace' : [
		#'pwd ; cd .. ; sh ./autogen.sh ; cd _build ; pwd',
		'sh ./autogen.sh',
	],
	'depends_on': [
		'zlib', 'bzip2', 'libpng',
	],
	#'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', 'regex' : r'(?P<version_num>[\d.]+)'},
    'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '2.11.1', 'fancy_name' : 'freetype2_lib' },
}
