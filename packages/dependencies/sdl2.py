{
	'repo_type' : 'mercurial',
	'url' : 'https://hg.libsdl.org/SDL',
	'folder_name' : 'sdl2_hg',

	'conf_system' : 'cmake',
    'custom_cflag' : '-DDECLSPEC= {original_cflags}', # 2019.12.13
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DSDL_SHARED=OFF',
	'source_subfolder': '_build',

	'regex_replace': {
		'post_patch': [
			{
				0: r'if\(NOT WINDOWS OR CYGWIN\)',
				1: r'if(NOT MSVC OR CYGWIN)',
				'in_file': '../CMakeLists.txt' # why "WINDOWS", why not "MSVC"...
			},
			{
				0: r'if\(NOT \(WINDOWS OR CYGWIN\)\)',
				1: r'if(NOT (MSVC OR CYGWIN))',
				'in_file': '../CMakeLists.txt'
			},
		],
	},
    'run_post_install': ( # 2019.12.13 added these 2 sed lines
		'sed -i.bak "s/  -lmingw32 -lSDL2main -lSDL2 /  -lmingw32 -lSDL2main -lSDL2  -ldinput8 -ldxguid -ldxerr8 -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lshell32 -lversion -luuid/" "{pkg_config_path}/sdl2.pc"', # allow ffmpeg to output anything to console :|
		'cp -fv "{target_prefix}/bin/sdl2-config" "{cross_prefix_full}sdl2-config"', # this is the only mingw dir in the PATH so use it for now [though FFmpeg doesn't use it?]
		),
	'_info' : { 'version' : None, 'fancy_name' : 'SDL2' },
}