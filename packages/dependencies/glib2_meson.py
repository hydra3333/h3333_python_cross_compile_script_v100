{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://download.gnome.org/sources/glib/2.72/glib-2.72.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c07e57147b254cef92ce80a0378dc0c02a4358e7de4702e9f403069781095fe2' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/glib-2.72.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c07e57147b254cef92ce80a0378dc0c02a4358e7de4702e9f403069781095fe2' }, ], },
	],
	'conf_system' : 'meson', # not cmake
	'build_system' : 'ninja',
	'source_subfolder' : 'build',

    'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'CXXFLAGS' : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'CPPFLAGS' : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'LDFLAGS'  : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib ',
		'PKG_CONFIG_LIBDIR' : '{target_prefix}/lib',
		'PKG_CONFIG_PATH'   : '{target_prefix}/lib/pkgconfig',
	},
	'custom_ldflag' : ' -pthread -DGLIB_STATIC_COMPILATION {original_cflags} -L{target_prefix}/lib -lintl -liconv -lintl ',
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		#'--wrap-mode=nodownload '
		#'--auto-features=enabled '
		'-Dinternal_pcre=true '
		'-Dforce_posix_threads=true '
		#'-Dlibelf=disabled '
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
		('glib2/ALEXPUX_2.72.1_0001-Update-g_fopen-g_open-and-g_creat-to-open-with-FILE_.patch', '-Np1', '..'), 
		('glib2/ALEXPUX_2.72.1_0002-disable_glib_compile_schemas_warning.patch', '-Np1', '..'), 
		# https://gitlab.gnome.org/GNOME/glib/-/merge_requests/2613
		('glib2/ALEXPUX_2.72.1_0003-gtestutils-include-stdlib.patch', '-Np1', '..'), 
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
#
# 2022.05.06 for 2.58.3 it builds OK
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#		{ 'url' : 'https://fossies.org/linux/misc/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#	],
#	# 2020.05.12 DISABLED changed to use my configure to be like deadsix27 (i.e. without old PCRE)
#	#'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static '
#	#'--with-threads=posix --enable-gc-friendly --disable-fam --disable-man --disable-gtk-doc '
#	#'--with-pcre=external --with-libiconv --disable-libmount --disable-selinux ',
#	# 2020.05.12 configure more like deadsix27
#	'configure_options' :	'--host={target_host} --prefix={target_prefix} --disable-shared --enable-static '
#							'--with-pcre=external --with-threads=posix --disable-fam --disable-libmount',
#	'run_post_regexreplace' : [
#		'if [ ! -f "INSTALL" ] ; then touch INSTALL ; fi',
#		'echo \'<<EOF\nEXTRA_DIST =\nCLEANFILES =\nEOF\' > gtk-doc.make',
#		'sed -i.bak "s/SUBDIRS = . m4macros glib gmodule gthread gobject gio po docs tests subprojects/SUBDIRS = . m4macros glib gmodule gthread gobject gio po subprojects/" Makefile.am', # remove docs and tests
#		'autoreconf -fiv', # 2019.12.13
#		#'rm -fv ./configure',  # 2019.12.13 # 2020.05.12 comment out to be more like deadsix27
#		#'./autogen.sh NOCONFIGURE=1', # 2019.12.13 # 2020.05.12 comment out to be more like deadsix27
#	],
#	'patches' : [
#		('glib2/0001-Use-CreateFile-on-Win32-to-make-sure-g_unlink-always.patch', '-Np1'), 
#		('glib2/0001-win32-Make-the-static-build-work-with-MinGW-when-pos.patch', '-Np1'), 
#		('glib2/disable_libmount-make-UTF-yes.patch', '-Np0' ), # 2019.12.13 also note Np0
#		('glib2/0001-disable-some-tests-when-static.patch', '-Np1' ),              # 2019.12.13
#		('glib2/0001-Revert-tests-W32-ugly-fix-for-sscanf-format.patch', '-Np1' ), # 2019.12.13
#	],
#	'custom_ldflag' : ' {original_cflags} -lintl -liconv -lintl ',
#	'run_post_install' : [
#		'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#	],
#	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2020.05.12 'pcre', # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
#	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	'_info' : { 'version' : '2.58.3', 'fancy_name' : 'glib2 lib' },
#}


