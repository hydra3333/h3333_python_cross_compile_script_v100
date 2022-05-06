{ # cmake doesn't work, throws an issue with custom_cflags
	'repo_type' : 'archive', # 2020.05.11 change to download the archive
	'download_locations' : [ # https://www.libsdl.org/release/
		#{ 'url' : 'https://fossies.org/linux/misc/SDL2-2.0.20.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c56aba1d7b5b0e7e999e4a7698c70b63a3394ff9704b5f6e1c57e0c16f04dd06' }, ], },
		#{ 'url' : 'https://www.libsdl.org/release/SDL2-2.0.20.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c56aba1d7b5b0e7e999e4a7698c70b63a3394ff9704b5f6e1c57e0c16f04dd06' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/SDL2-2.0.22.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fe7cbf3127882e3fc7259a75a0cb585620272c51745d3852ab9dd87960697f2e' }, ], },
		{ 'url' : 'https://www.libsdl.org/release/SDL2-2.0.22.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fe7cbf3127882e3fc7259a75a0cb585620272c51745d3852ab9dd87960697f2e' }, ], },
	],
	#
	#'conf_system' : 'cmake',
	## Hmm, SDL2 is fussy about CFLAGS and leading/trailing whitespace
	##'custom_cflag' : '-O3 -fstack-protector-all -D_FORTIFY_SOURCE=2', # 2020.05.13
	#'custom_cflag' : '{original_cflags_trim}', # 2020.05.13  Target "SDL2-static" links to item " -O3 -fstack-protector-all -D_FORTIFY_SOURCE=2 " which has leading or trailing whitespace.  This is now an error according to policy CMP0004.
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DSDL_SHARED=OFF',
	#'source_subfolder': '_build',
	#'regex_replace': {
	#	'post_patch': [
	#		{
	#			0: r'if\(NOT WINDOWS OR CYGWIN\)',
	#			1: r'if(NOT MSVC OR CYGWIN)',
	#			'in_file': '../CMakeLists.txt' # why "WINDOWS", why not "MSVC"...
	#		},
	#		{
	#			0: r'if\(NOT \(WINDOWS OR CYGWIN\)\)',
	#			1: r'if(NOT (MSVC OR CYGWIN))',
	#			'in_file': '../CMakeLists.txt'
	#		},
	#	],
	#},
	#'run_post_regexreplace' : (
	#	'../autogen.sh --build-w64 ',							 
	#),
	#
	'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
	'regex_replace': {
		'post_patch': [
			{
				0: r'if\(NOT WINDOWS OR CYGWIN\)',
				1: r'if(NOT MSVC OR CYGWIN)',
				'in_file': './CMakeLists.txt' # why "WINDOWS", why not "MSVC"...
			},
			{
				0: r'if\(NOT \(WINDOWS OR CYGWIN\)\)',
				1: r'if(NOT (MSVC OR CYGWIN))',
				'in_file': './CMakeLists.txt'
			},
		],
	},
	'run_post_regexreplace' : (
		'./autogen.sh --build-w64 ',							 
	),
	#'run_post_install': ( # 2019.12.13 added these 2 sed lines # 2020.05.11 comment this stuff out like deadsix27
	#	'sed -i.bak "s/  -lmingw32 -lSDL2main -lSDL2 /  -lmingw32 -lSDL2main -lSDL2  -ldinput8 -ldxguid -ldxerr8 -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lshell32 -lversion -luuid/" "{pkg_config_path}/sdl2.pc"', # allow ffmpeg to output anything to console :|
	#	'cp -fv "{target_prefix}/bin/sdl2-config" "{cross_prefix_full}sdl2-config"', # this is the only mingw dir in the PATH so use it for now [though FFmpeg doesn't use it?]
	#),
	'update_check' : { 'url' : 'https://www.libsdl.org/release/', 'type' : 'httpindex', 'regex' : r'SDL2-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '2.0.22', 'fancy_name' : 'SDL2' },
}
