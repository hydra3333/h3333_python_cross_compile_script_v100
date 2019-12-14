{
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS: http://fftw.org/download.html
		{ "url" : "http://fftw.org/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
		{ "url" : "https://fossies.org/linux/misc/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
	],
    'env_exports' : {
		'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
		'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
	},
	'configure_options': '--host={target_host} --prefix={product_prefix}/fftw3_dll_quad --exec-prefix={product_prefix}/fftw3_dll_quad '
                         '--disable-shared --enable-static '
                         '--disable-silent-rules --disable-doc '
                         '--disable-alloca --with-our-malloc --with-windows-f77-mangling '
                         '--enable-threads --with-combined-threads '
                         '--disable-float --disable-long-double -enable-quad-precision ' # 2019.12.13 (the default is "DOUBLE") we ask quad
                         '--enable-sse2 --enable-avx --enable-avx2 --disable-altivec --disable-vsx --disable-neon ', # 2019.12.13 removed --enable-sse as SSE only builds with "FLOAT/SINGLE"
    #
	'regex_replace': {
		'post_patch': [
			{
				0: r'fftw\${{PREC_SUFFIX}}\.pc',
				1: r'fftw3${{PREC_SUFFIX}}.pc',
				'in_file': '../CMakeLists.txt'
			},
		],
	},
    'run_post_install' : (
		'ls -alR {product_prefix}/fftw3_dll_quad/bin',
	),
	'update_check' : { 'url' : 'ftp://ftp.fftw.org/pub/fftw/', 'type' : 'ftpindex', 'regex' : r'fftw-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '3.3.8', 'fancy_name' : 'fftw3 DLL single' },
}