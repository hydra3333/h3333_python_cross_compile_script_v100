{
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS: http://fftw.org/download.html
		#{ "url" : "http://fftw.org/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
		#{ "url" : "https://fossies.org/linux/misc/fftw-3.3.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303" }, ], },
		{ "url" : "http://fftw.org/fftw-3.3.9.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "bf2c7ce40b04ae811af714deb512510cc2c17b9ab9d6ddcf49fe4487eea7af3d" }, ], },
		{ "url" : "https://fossies.org/linux/misc/fftw-3.3.9.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "bf2c7ce40b04ae811af714deb512510cc2c17b9ab9d6ddcf49fe4487eea7af3d" }, ], },
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
	'_info' : { 'version' : '3.3.9', 'fancy_name' : 'fftw3_dll_single' },
}
