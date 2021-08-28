{
	'repo_type' : 'git',
	'depth_git' : 0,
	#'branch' : 'ce9a843ffcd941d3d17a7bab20749b94a8e3c43c', # as at 2020.06.19, ce9a843ffcd941d3d17a7bab20749b94a8e3c43c is top of the tree 'legacy' (not the master tree)
	#'branch' : 'tags/v0.8.1', # 2020.06.19 0.8.1 is not the master, it's a separate branch named legacy. the commit above is to the legacy tree
	#'branch' : '7d0bb6eb526f0bd9fae53fcbdd846cfe839ed821', # 2020.06.19 as of april 8th, first use of "#include <Windows.h>" in the non-Legacy tree
	'url' : 'https://github.com/gpac/gpac.git',
	'rename_folder' : 'GPAC_git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		#'sed -i.bak \'s/Windows.h/windows.h/g\' "include/gpac/thread.h"', # 2020.06.19 ah, tree "legacy" does not have these to do a sed on
		#'sed -i.bak \'s/WinBase.h/winbase.h/g\' "include/gpac/thread.h"', # 2020.06.19 ah, tree "legacy" does not have these to do a sed on 
		#'sed -i.bak \'s/Windows.h/windows.h/g\' "src/filters/dec_nvdec_sdk.c"', # 2020.06.19 ah, tree "legacy" does not have these to do a sed on
		#'sed -i.bak \'s/Windows.h/windows.h/g\' "src/filters/dec_nvdec_sdk.h"', # 2020.06.19 ah, tree "legacy" does not have these to do a sed on
		'sed -i.bak \'s/has_dvb4linux="yes"/has_dvb4linux="no"/g\' configure',
		'sed -i.bak \'s/targetos=`uname -s`/targetos=MINGW64/g\' configure',
		'sed -i.bak \'s/extralibs="-lm"/extralibs=""/g\' configure',
		'sed -i.bak \'s/SHFLAGS=-shared/SHFLAGS=/g\' configure',
		'sed -i.bak \'s/extralibs="$extralibs -lws2_32 -lwinmm -limagehlp"/extralibs="$extralibs -lws2_32 -lwinmm -lz -lssp"/g\' configure',
	],
	#'configure_options' : '--host={target_host} --target-os={bit_name3} --prefix={output_prefix}/mp4box_git.installed --static-modules --cross-prefix={cross_prefix_bare} --static-mp4box --enable-static-bin --disable-oss-audio --disable-x11 --disable-docs --disable-shared --enable-static --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" --enable-sdl-static ', # 2019.12.13 # 2020.05.13 remove --sdl-cfg={cross_prefix_full}sdl2-config 
	'configure_options' : '--host={target_host} --target-os={bit_name3} --prefix={output_prefix}/mp4box_git.installed --cross-prefix={cross_prefix_bare} '
        '--enable-static --static-modules --static-build --static-bin --disable-shared '
        '--disable-docs --disable-ipv6 --enable-mem-track --enable-depth '
        '--enable-sdl-static '
        '--disable-oss-audio --disable-x11 '
        '--extra-cflags="-DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION" '
        #'--use-ffmpeg=local --extra-ldflags="-L{target_prefix}/lib -lavutil -lavcodec -lavfilter -lavformat -lpostproc" ' # add ffmpeg 
    , # 2019.12.13 # 2020.05.13 remove --sdl-cfg={cross_prefix_full}sdl2-config 
	#'run_post_configure' : [ 
	#	'./check_revision.sh', # 2021.04.10 per https://github.com/rdp/ffmpeg-windows-build-helpers/commit/f8f1c51573b7e3a85183e9f2a1ddcb6895d1e844
	#],
	'depends_on' : [
		 'libffmpeg_extra', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'GPAC library' },
}