{
	'repo_type' : 'git',
	'url' : 'https://github.com/mpv-player/mpv.git',
	'build_system' : 'waf',
	'conf_system' : 'waf',
	'rename_folder' : 'libmpv_git',
	#'env_exports' : {
	#	'DEST_OS' : 'win32',
	#	'TARGET'  : '{target_host}',
	#	'PKG_CONFIG' : 'pkg-config',
	#	'LDFLAGS': '-Wl,-Bdynamic -lvulkan-1 -fstack-protector-strong' # See near 'regex_replace'
	#},
	'env_exports' : {
		'DEST_OS' : '{bit_name_win}', #'DEST_OS' : 'win32',
		'TARGET'  : '{target_host}',
		'PKG_CONFIG' : 'pkg-config',
		#'LDFLAGS' : '-Wl,-Bdynamic -lvulkan-1 -fstack-protector-strong ' # see my 'custom_ldflag' instead
	},
	'custom_cflag' : ' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} ', # 2020.05.13 
	'custom_ldflag' : ' -Wl,-Bdynamic {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -fstack-protector-strong -lvulkan -lz -ld3d11 -lintl -liconv ',
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
		'--enable-sdl2 ' # 2020.05.14 added back ... no it fails in mpv.py (not the lib)
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
		'--disable-wayland-protocols '
		'--disable-wayland-scanner '
		#'--enable-libass ' # commented out, no such option
		'--enable-lua '
		'--enable-vapoursynth '
		'--enable-uchardet '
		#'--enable-vulkan ' # 2020.10.12 comment out vulkan since it an no longer be statically linked
		'--enable-vulkan ' # 2021.10.30 re-try vulkan
		'--enable-libplacebo '
		'--enable-libarchive '
		'--enable-javascript '
		'--disable-manpage-build '
		'--disable-pdf-build '
	,
	'depends_on' : [
		#'opencl_icd', # 2020.11.24
		'opencl_non_icd', # 2020.11.24
		#'vulkan_loader', # 2020.10.12 comment out vulkan since it can no longer be statically linked
		'vulkan_loader', # 2021.10.30 re-try vulkan
		'zlib',
		#'libzimg', # including -lzimg always throws an error
		'iconv',
		'python3_libs',
		'vapoursynth_libs',
		'sdl2', # 2020.05.13 re-enable # 2020.05.13 remove SDL2
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

	'patches': [
		('mpv/0001-resolve-naming-collision-with-xavs2.patch', '-p1'),
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mpv (library)' },
}