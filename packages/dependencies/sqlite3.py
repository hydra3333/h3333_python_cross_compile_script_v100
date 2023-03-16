{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/ 
		#{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3400100.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '2c5dea207fa508d765af1ef620b637dcb06572afa6f01f0815bd5bbf864b33d9' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3400100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2c5dea207fa508d765af1ef620b637dcb06572afa6f01f0815bd5bbf864b33d9' }, ], },
		{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3410000.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '49f77ac53fd9aa5d7395f2499cb816410e5621984a121b858ccca05310b05c70' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3410000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '49f77ac53fd9aa5d7395f2499cb816410e5621984a121b858ccca05310b05c70' }, ], },
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
	'_info' : { 'version' : '3.41.0', 'fancy_name' : 'libsqlite3' },
}
