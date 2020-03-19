{
	'repo_type' : 'git',
	'url' : 'https://github.com/mpv-player/mpv.git',
	'build_system' : 'waf',
	'conf_system' : 'waf',
	'rename_folder' : 'libmpv_git',
	#'env_exports' : {
	#	'DEST_OS' : 'win32',
	#	'TARGET'  : '{target_host}',
	#	'LDFLAGS' : '-ld3d11',
	#},
		'env_exports' : {
		'DEST_OS' : '{bit_name_win}', #'DEST_OS' : 'win32',
		'TARGET'  : '{target_host}',
		'PKG_CONFIG' : 'pkg-config',
		#'LDFLAGS': '-Wl,-Bdynamic -lvulkan-1 -fstack-protector-strong' # see my 'custom_ldflag' instead
	},
	'custom_cflag'  : ' -O3 ',
	'custom_ldflag' : ' -Wl,-Bdynamic -lvulkan-1 -fstack-protector-strong -ld3d11 ',
	'run_post_patch' : [ # 2020.03.19 not sure about this, it is not in mpv.py
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
		#'--enable-openal '
		'--enable-dvdread '
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
		'--enable-vulkan '
		'--enable-libplacebo '
		'--enable-libarchive '
		'--enable-javascript '
		'--disable-manpage-build '
		'--enable-pdf-build '
		'TARGET={target_host} '
		'DEST_OS={bit_name_win} ' # 2020.03.19 changed from win32 '
	,
	'depends_on' : [
		'libffmpeg', 
		'zlib',
		'iconv',
		'python3_libs', 
		'vapoursynth_libs',
		'sdl2', 
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
		'vulkan_loader',
		'libplacebo',
	],
	# Dirty hack, so far I've found no way to get -Wl,-Bdynamic into the .pc file or mpv itself without the use of LDFLAGS...
	'regex_replace': {
		'post_patch': [
			{
				0: r'Libs: -L\${{libdir}} -lvulkan',
				1: r'Libs: -L${{libdir}}',
				'in_file': '{pkg_config_path}/vulkan.pc',
				'out_file': '{pkg_config_path}/vulkan.pc'
			},
			{
				0: r' --dirty', # dirty.
				1: r'',
				'in_file': 'version.sh',
			},
		],
		'post_install': [
			{
				0: r'Libs: -L\${{libdir}}',
				1: r'Libs: -L${{libdir}} -lvulkan',
				'in_file': '{pkg_config_path}/vulkan.pc',
				'out_file': '{pkg_config_path}/vulkan.pc'
			}
		]
	},
	'patches': [
		('mpv/0001-resolve-naming-collision-with-xavs2.patch', '-p1'),
	],
	#'packages' : {
	#	'arch' : [ 'rst2pdf' ],
	#},
	#'run_post_configure' : [
	#	'sed -i.bak -r "s/(--prefix=)([^ ]+)//g;s/--color=yes//g" build/config.h',
	#],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mpv (library)' },
}