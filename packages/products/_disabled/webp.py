{
	'repo_type' : 'git',
	'url' : 'https://chromium.googlesource.com/webm/libwebp',
	'rename_folder' : 'webp_git',
	'configure_options': '--host={target_host} --prefix={output_prefix}/webp.installed --disable-shared --enable-static --enable-swap-16bit-csp --enable-libwebpmux --enable-libwebpdemux --enable-libwebpdecoder --enable-libwebpextras',
    'run_post_regexreplace': [ # 2019.12.13
		'sed -i.bak "s/\$LIBPNG_CONFIG /\$LIBPNG_CONFIG --static /g" ./configure.ac', # fix building with libpng # 2019.12.13
		'autoreconf -fiv', # 2019.12.13
	],
	'regex_replace': {
		'post_patch': [
			{
				# for some silly reason they only build libwebpmux when these variables are set ON,
				# however if they're on it will also build the binary CLI tools IMG2WEBP.exe and GIF2WEBP.exe,
				# which we do not want or need... so this hack exists.
				#
				# Note: Probably warrants a pull-request, maybe later.
				#
				0: r'if\(WEBP_BUILD_GIF2WEBP OR WEBP_BUILD_IMG2WEBP\)',
				1: r'if(MINGW)',
				'in_file': './CMakeLists.txt'
			},
		],
	},
	'depends_on' : [ 'xz', 'libpng', 'libjpeg-turbo', 'libwebp', ],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libwebp' },
}
# grr, the muxer and demuxer won;t build under cmake.
# original:
#{
#	'repo_type' : 'git',
#	'url' : 'https://chromium.googlesource.com/webm/libwebp',
#	'rename_folder' : 'webp_muxer_git',
#	'source_subfolder': '_build',
#	'conf_system' : 'cmake',
#	'configure_options' : '.. {cmake_prefix_options} '
#		'-DCMAKE_INSTALL_PREFIX={output_prefix}/webp.installed -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release'
#		'-DWEBP_ENABLE_SIMD=ON '
#		'-DWEBP_NEAR_LOSSLESS=ON '
#		'-DWEBP_UNICODE=ON '
#		'-DWEBP_BUILD_CWEBP=OFF '
#		'-DWEBP_BUILD_DWEBP=OFF '
#		'-DWEBP_BUILD_VWEBP=OFF '
#		'-DWEBP_BUILD_WEBPINFO=OFF ' #
#		'-DWEBP_BUILD_WEBPMUX=OFF ' #
#		'-DWEBP_BUILD_EXTRAS=OFF '
#		'-DWEBP_BUILD_ANIM_UTILS=OFF '
#		'-DWEBP_BUILD_GIF2WEBP=OFF '
#		'-DWEBP_BUILD_IMG2WEBP=OFF '
#		'-DWEBP_BUILD_WEBP_JS=OFF '
#		'-DWEBP_ENABLE_SWAP_16BIT_CSP=ON ' #
#	,
#    'run_post_regexreplace': [ # 2019.12.13
#		'sed -i.bak "s/\$LIBPNG_CONFIG /\$LIBPNG_CONFIG --static /g" ../configure.ac', # fix building with libpng # 2019.12.13
#		#'autoreconf -fiv', # 2019.12.13
#	], # 2019.12.13
#	'regex_replace': {
#		'post_patch': [
#			{
#				# for some silly reason they only build libwebpmux when these variables are set ON,
#				# however if they're on it will also build the binary CLI tools IMG2WEBP.exe and GIF2WEBP.exe,
#				# which we do not want or need... so this hack exists.
#				#
#				# Note: Probably warrants a pull-request, maybe later.
#				#
#				0: r'if\(WEBP_BUILD_GIF2WEBP OR WEBP_BUILD_IMG2WEBP\)',
#				1: r'if(MINGW)',
#				'in_file': '../CMakeLists.txt'
#			},
#		],
#	},
#	'depends_on' : [ 'xz', 'libpng', 'libjpeg-turbo', 'libwebp', ],
#	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libwebp' },
#}
# 2019.12.13 old:
#	'libwebp' : {
#		'repo_type' : 'git',
#		'url' : 'https://chromium.googlesource.com/webm/libwebp',
#		#'branch' : '082757087332f55c7daa5a869a19f1598d0be401', #old: e4eb458741f61a95679a44995c212b5f412cf5a1
#		'run_post_regexreplace': [
#			'sed -i.bak "s/\$LIBPNG_CONFIG /\$LIBPNG_CONFIG --static /g" configure.ac', # fix building with libpng
#			'autoreconf -fiv',
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-swap-16bit-csp --enable-libwebpmux --enable-libwebpdemux --enable-libwebpdecoder --enable-libwebpextras',
#		'depends_on' : [ 'libpng', 'libjpeg-turbo' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libwebp' },
#	},
