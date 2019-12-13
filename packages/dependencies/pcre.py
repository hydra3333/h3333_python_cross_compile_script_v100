{ # pcre aded 2019.12.13
	'repo_type' : 'archive',
	'download_locations' : [
		{ "url" : "https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "91e762520003013834ac1adb4a938d53b22a216341c061b0cf05603b290faf6b" }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-unicode-properties --enable-utf --enable-pcre8 --enable-pcre16 --enable-pcre32 --enable-pcregrep-libz --enable-pcregrep-libbz2 --enable-newline-is-anycrlf --disable-pcre2test-libedit --disable-pcretest-libreadline --enable-jit ', 
	'depends_on' : [
		'bzip2', 'zlib',
	],
	'_info' : { 'version' : '8.43', 'fancy_name' : 'pcre' },
},