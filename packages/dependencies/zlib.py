{ # 2019.12.13
	'repo_type' : 'git',
	'url' : 'https://github.com/madler/zlib.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	#'env_exports' : { # 2020.06.19
	#	'CFLAGS'   : ' {original_cflags} -fPIC ', # 2022.05.06 RDP says: For some reason glib needs -fPIC even though we build a static library
	#},
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DINSTALL_PKGCONFIG_DIR="{target_prefix}/lib/pkgconfig" '
							'-DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release '
							'-D_FILE_OFFSET_BITS=64 ', # 2019.12.13
	'depends_on' : [
		'pkg-config', 
	],
	'patches' : [
		('zlib/0001-mingw-workarounds.patch', '-p1', '..'),
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zlib' },
}
