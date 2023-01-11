{
	'repo_type' : 'git',
	'url' : 'https://github.com/mpv-player/mpv.git',
	'build_system' : 'waf',
	'conf_system' : 'waf',
	'rename_folder' : 'libmpv_git',
	'env_exports' : {
		'DEST_OS' : '{bit_name_win}', #'DEST_OS' : 'win32',
		'TARGET'  : '{target_host}',
		'PKG_CONFIG' : 'pkg-config',
		#'LDFLAGS' : '-Wl,-Bdynamic -lvulkan-1 -fstack-protector-strong ' # see my 'custom_ldflag' instead
		#'WAF_NO_PREFORK' : '1', # 2023.01.11 per https://github.com/m-ab-s/media-autobuild_suite/commit/df2e20294debda9780da42738e003818243be06c?diff=split
	},
	'custom_cflag' : ' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} ', # 2020.05.13 
	'custom_ldflag' : ' -Wl,-Bdynamic {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -fstack-protector-strong -lvulkan-1 -lz -ld3d11 -lintl -liconv ',
	#'patches': [
	#	('mpv/0001-resolve-naming-collision-with-xavs2.patch', '-p1'), # resolve naming collision with xavs2
	#],
	'run_post_regexreplace' : [ # 2022.03.18 replace the patch with some sed # resolve naming collision with xavs2
		'sed -i.bak \'s/encoder_encode(/encoder_encode_mpv(/g\' audio/out/ao_lavc.c',
		'sed -i.bak \'s/encoder_encode(/encoder_encode_mpv(/g\' common/encode_lavc.c',
		'sed -i.bak \'s/encoder_encode(/encoder_encode_mpv(/g\' common/encode_lavc.h',
		'sed -i.bak \'s/encoder_encode(/encoder_encode_mpv(/g\' video/out/vo_lavc.c',
	],
	'configure_options' :
		'--prefix={target_prefix} '
		'TARGET={target_host} '
		'DEST_OS={bit_name_win} ' # 2020.03.19 changed from DEST_OS=win32
		'--force '
		'--enable-libmpv-shared '
		'--enable-static-build '
		'--disable-debug-build '
		'--disable-html-build '
		'--disable-android '
		'--disable-egl-android '
		'--disable-tvos '
		'--disable-swift '
		'--enable-iconv '
		'--enable-zlib '
		#'--enable-zimg ' # including -lzimg always throws an error
		'--enable-libavdevice '
		'--enable-cuda-hwaccel '
		'--enable-cuda-interop '
		#'--enable-sdl2 ' # 2020.05.14 added back ... no it fails in mpv.py (not the lib)
		'--disable-sdl2 ' # 2022.12.18 per DEADSIX27
		'--enable-rubberband '
		'--enable-lcms2 '
		# '--enable-openal '
		# '--enable-dvdread ' # commented out, no such option
		'--enable-dvdnav '
		'--enable-libbluray '
		'--enable-cdda '
		#'--enable-egl-angle-lib ' # not maintained anymore apparently, crashes for me anyway.
		'--disable-xv '
		'--disable-alsa '
		'--disable-pulse '
		'--disable-jack '
		'--disable-x11 '
		'--disable-wayland '
		#'--disable-wayland-protocols '
		#'--disable-wayland-scanner '
		#'--enable-libass ' # commented out, no such option
		'--enable-lua '
		'--enable-vapoursynth '
		'--enable-uchardet '
		'--enable-vulkan '
		'--enable-libplacebo '
		'--enable-libarchive '
		'--enable-javascript '
		'--disable-manpage-build '
		'--disable-pdf-build '
	,
	'depends_on' : [
		#'opencl_icd', # 2020.11.24
		'opencl_non_icd', # 2020.11.24
		'vulkan_from_windows_dll', # 'vulkan_loader',
		'zlib',
		#'libzimg', # including -lzimg always throws an error
		'iconv',
		'python3_libs',
		'vapoursynth_libs',
		#'sdl2', # 2022.12.18 per DEADSIX27
		'luajit',
		'rubberband',
		'lcms2',
		'libcdio-paranoia',
		'libdvdread',
		'libdvdnav',
		'libbluray',
		#'openal',
		'libass',
		'libjpeg-turbo',
		'uchardet',
		'libarchive',
		'mujs',
		'shaderc',
		'libplacebo',
		'libffmpeg_extra',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mpv (library)' },
}