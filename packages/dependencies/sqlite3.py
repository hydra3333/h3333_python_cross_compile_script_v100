{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/
		#{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3340100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2a3bca581117b3b88e5361d0ef3803ba6d8da604b1c1a47d902ef785c1b53e89' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3340100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2a3bca581117b3b88e5361d0ef3803ba6d8da604b1c1a47d902ef785c1b53e89' }, ], },
		#{ 'url' : 'https://www.sqlite.org/2021/sqlite-autoconf-3350400.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '7771525dff0185bfe9638ccce23faa0e1451757ddbda5a6c853bb80b923a512d' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3350400.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '7771525dff0185bfe9638ccce23faa0e1451757ddbda5a6c853bb80b923a512d' }, ], },
		{ 'url' : 'https://www.sqlite.org/2021/sqlite-autoconf-3350500.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f52b72a5c319c3e516ed7a92e123139a6e87af08a2dc43d7757724f6132e6db0' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3350500.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f52b72a5c319c3e516ed7a92e123139a6e87af08a2dc43d7757724f6132e6db0' }, ], },
	],
	'cflag_addition' : '-fexceptions -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_USE_MALLOC_H=1 -DSQLITE_USE_MSIZE=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing',
	'strip_cflags': ['-ffast-math', ],
	'configure_options': '{autoconf_prefix_options} --enable-threadsafe --disable-editline --enable-readline --enable-json1 --enable-fts5 --enable-session',
	'depends_on': (
		'zlib',
	),
	'update_check' : { 'url' : 'https://www.sqlite.org/index.html', 'type' : 'httpregex', 'regex' : r'<a href="releaselog/.*\.html">Version (?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '3.35.4', 'fancy_name' : 'libsqlite3' },
}