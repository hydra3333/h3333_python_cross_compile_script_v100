{
	'is_dep_inheriter' : True,
	'depends_on' : [
		'bzip2',
		'zlib',
		'lzma',
		'fontconfig', # fontconfig builds 'freetype'
		'gnutls',
		#'freetype', # it depends on 'freetype_lib', 'harfbuzz_lib-with-freetype' so it builds these in the right order
		'libbluray',
		'libcdio',
		'python3_libs',
		'vapoursynth_libs',
		'rtmpdump',
		'librist',  # 2021.08.27
		#'libcaca', # 2021.10.23 now requires autoconf 2.71 which causes other dependencies to fail
		'iconv',
		'libzimg',
		'libx264', # 2020.06.09 only the x264 package, not the dependency depends on libffmpeg_extra being built first
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
		'libfribidi',
		'libass',
		#'tesseract', # 2020.06.27 comment out as no longer required
		#'lensfun',  # 2020.05.12 comment out so we do not have to build glib2
		'libjxl',
		'libwebp',
		'rav1e',
		'nv-codec-headers',
		'intel_quicksync_mfx', # 2022.05.27 re-enable # 2022.05.25 comment out intel_quicksync_mfx since ffmpeg quicksync no longer detects https://github.com/lu-zero/mfx_dispatch.git as valid.
		'amf_headers',
		#'opencl_icd', # 2020.11.24
		'opencl_non_icd', # 2020.11.24
		'vulkan_from_windows_dll', # 'vulkan_loader',
		'spirv-headers', 'spirv-cross', 'spirv-tools', 'shaderc', 'glslang', 'libplacebo', # all these go together
		'avisynth_plus_headers',
		'sdl2', # 2020.05.13 re-enabled sdl2 # 2020.05.13 remove sdl2
	],
}
