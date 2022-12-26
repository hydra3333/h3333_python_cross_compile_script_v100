{
	'repo_type' : 'git',
	#'url' : 'https://git.videolan.org/git/ffmpeg/nv-codec-headers.git',
	'url' : 'https://github.com/FFmpeg/nv-codec-headers.git', # 2020.09.30 videolan not responding :(
	'needs_configure' : False,
	'build_options' : 'PREFIX={target_prefix}',
	'install_options' : 'PREFIX={target_prefix}',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'nVidia (headers)' },
}
