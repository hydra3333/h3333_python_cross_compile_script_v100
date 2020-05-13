{
	'repo_type' : 'git',
	'url' : 'https://github.com/mpv-player/mpv.git',
	'build_system' : 'waf',
	'conf_system' : 'waf',
	'rename_folder' : 'mpv_git',
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
	#'custom_cflag'  : ' -O3 ',
	'custom_cflag'  :' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} ', # 2020.05.13 
	#'custom_ldflag' : ' -Wl,-Bdynamic -lvulkan-1 -fstack-protector-strong -lz -ld3d11 -lintl -liconv ', # 2020.03.19 added -ld3d11 per from libmpv.py also added -lintl -liconv # including -lzimg always throws an error
	'custom_ldflag' : ' -Wl,-Bdynamic {original_cflag_trim} {original_stack_protector_trim} -lz -ld3d11 -lintl -liconv ', # 2020.04.09
	'configure_options' :
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
		'--prefix={output_prefix}/mpv_git.installed '
		'--disable-sdl2 ' ## 2020.05.13 removed SDL2 '--enable-sdl2 ' 
		'--enable-rubberband '
		'--enable-lcms2 '
		# '--enable-openal '
		# '--enable-dvdread ' # commented out, no such option
		'--enable-dvdnav '
		'--enable-libbluray '
		#'--enable-egl-angle-lib ' # not maintained anymore apparently, crashes for me anyway.
		'--disable-xv '
		'--disable-alsa '
		'--disable-pulse '
		'--disable-jack '
		'--disable-x11 '
		'--disable-wayland '
		'--disable-wayland-protocols '
		'--disable-wayland-scanner '
		'--enable-cdda '
		#'--enable-libass ' # commented out, no such option
		'--enable-lua '
		'--enable-vapoursynth '
		'--enable-uchardet '
		# '--enable-vulkan '
		'--enable-libplacebo '
		'--enable-libarchive '
		'--enable-javascript '
		'--disable-manpage-build '
		'--disable-pdf-build '
		'TARGET={target_host} '
		'DEST_OS={bit_name_win} ' # 2020.03.19 changed from 'DEST_OS=win32 '
	,
	'depends_on' : [
		'opencl_icd',
		#'vulkan_loader',
		'zlib',
		#'libzimg', # including -lzimg always throws an error
		'iconv',
		'python3_libs',
		'vapoursynth_libs',
		#'sdl2',
		'luajit',
		'rubberband',
		'lcms2',
		'libdvdread',
		'libdvdnav',
		'libbluray',
		#'openal',
		'libass',
		'libcdio-paranoia',
		'libjpeg-turbo',
		'uchardet',
		'libarchive',
		'mujs',
		'shaderc',
		'libplacebo',
		'libffmpeg',
	],
	# 2020.04.09 commented out
	# Dirty hack, so far I've found no way to get -Wl,-Bdynamic into the .pc file or mpv itself without the use of LDFLAGS...
	#'regex_replace': {
	#	'post_patch': [
	#		{
	#			0: r'Libs: -L\${{libdir}} -lvulkan-1',
	#			1: r'Libs: -L${{libdir}}',
	#			'in_file': '{pkg_config_path}/vulkan.pc',
	#			'out_file': '{pkg_config_path}/vulkan.pc'
	#		},
	#		{
	#			0: r' --dirty', # dirty.
	#			1: r'',
	#			'in_file': 'version.sh',
	#		},
	#	],
	#	'post_install': [
	#		{
	#			0: r'Libs: -L\${{libdir}}',
	#			1: r'Libs: -L${{libdir}} -lvulkan-1',
	#			'in_file': '{pkg_config_path}/vulkan.pc',
	#			'out_file': '{pkg_config_path}/vulkan.pc'
	#		}
	#	]
	#},
	'patches': [
		('mpv/0001-resolve-naming-collision-with-xavs2.patch', '-p1'),
	],
	'run_post_install' : (
		'{cross_prefix_bare}strip -v {output_prefix}/mpv_git.installed/bin/mpv.com',
		'{cross_prefix_bare}strip -v {output_prefix}/mpv_git.installed/bin/mpv.exe',
		'{cross_prefix_bare}strip -v {output_prefix}/mpv_git.installed/bin/mpv-1.dll',
	),
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mpv' },
}