{
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	#'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'libffmpeg_git',
    #'patches' : [
	#	('ffmpeg/ffmpeg-windres-fix.patch', '-p0' ), # 2021.04.10 for binutils 2.36.1 per https://github.com/rdp/ffmpeg-windows-build-helpers/pull/558/commits/4ec72f9f9dab96f7d2fcb1d5935deded53f4ec21
	#],
	#'configure_options' : '--sysroot={target_sub_prefix} !VAR(ffmpeg_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={target_prefix} --disable-sdl2 --disable-shared --enable-static --disable-doc --disable-programs',
	'configure_options' : '--sysroot={target_sub_prefix} !VAR(ffmpeg_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={target_prefix} --disable-shared --enable-static --disable-doc --disable-programs',
	'depends_on' : [ 'ffmpeg_depends', 'ffmpeg_depends_extra', 'ffmpeg_depends_nonfree',  ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'FFmpeg (library,nonfree)' },
}
