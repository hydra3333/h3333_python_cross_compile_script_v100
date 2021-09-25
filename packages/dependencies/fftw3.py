{
    #----------------------------------------------------------------------------
    # Deadsix27's cmake version wouldn't build for me !!!   No idea why.
    #    error: 'ALIGNMENTA' undeclared (first use in this function); did you mean 'ALIGNEDA'?
    #    error: 'ALIGNMENT' undeclared (first use in this function); did you mean 'ALIGNED'?
    # So revert to my known good build using old make
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'http://fftw.org/fftw-3.3.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303' }, ], },
	#	{ 'url' : 'https://fossies.org/linux/misc/fftw-3.3.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303' }, ], },
	#],
    #'cflag_addition': '-DWITH_OUR_MALLOC',
	#'conf_system' : 'cmake',
	#'source_subfolder' : '_build',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release '
	#	'-DBUILD_TESTS=OFF '
	#	'-DENABLE_THREADS=ON '
	#	'-DENABLE_FLOAT=OFF ' # 2019.12.13 ?? SSE requires SINGLE (FLOAT) precision and does not build without it ??? also, the default build is DOULBLE (no separate flag for it)
	#	'-DENABLE_LONG_DOUBLE=OFF '
	#	'-DENABLE_QUAD_PRECISION=OFF '
	#	'-DENABLE_SSE=ON '
	#	'-DENABLE_SSE2=ON '
	#	'-DENABLE_AVX=ON '
	#	'-DENABLE_AVX2=ON '
    #   '-DBUILD_DOC=OFF ' # 2019.12.13
    #   # In some things "-lfftw" must be changed to "-lfftw3", however also note the ".pc" change below (check libramplerate, rubberbabd)
	#,
    #
    # 2019.12.13  'fftw3' from my build, it works.
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS: http://fftw.org/download.html
		#{ "url" : "http://fftw.org/fftw-3.3.9.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "bf2c7ce40b04ae811af714deb512510cc2c17b9ab9d6ddcf49fe4487eea7af3d" }, ], },
		#{ "url" : "https://fossies.org/linux/misc/fftw-3.3.9.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "bf2c7ce40b04ae811af714deb512510cc2c17b9ab9d6ddcf49fe4487eea7af3d" }, ], },
		{ "url" : "http://fftw.org/fftw-3.3.10.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "56c932549852cddcfafdab3820b0200c7742675be92179e59e6215b340e26467" }, ], },
		{ "url" : "https://fossies.org/linux/misc/fftw-3.3.10.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "56c932549852cddcfafdab3820b0200c7742675be92179e59e6215b340e26467" }, ], },
	],
	'rename_folder' : 'fftw3_for_ffmpeg',
	'configure_options': '--host={target_host} --prefix={target_prefix} '
						 '--disable-shared --enable-static '
                            '--disable-silent-rules --disable-doc '
                            '--disable-alloca --with-our-malloc --with-windows-f77-mangling '
                            '--enable-threads --with-combined-threads '
                            '--disable-float --disable-long-double -disable-quad-precision ' # 2019.12.13 so the default is "DOUBLE"
                            '--enable-sse2 --enable-avx --enable-avx2 --disable-altivec --disable-vsx --disable-neon ' # 2019.12.13 removed --enable-sse as SSE only builds with "FLOAT/SINGLE"
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
	'update_check' : { 'url' : 'ftp://ftp.fftw.org/pub/fftw/', 'type' : 'ftpindex', 'regex' : r'fftw-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '3.3.9', 'fancy_name' : 'fftw3' },
}
