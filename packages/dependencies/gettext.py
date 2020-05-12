{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.20.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/gettext-0.20.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800' }, ], },
		{ 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.20.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b22b818e644c37f6e3d1643a1943c32c3a9bff726d601e53047d2682019ceaba' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gettext-0.20.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b22b818e644c37f6e3d1643a1943c32c3a9bff726d601e53047d2682019ceaba' }, ], },
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-threads=posix --without-libexpat-prefix --without-libxml2-prefix CPPFLAGS=-DLIBXML_STATIC --disable-rpath --enable-relocatable ', # 2020.03.19 removed --enable-nls 
	#'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-threads=posix --without-libexpat-prefix --without-libxml2-prefix CPPFLAGS=-DLIBXML_STATIC ', # 2020.05.12 make more like deadsix27 --disable-rpath --enable-relocatable
	'depends_on' : [ 'iconv' ],
	'update_check' : { 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'gettext-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '0.20.2', 'fancy_name' : 'gettext' },
}
