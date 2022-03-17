{
	'repo_type' : 'git',
	'url' : 'https://chromium.googlesource.com/webm/libwebp',
    'depth_git' : 0,
	'branch' : 'main',  # they've changed the trunk from master to main (a US political race thing against the word, apparently)
	'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF '
		'-DWEBP_ENABLE_SIMD=ON '
		'-DWEBP_NEAR_LOSSLESS=ON '
		'-DWEBP_UNICODE=ON '
		'-DWEBP_BUILD_GIF2WEBP=OFF '
		'-DWEBP_BUILD_IMG2WEBP=OFF '
		'-DWEBP_BUILD_CWEBP=OFF '
		'-DWEBP_BUILD_DWEBP=OFF '
		'-DWEBP_BUILD_VWEBP=OFF '
		'-DWEBP_BUILD_WEBPINFO=OFF '
		'-DWEBP_BUILD_WEBPMUX=OFF '
		'-DWEBP_BUILD_EXTRAS=OFF '
		'-DWEBP_BUILD_ANIM_UTILS=OFF '
		'-DWEBP_BUILD_WEBP_JS=OFF '
		'-DWEBP_ENABLE_SWAP_16BIT_CSP=ON '
        '-DCMAKE_BUILD_TYPE=Release '
	,
    'run_post_regexreplace': [ # 2019.12.13
		'sed -i.bak "s/\$LIBPNG_CONFIG /\$LIBPNG_CONFIG --static /g" ../configure.ac', # fix building with libpng # 2019.12.13
		#'autoreconf -fiv', # 2019.12.13
	], # 2019.12.13
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
				'in_file': '../CMakeLists.txt'
			},
		],
	},
	'run_post_regexreplace' : [
		'pwd ; cd .. ; sh ./autogen.sh ; cd _build ; pwd',
	],
	'depends_on' : [ 'xz', 'libpng', 'libjpeg-turbo' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libwebp' },
}
