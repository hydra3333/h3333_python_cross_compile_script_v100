{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'rename_folder' : 'libx264_git',
	#'configure_options' : '--host={target_host} --prefix={target_prefix} --enable-static --cross-prefix={cross_prefix_bare} --enable-strip --disable-lavf --disable-cli',  # 2019.12.13
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} --prefix={target_prefix} --enable-strip --disable-lavf --disable-cli --enable-strip --bit-depth=all --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ', # 2019.12.13
	'_info' : { 'version' : None, 'fancy_name' : 'x264 (library) multibit' },
}