{ # 2019.12.13 can't get the cmake to work, stick with the old configure
	'repo_type' : 'git',
	'url' : 'https://github.com/libressl-portable/portable.git',
	'folder_name' : 'libressl_git',
	#--------------------
	'run_post_patch' : ( './autogen.sh ', ), # per instructions from the git website above
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static ', # 2019.12.13 remove --disable-hardening fear too much, lets see what happens
	#--------------------
	#'conf_system' : 'cmake',
	#'source_subfolder' : 'build',
	#'configure_options': '.. {cmake_prefix_options} ' 
	#	'-DLIBRESSL_SKIP_INSTALL=OFF '
	#	'-DENABLE_LIBRESSL_INSTALL=ON '
	#	'-DENABLE_ASM=ON '
	#	'-DLIBRESSL_APPS=OFF '
	#	'-DLIBRESSL_TESTS=OFF '
	##	'-DENABLE_NC=ON '
	##	'-D_POSIX_THREAD_SAFE_FUNCTIONS=ON '
	#,
	#--------------------
	'depends_on' : [ ], # 2019.12.13
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libressl' },
}
# 2019.12.13 old:
#	'libressl' : { # 2018.11.12 since git libressl is broken :( :( :( ... build per Alexpux
#		'repo_type' : 'archive',
#		'folder_name' : 'libressl_2.9.2',
#		'download_locations' : [
#			#UPDATECHECKS: https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/
#			{ "url" : "https://fossies.org/linux/misc/libressl-2.9.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4" }, ], },
#			{ "url" : "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.9.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static ', # remove --disable-hardening 2019.10.19 i fear too much, lets see what happens
#		'patches' : [
#			#( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libressl-from-Alexpux/libressl-0001-ignore-compiling-test-and-man-module.patch', '-Np1' ),
#			#( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libressl-from-Alexpux/0001-libressl_relocation-msys.patch', '-Np1' ), # ??? do msys patches apply to minw64 ???
#			#( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libressl-from-Alexpux/0002-libressl_relocation-tests.patch', '-Np1' ),
#		],
#		'run_post_patch' : (
#			'cp -fv libtls.pc.in liblibretls.pc.in', 
#			'cp -fv libcrypto.pc.in liblibrecrypto.pc.in', 
#			'cp -fv libssl.pc.in liblibressl.pc.in', 
#			'cp -fv openssl.pc.in libressl.pc.in', 
#			'cp -fv apps/openssl/openssl.c apps/openssl/libressl.c', 
#			'autoreconf -fiv',
#		),
#		'_info' : { 'version' : '2.9.2', 'fancy_name' : 'libressl' },
#	},
#
#option(ENABLE_ASM "Skip installation" ${LIBRESSL_SKIP_INSTALL})
#option(LIBRESSL_APPS "Build apps" ON)
#option(LIBRESSL_TESTS "Build tests" ON)
#option(ENABLE_ASM "Enable assembly" ON)
#option(ENABLE_EXTRATESTS "Enable extra tests that may be unreliable on some platforms" OFF)
#option(ENABLE_NC "Enable installing TLS-enabled nc(1)" OFF)
#if(NOT LIBRESSL_SKIP_INSTALL)
#	set( ENABLE_LIBRESSL_INSTALL ON )
#endif(NOT LIBRESSL_SKIP_INSTALL)
#set(BUILD_NC true)
#if(CMAKE_SYSTEM_NAME MATCHES "Linux")
#	add_definitions(-D_DEFAULT_SOURCE)
#	add_definitions(-D_BSD_SOURCE)
#	add_definitions(-D_POSIX_SOURCE)
#	add_definitions(-D_GNU_SOURCE)
#	set(PLATFORM_LIBS ${PLATFORM_LIBS} pthread)
#endif()
#if(WIN32 OR (CMAKE_SYSTEM_NAME MATCHES "MINGW"))
#	set(BUILD_NC false)
#	add_definitions(-D_GNU_SOURCE)
#	add_definitions(-D_POSIX)
#	add_definitions(-D_POSIX_SOURCE)
#	add_definitions(-D__USE_MINGW_ANSI_STDIO)
#endif()
#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2 -Wall")
#add_definitions(-DLIBRESSL_INTERNAL)
#add_definitions(-DOPENSSL_NO_HW_PADLOCK)
#add_definitions(-D__BEGIN_HIDDEN_DECLS=)
#add_definitions(-D__END_HIDDEN_DECLS=)
#set(CMAKE_POSITION_INDEPENDENT_CODE true)
#if (CMAKE_COMPILER_IS_GNUCC OR CMAKE_C_COMPILER_ID MATCHES "Clang")
#	add_definitions(-Wno-pointer-sign)
#endif()
#if(WIN32)
#	add_definitions(-Drestrict)
#	add_definitions(-D_CRT_SECURE_NO_WARNINGS)
#	add_definitions(-D_CRT_DEPRECATED_NO_WARNINGS)
#	add_definitions(-D_REENTRANT -D_POSIX_THREAD_SAFE_FUNCTIONS)
#	add_definitions(-DWIN32_LEAN_AND_MEAN -D_WIN32_WINNT=0x0600)
#	add_definitions(-DCPPFLAGS -DNO_SYSLOG -DNO_CRYPT)
#	set(PLATFORM_LIBS ${PLATFORM_LIBS} ws2_32)
#endif()
