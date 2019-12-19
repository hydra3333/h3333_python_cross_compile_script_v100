{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://ftp.gnu.org/gnu/nettle/nettle-3.5.1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '75cca1998761b02e16f2db56da52992aef622bf55a3b45ec538bc2eedadc9419' }, ], },
		{ 'url' : 'https://fossies.org/linux/privat/nettle-3.5.1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '75cca1998761b02e16f2db56da52992aef622bf55a3b45ec538bc2eedadc9419' }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-openssl --disable-mini-gmp --with-included-libtasn1', # 2019.12.13
	'depends_on' : [
		'gmp',
	],
	'update_check' : { 'url' : 'https://ftp.gnu.org/gnu/nettle/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'nettle-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '3.5.1', 'fancy_name' : 'nettle' },
}
# 2019.12.13 old:
#	'libnettle' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://ftp.gnu.org/gnu/nettle/?C=M;O=D
#			# 2018.12.05 libnettle 3.4.1 required for gnutls 3.6.5
#			{ "url" : "https://ftp.gnu.org/gnu/nettle/nettle-3.5.1.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "75cca1998761b02e16f2db56da52992aef622bf55a3b45ec538bc2eedadc9419" }, ], },
#			{ "url" : "https://fossies.org/linux/privat/nettle-3.5.1.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "75cca1998761b02e16f2db56da52992aef622bf55a3b45ec538bc2eedadc9419" }, ], },
#		],
#		'folder_name' : 'libnettle',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-openssl --with-included-libtasn1',
#		'depends_on' : [
#			'gmp',
#		],
#		'_info' : { 'version' : '3.5.1', 'fancy_name' : 'libnettle' },
#	},