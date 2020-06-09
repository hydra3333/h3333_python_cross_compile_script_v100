{ # 2020.06.09 now built with lavf 
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} '
							'--prefix={output_prefix}/x264_git.installed '
							'--enable-strip --enable-lto --enable-pic '
							'--bit-depth=all '
							'--chroma-format=all ' # 2020.06.09
							'--extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" '
							#'--disable-cli --disable-lavf ' # 2020.06.09 when building .exe do not --disable-cli and also leave off --disable-lavf																								
							,
	'depends_on' : [
		'opencl_icd.py', # 2020.06.09
		'libffmpeg_extra', 'liblsw',  # 2019.12.13 HolyWu's lsw does not need avresample as it uses libswresample # 2018.11.23 superseded: liblsw required --enable-avresample which was deprecated
	],
	'env_exports' : { # 2020.06.09 hope this happens AFTER dependencies built
		'PKGCONFIG' : 'pkg-config',
		'SWSCALE_LIBS' : '!CMD(pkg-config --libs libswscale)CMD!',
		'LAVF_LIBS'    : '!CMD(pkg-config --libs libavformat libavcodec libavutil libswscale)CMD!',  # 2020.06.09
		'LAVF_CFLAGS'  : '!CMD(pkg-config --cflags libavformat libavcodec libavutil libswscale)CMD!',  # 2020.06.09
	},
	#'run_post_patch' : [ # 2020.06.09 see what should be returned for env_exports
	#	'pkg-config --libs libswscale',
	#	'pkg-config --libs libavformat libavcodec libavutil libswscale',
	#	'pkg-config --cflags libavformat libavcodec libavutil libswscale',  # 2020.06.09
	#],
	#'run_post_configure' : [ # 2020.06.09 see if the EXPORT stuff worked
	#	'export | grep SWSCALE_LIBS',
	#	'export | grep LAVF_LIBS',
	#	'export | grep LAVF_CFLAGS',
	#],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264 multibit built with lsw and lavf' },
}
