{
	'repo_type' : 'git',
	'depth_git' : 0,
	'url' : 'https://github.com/gpac/gpac.git',
	#'branch' : 'tags/v2.0.0',
	#'folder_name' : 'gpac_lib_git',
	#'rename_folder' : 'gpac_lib_git',
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
		'sed -i.bak \'s/extralibs="$extralibs -lws2_32 -lwinmm -limagehlp"/extralibs="$extralibs -lws2_32 -lwinmm -lz -lbz2 -lssp"/g\' configure',
	],
	'env_exports' : {
		'CFLAGS'   : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -municode "',
		'CXXFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -municode "',
		'CPPFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -municode "',
		'LDFLAGS'  : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -municode "',
	},
	'configure_options' : '--host={target_host} --target-os={bit_name3} --prefix={output_prefix}/mp4box_git.installed --cross-prefix={cross_prefix_bare} '
        '--enable-static --static-modules --static-build --static-bin --disable-shared '
        '--disable-docs --disable-ipv6 --enable-mem-track --enable-depth '
        '--disable-oss-audio --disable-x11 '
        '--use-ffmpeg=no '
        #'--extra-cflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION " '
        #'--extra-ldflags=" -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc " '
        #'--extra-cflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION" -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc " '
        #'--extra-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION" -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc " '
        '--extra-cflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -municode " '
        '--extra-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -municode " '
		'--extra-libs=" -L{target_prefix}/lib -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		#'--disable-all '
		'--enable-mem-track --enable-depth --enable-sdl-static '
		'--enable-avi --enable-m2ps --enable-m2ts --enable-m2ts-mux --enable-parsers --enable-import '
		'--enable-loader-isoff --enable-loader-bt --enable-loader-xmt '
		'--enable-isoff --enable-isoff-write --enable-isoff-hint --enable-isoff-frag --enable-isoff-hds '
		'--enable-streaming --enable-hevc --enable-nvdec '
    ,
	#'run_post_configure' : [ 
	#	'./check_revision.sh', # 2021.04.10 per https://github.com/rdp/ffmpeg-windows-build-helpers/commit/f8f1c51573b7e3a85183e9f2a1ddcb6895d1e844
	#],
	'depends_on' : [
		 'zlib', 'bzip2', 'libffmpeg_extra', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'GPAC library' },
}
