{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/libiconv-1.16.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04' }, ], },
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-nls --enable-extra-encodings', # 2019.12.13
	#'depends_on' : [ 'gettext', ], # no, gettext depends on iconv
	'update_check' : { 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'libiconv-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.16', 'fancy_name' : 'libiconv' },
}
# 2019.12.13 old:
#	'iconv' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://ftp.gnu.org/pub/gnu/libiconv/?C=M;O=D
#			{ "url" : "https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/libiconv-1.16.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-nls --enable-extra-encodings', # 2018.11.23 --enable-nls
#		'_info' : { 'version' : '1.16', 'fancy_name' : 'libiconv' },
#	},