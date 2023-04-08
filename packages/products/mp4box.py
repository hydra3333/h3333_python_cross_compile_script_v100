{
	'repo_type' : 'git',
	#'depth_git' : 0,
	'url' : 'https://github.com/gpac/gpac.git',
	#'branch' : 'c68d8a53ec84af125fb51e4fe58d4d09254a58d6',
	#'branch' : 'tags/v2.0.0',
	'rename_folder' : 'mp4box_git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		'cp -fv "configure" "configure.orig"',
		'sed -i.bak \'s/is_64="no"/is_64="yes"/g\' configure',
		#
		#'sed -i.bak \'s/ vorbis theora ogg / /g\' configure', # in 'all_packages'
		#'sed -i.bak \'s/disabled_packages=""/disabled_packages="ogg theora vorbis"/g\' configure',
		#'sed -i.bak \'s/push_feature "ogg"/#push_feature "ogg"/g\' configure', 
		#'sed -i.bak \'s/push_feature "theora"/#push_feature "theora"/g\' configure', 
		#'sed -i.bak \'s/push_feature "vorbis"/#push_feature "vorbis"/g\' configure', 
		#'sed -i.bak \'/push_feature "ogg"/a disable_ogg="yes"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a disable_theora="yes"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a use_ogg="no"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a use_theora="no"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a use_vorbis="no"\' configure',
		#
		'sed -i.bak \'s/sdl_static="no"/sdl_static="yes"/g\' configure',
		'sed -i.bak \'s/has_dvb4linux="yes"/has_dvb4linux="no"/g\' configure',
		'sed -i.bak \'s/targetos=`uname -s`/targetos=MINGW64/g\' configure',
		'sed -i.bak \'s/extralibs="-lm"/extralibs=""/g\' configure',
		'sed -i.bak \'s/SHFLAGS=-shared/SHFLAGS=/g\' configure',
		'sed -i.bak \'s/extralibs="$extralibs -lws2_32 -lwinmm -limagehlp"/extralibs="$extralibs -lws2_32 -lwinmm -lz -lbz2 -lssp"/g\' configure',
		'sed -i.bak \'s/Psapi.h/psapi.h/g\' applications/gpac/compositor_tools.c',
		#'sed -i.bak \'s/Psapi.h/psapi.h/g\' applications/deprecated/mp4client/main.c',
		#
		#'sed -i.bak \'/is_64="yes"/a disable_ogg="yes"\' configure',
		#'sed -i.bak \'/is_64="yes"/a disable_theora="yes"\' configure',
		#'sed -i.bak \'/is_64="yes"/a disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/is_64="yes"/a has_ogg="no"\' configure',
		#'sed -i.bak \'/is_64="yes"/a has_theora="no"\' configure',
		#'sed -i.bak \'/is_64="yes"/a has_vorbis="no"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a disable_ogg="yes"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a disable_theora="yes"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a has_ogg="no"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a has_theora="no"\' configure',
		#'sed -i.bak \'/push_feature "ogg"/a has_vorbis="no"\' configure',
		#'sed -i.bak \'/push_feature "theora"/a disable_ogg="yes"\' configure',
		#'sed -i.bak \'/push_feature "theora"/a disable_theora="yes"\' configure',
		#'sed -i.bak \'/push_feature "theora"/a disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/push_feature "theora"/a has_ogg="no"\' configure',
		#'sed -i.bak \'/push_feature "theora"/a has_theora="no"\' configure',
		#'sed -i.bak \'/push_feature "theora"/a has_vorbis="no"\' configure',
		#'sed -i.bak \'/push_feature "vorbis"/a disable_ogg="yes"\' configure',
		#'sed -i.bak \'/push_feature "vorbis"/a disable_theora="yes"\' configure',
		#'sed -i.bak \'/push_feature "vorbis"/a disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/push_feature "vorbis"/a has_ogg="no"\' configure',
		#'sed -i.bak \'/push_feature "vorbis"/a has_theora="no"\' configure',
		#'sed -i.bak \'/push_feature "vorbis"/a has_vorbis="no"\' configure',
		#'sed -i.bak \'/config_package_test "$1" "$2" "$3" "$4" "$5" "$6"/a has_ogg="no"\' configure'
		#'sed -i.bak \'/config_package_test "$1" "$2" "$3" "$4" "$5" "$6"/a has_theora="no"\' configure'
		#'sed -i.bak \'/config_package_test "$1" "$2" "$3" "$4" "$5" "$6"/a has_vorbis="no"\' configure'
		#'sed -i.bak \'/if test "$has_ogg" = "no"; then/i disable_ogg="yes"\' configure',
		#'sed -i.bak \'/if test "$has_ogg" = "no"; then/i disable_theora="yes"\' configure',
		#'sed -i.bak \'/if test "$has_ogg" = "no"; then/i disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/if test "$has_ogg" = "no"; then/i has_ogg="no"\' configure',
		#'sed -i.bak \'/if test "$has_ogg" = "no"; then/i has_theora="no"\' configure',
		#'sed -i.bak \'/if test "$has_ogg" = "no"; then/i has_vorbis="no"\' configure',
		#'sed -i.bak \'/has_dvb4linux="no"/a disable_ogg="yes"\' configure',
		#'sed -i.bak \'/has_dvb4linux="no"/a disable_theora="yes"\' configure',
		#'sed -i.bak \'/has_dvb4linux="no"/a disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/has_dvb4linux="no"/a has_ogg="no"\' configure',
		#'sed -i.bak \'/has_dvb4linux="no"/a has_theora="no"\' configure',
		#'sed -i.bak \'/has_dvb4linux="no"/a has_vorbis="no"\' configure',
		#'sed -i.bak \'/echo "CONFIG_OGG=$has_ogg"/i disable_ogg="yes"\' configure',
		#'sed -i.bak \'/echo "CONFIG_OGG=$has_ogg"/i disable_theora="yes"\' configure',
		#'sed -i.bak \'/echo "CONFIG_OGG=$has_ogg"/i disable_vorbis="yes"\' configure',
		#'sed -i.bak \'/echo "CONFIG_OGG=$has_ogg"/i has_ogg="no"\' configure',
		#'sed -i.bak \'/echo "CONFIG_OGG=$has_ogg"/i has_theora="no"\' configure',
		#'sed -i.bak \'/echo "CONFIG_OGG=$has_ogg"/i has_vorbis="no"\' configure',
		#'sed -i.bak \'/disable_svg="yes"/i disable_ogg="yes"\' configure',
		#'sed -i.bak \'/disable_svg="yes"/i disable_theora="yes"\' configure',
		#'sed -i.bak \'/disable_svg="yes"/i disable_vorbis="yes"\' configure',
		#
		# DEBUG for zlib not found:
		#'sed -i.BAK0 \'s|has_ffmpeg="no"|has_ffmpeg="system"|g\' configure',
		#'diff -U 1 configure.BAK0 configure && echo "NO difference" || echo "YES differences!"',
		#'sed -i.BAK1 \'s|ffmpeg_cflags=""|ffmpeg_cflags="-L{target_prefix}/lib/ -lz -lavcodec -lavformat -lavutil -lavdevice -lswscale -lswresample -lavfilter \$ffmpeg_extra_ldflags"\\nhas_ffmpeg="system"|\' configure',
		#'diff -U 5 configure.BAK1 configure && echo "NO difference" || echo "YES differences!"',
		#
		# DEBUG for configure:
		'diff -U 3 ./configure.orig ./configure && echo "NO difference" || echo "YES differences!"',
	],
	'env_exports' : {
		'CFLAGS'   : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'CXXFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'CPPFLAGS' : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'LDFLAGS'  : ' {original_cflags} -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 ',
		'LIBS'     : ' -lbz2 ',
	},
	#'cpu_count' : '1',
	# from MABS: --static-bin --static-build --static-modules --enable-all
	'configure_options' : 
		'--host={target_host} '
		#'--target-os={bit_name3} ' # --target-os=mingw64
		'--target-os=MINGW64 '
		'--prefix={output_prefix}/mp4box_git.installed '
		'--cross-prefix={cross_prefix_bare} '
		#'--enable-static '
		'--static-modules '
		'--static-build '
		'--static-bin '
		#'--strip '
		#'--disable-shared '
		'--enable-pic '
		'--disable-ipv6 '
		'--disable-oss-audio --disable-x11 '
		'    --extra-cflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -lpsapi " '
		'   --extra-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -lpsapi " '
		'--extra-ff-ldflags=" -DGPAC_STATIC_MODULES -DLIBXML_STATIC -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -lpsapi " '
		'--extra-libs=" -L{target_prefix}/lib/ -lbz2 -lavutil -lavdevice -lavcodec -lavfilter -lavformat -lpostproc -lz -lbz2 -lpsapi " '
		'--enable-mem-track --enable-depth '
		#
		'--enable-avi --enable-m2ps --enable-m2ts --enable-m2ts-mux --enable-parsers --enable-import '
		'--enable-loader-isoff --enable-loader-bt --enable-loader-xmt '
		'--enable-isoff --enable-isoff-write --enable-isoff-hint --enable-isoff-frag --enable-isoff-hds '
		'--enable-streaming '
		'--enable-hevc '
		'--enable-nvdec '
		'--use-a52=system '
		'--use-zlib=system '
		'--use-theora=system '
		'--use-vorbis=system '
		'--use-ogg=system '
		'--use-ffmpeg=no '
		#'--use-ffmpeg=system '
	,
	#'run_post_configure' : [ 
	#	'./check_revision.sh', # 2021.04.10 per https://github.com/rdp/ffmpeg-windows-build-helpers/commit/f8f1c51573b7e3a85183e9f2a1ddcb6895d1e844
	#],
	'depends_on' : [
		 #'a52dec', 'bzip2', 'zlib', 'libffmpeg_extra', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
		 'a52dec', 'bzip2', 'zlib', 'libogg', 'libvorbis', 'libtheora',  'libffmpeg_extra', 'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2 'sdl2', 
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mp4box (GPAC)' },
}
#
# MABS 2023.04.02:
#_check=(libgpac_static.a bin-video/{MP4Box,gpac}.exe)
#if [[ $mp4box = y ]] && do_vcs "$SOURCE_REPO_GPAC"; then
#    do_uninstall include/gpac "${_check[@]}"
#    git grep -PIl "\xC2\xA0" | xargs -r sed -i 's/\xC2\xA0/ /g'
#    LDFLAGS+=" -L$LOCALDESTDIR/lib -L$MINGW_PREFIX/lib" \
#        do_separate_conf --static-bin --static-build --static-modules --enable-all
#    do_make
#    log "install" make install-lib
#    do_install bin/gcc/MP4Box.exe bin/gcc/gpac.exe bin-video/
#    do_checkIfExist
#fi