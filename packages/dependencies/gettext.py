{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.20.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gettext-0.20.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800' }, ], },
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-threads=posix --without-libexpat-prefix --without-libxml2-prefix CPPFLAGS=-DLIBXML_STATIC --disable-rpath --enable-relocatable ', # 2020.03.19 removed --enable-nls 
	'depends_on' : [ 'iconv' ],
	'update_check' : { 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'gettext-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '0.20.1', 'fancy_name' : 'gettext' },
}
# 2019.12.13 old:
#	'gettext' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://ftp.gnu.org/pub/gnu/gettext/?C=M;O=D
#			{ "url" : "https://ftp.gnu.org/pub/gnu/gettext/gettext-0.20.1.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/gettext-0.20.1.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "53f02fbbec9e798b0faaf7c73272f83608e835c6288dd58be6c9bb54624a3800" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-threads=posix --without-libexpat-prefix --without-libxml2-prefix CPPFLAGS=-DLIBXML_STATIC --disable-rpath --enable-nls --enable-relocatable ', # 2018.11.23 --enable-threads=posix (not win32) --disable-rpath --enable-nls --enable-relocatable 
#		'run_post_patch' :  (
#			#'libtoolize --automake --copy --force', # 2018.08.18
#			#'./autogen.sh --skip-gnulib', # 2018.08.18
#			'autoreconf -fiv',
#		),
#		'version' : '0.20.1',
#		'_info' : { 'version' : '0.20.1', 'fancy_name' : 'gettext' },
#		'depends_on' : [ 'iconv' ],
#	},