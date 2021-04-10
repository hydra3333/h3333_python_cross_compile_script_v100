{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3340100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2a3bca581117b3b88e5361d0ef3803ba6d8da604b1c1a47d902ef785c1b53e89' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3340100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2a3bca581117b3b88e5361d0ef3803ba6d8da604b1c1a47d902ef785c1b53e89' }, ], },
		{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3350400.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2a3bca581117b3b88e5361d0ef3803ba6d8da604b1c1a47d902ef785c1b53e89' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3350400.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2a3bca581117b3b88e5361d0ef3803ba6d8da604b1c1a47d902ef785c1b53e89' }, ], },
	],
	'cflag_addition' : '-fexceptions -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_USE_MALLOC_H=1 -DSQLITE_USE_MSIZE=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing',
	'strip_cflags': ['-ffast-math', ],
	'configure_options': '{autoconf_prefix_options} --enable-threadsafe --disable-editline --enable-readline --enable-json1 --enable-fts5 --enable-session',
	'depends_on': (
		'zlib',
	),
	'update_check' : { 'url' : 'https://www.sqlite.org/index.html', 'type' : 'httpregex', 'regex' : r'<a href="releaselog/.*\.html">Version (?P<version_num>[\d.]+)<\/a>' },
	#'_info' : { 'version' : '3.34', 'fancy_name' : 'libsqlite3' },
	'_info' : { 'version' : '3.34.1', 'fancy_name' : 'libsqlite3' },
}