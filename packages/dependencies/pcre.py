{ # pcre added 2019.12.13  ... superseded by pcre2 ? Nope, not for glib2
	'repo_type' : 'archive',
	'download_locations' : [
		#{ "url" : "https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "0b8e7465dc5e98c757cc3650a20a7843ee4c3edf50aaf60bb33fd879690d2c73" }, ], },
		{ "url" : "https://fossies.org/linux/misc/pcre-8.44.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "19108658b23b3ec5058edc9f66ac545ea19f9537234be1ec62b714c84399366d" }, ], },
		{ "url" : "https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "19108658b23b3ec5058edc9f66ac545ea19f9537234be1ec62b714c84399366d" }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-unicode-properties --enable-utf --enable-pcre8 --enable-pcre16 --enable-pcre32 --enable-pcregrep-libz --enable-pcregrep-libbz2 --enable-newline-is-anycrlf --disable-pcre2test-libedit --disable-pcretest-libreadline --enable-jit ', 
	'depends_on' : [
		'bzip2', 'zlib',
	],
	'_info' : { 'version' : '8.43', 'fancy_name' : 'pcre' },
}
# 2019.12.13 old:
#	'pcre' : { # Alexpux
#		'repo_type' : 'archive',
#		'download_locations' : [
#			{ "url" : "https://ftp.pcre.org/pub/pcre/pcre-8.42.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "69acbc2fbdefb955d42a4c606dfde800c2885711d2979e356c0636efde9ec3b5" }, ], },
#		],
#		'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-unicode-properties --enable-utf --enable-pcre8 --enable-pcre16 --enable-pcre32 --enable-pcregrep-libz --enable-pcregrep-libbz2 --enable-newline-is-anycrlf --disable-pcre2test-libedit --disable-pcretest-libreadline --enable-jit ', 
#		'depends_on' : [
#			'bzip2', 'zlib',
#		],
#		'_info' : { 'version' : '8.42', 'fancy_name' : 'pcre' },
#	},