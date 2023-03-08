{
	'repo_type' : 'git',
	#'url' : 'https://github.com/hydra3333/FFmpeg.git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	#'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'ffms2_libffmpeg',
	'env_exports' : {
		# had to remove {original_stack_protector} {original_fortify_source} {original_cflag}
		'CXXFLAGS' :  ' -Wl,-Bsymbolic {original_fortify_source} {original_stack_protector} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'CPPFLAGS' :  ' -Wl,-Bsymbolic {original_fortify_source} {original_stack_protector} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'CFLAGS'   :  ' -Wl,-Bsymbolic {original_fortify_source} {original_stack_protector} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'LDFLAGS'  :  ' -fstack-protector -Wl,-Bsymbolic {original_fortify_source} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	'configure_options' :	#'--sysroot={target_sub_prefix} '
							'--prefix={output_prefix}/ffms2_dll.installed '
							'--enable-shared --disable-static '
							'--disable-programs --disable-doc --disable-htmlpages --disable-manpages --disable-podpages --disable-txtpages '
							#'--extra-libs="-lpsapi -lintl" '
							'--arch={bit_name2} '
							'--target-os={target_OS} '
							'--cross-prefix={cross_prefix_bare} '
							'--pkgconfigdir={output_prefix}/ffms2_dll.installed/lib/pkgconfig '
							'--pkg-config=pkg-config '
							#'--pkg-config-flags=--shared '
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
							'--enable-ffnvcodec '
							'--enable-cuvid '
							'--enable-cuda-llvm '
							'--enable-d3d11va '
							'--enable-nvdec '
							'--enable-dxva2 '
							#
							'--enable-zlib '				# build shared with right --prefix -enable-shared --disable-static
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
		#'./configure --help',
		#'export',
		#'pkg-config --exists --print-errors zimg >= 2.7.0 && echo "found OK" || echo "NOT found!"'
	],
	'depends_on' : [ 
		'ffms2_libzimg',		# ok
		'ffms2_xz',				# ok
		'ffms2_zlib',			# ??? no produces a dll ???
		'ffms2_nv-codec-headers',
		#'ffms2_lzma',			# another name for xz	
		#
		#'ffms2_libwebp', ?????????
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'FFmpeg (library,extra)' },
}