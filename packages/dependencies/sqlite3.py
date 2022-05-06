{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/ 
		#{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3380000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1c76e25dc63d9f3935e0f406aec520a33ee77cf54ea5147dffe1fae8369eff68' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3380000.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '1c76e25dc63d9f3935e0f406aec520a33ee77cf54ea5147dffe1fae8369eff68' }, ], },
		{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3380200.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e7974aa1430bad690a5e9f79a6ee5c8492ada8269dc675875ad0fb747d7cada4' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3380200.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e7974aa1430bad690a5e9f79a6ee5c8492ada8269dc675875ad0fb747d7cada4' }, ], },
	],
	'cflag_addition' : '-fexceptions -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_USE_MALLOC_H=1 -DSQLITE_USE_MSIZE=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing',
	'strip_cflags': ['-ffast-math', ],
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'configure_options': '{autoconf_prefix_options} --enable-threadsafe --disable-editline --enable-readline --enable-json1 --enable-fts5 --enable-session',
	'depends_on': (
		'zlib',
	),
	'update_check' : { 'url' : 'https://www.sqlite.org/index.html', 'type' : 'httpregex', 'regex' : r'<a href="releaselog/.*\.html">Version (?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '3.38.2', 'fancy_name' : 'libsqlite3' },
}
