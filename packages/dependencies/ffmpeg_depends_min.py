{
	'is_dep_inheriter' : True,
	'depends_on' : [
		'bzip2',
		'zlib',
		'lzma',
		'fontconfig',
		'freetype',
		'libbluray',
		'libcdio',
		'vapoursynth_libs',
		'rtmpdump',
		'libcaca',
		'iconv',
		'libzimg', # 2019.12.13 - ??????? query is this multibit ???
		'libx264', # 2019.12.13 - ??????? query is this multibit ???
		'libx265_multibit',
		#'openh264', # 2019.12.13 comment out
		#'kvazaar',  # 2019.12.13 comment out
		'libvpx',
		'libdav1d',
		'libaom',
		'libxvid',
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
        'opencl_icd',  # 2019.12.13 added this to the minimum configuration, I depend on it
	],
}