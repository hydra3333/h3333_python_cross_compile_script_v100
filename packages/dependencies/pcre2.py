{ # 2021.12.05 https://pcre.org/ says now use https://github.com/PhilipHazel/pcre2.git
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://ftp.pcre.org/pub/pcre/pcre2-10.39.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0f03caf57f81d9ff362ac28cd389c055ec2bf0678d277349a1a4bee00ad6d440' }, ], },
	#	{ 'url' : 'https://fossies.org/linux/misc/pcre2-10.39.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0f03caf57f81d9ff362ac28cd389c055ec2bf0678d277349a1a4bee00ad6d440' }, ], },
	#],
    'repo_type' : 'git',
    'url' : 'https://github.com/PhilipHazel/pcre2.git',
    'folder_name' : 'pcre2_git',
	'recursive_git' : True,
    'branch' : 'tags/pcre2-10.39', # 2021.12.05
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
		'bzip2', 'zlib',  # # 2020.05.12 'pcre', 2019.12.13 removed 'pcre'
	],
	#'update_check' : { 'url' : 'ftp://ftp.pcre.org/pub/pcre/', 'type' : 'ftpindex', 'regex' : r'pcre2-(?P<version_num>[\d.]+)\.tar\.bz2' }, # ! TODO Fix version check
    'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : '10.39', 'fancy_name' : 'pcre2' },
}
