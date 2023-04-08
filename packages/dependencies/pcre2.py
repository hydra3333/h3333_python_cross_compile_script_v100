{ # 2021.12.05 https://pcre.org/ says now use https://github.com/PhilipHazel/pcre2.git
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/PhilipHazel/pcre2/releases/download/pcre2-10.40/pcre2-10.40.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '14e4b83c4783933dc17e964318e6324f7cae1bc75d8f3c79bc6969f00c159d68' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/pcre2-10.40.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '14e4b83c4783933dc17e964318e6324f7cae1bc75d8f3c79bc6969f00c159d68' }, ], },
		{ 'url' : 'https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.42/pcre2-10.42.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8d36cd8cb6ea2a4c2bb358ff6411b0c788633a2a45dabbf1aeb4b701d1b5e840' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/pcre2-10.42.tar.bz2 ', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8d36cd8cb6ea2a4c2bb358ff6411b0c788633a2a45dabbf1aeb4b701d1b5e840' }, ], },
	],
    #
	#'repo_type' : 'git',
	#'url' : 'https://github.com/PhilipHazel/pcre2.git',
	#'folder_name' : 'pcre2_git',
	#'recursive_git' : True,
	#'branch' : 'tags/pcre2-10.39', # 2021.12.05
	#'branch' : '35fee4193b852cb504892352bd0155de10809889', # 35fee4193b852cb504892352bd0155de10809889 is 'tags/pcre2-10.39', # 2021.12.05
	#
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
		'bzip2', 'zlib',  # 2020.05.12 'pcre', 2019.12.13 removed 'pcre'
	],
	#'update_check' : { 'type' : 'git', },
   	'update_check' : { 'url' : 'https://github.com/PCRE2Project/pcre2/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	'_info' : { 'version' : '10.42', 'fancy_name' : 'pcre2' },
}
