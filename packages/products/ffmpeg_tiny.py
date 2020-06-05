{
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	#'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'ffmpeg_tiny',
	'configure_options' : '!VAR(ffmpeg_config_tiny)VAR! --prefix={output_prefix}/ffmpeg_tiny_git.installed --disable-shared --enable-static',
	'depends_on' : [ 'ffmpeg_depends_tiny', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffmpeg (static) tiny nonfree with OpenCL' }, # 2019.12.13 say that it includes nonfree and openCL
}
