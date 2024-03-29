{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/
		#{ 'url' : 'https://fossies.org/linux/misc/boost_1_80_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1e19565d82e43bc59209a168f5ac899d3ba471d55c7610c677d4ccf2c9c500c0' }, ], },
		#{ 'url' : 'https://dl.bintray.com/boostorg/release/1.80.0/source/boost_1_80_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1e19565d82e43bc59209a168f5ac899d3ba471d55c7610c677d4ccf2c9c500c0' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/boost_1_81_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '71feeed900fbccca04a3b4f2f84a7c217186f28a940ed8b7ed4725986baf99fa' }, ], },
		{ 'url' : 'https://dl.bintray.com/boostorg/release/1.81.0/source/boost_1_81_0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '71feeed900fbccca04a3b4f2f84a7c217186f28a940ed8b7ed4725986baf99fa' }, ], },
		# in WIn10 use powershell to find the sha256 of a file https://www.youtube.com/watch?v=YM2CE6zKvoo&t=57
		# in linux: sha256sum filename
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
	'_info' : { 'version' : '1.81.0', 'fancy_name' : 'Boost' },
}
