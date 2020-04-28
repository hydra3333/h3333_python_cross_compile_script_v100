{
	'is_dep_inheriter' : True,
	'depends_on' : [
		'bzip2',
		'zlib',
		'lzma',
		'fontconfig',
		'freetype', # it depends on 'freetype_lib', 'harfbuzz_lib-with-freetype'
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
		'lensfun',
		'libwebp',
		'nv-codec-headers',
		'intel_quicksync_mfx',
		'amf_headers',
        'opencl_non_icd', # 2020.04.28 swap to non ICD LOADER # 2019.12.13 added this to the minimum configuration, I depend on openCL
		#'vulkan_loader',
		'avisynth_plus_headers',
	],
}
