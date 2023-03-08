{ # 2019.12.13
	'repo_type' : 'git',
	'url' : 'https://github.com/madler/zlib.git',
	'conf_system' : 'cmake',
	'folder_name' : 'ffms2_zlib',
	'source_subfolder' : '_build',
	'env_exports' : {
		'CXXFLAGS' :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'CPPFLAGS' :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'CFLAGS'   :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'LDFLAGS'  :  ' -Wl,-Bsymbolic {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib -lssp ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX="{output_prefix}/ffms2_dll.installed" '
							'-DINSTALL_PKGCONFIG_DIR="{output_prefix}/ffms2_dll.installed/lib/pkgconfig" '
							#'-DINSTALL_PKGCONFIG_DIR="{output_prefix}/ffms2_dll.installed//share/pkgconfig '
							'-DBUILD_SHARED_LIBS=1 '
							'-DCMAKE_BUILD_TYPE=Release '
							'-D_FILE_OFFSET_BITS=64 '
							'-D_LARGEFILE64_SOURCE=1 ',
	'patches' : [
		('zlib/0001-mingw-workarounds.patch', '-p1', '..'),
	],
	'run_post_patch' : [ 
		'cp -fv "../CMakeLists.txt" "../CMakeLists.txt.orig"',
		#'sed -ibak "s/install(TARGETS zlibstatic/install(TARGETS zlib/" ../CMakeLists.txt'
		'diff -U 10 "../CMakeLists.txt.orig" "../CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"',
	],
	'run_post_install;' :
		'cat {output_prefix}/ffms2_dll.installed/lib/pkgconfig/zlib.pc',
	],	
	'depends_on' : [
		'pkg-config', 
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffms2_zlib' },
}
