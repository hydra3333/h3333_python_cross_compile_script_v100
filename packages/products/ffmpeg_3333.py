{ 
	# 2021.02.03 - minimum viable for NV/Vapoursynth/mp4/h.264/h.265/mpeg2/aac,ac3,etc conversions
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	#'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'ffmpeg_3333',
	'env_exports' : { # 2020.06.19
		'CFLAGS'   : ' -DFRIBIDI_LIB_STATIC {original_cflags}',
		'CXXFLAGS' : ' -DFRIBIDI_LIB_STATIC {original_cflags}',
		'CPPFLAGS' : ' -DFRIBIDI_LIB_STATIC {original_cflags}', # 2020.06.20 per https://github.com/fribidi/fribidi/issues/146#issuecomment-646991416
		'LDFLAGS'  : ' -DFRIBIDI_LIB_STATIC {original_cflags}',
	},
	#'patches' : [
	#	('ffmpeg/ffmpeg-windres-fix.patch', '-p0' ), # 2021.04.10 for binutils 2.36.1 per https://github.com/rdp/ffmpeg-windows-build-helpers/pull/558/commits/4ec72f9f9dab96f7d2fcb1d5935deded53f4ec21
	#],
	'configure_options' : 
		'--prefix={output_prefix}/ffmpeg_git_3333.installed --disable-shared --enable-static '
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
		'--extra-version="Hydra3333/python_cross_compile_script_v100/3333" '
		##
		## Misc.
		##
		'--enable-pic '
		'--enable-bzlib '
		'--enable-zlib '
		'--enable-lzma '
		'--disable-fontconfig '		# 2021.02.03
		'--disable-libfontconfig '	# 2021.02.03
		'--disable-libfreetype '	# 2021.02.03
		'--disable-libfribidi '		# 2021.02.03
		'--disable-libbluray '		# 2021.02.03
		'--disable-libcdio '		# 2021.02.03
		'--enable-avisynth '
		'--enable-vapoursynth '
		'--enable-librtmp '		# 2021.08.27
        '--enable-librist',         # 2021.08.27
		'--disable-libcaca '		# 2021.02.03
		'--enable-iconv '
		'--enable-libxml2 '
		'--enable-gmp '
		'--enable-gnutls '			# # nongpl: openssl,libtls(libressl)
		#'--enable-avresample ' # deprecated. 2018.11.23 ... but LSW depends on it # 2019.11.19 HolyWu's lsw does not need avresample as it uses libswresample
		##
		## Video/Picture Libs
		##
		'--enable-libzimg '
		'--enable-libx264 '
		#'--enable-libopenh264 
		'--enable-libx265 '
		# '--enable-libkvazaar '
		'--enable-libvpx '
		'--enable-libdav1d '
		'--disable-libaom '
		'--enable-libxvid '
		'--enable-gray '
		##
		## Audio Libs
		##
		'--enable-libopus '
		'--enable-libmp3lame '
		'--enable-libvorbis '
		'--enable-libtheora '
		'--enable-libspeex '
		'--enable-libsoxr '
		'--enable-librubberband '
		##
		## Subtitle/OCR Libs:
		##
		'--disable-libass '			# 2021.02.03
		#'--enable-libtesseract ' 	# 2020.06.27 comment out as no longer required
		#'--enable-liblensfun ' 	# 2020.05.12 comment out so we do not have to build glib2
		##
		## Image libs
		##
		'--enable-libwebp '
		##
		## HW Decoders
		##
		'--enable-ffnvcodec '
		'--enable-cuvid '
		#'--enable-cuda-nvcc ' # 2019.10.31 MADE IT TO FREE#
		'--enable-cuda-llvm '
		'--disable-opengl '		# 2021.02.03
		'--enable-d3d11va '
		'--enable-nvenc '
		'--enable-nvdec '
		'--enable-dxva2 '
		'--disable-libmfx '			# 2021.02.03
		'--disable-amf '			# 2021.02.03
		'--disable-opencl '			# 2021.02.03
		#'--enable-vulkan --enable-filter=scale_vulkan --enable-filter=avgblur_vulkan --enable-filter=chromaber_vulkan --enable-filter=overlay_vulkan ' # 2021.02.03 # 2020.10.12 pith off vulcan since vulkan_loader can no longer be statically linked
		#'--extra-cflags="-DFRIBIDI_LIB_STATIC" ' # 2020.06.20 per https://github.com/fribidi/fribidi/issues/146#issuecomment-646991416 # --extra-libs="-lfribidi"
		'--extra-libs="-lpsapi -liconv -lssp" '#  add  -lssp for -fstack-protector-all, # 2021.04.11 removed -lintl  (ex gettext) #2020.10.12 moved here from ffmpeg_extra_config
		##
		## nonfree
		##
		'--enable-nonfree '
		'--enable-libfdk-aac '
		'--disable-decklink '		# 2021.02.03
		#'--enable-cuda-sdk ' # old
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
		#'--disable-filter=frei0r '		# 2021.02.03
		'--enable-libsrt '
		'--enable-libbs2b '
		#'--enable-libwavpack ' # 'libwavpack' deleted from ffmpeg 2020.10.04
		'--enable-libilbc '
		'--disable-libgme '		# 2021.02.03
		'--disable-libflite '	# 2021.02.03
		'--enable-sdl2 ' # 2020.05.13 renabled. Removed '--disable-sdl2 ' # 2020.05.13 removed SDL2 '--enable-sdl2 '
		#'--enable-libdavs2 '
		#'--enable-libxavs '
		#'--enable-libxavs2 '
		'--enable-libopenmpt '
		'--enable-libmysofa '
		'--enable-libvidstab '
		'--disable-libmodplug '	# 2021.02.03
		'--disable-schannel '
		#'--disable-gcrypt '
		#'--enable-ladspa ' #  deadsix27 had this commented out, review it later
		# '--enable-libcodec2 ' # Requires https://github.com/traviscross/freeswitch/tree/master/libs/libcodec2, too lazy to split that off.
		# '--enable-libvmaf '
		# '--extra-libs="-lpsapi" '
		# '--extra-libs="-liconv" ' # -lschannel #-lsecurity -lz -lcrypt32 -lintl -liconv -lpng -loleaut32 -lstdc++ -lspeexdsp -lpsapi
		'--extra-cflags="-DLIBTWOLAME_STATIC -lssp" '
		'--extra-cflags="-DMODPLUG_STATIC -lssp"  ' 	# 2021.02.03
		'--extra-cflags="-DLIBXML_STATIC -lssp" '
		'--extra-cflags="-DGLIB_STATIC_COMPILATION -lssp" '	# 2021.02.03
		'--extra-libs=" -lssp " '
		## ####################################################################################
		'--prefix={output_prefix}/ffmpeg_git_3333.installed --disable-shared --enable-static '
		## ####################################################################################
		,
	'depends_on' : [ 
		'bzip2',
		'zlib',
		'lzma',
		##'fontconfig',		# 2021.02.03
		#'freetype', # it depends on 'freetype_lib', 'harfbuzz_lib-with-freetype' so it builds these in the right order
		#'libbluray',		# 2021.02.03
		#'libcdio',			# 2021.02.03
        'python3_libs',
		'vapoursynth_libs',
		'rtmpdump',		# 2021.08.27
        'librist',      # 2021.08.27
		#'libcaca',		# 2021.02.03
		'iconv',
		'libzimg',
		'libxml2',
		'libx264_3333',	# 2020.06.09 only the x264 package, not the dependency depends on libffmpeg_extra being built first
		#'openh264', # 2019.12.13 comment out
		'libx265_multibit',
		#'kvazaar',  # 2019.12.13 comment out
		'libvpx',
		'libdav1d',
		#'libaom',
		'xvidcore', # was 'libxvid',
		'libopus',
		'liblame',
		'libogg',
		'libvorbis',
		'libtheora',
		'libspeex',
		'libsoxr_3333',
		'rubberband',
		#'libfribidi',		# 2021.02.03
		#'libass',			# 2021.02.03
		#'tesseract', # 2020.06.27 comment out as no longer required
		#'lensfun',  # 2020.05.12 comment out so we do not have to build glib2
		'libwebp',
		'nv-codec-headers',
		#'intel_quicksync_mfx',		# 2021.02.03
		#'amf_headers',			# 2021.02.03
        #'opencl_icd', # 2020.11.24
        #'opencl_non_icd',		# 2021.02.03
		#'vulkan_loader', # 2020.10.12 pith off vulcan since vulkan_loader can no longer be statically linked
		'avisynth_plus_headers',
		'sdl2', # 2020.05.13 re-enabled sdl2 # 2020.05.13 remove sdl2
##
		'twolame',
		'zvbi',
		'libgsm',
		'opencore-amr',
		'vo-amrwbenc',
		'gnutls_3333',
		'libsnappy',
		#'frei0r',				# 2021.02.03
		'srt_3333',
		'libbs2b',
		#'wavpack', # deleted from ffmpeg 2020.10.04
		'libilbc',
		#'libgme_game_music_emu',				# 2021.02.03
		#'flite',				# 2021.02.03
		#'davs2', # don't build the chinese software :)
		#'xavs', # don't build the chinese software :)
		#'xavs2', # don't build the chinese software :)
		'openmpt',
		'libmysofa_3333',
		'vidstab',
		'fftw3',
		#'libmodplug',			# 2021.02.03
##
		#'decklink_headers',		# 2021.02.03
		'fdk_aac',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffmpeg (static) 3333 SPECIAL' },
}
#-------------------------------------------

