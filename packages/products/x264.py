{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} --prefix={output_prefix}/x264_git.installed --enable-strip --bit-depth=all --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ', # 2019.12.13
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	'depends_on' : [
		'libffmpeg', 'liblsw',  # 2019.12.13 HolyWu's lsw does not need avresample as it uses libswresample # 2018.11.23 superseded: liblsw required --enable-avresample which was deprecated
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264' },
}
# 2019.12.13 old:
#	'x264' : {
#		'repo_type' : 'git',
#		#'url' : 'https://git.videolan.org/git/x264.git',
#		'url' : 'https://code.videolan.org/videolan/x264.git',
#		'configure_options': '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} --prefix={product_prefix}/x264_git.installed --enable-strip --bit-depth=all --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ', 
#		'env_exports' : {
#			'PKGCONFIG' : 'pkg-config',
#		},
#		'depends_on' : [
#			'libffmpeg', 'liblsw',  # 2019.11.19 HolyWu's lsw does not need avresample as it uses libswresample # 2018.11.23 added liblsw. Note: lsw requires --enable-avresample which is deprecated # 'libgpac', gave up on gpac
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264' },
#	},