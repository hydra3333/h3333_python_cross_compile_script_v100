{
	'repo_type' : 'git',
	'url' : 'https://github.com/FFMS/ffms2', 
	'depth_git' : 0,
	'rename_folder' : 'ffms2_dll',
	'env_exports' : {
		#'CXXFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
		#'CPPFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
		#'CFLAGS'   :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
		#'LDFLAGS'  :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp -Wl,-Bsymbolic ', # to mitigate lock per https://github.com/ffms/ffms2/issues/90
		'CXXFLAGS' :  ' {original_stack_protector_trim} -I{output_prefix}/include -L{output_prefix}/lib -lintl -liconv -lssp ',
		'CPPFLAGS' :  ' {original_stack_protector_trim} -I{output_prefix}/include -L{output_prefix}/lib -lintl -liconv -lssp ',
		'CFLAGS'   :  ' {original_stack_protector_trim} -I{output_prefix}/include -L{output_prefix}/lib -lintl -liconv -lssp ',
		'LDFLAGS'  :  ' {original_stack_protector_trim} -I{output_prefix}/include -L{output_prefix}/lib -lintl -liconv -lssp -Wl,-Bsymbolic ', # to mitigate lock per https://github.com/ffms/ffms2/issues/90
	},
	#'configure_options': '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --enable-static -disable-shared --with-pic --with-zlib={target_prefix}/lib ', # --with-pic per https://github.com/ffms/ffms2/issues/90
	'configure_options': '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --disable-static -enable-shared --with-pic --with-zlib={output_prefix}/ffms2_dll.installed/lib ', # --with-pic per https://github.com/ffms/ffms2/issues/90
	'run_pre_patch' : [
		'cp -fv "Makefile.am" "Makefile.am.orig"',
		'cp -fv "configure.ac" "configure.ac.orig"',
	],
	'patches' : [
		( 'ffms2/0001-ffmsindex-fix-linking-issues.patch', '-Np1' ),
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
	'depends_on': [
		'ffms2_libzimg',		# ok
		'ffms2_xz',				# ok
		'ffms2_zlib',			# ??? no produces a dll ???
		#'ffms2_lzma',			# another name for xz	
		#
		# MABS: {lzma,bzlib,zlib}
		#'ffms2_bzip2',			# no does not install .la file
		#'ffms2_iconv',			# no fails to build shared
		#'ffms2_libxml2',
		#'ffms2_libvpx',
		#'ffms2_libaom',
		#'ffms2_libxvid',
		#'ffms2_libopus',
		#'ffms2_libmp3lame',
		#'ffms2_libvorbis',
		#'ffms2_libtheora',
		#'ffms2_libsoxr',
		#'ffms2_librubberband',
		#'ffms2_libwebp',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'ffms2_dll' },
}


