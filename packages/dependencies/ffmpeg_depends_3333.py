{
	'is_dep_inheriter' : True,
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
		#'rtmpdump',		# 2021.02.03
		#'libcaca',		# 2021.02.03
		'iconv',
		'libzimg',
		'libx264',	# 2020.06.09 only the x264 package, not the dependency depends on libffmpeg_extra being built first
		#'openh264', # 2019.12.13 comment out
		'libx265_multibit',
		#'kvazaar',  # 2019.12.13 comment out
		'libvpx',
		'libdav1d',
		'libaom',
		'xvidcore', # was 'libxvid',
		'libopus',
		'liblame',
		'libogg',
		'libvorbis',
		'libtheora',
		#'libspeex', 		# 2021.02.03
		'libsoxr',
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
		'libsnappy',
		#'frei0r',				# 2021.02.03
		'srt',
		'libbs2b',
		#'wavpack', # deleted from ffmpeg 2020.10.04
		'libilbc',
		#'libgme_game_music_emu',				# 2021.02.03
		#'flite',				# 2021.02.03
		#'davs2', # don't build the chinese software :)
		#'xavs', # don't build the chinese software :)
		#'xavs2', # don't build the chinese software :)
		'openmpt',
		'libmysofa',
		'vidstab',
		'fftw3',
		#'libmodplug',			# 2021.02.03
##
		#'decklink_headers',		# 2021.02.03
		'fdk_aac'
}
