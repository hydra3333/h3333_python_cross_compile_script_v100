{
	'repo_type' : 'mercurial',
	'url' : 'https://hg.libsdl.org/SDL',
	'folder_name' : 'sdl2_hg',
	'source_subfolder': '_build',
	'conf_system' : 'cmake',
    'custom_cflag' : '{original_cflags} -DDECLSPEC=', # 2019.12.13
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DSDL_SHARED=OFF',
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
# 2019.12.13 old:
#	'sdl2' : {
#		'folder_name' : 'sdl2_merc',
#		'repo_type' : 'mercurial',
#		'source_subfolder' : '_build',
#		'url' : 'https://hg.libsdl.org/SDL',
#		'configure_path' : '../configure',
#		'run_post_patch' : [
#			'sed -i.bak "s/ -mwindows//" ../configure',
#		],
#		# SDL2 patch superseded per https://hg.libsdl.org/SDL/rev/117d4ce1390e
#		#'patches' : (
#		#	('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/sdl2/0001-SDL2_hg.xinput_state_ex.patch', '-p1', '..'),
#		#),
#		'custom_cflag' : '-DDECLSPEC= {original_cflags}', # avoid SDL trac tickets 939 and 282, and not worried about optimizing yet...
#		"run_post_install": (
#			'sed -i.bak "s/  -lmingw32 -lSDL2main -lSDL2 /  -lmingw32 -lSDL2main -lSDL2  -ldinput8 -ldxguid -ldxerr8 -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lshell32 -lversion -luuid/" "{pkg_config_path}/sdl2.pc"', # allow ffmpeg to output anything to console :|
#			#'sed -i.bak "s/-mwindows/-ldinput8 -ldxguid -ldxerr8 -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lshell32 -lversion -luuid/" "{target_prefix}/bin/sdl2-config"', # update this one too for good measure, FFmpeg can use either, not sure which one it defaults to...
#			'cp -fv "{target_prefix}/bin/sdl2-config" "{cross_prefix_full}sdl2-config"', # this is the only mingw dir in the PATH so use it for now [though FFmpeg doesn't use it?]
#		),
#		'configure_options': '--prefix={target_prefix} --host={target_host} --disable-shared --enable-static',
#		'_info' : { 'version' : 'mercurial (default)', 'fancy_name' : 'SDL2' },
#	},
	