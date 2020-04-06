{
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	'depth_git': 0,
	'branch' : '7b0f7a7f3b6bf09c076c23d0701bf42a2c997ca2',
	'rename_folder' : 'libffmpeg_extra_git',
	'configure_options' : '--sysroot={target_sub_prefix} !VAR(ffmpeg_config)VAR! !VAR(ffmpeg_extra_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={target_prefix} --disable-sdl2 --disable-shared --enable-static --disable-doc --disable-programs',
	'depends_on' : [ 'ffmpeg_depends', 'ffmpeg_depends_extra', 'ffmpeg_depends_nonfree', ],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'FFmpeg (library,nonfree,extra)' },
}
