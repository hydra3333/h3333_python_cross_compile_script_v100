{
	'repo_type' : 'git',
	#'url' : 'https://git.videolan.org/git/ffmpeg/nv-codec-headers.git',
	'url' : 'https://github.com/FFmpeg/nv-codec-headers.git', # 2020.09.30 videolan not responding :(
	'folder_name' : 'ffms2_nv-codec-headers',
	'needs_configure' : False,
	'build_options' : 'PREFIX={output_prefix}/ffms2_dll.installed',
	'install_options' : 'PREFIX={output_prefix}/ffms2_dll.installed',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffms2_nVidia (headers)' },
}
