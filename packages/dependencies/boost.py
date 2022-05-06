{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://fossies.org/linux/misc/boost_1_78_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8681f175d4bdb26c52222665793eef08490d7758529330f98d3b29dd0735bccc' }, ], },
		#{ 'url' : 'https://dl.bintray.com/boostorg/release/1.78.0/source/boost_1_78_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8681f175d4bdb26c52222665793eef08490d7758529330f98d3b29dd0735bccc' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/boost_1_79_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '475d589d51a7f8b3ba2ba4eda022b170e562ca3b760ee922c146b6c65856ef39' }, ], },
		{ 'url' : 'https://dl.bintray.com/boostorg/release/1.79.0/source/boost_1_79_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '475d589d51a7f8b3ba2ba4eda022b170e562ca3b760ee922c146b6c65856ef39' }, ], },
		# in WIn10 use powershell to find the sha256 of a file https://www.youtube.com/watch?v=YM2CE6zKvoo&t=57
	],
	'needs_make' :False,
	'needs_make_install' :False,
	'needs_configure' :False,
	#'run_post_regexreplace' : [ # 2020.08.23 comment out
	#	'if [ ! -f "already_configured_0" ] ; then ./bootstrap.sh mingw --prefix={target_prefix} ; fi',
	#	'if [ ! -f "already_configured_0" ] ; then sed -i.bak \'s/case \*       : option = -pthread ; libs = rt ;/case *      : option = -pthread ;/\' tools/build/src/tools/gcc.jam ; fi',
	#	'if [ ! -f "already_configured_0" ] ; then touch already_configured_0 ; fi',
	#	
	#	'if [ ! -f "already_ran_make_0" ] ; then echo "using gcc : mingw : {cross_prefix_bare}g++ : <rc>{cross_prefix_bare}windres <archiver>{cross_prefix_bare}ar <ranlib>{cross_prefix_bare}ranlib ;" > user-config.jam ; fi',
	#	'if [ ! -f "already_ran_make_0" ] ; then ./b2 toolset=gcc-mingw link=static threading=multi target-os=windows address-model=64 architecture=x86 --prefix={target_prefix} variant=release --with-system --with-filesystem --with-regex --with-date_time --with-thread --user-config=user-config.jam install ; fi',
	#	'if [ ! -f "already_ran_make_0" ] ; then touch already_ran_make_0 ; fi',
	#],
	'run_post_regexreplace' : [ # 2020.08.23 always do the actions
		'./bootstrap.sh mingw --prefix={target_prefix}',
		'sed -i.bak \'s/case \*       : option = -pthread ; libs = rt ;/case *      : option = -pthread ;/\' tools/build/src/tools/gcc.jam',
		'echo "using gcc : mingw : {cross_prefix_bare}g++ : <rc>{cross_prefix_bare}windres <archiver>{cross_prefix_bare}ar <ranlib>{cross_prefix_bare}ranlib ;" > user-config.jam',
		'./b2 toolset=gcc-mingw link=static threading=multi target-os=windows address-model=64 architecture=x86 --prefix={target_prefix} variant=release --with-system --with-filesystem --with-regex --with-date_time --with-thread --user-config=user-config.jam install',
	],
	'update_check' : { 'url' : 'https://sourceforge.net/projects/boost/files/boost/', 'type' : 'sourceforge', 'regex' : r'(?P<version_num>[\d.]+)', },
	'_info' : { 'version' : '1.79.0', 'fancy_name' : 'Boost' },
}
