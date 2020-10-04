{
	'is_dep_inheriter' : True,
	'depends_on' : [
		'libxml2',
		'libx264', # 2020.06.09 only the x264 package, not the dependency depends on libffmpeg_extra being built first
		'libx265_multibit',
		'libvpx',
		'libaom',
		'xvidcore',
		'libopus',
		'liblame',
		'libogg',
		'libvorbis',
		'libtheora',
		'libsoxr',
		'rubberband',
		'libwebp',
		'nv-codec-headers',
		'opencl_icd',
		'vulkan_loader',
		'fdk_aac',
		'twolame',
		#'wavpack', # deleted from ffmpeg 2020.10.04
		'fftw3',
	],
}
