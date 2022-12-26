{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://download.gnome.org/sources/glib/2.64/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c07e57147b254cef92ce80a0378dc0c02a4358e7de4702e9f403069781095fe2' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c07e57147b254cef92ce80a0378dc0c02a4358e7de4702e9f403069781095fe2' }, ], },
	],
	'conf_system' : 'meson', # not cmake
	'build_system' : 'ninja',
	'source_subfolder' : 'build',

    'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'CXXFLAGS' : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'CPPFLAGS' : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'LDFLAGS'  : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		#'PKG_CONFIG_LIBDIR' : '{target_prefix}/lib',
		#'PKG_CONFIG_PATH'   : '{target_prefix}/lib/pkgconfig',
	},
	'custom_ldflag' : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib -lintl -liconv -lintl ',
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		#'--with-pcre=external '
		'-Dinternal_pcre=true '
		'-Diconv=external '
		'-Dforce_posix_threads=true '
		'-Dglib_debug=disabled '
		'-Dtests=false '
		'-Dman=false '
		'-Dlibmount=disabled '
		'-Dfam=false '
		'--cross-file={meson_env_file} ./ ..'
	,
	'run_post_regexreplace' : [
		'if [ ! -f "INSTALL" ] ; then touch INSTALL ; fi',
		'pwd ; cd .. ; autoreconf -fiv ; cd build ; pwd',
		#'rm -fv ./configure',  # 2019.12.13 # 2020.05.12 comment out to be more like deadsix27
		#'./autogen.sh NOCONFIGURE=1', # 2019.12.13 # 2020.05.12 comment out to be more like deadsix27
	],
	'patches' : [
		('glib2/rdp-glib-2.64.3_mingw-static.patch', '-Np1', '..'), 
  	],
	'run_post_install' : [
		'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"',
		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "glib-2.0.pc"',
		'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"',
		#
		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"',
		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "{pkg_config_path}/glib-2.0.pc"',
		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"',
	],
	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2020.05.12 'pcre', # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '2.71.2', 'fancy_name' : 'glib2 lib' },
}
