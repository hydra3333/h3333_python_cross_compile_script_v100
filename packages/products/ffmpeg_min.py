{
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	'rename_folder' : 'ffmpeg_min',
	'configure_options' : '!VAR(ffmpeg_min_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={output_prefix}/ffmpeg_min_git.installed --enable-sdl --disable-shared --enable-static', # 2019.12.13
	'depends_on' : [ 'ffmpeg_depends_min', 'ffmpeg_depends_nonfree', 'sdl2'],
	'_info' : { 'version' : None, 'fancy_name' : 'ffmpeg (static, min) free with OpenCL ex fdk_aac' }, # 2019.12.13 clarify that it means non free with OpenCL (but no fdk_aac)
}