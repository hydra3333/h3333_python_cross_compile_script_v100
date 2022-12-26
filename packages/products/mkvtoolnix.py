{ # 2019.12.13 I could not get mkvtoolnix to build in the old scheme, let's see how deadsix27 goes now
	'repo_type' : 'git',
	'recursive_git' : True,
	'build_system' : 'rake',
	'url' : 'https://gitlab.com/mbunkus/mkvtoolnix.git',
	'branch' : 'main',  # 2020.11.05 they've changed the trunk from master to main (a US political race thing against the word, apparently)
	#'depth_git': 0,
	#'branch' : '1465b5834289d4d18bc26c425666ea02a8e2debb', # 2020.08.22 https://gitlab.com/mbunkus/mkvtoolnix/-/issues/2904
    'run_post_regexreplace' : [ # 2021.06.19
		'rm -fv ./configure',
		'./autogen.sh --build-w64 ',	
		#'autoreconf -fiv',
	],
	'configure_options':
		'--host={target_host} --prefix={output_prefix}/mkvtoolnix_git.installed --enable-static '
		'--with-boost={target_prefix} '
		'--with-boost-system=boost_system '
		'--with-boost-filesystem=boost_filesystem '
		'--enable-optimization '
		'--enable-qt '
		'--enable-static-qt '
		'--with-moc={mingw_binpath2}/moc '
		'--with-uic={mingw_binpath2}/uic '
		'--with-rcc={mingw_binpath2}/rcc '
		'--with-qmake={mingw_binpath2}/qmake ',
	'build_options': '-v',
	'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -DPCRE2_STATIC {original_cflags}',
		'CXXFLAGS' : ' -DPCRE2_STATIC {original_cflags}',
		'CPPFLAGS' : ' -DPCRE2_STATIC {original_cflags}',
		'LDFLAGS'  : ' -DPCRE2_STATIC {original_cflags}',
	},
	'custom_ldflag' : ' {original_cflags} -lpcre2-8 ',
	'depends_on' : [
		'pcre2', 'iconv', 'cmark', 'libfile', 'libflac', 'libvorbis', 'boost', 'gettext', 'zlib', 'libogg', 'libdvdread',
	],
	'packages': {
		'ubuntu' : [ 'xsltproc', 'docbook-utils', 'rake', 'docbook-xsl' ],
	},
	'run_post_install': (
		'{cross_prefix_bare}strip -v {output_prefix}/mkvtoolnix_git.installed/bin/mkvmerge.exe',
		# '{cross_prefix_bare}strip -v {product_prefix}/mkvtoolnix_git.installed/bin/mkvtoolnix-gui.exe',
		'{cross_prefix_bare}strip -v {output_prefix}/mkvtoolnix_git.installed/bin/mkvextract.exe',
		# '{cross_prefix_bare}strip -v {product_prefix}/mkvtoolnix_git.installed/bin/mkvinfo-gui.exe',
		'{cross_prefix_bare}strip -v {output_prefix}/mkvtoolnix_git.installed/bin/mkvpropedit.exe',
		'{cross_prefix_bare}strip -v {output_prefix}/mkvtoolnix_git.installed/bin/mkvinfo.exe',
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mkvtoolnix' },
}
