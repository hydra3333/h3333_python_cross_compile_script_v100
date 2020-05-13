{
	'is_dep_inheriter' : True,
	'depends_on' : [
		'bzip2',
		'zlib',
		'lzma',
		'fontconfig', # fontconfig builds 'freetype'
		#'freetype', # it depends on 'freetype_lib', 'harfbuzz_lib-with-freetype' so it builds these in the right order
		'libbluray',
		'libcdio',
        'python3_libs', # 2019.12.13
		'vapoursynth_libs',
		'rtmpdump',
		'libcaca',
		'iconv',
		'libzimg',
		'libx264', # 2019.12.13 - ??????? query is this multibit ???
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
		'libspeex',
		'libsoxr',
		'rubberband',
		'libass',
		'tesseract',
		#'lensfun',  # 2020.05.12 comment out so we do not have to build glib2
		'libwebp',
		'nv-codec-headers',
		'intel_quicksync_mfx',
		'amf_headers',
        'opencl_icd', #'opencl_non_icd', # 2020.05.09 swap to back to ICD LOADER since they implemented the symbols-only flag
		#'vulkan_loader',
		'avisynth_plus_headers',
		'sdl2', # 2020.05.13 re-enabled sdl2 # 2020.05.13 remove sdl2
	],
}
