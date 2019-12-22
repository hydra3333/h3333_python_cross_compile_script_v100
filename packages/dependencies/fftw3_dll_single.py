{
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS: http://fftw.org/download.html
		{ "url" : "http://fftw.org/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
		{ "url" : "https://fossies.org/linux/misc/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
	],
	'rename_folder' : 'fftw3_dll_single',
	'configure_options': '--host={target_host} --prefix={output_prefix}/fftw3_dll --exec-prefix={output_prefix}/fftw3_dll '
                         '--enable-shared --disable-static '
                         '--disable-silent-rules --disable-doc '
                         '--disable-alloca --with-our-malloc --with-windows-f77-mangling '
                         '--enable-threads --with-combined-threads '
                         '--enable-float --disable-long-double -disable-quad-precision ' # 2019.12.13 (the default is "DOUBLE") "float" is single
                         '--enable-sse --enable-sse2 --enable-avx --enable-avx2 --disable-altivec --disable-vsx --disable-neon ' # 2019.12.13 did not removed --enable-sse as SSE only builds with "FLOAT/SINGLE"
    ,
	'regex_replace': {
		'post_patch': [
			{
				0: r'fftw\${{PREC_SUFFIX}}\.pc',
				1: r'fftw3${{PREC_SUFFIX}}.pc',
				'in_file': './CMakeLists.txt'
			},
		],
	},
    'run_post_install' : (
		'ls -alR {output_prefix}/fftw3_dll/bin',
	),
	'update_check' : { 'url' : 'ftp://ftp.fftw.org/pub/fftw/', 'type' : 'ftpindex', 'regex' : r'fftw-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '3.3.8', 'fancy_name' : 'fftw3_dll_single' },
}
# 2019.12.13 old:
#	'fftw3_dll_single' : { # libfftw3f.dll.a # create the FFTW DLLs which we can use with things like avisynth etc
#	    # see 
#		#	ftp://ftp.fftw.org/pub/fftw/ for the source
#		#	ftp://ftp.fftw.org/pub/fftw/BUILD-MINGW64.sh for their 64bit build script
#		#	http://www.fftw.org/install/windows.html for extra advice on building, eg --enable-portable-binary
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: http://fftw.org/download.html
#			{ "url" : "http://fftw.org/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
#		],
#		'rename_folder' : 'fftw3_dll_single',
#		'env_exports' : {
#			'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		},
#		# note: this "configure" line is for type "single" only, refer to ftp://ftp.fftw.org/pub/fftw/BUILD-MINGW64.sh 
#		# http://forum.doom9.org/showthread.php?p=1857272#post1857272 about stack boundary --with-incoming-stack-boundary=2  for 32bit only
#		'configure_options': '--host={target_host} --prefix={product_prefix}/fftw3_dll_single --exec-prefix={product_prefix}/fftw3_dll_single '
#							'--disable-silent-rules --disable-doc --disable-alloca --with-our-malloc --with-windows-f77-mangling '
#							'--enable-shared --disable-static --enable-threads --with-combined-threads --enable-sse2 --enable-avx '
#							'--disable-altivec --disable-vsx --disable-neon --enable-single ',
#		'run_post_install' : (
#			'ls -alR {product_prefix}/fftw3_dll_single/bin',
#		),
#		'_info' : { 'version' : '3.3.8', 'fancy_name' : 'fftw3-dll-single only' },
#	},