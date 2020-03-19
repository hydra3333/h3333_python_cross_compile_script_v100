{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/x264.git',
	'rename_folder' : 'libx264_git',
	'configure_options' : '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} --prefix={target_prefix} --enable-strip --disable-lavf --disable-cli --enable-strip --bit-depth=all --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ', # 2019.12.13
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264 (library) multibit' },
}
# 2019.12.13 old:
#	'libx264' : { # http://code.videolan.org/?p=x264.git;a=shortlog
#		'repo_type' : 'git',
#		#'url' : 'https://git.videolan.org/git/x264.git',
#		'url' : 'https://code.videolan.org/videolan/x264.git',
#		'rename_folder' : 'libx264_git',
#		'needs_configure': True,
#		'configure_options': '--host={target_host} --enable-static --cross-prefix={cross_prefix_bare} --prefix={target_prefix} --enable-strip --disable-lavf --disable-cli --enable-strip --bit-depth=all --extra-cflags="-DLIBXML_STATIC" --extra-cflags="-DGLIB_STATIC_COMPILATION" ',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x264 (library) multibit' },
#	},