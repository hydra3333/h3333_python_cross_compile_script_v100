{
	'repo_type' : 'git',
	#'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	'url' : 'https://github.com/hydra3333/FFmpeg.git',
	'depth_git': 0,
	#'branch' : '5727b1f13f36c4db30d5d0de51640f740edf01e8',
	'rename_folder' : 'ffmpeg',
	'env_exports' : { # 2020.06.19
		'CFLAGS'   : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ',
		'CXXFLAGS' : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ',
		'CPPFLAGS' : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ', # 2020.06.20 per https://github.com/fribidi/fribidi/issues/146#issuecomment-646991416
		'LDFLAGS'  : ' -DFRIBIDI_LIB_STATIC {original_cflags} -lssp ',
	},
	# 2022.05.10 MABS added the below to patch ffmpeg, so when 2.23 is released we should add it to all ffmpeg product/dependency .py !
	#'patches' : [
	#	('ffmpeg/MABS-0001-configure-add-check-for-sdl2-2.23.0.patch', '-Np1'),
	#],
	'cpu_count' : '1',
	'configure_options' : 
		'!VAR(ffmpeg_config)VAR! '
		'!VAR(ffmpeg_extra_config)VAR! '
		'!VAR(ffmpeg_nonfree)VAR! '
		'--prefix={output_prefix}/ffmpeg_git.installed --disable-shared --enable-static ',
	'depends_on' : [ 'ffmpeg_depends', 'ffmpeg_depends_extra', 'ffmpeg_depends_nonfree', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffmpeg (static) nonfree with OpenCL' }, # 2019.12.13 say that it includes nonfree and openCL
}
