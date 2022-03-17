{
	'repo_type' : 'git',
	'url' : 'https://chromium.googlesource.com/webm/libvpx',
	'depth_git' : 0,
	'branch' : 'main',  # they've changed the trunk from master to main (a US political race thing against the word, apparently)
	'configure_options' :
		'--target={bit_name2}-{bit_name_win}-gcc '
		'--prefix={target_prefix} '
		'--disable-shared --enable-static --enable-webm-io --enable-libyuv --enable-vp9 '
		'--enable-vp8 --enable-ssse3 --enable-runtime-cpu-detect --enable-postproc '
		'--enable-vp9-highbitdepth --enable-vp9-postproc --enable-postproc-visualizer ' # 2020.10.01 removed --enable-coefficient-range-checking 
		'--enable-error-concealment --enable-better-hw-compatibility '
		'--enable-multi-res-encoding --enable-vp9-temporal-denoising '
		'--disable-tools --disable-docs --disable-examples --disable-install-docs ' # 2019.12.13 enable tools and examples
		'--disable-unit-tests --disable-decode-perf-tests --disable-encode-perf-tests '
        '--disable-avx512 --as=nasm ' # 2013.13.13 back to --as=nasm rather than yasm # 2019.12.13 removed --as=yasm, added --disable-avx512
	,
	'env_exports' : {
		'CROSS' : '{cross_prefix_bare}',
	},
	#'custom_cflag' : ' -fno-asynchronous-unwind-tables {original_cflags} ', # 2019.12.13
	'patches' : [
		( 'vpx/vpx_160_semaphore.patch', '-p1' ),
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libvpx' },
}
