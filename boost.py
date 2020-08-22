{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://dl.bintray.com/boostorg/release/1.73.0/source/boost_1_73_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4eb3b8d442b426dc35346235c8733b5ae35ba431690e38c6a8263dce9fcbb402' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/boost_1_73_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4eb3b8d442b426dc35346235c8733b5ae35ba431690e38c6a8263dce9fcbb402' }, ], },
		{ 'url' : 'https://dl.bintray.com/boostorg/release/1.74.0/source/boost_1_74_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '83bfc1507731a0906e387fc28b7ef5417d591429e51e788417fe9ff025e116b1' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/boost_1_74_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '83bfc1507731a0906e387fc28b7ef5417d591429e51e788417fe9ff025e116b1' }, ], },
		# in WIn10 use powershell to find the sha256 of a file https://www.youtube.com/watch?v=YM2CE6zKvoo&t=57
	],
	'needs_make' :False,
	'needs_make_install' :False,
	'needs_configure' :False,
	'run_post_regexreplace' : [
		'if [ ! -f "already_configured_0" ] ; then ./bootstrap.sh mingw --prefix={target_prefix} ; fi',
		'if [ ! -f "already_configured_0" ] ; then sed -i.bak \'s/case \*       : option = -pthread ; libs = rt ;/case *      : option = -pthread ;/\' tools/build/src/tools/gcc.jam ; fi',
		'if [ ! -f "already_configured_0" ] ; then touch already_configured_0 ; fi',
		'if [ ! -f "already_ran_make_0" ] ; then echo "using gcc : mingw : {cross_prefix_bare}g++ : <rc>{cross_prefix_bare}windres <archiver>{cross_prefix_bare}ar <ranlib>{cross_prefix_bare}ranlib ;" > user-config.jam ; fi',
		'if [ ! -f "already_ran_make_0" ] ; then ./b2 toolset=gcc-mingw link=static threading=multi target-os=windows address-model=64 architecture=x86 --prefix={target_prefix} variant=release --with-system --with-filesystem --with-regex --with-date_time --with-thread --user-config=user-config.jam install ; fi',
		'if [ ! -f "already_ran_make_0" ] ; then touch already_ran_make_0 ; fi',
	],
	'update_check' : { 'url' : 'https://sourceforge.net/projects/boost/files/boost/', 'type' : 'sourceforge', 'regex' : r'(?P<version_num>[\d.]+)', },
	'_info' : { 'version' : '1.74.0', 'fancy_name' : 'Boost' },
}
