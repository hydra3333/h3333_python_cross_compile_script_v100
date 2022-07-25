{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/ 
		#{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3390100.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '87c8e7a7fa0c68ab28e208ba49f3a22a56000dbf53a6f90206e2bc5843931cc4' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3390100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '87c8e7a7fa0c68ab28e208ba49f3a22a56000dbf53a6f90206e2bc5843931cc4' }, ], },
		{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3390200.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '852be8a6183a17ba47cee0bbff7400b7aa5affd283bf3beefc34fcd088a239de' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3390200.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '852be8a6183a17ba47cee0bbff7400b7aa5affd283bf3beefc34fcd088a239de' }, ], },
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
	'_info' : { 'version' : '3.39.1', 'fancy_name' : 'libsqlite3' },
}
