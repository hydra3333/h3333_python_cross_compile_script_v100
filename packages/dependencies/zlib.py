{ # 2019.12.13
	'repo_type' : 'git',
	'url' : 'https://github.com/madler/zlib.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' :	'.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DINSTALL_PKGCONFIG_DIR="{target_prefix}/lib/pkgconfig" '
							'-DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release '
							'-D_FILE_OFFSET_BITS=64 ', # 2019.12.13
	'patches' : [
		('zlib/0001-mingw-workarounds.patch', '-p1', '..'),
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zlib' },
}
# 2019.12.13 old:
#	'zlib' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/madler/zlib.git',
#		'env_exports' : {
#			'AR' : '{cross_prefix_bare}ar',
#			'CC' : '{cross_prefix_bare}gcc',
#			'PREFIX' : '{target_prefix}',
#			'RANLIB' : '{cross_prefix_bare}ranlib',
#			'LD'     : '{cross_prefix_bare}ld',
#			'STRIP'  : '{cross_prefix_bare}strip',
#			'CXX'    : '{cross_prefix_bare}g++',
#		},
#		'configure_options': '--static --prefix={target_prefix}',
#		'build_options': '{make_prefix_options} ARFLAGS=rcs',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zlib' },
#	},
