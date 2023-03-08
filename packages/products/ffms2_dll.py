{
	'repo_type' : 'git',
	'url' : 'https://github.com/FFMS/ffms2', 
	'depth_git' : 0,
	#'recursive_git' : True,
	'rename_folder' : 'ffms2_dll',
	'env_exports' : {
		'CXXFLAGS' :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp -lpthread ',
		'CPPFLAGS' :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp -lpthread ',
		'CFLAGS'   :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp -lpthread ',
		'LDFLAGS'  :  ' -fstack-protector -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp -lpthread ', # to mitigate lock per https://github.com/ffms/ffms2/issues/90
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	'patches' : [
		( 'ffms2/0001-ffmsindex-fix-linking-issues.patch', '-Np1' ),# from MABS
	],
	'run_post_patch' : [ 
		# diff for the patch
		'diff -U 10 "Makefile.am.orig" "Makefile.am"  && echo "NO difference" || echo "YES differences!"',
		'diff -U 10 "configure.ac.orig" "configure.ac"  && echo "NO difference" || echo "YES differences!"',
		# diff for the sed
		'cp -fv "ffms2.pc.in" "ffms2.pc.in.orig"',
		#'sed -i "s/Libs.private.*/& -lstdc++/;s/Cflags.*/& -DFFMS_STATIC/" "ffms2.pc.in"',
		'diff -U 10 "ffms2.pc.in.orig" "ffms2.pc.in"  && echo "NO difference" || echo "YES differences!"',
		#
		'if [ -f "./configure" ] ; then rm -fv ./configure ; fi',
		'if [ ! -d "src/config" ] ; then mkdir -p "src/config" ; fi',
		'autoreconf -fiv',
		'./configure --help=recursive',
	],
	#'configure_options': '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --enable-static -disable-shared --with-pic --with-zlib={target_prefix}/lib ', # --with-pic per https://github.com/ffms/ffms2/issues/90
	'configure_options': '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --disable-static -enable-shared --with-pic --with-zlib={output_prefix}/ffms2_dll.installed/lib ', # --with-pic per https://github.com/ffms/ffms2/issues/90
	'run_pre_patch' : [
		'cp -fv "Makefile.am" "Makefile.am.orig"',
		'cp -fv "configure.ac" "configure.ac.orig"',
	],
	'depends_on': [
		'ffms2_libffmpeg',		# has its own dependencies
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'ffms2_dll' },
}


