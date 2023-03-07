{ # 2019.12.13
	'repo_type' : 'git',
	'url' : 'https://github.com/madler/zlib.git',
	'conf_system' : 'cmake',
	'folder_name' : 'ffms2_zlib',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX="{output_prefix}/ffms2_dll.installed" -DINSTALL_PKGCONFIG_DIR="{output_prefix}/ffms2_dll.installed/lib/pkgconfig" '
							'-DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release '
							'-D_FILE_OFFSET_BITS=64 ', # 2019.12.13
	'patches' : [
		('zlib/0001-mingw-workarounds.patch', '-p1', '..'),
	],
	'depends_on' : [
		'pkg-config', 
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffms2_zlib' },
}
