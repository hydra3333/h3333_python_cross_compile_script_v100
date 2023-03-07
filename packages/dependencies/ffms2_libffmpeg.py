{
	'repo_type' : 'git',
	#'url' : 'https://github.com/hydra3333/FFmpeg.git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	#'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'ffms2_libffmpeg',
	'env_exports' : {
		#'CFLAGS'   : ' {original_cflags} ',
		#'CXXFLAGS' : ' {original_cflags} ',
		#'CPPFLAGS' : ' {original_cflags} ',
		#'LDFLAGS'  : ' {original_cflags} ',
		'CXXFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CPPFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CFLAGS'   :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'LDFLAGS'  :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	'configure_options' :	'--sysroot={target_sub_prefix} '
							'--prefix={output_prefix}/ffms2_dll.installed '
							'--enable-shared --disable-static '
							'--disable-programs --disable-doc --disable-htmlpages --disable-manpages --disable-podpages --disable-txtpages '
							#'--extra-libs="-lpsapi -lintl" '
							'--arch={bit_name2} '
							'--target-os={target_OS} '
							'--cross-prefix={cross_prefix_bare} '
							'--pkgconfigdir={output_prefix}/ffms2_dll.installed/lib/pkgconfig ',
							'--pkg-config=pkg-config '
							'--pkg-config-flags=--shared '
							'--enable-shared --disable-static '
							'--disable-w32threads '
							'--enable-pthreads '
							'--enable-pic '
							'--enable-cross-compile '
							'--target-exec=wine '
							'--enable-runtime-cpudetect '
							'--enable-gpl '
							'--enable-nonfree '
							'--enable-version3 '
							'--extra-version="xcompile" '
							'--disable-programs '
							'--disable-devices '
							'--disable-filters '
							'--disable-encoders '
							'--disable-muxers '
							'--disable-debug '
							'--disable-sdl2 '
							'--disable-doc '
							'--enable-protocol=file,pipe '
							'--disable-autodetect '
							#
							#'--enable-ffnvcodec '
							#'--enable-cuvid '
							#'--enable-cuda-llvm '
							#'--enable-d3d11va '
							#'--enable-nvdec '
							#'--enable-dxva2 '
							#
							#--enable-{lzma,bzlib,zlib} 	# MABS
							'--enable-zlib '				# build shared with right --prefix -enable-shared --disable-static
							#'--enable-bzlib '				# build shared with right --prefix -enable-shared --disable-static
							'--enable-lzma '				# build shared with right --prefix -enable-shared --disable-static
							'--enable-libzimg '				# build shared with right --prefix -enable-shared --disable-static
							#
							#'--enable-libxml2 '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libvpx '				# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libaom ' 			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libxvid '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libopus '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libmp3lame '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libvorbis '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libtheora '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libsoxr '			# build shared with right --prefix -enable-shared --disable-static
							#'--enable-librubberband '		# build shared with right --prefix -enable-shared --disable-static
							#'--enable-libwebp '			# build shared with right --prefix -enable-shared --disable-static
							,
	'run_post_patch' : [
		'./configure --help',
	],
	'depends_on' : [ 
		'ffms2_libzimg',		# ok
		'ffms2_xz',				# ok
		'ffms2_zlib',			# ??? no produces a dll ???
		#'ffms2_lzma',			# another name for xz	
		#
		# MABS: {lzma,bzlib,zlib}
		#'ffms2_bzip2',			# no does not install .la file
		#'ffms2_iconv',			# no fails to build shared
		#'ffms2_libxml2',
		#'ffms2_libvpx',
		#'ffms2_libaom',
		#'ffms2_libxvid',
		#'ffms2_libopus',
		#'ffms2_libmp3lame',
		#'ffms2_libvorbis',
		#'ffms2_libtheora',
		#'ffms2_libsoxr',
		#'ffms2_librubberband',
		#'ffms2_libwebp',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'FFmpeg (library,extra)' },
}
