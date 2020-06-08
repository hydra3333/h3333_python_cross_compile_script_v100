{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3320000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '598317fd74f5dcc8921949c47665b9e512d0d9c6a445a2e843430f04dc10bda4' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3320000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '598317fd74f5dcc8921949c47665b9e512d0d9c6a445a2e843430f04dc10bda4' }, ], },
		{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3320200.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2dbef1254c1dbeeb5d13d7722d37e633f18ccbba689806b0a65b68701a5b6084' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3320200.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2dbef1254c1dbeeb5d13d7722d37e633f18ccbba689806b0a65b68701a5b6084' }, ], },
	],
	'cflag_addition' : '-fexceptions -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_USE_MALLOC_H=1 -DSQLITE_USE_MSIZE=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing',
	'strip_cflags': ['-ffast-math', ],
	'configure_options': '{autoconf_prefix_options} --enable-threadsafe --disable-editline --enable-readline --enable-json1 --enable-fts5 --enable-session',
	'depends_on': (
		'zlib',
	),
	'update_check' : { 'url' : 'https://www.sqlite.org/index.html', 'type' : 'httpregex', 'regex' : r'<a href="releaselog/.*\.html">Version (?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '3.32.2', 'fancy_name' : 'libsqlite3' },
}
