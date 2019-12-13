{
	'repo_type' : 'git',
	'url' : 'https://github.com/mpv-player/mpv.git',
	'build_system' : 'waf',
	'conf_system' : 'waf',
	'rename_folder' : 'libmpv_git',
	'env_exports' : {
		'DEST_OS' : 'win32',
		'TARGET'  : '{target_host}',
		'LDFLAGS' : '-ld3d11',
	},
	'run_post_patch' : [
		'cp -nv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"',
		'sed -i.bak "s/encoder_encode/mpv_encoder_encode/" common/encode_lavc.h', # Dirty work-around for xavs2, no idea how else to fix this.
		'sed -i.bak "s/encoder_encode/mpv_encoder_encode/" video/out/vo_lavc.c',  #
		'sed -i.bak "s/encoder_encode/mpv_encoder_encode/" audio/out/ao_lavc.c',  #
		'sed -i.bak "s/encoder_encode/mpv_encoder_encode/" common/encode_lavc.c', #
	],
	'configure_options' :
		'--enable-libmpv-shared '
		'--disable-debug-build '
		'--prefix={target_prefix} '
		'--enable-sdl2 '
		'--enable-rubberband '
		'--enable-lcms2 '
		'--enable-dvdread '
		'--enable-openal '
		'--enable-dvdnav '
		'--enable-libbluray '
		#'--enable-egl-angle-lib '
		'--disable-xv '
		'--disable-alsa '
		'--disable-pulse '
		'--disable-jack '
		'--disable-x11 '
		'--disable-wayland '
		'--disable-wayland-protocols '
		'--disable-wayland-scanner '
		'--enable-cdda '
		'--enable-libass '
		'--enable-lua '
		'--enable-vapoursynth '
		'--enable-encoding '
		'--enable-uchardet '
		'--enable-libarchive '
		'--enable-javascript '
		'--disable-manpage-build '
		'--enable-pdf-build '
		'TARGET={target_host} '
		'DEST_OS=win32 '
	,
	'depends_on' : [
		'libffmpeg', 'python3_libs', 'vapoursynth_libs','sdl2', 'luajit', 'lcms2', 'libdvdnav', 'libbluray', 'openal', 'libass', 'libcdio-paranoia', 'libjpeg-turbo', 'uchardet', 'libarchive', 'mujs', 'shaderc', 'vulkan_loader',
	],
	'packages' : {
		'arch' : [ 'rst2pdf' ],
	},
	'run_post_configure' : [
		'sed -i.bak -r "s/(--prefix=)([^ ]+)//g;s/--color=yes//g" build/config.h',
	],
	'_info' : { 'version' : None, 'fancy_name' : 'mpv (library)' },
}