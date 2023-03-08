{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'http://xmlsoft.org/sources/libxml2-2.10.3.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5d2cc3d78bec3dbe212a9d7fa629ada25a7da928af432c93060ff5c17ee28a9c' }, ], },
		#{ 'url' : 'https://fossies.org/linux/www/libxml2-2.10.3.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5d2cc3d78bec3dbe212a9d7fa629ada25a7da928af432c93060ff5c17ee28a9c' }, ], },
		{ 'url' : 'http://xmlsoft.org/sources/libxml2-2.9.12.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c8d6681e38c56f172892c85ddc0852e1fd4b53b4209e7f4ebf17f7e2eae71d92' }, ], },
		{ 'url' : 'https://fossies.org/linux/www/libxml2-2.9.12.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c8d6681e38c56f172892c85ddc0852e1fd4b53b4209e7f4ebf17f7e2eae71d92' }, ], },
	],
	'folder_name' : 'ffms2_libxml2-2.10.3',
	'env_exports' : {
		'CXXFLAGS' :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'CPPFLAGS' :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'CFLAGS'   :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'LDFLAGS'  :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	## {autoconf_prefix_options} = --with-sysroot="{target_sub_prefix}" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static
	'run_post_patch' : [
		'sh ./autogen.sh '
						'--with-sysroot="{target_sub_prefix}" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static --disable-tests --disable-programs '
						'--disable-silent-rules --enable-dependency-tracking '
						'--disable-rebuild-docs --disable-ipv6 --with-pic '
						'--with-c14n --with-catalog --without-debug --with-docbook --with-ftp --without-history '
						'--with-html --with-http --without-iconv --without-icu --with-iso8859x --with-legacy --without-mem-debug '
						'--without-minimum --with-output --with-pattern --with-push --without-python  --with-reader  --with-regexps '
						'--without-run-debug --with-sax1 --with-schemas --with-schematron --with-threads --without-thread-alloc '
						'--with-tree --with-valid --with-writer --with-xinclude --with-xpath --with-xptr --with-modules '
						'--with-zlib --with-lzma --without-coverage ',
		'./configure --help',
	],	
	'configure_options' : 
						'--with-sysroot="{target_sub_prefix}" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static --disable-tests --disable-programs '
						'--disable-silent-rules --enable-dependency-tracking '
						'--disable-rebuild-docs --disable-ipv6 --with-pic '
						'--with-c14n --with-catalog --without-debug --with-docbook --with-ftp --without-history '
						'--with-html --with-http --without-iconv --without-icu --with-iso8859x --with-legacy --without-mem-debug '
						'--without-minimum --with-output --with-pattern --with-push --without-python  --with-reader  --with-regexps '
						'--without-run-debug --with-sax1 --with-schemas --with-schematron --with-threads --without-thread-alloc '
						'--with-tree --with-valid --with-writer --with-xinclude --with-xpath --with-xptr --with-modules '
						'--with-zlib --with-lzma --without-coverage ',
	'run_post_install' : [
		'sed -i.bak \'s/Libs: -L${{libdir}} -lxml2/Libs: -L${{libdir}} -lxml2 -lz -llzma -liconv -lws2_32/\' "{pkg_config_path}/libxml-2.0.pc"', # libarchive complaints without this.
	],
	'depends_on' : [
		'xz', 'zlib',
	],
	'update_check' : { 'url' : 'http://xmlsoft.org/sources/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'libxml2-(?P<version_num>[\d.]+)-rc(?P<rc_num>[0-9]).tar.gz' },
	'_info' : { 'version' : '2.10.3', 'fancy_name' : 'ffms2_libxml2' },
}

