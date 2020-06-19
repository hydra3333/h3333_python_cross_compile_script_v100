{
	'repo_type' : 'git',
	'depth_git' : 0,
	'branch' : 'tags/v0.8.1', # 2020.06.19 0.8.1 is not the master, it's a separate branch named legacy
	#'branch' : 'ce9a843ffcd941d3d17a7bab20749b94a8e3c43c', # as at 2020.06.19, is top of the tree 'legacy' (not the master tree)is ce9a843ffcd941d3d17a7bab20749b94a8e3c43c
	#'branch' : '7d0bb6eb526f0bd9fae53fcbdd846cfe839ed821', # 2020.06.19 as of april 8th, first use of "#include <Windows.h>" in the non-Legacy tree
	'url' : 'https://github.com/gpac/gpac.git',
	'rename_folder' : 'mp4box_git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		'sed -i.bak \'s/Windows.h/windows.h/g\' "include/gpac/thread.h"', # 2020.06.19 
		'sed -i.bak \'s/WinBase.h/winbase.h/g\' "include/gpac/thread.h"', # 2020.06.19 
		'sed -i.bak \'s/Windows.h/windows.h/g\' "src/filters/dec_nvdec_sdk.c"', # 2020.06.19 
		'sed -i.bak \'s/Windows.h/windows.h/g\' "src/filters/dec_nvdec_sdk.h"', # 2020.06.19 
		'sed -i.bak \'s/has_dvb4linux="yes"/has_dvb4linux="no"/g\' configure',
		'sed -i.bak \'s/targetos=`uname -s`/targetos=MINGW64/g\' configure',
		'sed -i.bak \'s/extralibs="-lm"/extralibs=""/g\' configure',
		'sed -i.bak \'s/SHFLAGS=-shared/SHFLAGS=/g\' configure',
		'sed -i.bak \'s/extralibs="$extralibs -lws2_32 -lwinmm -limagehlp"/extralibs="$extralibs -lws2_32 -lwinmm -lz"/g\' configure',
	],
	'configure_options' : '--host={target_host} --target-os={bit_name3} --prefix={output_prefix}/mp4box_git.installed --static-modules --cross-prefix={cross_prefix_bare} --static-mp4box --enable-static-bin --disable-oss-audio --disable-x11 --disable-docs --disable-shared --enable-static --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" --enable-sdl-static ', # 2019.12.13 # 2020.05.13 remove --sdl-cfg={cross_prefix_full}sdl2-config 
	'depends_on' : [
		 'libffmpeg_extra', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
	],
	'_info' : { 'version' : None, 'fancy_name' : 'mp4box' },
}
