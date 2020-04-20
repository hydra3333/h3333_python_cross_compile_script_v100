{
	'repo_type' : 'git',
	'url' : 'https://git.videolan.org/git/ffmpeg/nv-codec-headers.git',
	#'url' : 'https://github.com/FFmpeg/nv-codec-headers.git', # 2020.04.20 videolan not responding :(
	'needs_configure' : False,
	'build_options' : 'PREFIX={target_prefix}',
	'install_options' : 'PREFIX={target_prefix}',
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'nVidia (headers)' },
}
# 2019.12.13 old:
#	'nv-codec-headers' : { # https://code.videolan.org/ # https://code.videolan.org/?p=ffmpeg/nv-codec-headers.git;a=shortlog
#		'repo_type' : 'git',
#		'url' : 'https://git.videolan.org/git/ffmpeg/nv-codec-headers.git',
#		#'url' : 'https://code.videolan.org/videolan/ffmpeg/nv-codec-headers.git',
#		"needs_configure": False,
#		'build_options': 'PREFIX={target_prefix}',
#		'install_options' : 'PREFIX={target_prefix}',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'nVidia (headers)' },
#	},