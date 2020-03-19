{
	'repo_type' : 'git',
	'url' : 'https://chromium.googlesource.com/webm/libwebp',
	'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={output_prefix}/webp.installed -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release'
		'-DWEBP_ENABLE_SIMD=ON '
		'-DWEBP_NEAR_LOSSLESS=ON '
		'-DWEBP_UNICODE=ON '

		'-DWEBP_BUILD_GIF2WEBP=OFF '
		'-DWEBP_BUILD_IMG2WEBP=OFF '
		'-DWEBP_BUILD_WEBPMUX=OFF '
		'-DWEBP_BUILD_ANIM_UTILS=OFF '
		'-DWEBP_BUILD_CWEBP=ON '
		'-DWEBP_BUILD_DWEBP=ON '
		'-DWEBP_BUILD_VWEBP=ON '
		'-DWEBP_BUILD_WEBPINFO=ON '
		'-DWEBP_BUILD_EXTRAS=OFF '
		'-DWEBP_BUILD_WEBP_JS=OFF '
		'-DWEBP_ENABLE_SWAP_16BIT_CSP=ON '
	,
#   'run_post_patch': [ # 2019.12.13
#		'sed -i.bak "s/\$LIBPNG_CONFIG /\$LIBPNG_CONFIG --static /g" ../configure.ac', # fix building with libpng # 2019.12.13
#		#'autoreconf -fiv', # 2019.12.13
#	], # 2019.12.13
	'depends_on' : [ 'xz', 'libpng', 'libjpeg-turbo', 'libwebp', ], # [ 'libpng', 'libjpeg-turbo' ],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'webp' },
}