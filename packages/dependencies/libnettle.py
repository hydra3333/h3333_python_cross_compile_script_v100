{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.gnu.org/gnu/nettle/nettle-3.6.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'd24c0d0f2abffbc8f4f34dcf114b0f131ec3774895f3555922fe2f40f3d5e3f1' }, ], },
		#{ 'url' : 'https://fossies.org/linux/privat/nettle-3.6.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'd24c0d0f2abffbc8f4f34dcf114b0f131ec3774895f3555922fe2f40f3d5e3f1' }, ], },
		{ 'url' : 'https://ftp.gnu.org/gnu/nettle/nettle-3.7.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f001f64eb444bf13dd91bceccbc20acbc60c4311d6e2b20878452eb9a9cec75a' }, ], },
		{ 'url' : 'https://fossies.org/linux/privat/nettle-3.7.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f001f64eb444bf13dd91bceccbc20acbc60c4311d6e2b20878452eb9a9cec75a' }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-openssl --disable-mini-gmp --with-included-libtasn1', # 2019.12.13
	'depends_on' : [
		'gmp',
	],
	'update_check' : { 'url' : 'https://ftp.gnu.org/gnu/nettle/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'nettle-(?P<version_num>[\d.]+)\.tar\.gz' },
	#'_info' : { 'version' : '3.6', 'fancy_name' : 'nettle' },
	'_info' : { 'version' : '3.7', 'fancy_name' : 'nettle' },
}
