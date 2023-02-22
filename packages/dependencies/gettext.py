{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '50dbc8f39797950aa2c98e939947c527e5ac9ebd2c1b99dd7b06ba33a6767ae6' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/gettext-0.21.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '50dbc8f39797950aa2c98e939947c527e5ac9ebd2c1b99dd7b06ba33a6767ae6' }, ], },
		{ 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '50dbc8f39797950aa2c98e939947c527e5ac9ebd2c1b99dd7b06ba33a6767ae6' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/gettext-0.21.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '50dbc8f39797950aa2c98e939947c527e5ac9ebd2c1b99dd7b06ba33a6767ae6' }, ], },
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-threads=posix --without-libexpat-prefix --without-libxml2-prefix CPPFLAGS=-DLIBXML_STATIC --disable-rpath --enable-relocatable ', # 2020.03.19 removed --enable-nls 
	#'configure_options' : '{autoconf_prefix_options} CPPFLAGS=-DLIBXML_STATIC', # 2022.12.18 per DEADSIX27 uses only this
	'regex_replace': { # 2022.12.18 per DEADSIX27
		'post_patch': [ # 2022.12.18 per DEADSIX27
			{ # 2022.12.18 per DEADSIX27
				0: r'SUBDIRS = gnulib-local gettext-runtime libtextstyle gettext-tools', # 2022.12.18 per DEADSIX27
				1: r'SUBDIRS = gnulib-local gettext-runtime libtextstyle', # 2022.12.18 per DEADSIX27
				'in_file': 'Makefile.am'
			}, # 2022.12.18 per DEADSIX27
			{ # 2022.12.18 per DEADSIX27
				0: r'gettext-runtime libtextstyle gettext-tools', # 2022.12.18 per DEADSIX27
				1: r'gettext-runtime libtextstyle', # 2022.12.18 per DEADSIX27
				'in_file': 'configure.ac' # 2022.12.18 per DEADSIX27
			}, # 2022.12.18 per DEADSIX27
		], # 2022.12.18 per DEADSIX27
	}, # 2022.12.18 per DEADSIX27
	#'run_post_regexreplace' : [
	#	'autoreconf -fiv', # 2022.12.19
	#	'./autogen.sh ', # 2022.12.19
	#],	
	'depends_on' : [ 'iconv' ],
	'update_check' : { 'url' : 'https://ftp.gnu.org/pub/gnu/gettext/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'gettext-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '0.21.1', 'fancy_name' : 'gettext' },
}
