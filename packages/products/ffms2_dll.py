{
	'repo_type' : 'git',
	'url' : 'https://github.com/FFMS/ffms2', 
	'depth_git' : 0,
	'rename_folder' : 'ffms2_dll',
	'configure_options': '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --enable-static -disable-shared --with-zlib={target_prefix}/lib',
	'env_exports' : {
		'CXXFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CPPFLAGS' :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
		'CFLAGS'   :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
		'LDFLAGS'  :  ' {original_stack_protector_trim} -I{target_prefix}/include -L{target_prefix}/lib -lintl -liconv -lssp ',
	},
	'patches' : [
		( 'ffms2/0001-ffmsindex-fix-linking-issues.patch', '-Np1' ),
	],
	'run_post_patch' : [ 
		'sed -i "s/Libs.private.*/& -lstdc++/;s/Cflags.*/& -DFFMS_STATIC/" "ffms2.pc.in"',
		'if [ -f "./configure" ] ; then rm -fv ./configure ; fi',
		'if [ ! -d "src/config" ] ; then mkdir -p "src/config" ; fi',
		'autoreconf -fiv',
		'./configure --help=recursive',
	],
	'depends_on': [
		'libzimg', 'bzip2', 'libffmpeg_extra',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'ffms2_dll' },
}
