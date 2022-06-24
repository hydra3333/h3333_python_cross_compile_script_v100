{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.gnu.org/gnu/nettle/nettle-3.7.3.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '661f5eb03f048a3b924c3a8ad2515d4068e40f67e774e8a26827658007e3bcf0' }, ], },
		#{ 'url' : 'https://fossies.org/linux/privat/nettle-3.7.3.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '661f5eb03f048a3b924c3a8ad2515d4068e40f67e774e8a26827658007e3bcf0' }, ], },
		{ 'url' : 'https://ftp.gnu.org/gnu/nettle/nettle-3.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '7576c68481c198f644b08c160d1a4850ba9449e308069455b5213319f234e8e6' }, ], },
		{ 'url' : 'https://fossies.org/linux/privat/nettle-3.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '7576c68481c198f644b08c160d1a4850ba9449e308069455b5213319f234e8e6' }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-openssl --disable-mini-gmp --with-included-libtasn1', # 2019.12.13
	'depends_on' : [
		'gmp',
	],
	'update_check' : { 'url' : 'https://ftp.gnu.org/gnu/nettle/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'nettle-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '3.8', 'fancy_name' : 'nettle' },
}