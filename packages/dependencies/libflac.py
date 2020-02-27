{ # 2019.12.13 ---- using "cmake" results in stdlib.h: No such file or directory !!!!!!!!!!!!!!
	#
	# In file included from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/ext/string_conversions.h:41,
    #             from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/bits/basic_string.h:6493,
    #             from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/string:55,
    #             from ../include/FLAC++/decoder.h:38,
    #             from ../src/libFLAC++/stream_decoder.cpp:37:
	# /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/cstdlib:75:15: fatal error: stdlib.h: No such file or directory
	# 75 | #include_next <stdlib.h>
	#'repo_type' : 'git',
	#'url' : 'https://github.com/xiph/flac.git',
	#'conf_system' : 'cmake',
	#'source_subfolder' : '_build',
   	#'custom_cflag' : '{original_cflags}', # 2019.12.13
	#'env_exports' : {# 2019.12.13
	#	'PKGCONFIG' : 'pkg-config',# 2019.12.13
	#}, # 2019.12.13
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_64_BIT_WORDS=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release', # 2019.12.13 try to add -DENABLE_64_BIT_WORDS=ON (default was OFF)
	#'patches': [
	#	('flac/0001-mingw-fix.patch', '-p1', '..'),
	#],
	#'regex_replace': {
	#	'post_patch': [
	#		{
	#			0: r'add_subdirectory\("microbench"\)',
	#			'in_file': '../CMakeLists.txt'
	#		},
	#	],
	#},
	#'depends_on' : [
	#	'libogg',
	#],
	#'_info' : { 'version' : None, 'fancy_name' : 'flac (library)' },
	#
	# 2019.12.13 REVERT TO NON cmake ---- using "cmake" results in stdlib.h: No such file or directory !!!!!!!!!!!!!!
	#
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/flac', #'url' : 'https://git.xiph.org/flac.git',
	'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-64-bit-words --disable-oggtest --disable-examples --disable-rpath --disable-xmms-plugin --with-pic ', # 2018.11.23 ensure 64bit
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	#'patches': [
	#	('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/flac/0001-mingw-fix.patch', '-p1'), # , '..'),
	#],
	'patches': [
		('flac/0001-mingw-fix.patch', '-p1', '..'),
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r'add_subdirectory\("microbench"\)',
				'in_file': './CMakeLists.txt' # 2019.13.13 not cmalke, so is in current folder not '../CMakeLists.txt'
			},
		],
	},
	'depends_on': [
		'libogg',
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'flac (library)' },
}
#
# 2019.12.13 old:
#	'libflac' : { # https://git.xiph.org/?p=flac.git;a%3Dsummary # https://bitbucket.org/mpyne/game-music-emu/issues/36/commit
#		'repo_type' : 'git',
#		#'url' : 'https://git.xiph.org/flac.git',
#		'url' : 'https://github.com/xiph/flac',
#		#'branch' : 'tags/1.3.3',
#		#'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-64-bit-words --disable-oggtest --disable-examples --disable-rpath --disable-xmms-plugin --with-pic ', # 2018.11.23 ensure 64bit
#		'custom_cflag' : '{original_cflags}', #-DFLAC__USE_VISIBILITY_ATTR=OFF ', # 2019.10.19 D_FORTIFY_SOURCE=0' # 2019.11.02 added -DFLAC__USE_VISIBILITY_ATTR=FFF and yet to try ON as well # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		'env_exports' : {
#			'PKGCONFIG' : 'pkg-config',
#			'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		},
#		'patches': [
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/flac/0001-mingw-fix.patch', '-p1'), # , '..'),
#			#('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/flac/0002-cmakelists-libs.patch', '-p1'), # , '..'),
#		],
#		'depends_on': [
#			'libogg',
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'flac (library)' },
#	},