{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'rename_folder' : 'libx264_git',
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} '
							'--prefix={target_prefix} '
							'--enable-strip --enable-lto --enable-pic '
							'--bit-depth=all '
							'--chroma-format=all ' # 2020.06.09
                            '--disable-lsmash '
							'--disable-win32thread ' # make posix threeads like the other things being built
							'--extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" '
							'--disable-cli --disable-lavf ' # 2020.06.09 re-added --disable-lavf to libx264 building only
							,
	'env_exports' : { # 2020.06.09 hope this happens AFTER dependencies built
		#'PKGCONFIG' : 'pkg-config',
		## 2020.06.09 only the x264 package, not this dependency depends on libffmpeg_extra being built first, so comment this out or it fails to build
		#'SWSCALE_LIBS' : '!CMD(pkg-config --libs libswscale)CMD!',
		#'LAVF_LIBS'    : '!CMD(pkg-config --libs libavformat libavcodec libavutil libswscale)CMD!',  # 2020.06.09
		#'LAVF_CFLAGS'  : '!CMD(pkg-config --cflags libavformat libavcodec libavutil libswscale)CMD!',  # 2020.06.09
	},
	#'run_post_patch' : [ # 2020.06.09 see what should be returned for env_exports
	#	'pkg-config --libs libswscale',
	#	'pkg-config --libs libavformat libavcodec libavutil libswscale',
	#	'pkg-config --cflags libavformat libavcodec libavutil libswscale',	# 2020.06.09
	#],
	#'run_post_configure' : [ # 2020.06.09 see if the EXPORT stuff worked
	#	'export | grep SWSCALE_LIBS',
	#	'export | grep LAVF_LIBS',
	#	'export | grep LAVF_CFLAGS',
	#],
	'depends_on' : [
		'zlib', 
		'opencl_non_icd', # 2020.06.09
		# 2020.06.09 only the x264 package, not the libx264 dependency depends on libffmpeg_extra being built first,
		#'libffmpeg_extra',   # 2021.07.21 lsmashworks no longer builds :( 'liblsw',  # 2019.12.13 HolyWu's lsw does not need avresample as it uses libswresample # 2018.11.23 superseded: liblsw required --enable-avresample which was deprecated
		#'libgpac',  # libgpac depends on libffmpeg
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264 (library) multibit' },
}
