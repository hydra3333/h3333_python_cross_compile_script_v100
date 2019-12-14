{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} --prefix={output_prefix}/x264_git.installed --enable-strip --bit-depth=all --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ', # 2019.12.13
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	'depends_on' : [
		'libffmpeg', 'liblsw',  # 2019.12.13 HolyWu's lsw does not need avresample as it uses libswresample # 2018.11.23 old liblsw requires --enable-avresample which is deprecated
	],
	'_info' : { 'version' : None, 'fancy_name' : 'x264' },
}