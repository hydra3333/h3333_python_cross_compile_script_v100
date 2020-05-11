{ # pcre added 2019.12.13  ... superseded by pcre2 ? Nope, not for glib2
	'repo_type' : 'archive',
	'download_locations' : [
		{ "url" : "https://fossies.org/linux/misc/pcre-8.44.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "19108658b23b3ec5058edc9f66ac545ea19f9537234be1ec62b714c84399366d" }, ], },
		{ "url" : "https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "19108658b23b3ec5058edc9f66ac545ea19f9537234be1ec62b714c84399366d" }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-unicode-properties --enable-utf --enable-pcre8 --enable-pcre16 --enable-pcre32 --enable-pcregrep-libz --enable-pcregrep-libbz2 --enable-newline-is-anycrlf --disable-pcre2test-libedit --disable-pcretest-libreadline --enable-jit ', 
	'depends_on' : [
		'bzip2', 'zlib',
	],
	'_info' : { 'version' : '8.43', 'fancy_name' : 'pcre' },
}
