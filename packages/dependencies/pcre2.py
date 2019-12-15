{ # 2019.12.13 10.24 is later than my 10.33
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://ftp.pcre.org/pub/pcre/pcre2-10.34.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '74c473ffaba9e13db6951fd146e0143fe9887852ce73406a03277af1d9b798ca' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/pcre2-10.34.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '74c473ffaba9e13db6951fd146e0143fe9887852ce73406a03277af1d9b798ca' }, ], },
	],
	'conf_system' : 'cmake',
	'patches' : [
		('pcre2/0001-pcre2-iswild.patch', '-p1'),
	],
	'configure_options' : '. {cmake_prefix_options} '
        '-DBUILD_BINARY=OFF -DPCRE2_SUPPORT_LIBEDIT=OFF -DPCRE2_SUPPORT_LIBREADLINE=OFF -D_FILE_OFFSET_BITS=64 ' # 2019.12.13
		'-DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DPCRE2_BUILD_TESTS=OFF '
		'-DPCRE2_BUILD_PCRE2_8=ON -DPCRE2_BUILD_PCRE2_16=ON -DPCRE2_BUILD_PCRE2_32=ON -DPCRE2_NEWLINE=ANYCRLF '
		'-DPCRE2_SUPPORT_UNICODE=ON -DPCRE2_SUPPORT_JIT=ON'
	,
	'depends_on' : [
		'bzip2', 'zlib',  # 2019.12.13 removed 'pcre'
	],
	'update_check' : { 'url' : 'ftp://ftp.pcre.org/pub/pcre/', 'type' : 'ftpindex', 'regex' : r'pcre2-(?P<version_num>[\d.]+)\.tar\.bz2' }, # ! TODO Fix version check
	'_info' : { 'version' : '10.34', 'fancy_name' : 'pcre2' },
}
# 2019.12.13 old:
#	},
#	'pcre2' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://ftp.pcre.org/pub/pcre/
#			{ "url" : "https://ftp.pcre.org/pub/pcre/pcre2-10.33.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "35514dff0ccdf02b55bd2e9fa586a1b9d01f62332c3356e379eabb75f789d8aa" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/pcre2-10.33.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "35514dff0ccdf02b55bd2e9fa586a1b9d01f62332c3356e379eabb75f789d8aa" }, ], },
#		],
#		'conf_system' : 'cmake',
#		'patches' : [
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/pcre2/0001-pcre2-iswild.patch', '-p1'],
#		],
#		'configure_options': '. {cmake_prefix_options} '
#			'-DBUILD_BINARY=OFF -DPCRE2_SUPPORT_LIBEDIT=OFF -DPCRE2_SUPPORT_LIBREADLINE=OFF -D_FILE_OFFSET_BITS=64 ' # 2018.11.25
#			'-DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DPCRE2_BUILD_TESTS=OFF '
#			'-DPCRE2_BUILD_PCRE2_8=ON -DPCRE2_BUILD_PCRE2_16=ON -DPCRE2_BUILD_PCRE2_32=ON -DPCRE2_NEWLINE=ANYCRLF '
#			'-DPCRE2_SUPPORT_UNICODE=ON -DPCRE2_SUPPORT_JIT=ON',
#		'depends_on' : [
#			'bzip2', 'zlib', 'pcre', # 2018.11.23 added  'zlib', 'pcre'
#		],
#		'_info' : { 'version' : '10.33', 'fancy_name' : 'pcre2' },
#	},