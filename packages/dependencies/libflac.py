{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/flac.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
   	'custom_cflag' : '{original_cflags}', # 2019.12.13
	'env_exports' : {# 2019.12.13
		'PKGCONFIG' : 'pkg-config',# 2019.12.13
		'CFLAGS'   : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CXXFLAGS' : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CPPFLAGS' : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'LDFLAGS'  : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
	}, # 2019.12.13
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_64_BIT_WORDS=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release', # 2019.12.13 try to add -DENABLE_64_BIT_WORDS=ON (default was OFF)
	'patches': [
		('flac/0001-mingw-fix.patch', '-p1', '..'),
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r'add_subdirectory\("microbench"\)',
				'in_file': '../CMakeLists.txt'
			},
		],
	},
	'depends_on' : [
		'libogg',
	],
	'_info' : { 'version' : None, 'fancy_name' : 'flac (library)' },
}
