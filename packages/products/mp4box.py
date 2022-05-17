{
	'repo_type' : 'git',
	'depth_git' : 0,
	'url' : 'https://github.com/gpac/gpac.git',
	#'branch' : 'tags/v2.0.0',
	#'folder_name' : 'mp4box_git',
	#'rename_folder' : 'mp4box_git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		'sed -i.bak \'s/has_dvb4linux="yes"/has_dvb4linux="no"/g\' configure',
		'sed -i.bak \'s/targetos=`uname -s`/targetos=MINGW64/g\' configure',
		'sed -i.bak \'s/extralibs="-lm"/extralibs=""/g\' configure',
		'sed -i.bak \'s/SHFLAGS=-shared/SHFLAGS=/g\' configure',
		'sed -i.bak \'s/extralibs="$extralibs -lws2_32 -lwinmm -limagehlp"/extralibs="$extralibs -lws2_32 -lwinmm -lz -lbz2 -lssp"/g\' configure',
		# DEBUG for zlib not found:
		#'sed -i.BAK0 \'s|has_ffmpeg="no"|has_ffmpeg="system"|g\' configure',
		#'diff -U 1 configure.BAK0 configure && echo "NO difference" || echo "YES differences!"',
		#'sed -i.BAK1 \'s|ffmpeg_cflags=""|ffmpeg_cflags="-L{target_prefix}/lib/ -lz -lavcodec -lavformat -lavutil -lavdevice -lswscale -lswresample -lavfilter \$ffmpeg_extra_ldflags"\\nhas_ffmpeg="system"|\' configure',
		#'diff -U 5 configure.BAK1 configure && echo "NO difference" || echo "YES differences!"',
		'sed -i.bak "s/Psapi.h/psapi.h/g" applications/gpac/compositor_tools.c',
		'sed -i.bak "s/Psapi.h/psapi.h/g" applications/deprecated/mp4client/main.c',
	],
	'env_exports' : {
		'CFLAGS'   : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'CXXFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'CPPFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'LDFLAGS'  : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
	},
	#'cpu_count' : '1',
	'configure_options' : '--host={target_host} --target-os={bit_name3} --prefix={output_prefix}/mp4box_git.installed --cross-prefix={cross_prefix_bare} '
        '--enable-static --static-modules --static-build --static-bin --disable-shared --enable-pic '
        '--disable-docs --disable-ipv6 --enable-mem-track --enable-depth '
        '--disable-oss-audio --disable-x11 '
        '--extra-cflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
        '--extra-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		'--extra-ff-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		'--extra-libs=" -L{target_prefix}/lib/ -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		'--enable-mem-track --enable-depth '
		#'--enable-sdl-static '
		'--enable-avi --enable-m2ps --enable-m2ts --enable-m2ts-mux --enable-parsers --enable-import '
		'--enable-loader-isoff --enable-loader-bt --enable-loader-xmt '
		'--enable-isoff --enable-isoff-write --enable-isoff-hint --enable-isoff-frag --enable-isoff-hds '
		'--enable-streaming --enable-hevc --enable-nvdec '
		'--enable-streaming '
		'--enable-hevc '
		'--enable-nvdec '
		'--use-a52==system '
		'--use-zlib==system '
		'--use-vorbis=system '
		'--use-theora=system '
		'--use-ogg=system '
		'--use-ffmpeg=no '
		#'--use-ffmpeg=local '
		#'--use-ffmpeg=system '
	,
	'run_post_configure' : [ 
		'./check_revision.sh', # 2021.04.10 per https://github.com/rdp/ffmpeg-windows-build-helpers/commit/f8f1c51573b7e3a85183e9f2a1ddcb6895d1e844
	],
	'depends_on' : [
		 'a52dec', 'zlib', 'libffmpeg_extra', 'libgpac', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
	],
	'_info' : { 'version' : '(legacy tree)', 'fancy_name' : 'mp4box' },
}