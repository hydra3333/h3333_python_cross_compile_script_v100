{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/libiconv-1.16.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04' }, ], },
		{ 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.17.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f74213b56238c85a50a5329f77e06198771e70dd9a739779f4c02f65d971313' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/libiconv-1.17.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f74213b56238c85a50a5329f77e06198771e70dd9a739779f4c02f65d971313' }, ], },
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --disable-nls --enable-extra-encodings', # 2020.03.19 --enable-nls
	#'depends_on' : [ 'gettext', ], # no, instead, gettext depends on iconv
	'update_check' : { 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'libiconv-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.17', 'fancy_name' : 'libiconv' },
}
