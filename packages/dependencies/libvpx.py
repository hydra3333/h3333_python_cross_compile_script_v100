{
	'repo_type' : 'git',
	'url' : 'https://chromium.googlesource.com/webm/libvpx',
	'configure_options' :
		'--target={bit_name2}-{bit_name_win}-gcc '
		'--prefix={target_prefix} --disable-shared '
		'--enable-static --enable-webm-io --enable-libyuv --enable-vp9 '
		'--enable-vp8 --enable-runtime-cpu-detect --enable-postproc '
		'--enable-vp9-highbitdepth --enable-vp9-postproc --enable-coefficient-range-checking --enable-postproc-visualizer '
		'--enable-error-concealment --enable-better-hw-compatibility '
		'--enable-multi-res-encoding --enable-vp9-temporal-denoising '
		'--disable-tools --disable-docs --disable-examples --disable-install-docs --disable-unit-tests --disable-decode-perf-tests --disable-encode-perf-tests '
        '--disable-avx512 --as=nasm' # # 2019.12.13 removed --as=yasm, added --disable-avx512
	,
	'env_exports' : {
		'CROSS' : '{cross_prefix_bare}',
	},
    'custom_cflag' : '{original_cflags}', # 2019.12.13
	'cflag_addition' : '-fno-asynchronous-unwind-tables',
	'patches' : [
		( 'vpx/vpx_160_semaphore.patch', '-p1' ),
	],
	'_info' : { 'version' : None, 'fancy_name' : 'libvpx' },
}