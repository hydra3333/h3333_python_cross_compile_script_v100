{ # mine is 2.9.2 and this one is from git
	#'download_locations' : [
	#	#UPDATECHECKS: https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/
	#	{ "url" : "https://fossies.org/linux/misc/libressl-2.9.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4" }, ], },
	#	{ "url" : "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.9.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4" }, ], },
	#],
	'repo_type' : 'git',
	'url' : 'https://github.com/libressl-portable/portable.git',
	'folder_name' : 'libressl_git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static ', # 2019.12.13 remove --disable-hardening fear too much, lets see what happens
	'run_post_patch' : ( # 2019.12.13
		'cp -fv libtls.pc.in libretls.pc.in', 
		'cp -fv libcrypto.pc.in librecrypto.pc.in', 
		'cp -fv libssl.pc.in libressl.pc.in', 
		'cp -fv openssl.pc.in libressl.pc.in', 
		#'cp -fv apps/openssl/openssl.c apps/openssl/libressl.c', # no longer exists 2019.12.13
		'autoreconf -fiv',
		),
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libressl' },
}
# 2019.12.13 old:
#	'libressl' : { # 2018.11.12 since git libressl is broken :( :( :( ... build per Alexpux
#		'repo_type' : 'archive',
#		'folder_name' : 'libressl_2.9.2',
#		'download_locations' : [
#			#UPDATECHECKS: https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/
#			#{ "url" : "https://fossies.org/linux/misc/libressl-2.8.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "b8cb31e59f1294557bfc80f2a662969bc064e83006ceef0574e2553a1c254fd5" }, ], },
#			#{ "url" : "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.8.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "b8cb31e59f1294557bfc80f2a662969bc064e83006ceef0574e2553a1c254fd5" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/libressl-2.9.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4" }, ], },
#			{ "url" : "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.9.2.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "c4c78167fae325b47aebd8beb54b6041d6f6a56b3743f4bd5d79b15642f9d5d4" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static ', # remove --disable-hardening 2019.10.19 i fear too much, lets see what happens
#		'run_post_patch' : (
#			'cp -fv libtls.pc.in libretls.pc.in', 
#			'cp -fv libcrypto.pc.in librecrypto.pc.in', 
#			'cp -fv libssl.pc.in libressl.pc.in', 
#			'cp -fv openssl.pc.in libressl.pc.in', 
#			'cp -fv apps/openssl/openssl.c apps/openssl/libressl.c', 
#			'autoreconf -fiv',
#		),
#		'_info' : { 'version' : '2.9.2', 'fancy_name' : 'libressl' },
#	},