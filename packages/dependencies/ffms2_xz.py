{
	'repo_type' : 'git',
	#'url' : 'http://git.tukaani.org/xz.git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	'depth_git' : 0,
	'folder_name' : 'ffms2_xz',
	'custom_cflag' : ' -D_FORTIFY_SOURCE=2 ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all
	'env_exports' : {
		'CXXFLAGS' :  ' {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib ',
		'CPPFLAGS' :  ' {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib ',
		'CFLAGS'   :  ' {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib ',
		'LDFLAGS'  :  ' {original_stack_protector_trim} -I{output_prefix}/ffms2_dll.installed/inlcude -I{target_prefix}/include -L{output_prefix}/ffms2_dll.installed/lib -L{target_prefix}/lib ',
		'PKG_CONFIG_PATH'   : '{output_prefix}/ffms2_dll.installed/lib/pkgconfig',
		'PKG_CONFIG_LIBDIR' : '{output_prefix}/ffms2_dll.installed/lib',
	},
	'run_post_regexreplace' : [
		'pwd ; autoreconf -fiv ; pwd', # autoreconf is almost identical to ./autogen.sh
		'./configure --help',
	],
	#'configure_options' : '{autoconf_prefix_options} --enable-shared --disable-static --enable-assembler --disable-debug --disable-small ' # --enable-threads=posix
	'configure_options' : '--with-sysroot="{target_sub_prefix}" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static  --enable-assembler --disable-debug --disable-small ' # --enable-threads=posix
							'--disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc --without-iconv '
							'--disable-lzma-links --disable-scripts '
	,
	#'depends_on' : [ 
	#	'iconv',
	#],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'xz' },
}
#--with-sysroot="{target_sub_prefix}" --host="{target_host}" --prefix="{output_prefix}/ffms2_dll.installed" --enable-shared --disable-static 