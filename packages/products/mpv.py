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
	'custom_ldflag' : ' -Wl,-Bdynamic {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -lz -ld3d11 -lintl -liconv ', # 2020.04.09
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
		#'--enable-sdl2 ' # 2020.05.14 added back # 2020.05.13 re-enable '--disable-sdl2 ' ## 2020.05.13 removed SDL2 '--enable-sdl2 ' 
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
		#'--enable-vulkan ' # 2020.10.12 comment out vulkan since it an no longer be statically linked
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
		#'vulkan_loader', # 2020.10.12 comment out vulkan since it an no longer be statically linked
		'zlib',
		#'libzimg', # including -lzimg always throws an error
		'iconv',
		'python3_libs',
		'vapoursynth_libs',
		#'sdl2', # 2020.05.14 added back ... no it fails in mpv.py
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
		'libffmpeg_extra',
	],
	#'patches': [ 
	#	('mpv/0001-resolve-naming-collision-with-xavs2.patch', '-p1'), # 2020.09.01 replaced by the 4 "sed" below
	#],
	'run_post_regexreplace' : [
		'sed -i.bak1 "s/encoder_encode(/encoder_encode_mpv(/g" "audio/out/ao_lavc.c"',  # 2020.09.01 replaces the patch above
		'sed -i.bak1 "s/encoder_encode(/encoder_encode_mpv(/g" "common/encode_lavc.c"', # 2020.09.01 replaces the patch above
		'sed -i.bak1 "s/encoder_encode(/encoder_encode_mpv(/g" "common/encode_lavc.h"', # 2020.09.01 replaces the patch above
		'sed -i.bak1 "s/encoder_encode(/encoder_encode_mpv(/g" "video/out/vo_lavc.c"',  # 2020.09.01 replaces the patch above
	],
	'run_post_install' : (
		'{cross_prefix_bare}strip -v {output_prefix}/mpv_git.installed/bin/mpv.com',
		'{cross_prefix_bare}strip -v {output_prefix}/mpv_git.installed/bin/mpv.exe',
		'{cross_prefix_bare}strip -v {output_prefix}/mpv_git.installed/bin/mpv-1.dll',
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mpv' },
}