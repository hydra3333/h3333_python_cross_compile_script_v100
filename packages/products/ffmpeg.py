{
	'repo_type' : 'git',
	'url' : 'git://git.ffmpeg.org/ffmpeg.git',
	'rename_folder' : 'ffmpeg',
	'configure_options' : '!VAR(ffmpeg_config)VAR! !VAR(ffmpeg_extra_config)VAR! !VAR(ffmpeg_nonfree)VAR! --prefix={output_prefix}/ffmpeg_git.installed --enable-sdl --disable-shared --enable-static',
	'depends_on' : [ 'ffmpeg_depends', 'ffmpeg_depends_extra', 'ffmpeg_depends_nonfree', 'sdl2'],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffmpeg (static) nonfree with OpenCL' }, # 2019.12.13 say that it includes nonfree and openCL
}
# 2019.12.13 old:
#	'ffmpeg_static_non_free_opencl' : { # with decklink, fdk-aac and opencl
#		'repo_type' : 'git',
#		'url' : 'git://git.ffmpeg.org/ffmpeg.git',
#		'rename_folder' : 'ffmpeg_static_non_free_opencl',
#		'configure_options': '!VAR(ffmpeg_base_config)VAR! !VAR(ffmpeg_nonfree_config)VAR! --prefix={product_prefix}/ffmpeg_static_non_free_opencl.installed --enable-opencl ', 
#		'depends_on': [ 'ffmpeg_depends', 'ffmpeg_depends_nonfree', 'opencl_icd' ], # 'svt_av1', 'svt_vp9', 'svt_hevc' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffmpeg NonFree (static (OpenCL))' },
#	},
