{
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	#'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'libffmpeg_extra_git',
	#'configure_options' : '--sysroot={target_sub_prefix} !VAR(ffmpeg_config)VAR! !VAR(ffmpeg_extra_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={target_prefix} --disable-sdl2 --disable-shared --enable-static --disable-doc --disable-programs',
	'configure_options' : '--sysroot={target_sub_prefix} !VAR(ffmpeg_config)VAR! !VAR(ffmpeg_extra_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={target_prefix} --disable-shared --enable-static --disable-doc --disable-programs',
	'patches' : [
        ('ffmpeg/0001-Replace-deprecated-libsrt-calls-from-MABS.patch', '-p1'), # 2020.07.01 fix deprecated stuff
	 ],
	'depends_on' : [ 'ffmpeg_depends', 'ffmpeg_depends_extra', 'ffmpeg_depends_nonfree', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'FFmpeg (library,nonfree,extra)' },
}
