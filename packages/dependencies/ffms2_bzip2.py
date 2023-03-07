{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/bzip2-1.0.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269' }, ], },
	],
	'folder_name' : 'ffms2_bzip2',
	'patches' : [
		('bzip2/bzip2-1.0.6-gcc8.patch', '-p0'),
	],
	'env_exports' : {
		'CXXFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CPPFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CFLAGS'   :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'LDFLAGS'  :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lintl -liconv -lssp ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	#'custom_cflag' : '{original_cflags}',
	'needs_configure' : False,
	'needs_make' : True,
	'needs_make_install' : False,
	#'build_options' : '{make_prefix_options} libbz2.a bzip2 bzip2recover install ', # PREFIX={output_prefix}/ffms2_dll.installed
	'build_options' : '{make_prefix_options} -f Makefile-libbz2_so ', # PREFIX={output_prefix}/ffms2_dll.installed
	'run_post_build' : [
		'make {make_prefix_options} install PREFIX={output_prefix}/ffms2_dll.installed', #  PREFIX={output_prefix}/ffms2_dll.installed
		'cp -fv libbz2.def {output_prefix}/ffms2_dll.installed/lib',
		'cp -Lfv libbz2.so.1.0 {output_prefix}/ffms2_dll.installed/lib/libbz2.so',
		'ls -al {output_prefix}/ffms2_dll.installed/lib/libbz2.so',
		'mkdir -p "{output_prefix}/ffms2_dll.installed/lib/pkgconfig"',
		"echo 'prefix={output_prefix}/ffms2_dll.installed\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include\nName: bzip2\nDescription: bzip2\nVersion:\nLibs: -L${{libdir}} -lbz2\nCflags: -I${{includedir}}' > {output_prefix}/ffms2_dll.installed/lib/pkgconfig/bzip2.pc",
	],
	'update_check' : { 'url' : 'ftp://sourceware.org/pub/bzip2/', 'type' : 'ftpindex', 'regex' : r'bzip2-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.0.8', 'fancy_name' : 'ffms_BZip2 (library)' },
}
