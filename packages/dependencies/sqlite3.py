{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/
		#{ 'url' : 'https://www.sqlite.org/2021/sqlite-autoconf-3370000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '731a4651d4d4b36fc7d21db586b2de4dd00af31fd54fb5a9a4b7f492057479f7' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3370000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '731a4651d4d4b36fc7d21db586b2de4dd00af31fd54fb5a9a4b7f492057479f7' }, ], },
		{ 'url' : 'https://www.sqlite.org/2021/sqlite-autoconf-3370100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '40f22a13bf38bbcd4c7ac79bcfb42a72d5aa40930c1f3f822e30ccce295f0f2e' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3370100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '40f22a13bf38bbcd4c7ac79bcfb42a72d5aa40930c1f3f822e30ccce295f0f2e' }, ], },
	],
	'cflag_addition' : '-fexceptions -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_USE_MALLOC_H=1 -DSQLITE_USE_MSIZE=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing',
	'strip_cflags': ['-ffast-math', ],
	'configure_options': '{autoconf_prefix_options} --enable-threadsafe --disable-editline --enable-readline --enable-json1 --enable-fts5 --enable-session',
	'depends_on': (
		'zlib',
	),
	'update_check' : { 'url' : 'https://www.sqlite.org/index.html', 'type' : 'httpregex', 'regex' : r'<a href="releaselog/.*\.html">Version (?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '3.37.0', 'fancy_name' : 'libsqlite3' },
}