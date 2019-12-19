{
	'repo_type' : 'archive',
	'download_locations' : [ # 2019.12.13 1.7.0 is newer than mine at 1.6.1
		{ 'url' : 'https://files.dyne.org/frei0r/frei0r-plugins-1.7.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1b1ff8f0f9bc23eed724e94e9a7c1d8f0244bfe33424bb4fe68e6460c088523a' }, ], },
		{ 'url' : 'https://cdn.netbsd.org/pub/pkgsrc/distfiles/frei0r-plugins-1.7.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1b1ff8f0f9bc23eed724e94e9a7c1d8f0244bfe33424bb4fe68e6460c088523a' }, ], },
	],
	'depends_on' : [ 'dlfcn-win32', ],
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DWITHOUT_OPENCV=YES',
	'run_post_patch' : [
	# 	'sed -i.bak "s/find_package (Cairo)//g" CMakeLists.txt',
    #   'sed -i.bak "s/-arch i386//" CMakeLists.txt', # 2019.12.13 this sed not needed either
        'sed -i.bak "s/VERSION 1.6.1/VERSION 1.7.0/" CMakeLists.txt', # 2013.12.13 why didna they bump it ?
	],
	'update_check' : { 'url' : 'https://files.dyne.org/frei0r/releases/', 'type' : 'httpindex', 'regex' : r'frei0r-plugins-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.7.0', 'fancy_name' : 'frei0r-plugins' },
}
# 2019.12.13 old:
#	'frei0r' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://files.dyne.org/frei0r/
#			{ "url" : "https://files.dyne.org/frei0r/frei0r-plugins-1.6.1.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "e0c24630961195d9bd65aa8d43732469e8248e8918faa942cfb881769d11515e" }, ], },
#			{ "url" : "https://ftp.osuosl.org/pub/blfs/conglomeration/frei0r/frei0r-plugins-1.6.1.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "e0c24630961195d9bd65aa8d43732469e8248e8918faa942cfb881769d11515e" }, ], },
#		],
#		'conf_system' : 'cmake',
#		'run_post_patch': ( # runs commands post the patch process
#			'sed -i.bak "s/find_package (Cairo)//g" CMakeLists.txt', #idk
#			'sed -i.bak "s/-arch i386//" CMakeLists.txt',
#		),
#		'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DWITHOUT_OPENCV=YES',
#		'depends_on' : [ 'dlfcn-win32', ],
#		'_info' : { 'version' : '1.6.1', 'fancy_name' : 'frei0r-plugins' },
#	},