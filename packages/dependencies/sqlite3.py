{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/ 
		{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3380100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8e3a8ceb9794d968399590d2ddf9d5c044a97dd83d38b9613364a245ec8a2fc4' }, ], },
		# fall back to older version on fossies ... why did fossies revert ?
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3380000.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '1c76e25dc63d9f3935e0f406aec520a33ee77cf54ea5147dffe1fae8369eff68' }, ], },
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
	'_info' : { 'version' : '3.37.2', 'fancy_name' : 'libsqlite3' },
}
