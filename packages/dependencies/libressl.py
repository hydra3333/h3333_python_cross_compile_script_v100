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
		'cp -fv libtls.pc.in liblibretls.pc.in', 
		'cp -fv libcrypto.pc.in liblibrecrypto.pc.in', 
		'cp -fv libssl.pc.in liblibressl.pc.in', 
		'cp -fv openssl.pc.in libressl.pc.in', 
		'cp -fv apps/openssl/openssl.c apps/openssl/libressl.c', 
		'autoreconf -fiv',
		),
	'_info' : { 'version' : None, 'fancy_name' : 'libressl' },
}
