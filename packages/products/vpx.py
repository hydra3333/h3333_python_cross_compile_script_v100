{
	'repo_type' : 'git',
	'url' : 'https://chromium.googlesource.com/webm/libvpx',
	'rename_folder' : 'vpx_git',
	'configure_options' :
		'--target={bit_name2}-{bit_name_win}-gcc '
		'--prefix={output_prefix}/vpx_git.installed '
		'--disable-shared --enable-static --enable-webm-io --enable-libyuv --enable-vp9 ' # --disable-webm-io
		'--enable-vp8 --enable-runtime-cpu-detect --enable-postproc '
		'--enable-vp9-highbitdepth --enable-vp9-postproc --enable-coefficient-range-checking --enable-postproc-visualizer '
		'--enable-error-concealment --enable-better-hw-compatibility '
		'--enable-multi-res-encoding --enable-vp9-temporal-denoising '
		'--enable-tools --enable-docs --enable-examples --enable-install-docs '
		'--disable-unit-tests --disable-decode-perf-tests --disable-encode-perf-tests '
		'--disable-avx512 --as=nasm '  # 2013.13.13 back to --as=nasm rather than yasm # 2019.12.13 removed --as=yasm, added --disable-avx512
	,
	'env_exports' : {
		'CROSS' : '{cross_prefix_bare}',
	},
	#'custom_cflag' : ' -fno-asynchronous-unwind-tables {original_cflags} ', # 2019.12.13
	'patches' : [
		( 'vpx/vpx_160_semaphore.patch', '-p1' ),
	],
	'_info' : { 'version' : None, 'fancy_name' : 'vpx' },
}
# 2019.12.13 old:
#	'vpx' : {
#		'repo_type' : 'git',
#		'url' : 'https://chromium.googlesource.com/webm/libvpx',
#		'rename_folder' : 'vpx_git',
#		'configure_options':
#			'--target={bit_name2}-{bit_name_win}-gcc '
#			'--prefix={product_prefix}/vpx_git.installed '
#			'--disable-shared --enable-static --enable-webm-io --enable-vp9 '
#			'--enable-vp8 --enable-runtime-cpu-detect '
#			'--enable-vp9-highbitdepth --enable-vp9-postproc --enable-coefficient-range-checking '
#			'--enable-error-concealment --enable-better-hw-compatibility '
#			'--enable-multi-res-encoding --enable-vp9-temporal-denoising '
#			'--enable-tools --disable-docs --enable-examples --disable-install-docs --disable-unit-tests --disable-decode-perf-tests --disable-encode-perf-tests --disable-avx512 --as=nasm' #--as=yasm'
#		,
#		'env_exports' : {
#			'CROSS' : '{cross_prefix_bare}',
#		},
#		#'custom_cflag' : '-fno-asynchronous-unwind-tables {original_cflags}',
#		'custom_cflag' : '{original_cflags}',
#		'patches': (
#			( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/vpx_160_semaphore.patch', '-p1' ),
#		),
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'vpx' },
#	},