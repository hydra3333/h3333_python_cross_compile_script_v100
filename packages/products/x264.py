{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} '
							'--prefix={output_prefix}/x264_git.installed '
							'--enable-strip --bit-depth=all ' # 2020.06.09 when building .exe do not --disable-cli # leave off --disable-lavf
							'--extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ', # 2019.12.13
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	'depends_on' : [
		'libffmpeg_extra', 'liblsw',  # 2019.12.13 HolyWu's lsw does not need avresample as it uses libswresample # 2018.11.23 superseded: liblsw required --enable-avresample which was deprecated
	],
    'env_exports' : { # 2020.06.09 hope this happens AFTER dependencies built
		##'PKG_CONFIG'   : 'PKGCONFIG' : 'pkg-config', # 2020.06.09
		##'PKG_CONFIG'   : 'PKGCONFIG' : '{cross_prefix_full}pkg-config' # 2020.06.09
		'LAVF_LIBS'    : '!CMD({cross_prefix_full}pkg-config --libs libavformat libavcodec libavutil libswscale)CMD!',  # 2020.06.09
		'LAVF_CFLAGS'  : '!CMD({cross_prefix_full}pkg-config --cflags libavformat libavcodec libavutil libswscale)CMD!',  # 2020.06.09
		'SWSCALE_LIBS' : '!CMD({cross_prefix_full}pkg-config --libs libswscale)CMD!',
	},
	#'run_post_configure' : [ # 2020.06.09 see if the EXPORT stuff worked
	#	'export | grep LAVF_LIBS',
	#	'export | grep LAVF_CFLAGS',
	#	'export | grep SWSCALE_LIBS',
	#],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264' },
}
