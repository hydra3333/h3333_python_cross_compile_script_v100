{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/ 
		#{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3380500.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5af07de982ba658fd91a03170c945f99c971f6955bc79df3266544373e39869c' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3380500.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : '5af07de982ba658fd91a03170c945f99c971f6955bc79df3266544373e39869c' }, ], },
		{ 'url' : 'https://www.sqlite.org/2022/sqlite-autoconf-3390000.tar.gz' , 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e90bcaef6dd5813fcdee4e867f6b65f3c9bfd0aec0f1017f9f3bbce1e4ed09e2' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3390000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e90bcaef6dd5813fcdee4e867f6b65f3c9bfd0aec0f1017f9f3bbce1e4ed09e2' }, ], },
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
	'_info' : { 'version' : '3.38.5', 'fancy_name' : 'libsqlite3' },
}
