{
	'repo_type' : 'git',
	'url' : 'https://github.com/Haivision/srt.git',
	'depth_git' : 0,
	#'branch' : '10ed37b6d4b49a3042213b029f0de6bca4bcfe83', # 2020.06.27 the commit after this builds but breaks ffmpeg libsrt building
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
	'custom_cflag' : '',
	'configure_options' : 	'.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
							'-DCMAKE_BUILD_TYPE=Release '
							#'-D_WIN32_WINNT=0xA00 '
							'-DENABLE_SHARED=off -DENABLE_STATIC=on '
							'-DENABLE_ENCRYPTION=on '
							'-DENABLE_CXX11=on '
							'-DENABLE_CXX_DEPS=on '
							'-DUSE_STATIC_LIBSTDCXX=on '
							'-DENABLE_INET_PTON=off '
							#'-DUSE_GNUTLS=on ' # USE_GNUTLS is deprecated. Use -DUSE_ENCLIB=gnutls instead
							'-DUSE_ENCLIB=gnutls '
							'-DHAICRYPT_USE_OPENSSL_EVP=off '
							'-DHAICRYPT_USE_OPENSSL_AES=off '
							'-DENABLE_SUFLIP=off '
							'-DENABLE_EXAMPLES=off -DENABLE_APPS=off ' # 2019.12.13 # 
							'-DUSE_STATIC_LIBSTDCXX=ON ' # 2021.08.27 per MABS
							'-DENABLE_UNITTESTS=off ' # 2019.12.13 # 
							,
	'depends_on' : [ 'gnutls_3333' ], # 20921.02.03 'gettext',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'srt_3333' }, # it is actually srt 
}
#
#option(CYGWIN_USE_POSIX "Should the POSIX API be used for cygwin. Ignored if the system isn't cygwin." OFF)
#option(ENABLE_CXX11 "Should the c++11 parts (srt-live-transmit) be enabled" ON)
#option(ENABLE_APPS "Should the Support Applications be Built?" ON)
#option(ENABLE_PROFILE "Should instrument the code for profiling. Ignored for non-GNU compiler." $ENV{HAI_BUILD_PROFILE})
#option(ENABLE_LOGGING "Should logging be enabled" ON)
#option(ENABLE_HEAVY_LOGGING "Should heavy debug logging be enabled" ${ENABLE_HEAVY_LOGGING_DEFAULT})
#option(ENABLE_HAICRYPT_LOGGING "Should logging in haicrypt be enabled" 0)
#option(ENABLE_SHARED "Should libsrt be built as a shared library" ON)
#option(ENABLE_STATIC "Should libsrt be built as a static library" ON)
#option(ENABLE_RELATIVE_LIBPATH "Should application contain relative library paths, like ../lib" OFF)
#option(ENABLE_SUFLIP "Should suflip tool be built" OFF)
#option(ENABLE_GETNAMEINFO "In-logs sockaddr-to-string should do rev-dns" OFF)
#option(ENABLE_UNITTESTS "Enable unit tests" OFF)
#option(ENABLE_ENCRYPTION "Enable encryption in SRT" ON)
#option(ENABLE_CXX_DEPS "Extra library dependencies in srt.pc for the CXX libraries useful with C language" ON)
#option(USE_STATIC_LIBSTDCXX "Should use static rather than shared libstdc++" OFF)
#option(ENABLE_INET_PTON "Set to OFF to prevent usage of inet_pton when building against modern SDKs while still requiring compatibility with older Windows versions, such as Windows XP, Windows Server 2003 etc." ON)
#option(ENABLE_CODE_COVERAGE "Enable code coverage reporting" OFF)
#option(ENABLE_MONOTONIC_CLOCK "Enforced clock_gettime with monotonic clock on GC CV /temporary fix for #729/" OFF)
#option(USE_OPENSSL_PC "Use pkg-config to find OpenSSL libraries" ON)
#option(USE_BUSY_WAITING "Enable more accurate sending times at a cost of potentially higher CPU load" OFF)
#option(USE_GNUSTL "Get c++ library/headers from the gnustl.pc" OFF)