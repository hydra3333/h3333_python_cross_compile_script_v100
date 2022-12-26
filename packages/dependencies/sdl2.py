{
	#
	#'repo_type' : 'archive', # 2020.05.11 change to download the archive  # 2022.12.18 per DEADSIX27
	#'download_locations' : [ # https://www.libsdl.org/release/ https://fossies.org/linux/misc # 2022.12.18 per DEADSIX27
	#	{ 'url' : 'https://fossies.org/linux/misc/SDL2-2.26.1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '02537cc7ebd74071631038b237ec4bfbb3f4830ba019e569434da33f42373e04' }, ], }, # 2022.12.18 per DEADSIX27
	#	#{ 'url' : 'https://www.libsdl.org/release/SDL2-devel-2.26.1-mingw.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '02537cc7ebd74071631038b237ec4bfbb3f4830ba019e569434da33f42373e04' }, ], }, # 2022.12.18 per DEADSIX27
	#], # 2022.12.18 per DEADSIX27
	#
	'repo_type' : 'git', # 2022.12.18 per DEADSIX27
	'url' : 'https://github.com/libsdl-org/SDL', # 2022.12.18 per DEADSIX27
	'depth_git': 0, # 2022.12.18 per DEADSIX27
	'branch': 'SDL2', # 2022.12.18 per DEADSIX27
	'source_subfolder': '_build', # 2022.12.18 per DEADSIX27
	'env_exports' : {
		'DXSDK_DIR'  : '{target_prefix}/include', # 2022.12.18 per DEADSIX27
	},
	'conf_system' : 'cmake', # 2022.12.18 per DEADSIX27 added
	#
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DSDL_SHARED=OFF ', # 2022.12.21 from deadsix27 this builds seemingly
	#
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DBUILD_SHARED_LIBS=OFF '
		'-DSDL_SHARED=OFF '
		'-DSDL_STATIC=ON '
		'-DSDL_TEST=OFF -DSDL_TESTS=OFF -DSDL_INSTALL_TESTS=OFF '
		'-DSDL_STATIC_PIC=ON '
		'-DSDL_ASSERTIONS=release '
		'-DSDL_PTHREADS=ON '
		#'-DSDL_LIBSAMPLERATE=ON ' # 2022.12.21 - if we use this then, later, ffmpeg fails to build by chucking an error during configure
		'-DSDL_VULKAN=ON '
	,
	#
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DSDL_SHARED=OFF -DSDL_STATIC=ON -DBUILD_SHARED_LIBS=OFF '
	#	'-DSDL_TEST=OFF -DSDL_TESTS=OFF -DSDL_INSTALL_TESTS=OFF '
	#	'-DSDL_STATIC_PIC=ON '
	#	'-DSDL_ASSERTIONS=release '
	#	'-DSDL_PTHREADS=ON '
	#	'-DSDL_LIBSAMPLERATE=ON '
	#	'-DSDL_VULKAN=ON '
	#,
	#
	'run_post_patch' : [ # before regex_replace though
		'rm -fvR {target_prefix}/include/SDL2',
		'rm -fvR {target_prefix}/lib/cmake/SDL2',
		'rm -fvR {target_prefix}/bin/sdl2-config',
		'rm -fv "../CMakeLists.txt.orig"',
		'cp -fv "../CMakeLists.txt" "../CMakeLists.txt.orig"',
	],
	'regex_replace': {
		'post_patch': [  # 2022.12.18 per DEADSIX27 ... BUT these 2 result in NIL changes
			{
				0: r'if\(NOT WINDOWS OR CYGWIN OR MINGW\)',
				1: r'if(NOT APPLE)',
				'in_file': '../CMakeLists.txt'
			},
			{
				0: r'if\(NOT \(WINDOWS OR CYGWIN OR MINGW\)\)',
				1: r'if(NOT APPLE)',
				'in_file': '../CMakeLists.txt'
			},
		],
	},
	'run_post_regexreplace' : (
		'pwd ; cd .. ; sh ./autogen.sh --build-w64 ; cd _build ; pwd', # 2022.12.21 change directories for this now
		'diff -U 5 "../CMakeLists.txt.orig" "../CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"', 
	),
	#'run_post_install': ( # 2019.12.13 added these 2 sed lines # 2020.05.11 comment this stuff out like deadsix27
	#	'sed -i.bak "s/  -lmingw32 -lSDL2main -lSDL2 /  -lmingw32 -lSDL2main -lSDL2  -ldinput8 -ldxguid -ldxerr8 -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lshell32 -lversion -luuid/" "{pkg_config_path}/sdl2.pc"', # allow ffmpeg to output anything to console :|
	#	'cp -fv "{target_prefix}/bin/sdl2-config" "{cross_prefix_full}sdl2-config"', # this is the only mingw dir in the PATH so use it for now [though FFmpeg doesn't use it?]
	#),
	'depends_on' : [
		'libsamplerate', 'vulkan_headers', 'vulkan-d3dheaders', 'vulkan_from_windows_dll', # 'vulkan_loader',
	],
	'update_check' : { 'type' : 'git', }, # 2022.12.18 per DEADSIX27
	'_info' : { 'version' : 'git (SDL2) ', 'fancy_name' : 'SDL2' }, # 2022.12.18 per DEADSIX27
}

#
# MABS: as at 2022.12.21
#_check=(libSDL2{,_test,main}.a sdl2.pc SDL2/SDL.h)
#if { { [[ $ffmpeg != no ]] &&
#    { enabled sdl2 || ! disabled_any sdl2 autodetect; }; } ||
#    mpv_enabled sdl2; } &&
#    do_vcs "$SOURCE_REPO_SDL2"; then
#    do_uninstall include/SDL2 lib/cmake/SDL2 bin/sdl2-config "${_check[@]}"
#    do_autogen
#    sed -i 's|__declspec(dllexport)||g' include/{begin_code,SDL_opengl}.h
#    do_separate_confmakeinstall
#    do_checkIfExist
#fi