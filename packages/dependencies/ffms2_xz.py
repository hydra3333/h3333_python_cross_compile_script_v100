{
	'repo_type' : 'git',
	#'url' : 'http://git.tukaani.org/xz.git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	'depth_git' : 0,
	'folder_name' : 'ffms2_xz',
#	'custom_cflag' : ' -D_FORTIFY_SOURCE=2 ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all
	'env_exports' : {
		# ONLY this EXACT set of flags works ...
		'CXXFLAGS' :  ' {original_fortify_source} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include ',
		'CPPFLAGS' :  ' {original_fortify_source} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include ',
		'CFLAGS'   :  ' {original_fortify_source} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include ',
		'LDFLAGS'  :  ' -fstack-protector -Wl,-Bsymbolic {original_fortify_source} -I{output_prefix}/ffms2_dll.installed/include -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	'run_post_regexreplace' : [
		'pwd ; autoreconf -fiv ; pwd', # autoreconf is almost identical to ./autogen.sh
		#'./configure --help',
		#'cp -fv "src/liblzma/liblzma.pc.in" "src/liblzma/liblzma.pc.in.orig"',
		#'sed -ibak "s/ -llzma/ -llzma -lssp/g" src/liblzma/liblzma.pc.in',
		#'diff -U 10 "src/liblzma/liblzma.pc.in.orig" "src/liblzma/liblzma.pc.in"  && echo "NO difference" || echo "YES differences!"'
	],
	'configure_options' :	'--host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" '
							'--enable-shared --disable-static '
							#'--enable-threads=posix '
							'--disable-debug '
							'--enable-assembler '
							'--disable-small '
							'--disable-xz '
							'--disable-xzdec '
							'--disable-lzmadec '
							'--disable-lzmainfo '
							'--disable-doc '
							'--disable-lzma-links '
							'--disable-scripts '
							'--disable-nls '
							'--disable-rpath '
							'--enable-largefile '
							'--without-iconv '
	,
	'run_post_install' : [
		'cat {output_prefix}/ffms2_dll.installed/lib/pkgconfig/liblzma.pc',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ffms2_xz' },
}