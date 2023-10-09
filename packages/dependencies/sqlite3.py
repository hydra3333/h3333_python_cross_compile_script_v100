{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/ 
		#{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3410200.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e98c100dd1da4e30fa460761dab7c0b91a50b785e167f8c57acc46514fae9499' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3410200.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e98c100dd1da4e30fa460761dab7c0b91a50b785e167f8c57acc46514fae9499' }, ], },
		{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3430100.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '39116c94e76630f22d54cd82c3cea308565f1715f716d1b2527f1c9c969ba4d9' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3430100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '39116c94e76630f22d54cd82c3cea308565f1715f716d1b2527f1c9c969ba4d9' }, ], },
		
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
	'_info' : { 'version' : '3.41.2', 'fancy_name' : 'libsqlite3' },
}
