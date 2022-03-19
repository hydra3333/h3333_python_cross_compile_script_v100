{
	'repo_type' : 'git',
	'depth_git' : 0,
	'url' : 'https://github.com/gpac/gpac.git',
	#'branch' : 'tags/v2.0.0',
	#'folder_name' : 'gpac_lib_git',
	#'rename_folder' : 'gpac_lib_git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		'sed -i.bak \'s/has_dvb4linux="yes"/has_dvb4linux="no"/g\' configure',
		'sed -i.bak \'s/targetos=`uname -s`/targetos=MINGW64/g\' configure',
		'sed -i.bak \'s/extralibs="-lm"/extralibs=""/g\' configure',
		'sed -i.bak \'s/SHFLAGS=-shared/SHFLAGS=/g\' configure',
		'sed -i.bak \'s/extralibs="$extralibs -lws2_32 -lwinmm -limagehlp"/extralibs="$extralibs -lws2_32 -lwinmm -lz -lbz2 -lssp"/g\' configure',
		# DEBUG for zlib not found:
		#'sed -i.BAK0 \'s|if docc -lz $LDFLAGS ; then|if docczlib -lz \$LDFLAGS ; then|\' configure',
		#'sed -i.BAK1 \'s|docc()|docczlib() {\\n \$cc -o \$TMPO \$TMPC \$@ \\n \$cc -o \$TMPO \$TMPC \$@ 0\>/dev/null 2\>\$TMPL\\n dolog $@\\n}\\ndocc()|\' configure',
	],
	'env_exports' : {
		'CFLAGS'   : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'CXXFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'CPPFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'LDFLAGS'  : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
	},
	#'cpu_count' : '1',
	'configure_options' : '--host={target_host} --target-os={bit_name3} --prefix={target_prefix} --cross-prefix={cross_prefix_bare} '
		'--enable-static --static-modules --static-build --static-bin --disable-shared --enable-pic '
		'--disable-docs --disable-ipv6 --enable-mem-track --enable-depth '
		'--disable-oss-audio --disable-x11 '
		'--extra-cflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		'--extra-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		'--extra-libs=" -L{target_prefix}/lib/ -lbz2 -lavutil -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 " '
		'--enable-mem-track --enable-depth --enable-sdl-static '
		'--enable-avi --enable-m2ps --enable-m2ts --enable-m2ts-mux --enable-parsers --enable-import '
		'--enable-loader-isoff --enable-loader-bt --enable-loader-xmt '
		'--enable-isoff --enable-isoff-write --enable-isoff-hint --enable-isoff-frag --enable-isoff-hds '
		'--enable-streaming '
		'--enable-hevc '
		'--enable-nvdec '
		'--use-a52==system '
		'--use-zlib==system '
		'--use-vorbis=system '
		'--use-theora=system '
		'--use-ogg=system '
		'--use-ffmpeg=system '
    ,
	#'run_post_configure' : [ 
	#	'./check_revision.sh', # 2021.04.10 per https://github.com/rdp/ffmpeg-windows-build-helpers/commit/f8f1c51573b7e3a85183e9f2a1ddcb6895d1e844
	#],
	'depends_on' : [
		 'a52dec', 'zlib', 'bzip2', 'libffmpeg_extra', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'GPAC library' },
}