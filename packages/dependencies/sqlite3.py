{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3320300.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'a31507123c1c2e3a210afec19525fd7b5bb1e19a6a34ae5b998fbd7302568b66' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3320300.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'a31507123c1c2e3a210afec19525fd7b5bb1e19a6a34ae5b998fbd7302568b66' }, ], },
		{ 'url' : 'https://www.sqlite.org/2020/sqlite-autoconf-3330000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '106a2c48c7f75a298a7557bcc0d5f4f454e5b43811cc738b7ca294d6956bbb15' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sqlite-autoconf-3330000.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '106a2c48c7f75a298a7557bcc0d5f4f454e5b43811cc738b7ca294d6956bbb15' }, ], },
	],
	'cflag_addition' : '-fexceptions -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_USE_MALLOC_H=1 -DSQLITE_USE_MSIZE=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing',
	'strip_cflags': ['-ffast-math', ],
	'configure_options': '{autoconf_prefix_options} --enable-threadsafe --disable-editline --enable-readline --enable-json1 --enable-fts5 --enable-session',
	'depends_on': (
		'zlib',
	),
	'update_check' : { 'url' : 'https://www.sqlite.org/index.html', 'type' : 'httpregex', 'regex' : r'<a href="releaselog/.*\.html">Version (?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '3.33', 'fancy_name' : 'libsqlite3' },
}