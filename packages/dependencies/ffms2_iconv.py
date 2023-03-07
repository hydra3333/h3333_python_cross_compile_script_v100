{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.16.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/libiconv-1.16.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04' }, ], },
		{ 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.17.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f74213b56238c85a50a5329f77e06198771e70dd9a739779f4c02f65d971313' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/libiconv-1.17.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f74213b56238c85a50a5329f77e06198771e70dd9a739779f4c02f65d971313' }, ], },
	],
	'env_exports' : {
		'CXXFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CPPFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CFLAGS'   :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'LDFLAGS'  :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
	},
	'run_post_patch' : [
		'./configure --help',
	],
	## {autoconf_prefix_options} = --with-sysroot="{target_sub_prefix}" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static
	'configure_options' : '--with-sysroot="{output_prefix}/ffms2_dll.installed" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static --disable-nls --enable-extra-encodings',
	'update_check' : { 'url' : 'https://ftp.gnu.org/pub/gnu/libiconv/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'libiconv-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.17', 'fancy_name' : 'ffms2_libiconv' },
}
