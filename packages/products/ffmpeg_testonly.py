{ 
	# 2021.02.03 - minimum viable for NV/Vapoursynth/mp4/h.264/h.265/mpeg2/aac,ac3,etc conversions
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	'depth_git': 0,
	'branch' : '774d358e0fd520ab9503447c5f8f5e1633b96e39',	# 2023.04.02
	'rename_folder' : 'ffmpeg_testonly',
	'env_exports' : { # 2020.06.19
		'CFLAGS'   : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ',
		'CXXFLAGS' : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ',
		'CPPFLAGS' : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ', # 2020.06.20 per https://github.com/fribidi/fribidi/issues/146#issuecomment-646991416
		'LDFLAGS'  : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ',
	},
	'configure_options' : 
		'--prefix={output_prefix}/ffmpeg_testonly.installed '
		## ####################################################################
		## Main
		##
		'--arch={bit_name2} '
		'--target-os={target_OS} ' #  to enable mingw64 for 64-bit target ... {bit_name3} won't yield "mingw32" 
		'--cross-prefix={cross_prefix_bare} '
		'--pkg-config=pkg-config '
		'--pkg-config-flags=--static '
		'--disable-shared --enable-static ' # 2019.10.31 - I ENFORCE NOTHING BUT STATIC, disable shared !
		'--disable-w32threads '
		'--enable-pthreads ' 
		'--enable-cross-compile '
		'--target-exec=wine '
		'--enable-runtime-cpudetect '
		'--enable-gpl '
		'--enable-version3 '
		'--extra-version="testonly" '
		'--enable-pic '
		'--enable-gray '
		########################################################################
		########################################################################

		'--disable-autodetect '
		'--disable-ffplay '
		'--disable-ffprobe '
		'--disable-doc '

		########################################################################
		########################################################################
		##
		## Misc.
		##
		#'--enable-bzlib '
		#'--enable-zlib '
		#'--enable-lzma '
		#'--disable-fontconfig '		# 2021.02.03
		#'--disable-libfontconfig '	# 2021.02.03
		#'--disable-libfreetype '	# 2021.02.03
		#'--disable-libfribidi '		# 2021.02.03
		#'--disable-libbluray '		# 2021.02.03
		#--disable-libcdio '		# 2021.02.03
		#'--enable-avisynth '
		#'--enable-vapoursynth '
		#'--enable-librtmp '		# 2021.08.27
		#'--enable-librist '         # 2021.08.27
		#'--disable-libcaca '		# 2021.10.23 now requires autoconf 2.71 which causes other dependencies to fail
		#'--enable-iconv '
		#'--enable-libxml2 '
		#'--enable-gmp '
		#'--enable-gnutls '			# # nongpl: openssl,libtls(libressl)
		##
		## Video/Picture Libs
		##
		#'--enable-libzimg '
		#'--enable-libx264 '
		#'--enable-libx265 '
		#'--enable-libvpx '
		#'--enable-libdav1d '
		#'--disable-libaom '
		#'--enable-libxvid '
		##
		## Audio Libs
		##
		#'--enable-libopus '
		#'--enable-libmp3lame '
		#'--enable-libvorbis '
		#'--enable-libtheora '
		#'--enable-libspeex '
		#'--enable-libsoxr '
		#'--enable-librubberband '
		##
		## Subtitle/OCR Libs:
		##
		'--disable-libass '			# 2021.02.03
		##
		## Image libs
		##
		'--enable-libwebp '
		##
		## HW Decoders
		##
		'--enable-ffnvcodec '
		'--enable-cuvid '
		'--enable-cuda-llvm '
		'--disable-opengl '		# 2021.02.03
		'--enable-d3d11va '
		'--enable-nvenc '
		'--enable-nvdec '
		'--enable-dxva2 '
		'--disable-libmfx '			# 2021.02.03
		'--disable-amf '			# 2021.02.03
		'--disable-opencl '			# 2021.02.03
		'--enable-vulkan --enable-libglslang '  # ERROR: libshaderc and libglslang are mutually exclusive, if in doubt, disable libglslang
			'--enable-filter=scale_vulkan '
			'--enable-filter=avgblur_vulkan '
			'--enable-filter=chromaber_vulkan '
			'--enable-filter=overlay_vulkan '
			'--enable-filter=blend_vulkan '
			'--enable-filter=flip_vulkan '
			'--enable-filter=gblur_vulkan '
			'--enable-filter=hflip_vulkan '
			'--enable-filter=transpose_vulkan '
			'--enable-filter=vflip_vulkan '
		'--disable-libplacebo '
		'--extra-libs="-lpsapi -liconv -lssp" '#  add  -lssp for -fstack-protector-all, # 2021.04.11 removed -lintl  (ex gettext) #2020.10.12 moved here from ffmpeg_extra_config
		##
		## nonfree
		##
		'--enable-nonfree '
		'--enable-libfdk-aac '
		'--disable-decklink '		# 2021.02.03
		##
		## nonfree extra_config
		##
		'--enable-libtwolame '
		'--enable-libzvbi '
		'--enable-libgsm '
		'--enable-libopencore-amrnb '
		'--enable-libopencore-amrwb '
		'--enable-libvo-amrwbenc '
		'--enable-libsnappy '
		'--disable-frei0r '				# 2021.02.03
		'--enable-libsrt '
		'--disable-libbs2b ' #'--enable-libbs2b #  2022.04.22 commented out
		'--enable-libilbc '
		'--disable-libgme '		# 2021.02.03
		'--disable-libflite '	# 2021.02.03
		'--enable-sdl2 ' # 2020.05.13 renabled. Removed '--disable-sdl2 ' # 2020.05.13 removed SDL2 '--enable-sdl2 '
		'--enable-libmysofa '
		'--enable-libvidstab '
		'--disable-libmodplug '	# 2021.02.03
		'--disable-schannel '
		'--extra-cflags="-DLIBTWOLAME_STATIC -lssp" '
		'--extra-cflags="-DMODPLUG_STATIC -lssp"  ' 	# 2021.02.03
		'--extra-cflags="-DLIBXML_STATIC -lssp" '
		'--extra-cflags="-DGLIB_STATIC_COMPILATION -lssp" '	# 2021.02.03
		'--extra-libs=" -lssp " '
		,
	'depends_on' : [ 
		'gnutls_testonly',
		'bzip2',
		'zlib',
		'lzma',
		'python3_libs',
		'vapoursynth_libs',
		'rtmpdump',		# 2021.08.27
		'librist',      # 2021.08.27
		'iconv',
		'libzimg',
		'libxml2',
		'libx264_testonly',	# 2020.06.09 only the x264 package, not the dependency depends on libffmpeg_extra being built first
		'libx265_multibit',
		'libvpx',
		'libdav1d',
		'xvidcore', # was 'libxvid',
		'libopus',
		'liblame',
		'libogg',
		'libvorbis',
		'libtheora',
		'libspeex',
		'libsoxr_testonly',
		'rubberband',
		'libwebp',
		'nv-codec-headers',
		'vulkan_from_windows_dll', # 'vulkan_loader',
		'spirv-headers', 'spirv-cross', 'spirv-tools', 'libplacebo', 'shaderc',  # all these go together
		'avisynth_plus_headers',
		'sdl2', # 2020.05.13 re-enabled sdl2 # 2020.05.13 remove sdl2
		'twolame',
		'zvbi',
		'libgsm',
		'opencore-amr',
		'vo-amrwbenc',
		'libsnappy',
		'srt_testonly',
		'libilbc',
		'libmysofa_testonly',
		'vidstab',
		'fftw3',
		'fdk_aac',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffmpeg (static) testonly' },
}
#-------------------------------------------

