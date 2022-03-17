{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'http://xmlsoft.org/sources/libxml2-2.9.10-rc1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '913d85bf02ab22f07c76805522e013b7dfda7585dfe5addc465440880ef8cae5' }, ], },
		#{ 'url' : 'https://fossies.org/linux/www/libxml2-2.9.10-rc1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '913d85bf02ab22f07c76805522e013b7dfda7585dfe5addc465440880ef8cae5' }, ], },
		{ 'url' : 'http://xmlsoft.org/sources/libxml2-2.9.12.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c8d6681e38c56f172892c85ddc0852e1fd4b53b4209e7f4ebf17f7e2eae71d92' }, ], },
		{ 'url' : 'https://fossies.org/linux/www/libxml2-2.9.12.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c8d6681e38c56f172892c85ddc0852e1fd4b53b4209e7f4ebf17f7e2eae71d92' }, ], },
	],
	'folder_name' : 'libxml2-2.9.12',
	#'rename_folder' : 'libxml2-2.9.12',
	'run_post_patch' : [
		'sh ./autogen.sh '
						'{autoconf_prefix_options} --disable-shared --enable-static --disable-tests --disable-programs '
						'--disable-silent-rules --enable-dependency-tracking '
						'--disable-rebuild-docs --disable-ipv6 --with-pic '
						'--with-c14n --with-catalog --without-debug --with-docbook --with-ftp --without-history '
						'--with-html --with-http --with-iconv --without-icu --with-iso8859x --with-legacy --without-mem-debug '
						'--without-minimum --with-output --with-pattern --with-push --without-python  --with-reader  --with-regexps '
						'--without-run-debug --with-sax1 --with-schemas --with-schematron --with-threads --without-thread-alloc '
						'--with-tree --with-valid --with-writer --with-xinclude --with-xpath --with-xptr --with-modules '
						'--with-zlib --with-lzma --without-coverage ',
	],	
	'configure_options' : 
						'{autoconf_prefix_options} --disable-shared --enable-static --disable-tests --disable-programs '
						'--disable-silent-rules --enable-dependency-tracking '
						'--disable-rebuild-docs --disable-ipv6 --with-pic '
						'--with-c14n --with-catalog --without-debug --with-docbook --with-ftp --without-history '
						'--with-html --with-http --with-iconv --without-icu --with-iso8859x --with-legacy --without-mem-debug '
						'--without-minimum --with-output --with-pattern --with-push --without-python  --with-reader  --with-regexps '
						'--without-run-debug --with-sax1 --with-schemas --with-schematron --with-threads --without-thread-alloc '
						'--with-tree --with-valid --with-writer --with-xinclude --with-xpath --with-xptr --with-modules '
						'--with-zlib --with-lzma --without-coverage ',
	'run_post_install' : [
		'sed -i.bak \'s/Libs: -L${{libdir}} -lxml2/Libs: -L${{libdir}} -lxml2 -lz -llzma -liconv -lws2_32/\' "{pkg_config_path}/libxml-2.0.pc"', # libarchive complaints without this.
	],
	'depends_on' : [
		'xz', 'iconv', 'zlib',
	],
	'update_check' : { 'url' : 'http://xmlsoft.org/sources/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'libxml2-(?P<version_num>[\d.]+)-rc(?P<rc_num>[0-9]).tar.gz' },
	'_info' : { 'version' : '2.9.10.1', 'fancy_name' : 'libxml2' },
}
# OLD:
#	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --without-python --enable-tests=no --enable-programs=no',
#	'run_post_regexreplace' : [
#		#'autoreconf -fiv',
#		'./autogen.sh',
