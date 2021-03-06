{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.pcre.org/pub/pcre/pcre2-10.35.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9ccba8e02b0ce78046cdfb52e5c177f0f445e421059e43becca4359c669d4613' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/pcre2-10.35.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9ccba8e02b0ce78046cdfb52e5c177f0f445e421059e43becca4359c669d4613' }, ], },
		{ 'url' : 'https://ftp.pcre.org/pub/pcre/pcre2-10.36.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'a9ef39278113542968c7c73a31cfcb81aca1faa64690f400b907e8ab6b4a665c' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/pcre2-10.36.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'a9ef39278113542968c7c73a31cfcb81aca1faa64690f400b907e8ab6b4a665c' }, ], },
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
		'bzip2', 'zlib',  # # 2020.05.12 'pcre', 2019.12.13 removed 'pcre'
	],
	'update_check' : { 'url' : 'ftp://ftp.pcre.org/pub/pcre/', 'type' : 'ftpindex', 'regex' : r'pcre2-(?P<version_num>[\d.]+)\.tar\.bz2' }, # ! TODO Fix version check
	#'_info' : { 'version' : '10.35', 'fancy_name' : 'pcre2' },
	'_info' : { 'version' : '10.36', 'fancy_name' : 'pcre2' },
}
