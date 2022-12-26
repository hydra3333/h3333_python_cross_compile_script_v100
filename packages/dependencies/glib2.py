{ # 2022.12.18 per DEADSIX27 changed to try deadsix27, plus marked changes to that
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://download.gnome.org/sources/glib/2.75/glib-2.75.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6dde8e55cc4a2c83d96797120b08bcffb5f645b2e212164ae22d63c40e0e6360' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/glib-2.75.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6dde8e55cc4a2c83d96797120b08bcffb5f645b2e212164ae22d63c40e0e6360' }, ], },
	],
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'configure_options' : 
		'--host={target_host} ' # 2022.12.18 comment this out if it doesnt work
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--disable-shared --enable-static ' # 2022.12.18
		'--default-library=static ' 
		'--backend=ninja '
		'--buildtype=release '
		'-Dtests=false '
		'-Dinstalled_tests=false '
		'-Dglib_debug=false ' # 2022.12.18
		'-Dlibelf=true ' # 2022.12.18
		'-Diconv=external '	# 2022.12.18 choices : ['auto', 'libc', 'external'], so try external,l or omit and see if it builds
		'-Dlibmount=false '	# 2022.12.18
		'-Dforce_posix_threads=true '	# 2022.12.18 
		'--cross-file={meson_env_file} ./ ..'
	,
#	'configure_options' :	'--host={target_host} --prefix={target_prefix} --disable-shared --enable-static ' # 2022.12.18
#							'--with-pcre=external --with-threads=posix --disable-fam --disable-libmount', # 2022.12.18
	'patches' : [
		('glib2/disable_libmount-make-UTF-yes.patch', '-Np0', '..' ), # 2022.12.18 --- also note "-Np0" and ", '..'"
		# ( 'glib2/0001-Use-CreateFile-on-Win32-to-make-sure-g_unlink-always.patch', '-p1' ),
		# ( 'glib2/0001-win32-Make-the-static-build-work-with-MinGW-when-pos.patch', '-p1' ),
		# ( 'glib2/0001-disable-some-tests-when-static.patch', '-p1' ),
		# ( 'glib2/0001-Revert-tests-W32-ugly-fix-for-sscanf-format.patch', '-p1' ),
	],
	'run_post_patch' : [
		# 'if [ ! -f "INSTALL" ] ; then touch INSTALL ; fi',
		# 'echo \'<<EOF\nEXTRA_DIST =\nCLEANFILES =\nEOF\' > gtk-doc.make',
		# 'sed -i.bak "s/SUBDIRS = . m4macros glib gmodule gthread gobject gio po docs tests subprojects/SUBDIRS = . m4macros glib gmodule gthread gobject gio po subprojects/" Makefile.am',
		#'autoreconf -fiv',
	],
	#'custom_cflag' : '-O3', # 2022.12.18
	'custom_ldflag' : ' {original_cflags} -lintl -liconv -lintl ', # 2022.12.18
	#'run_post_install' : [ # 2022.12.18
	#	'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"', # 2019.12.13
	#	'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
	#	'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
	#	#
	#	'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"', # 2019.12.13
	#	'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
	#	'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
	#],
	#'depends_on' : [ 'pcre2', 'libffi','gettext' ], # 'libelf' ], # 2022.12.18
	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2022.12.18
	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.70/" lang="">(?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '2.75', 'fancy_name' : 'glib2' },
}
# ########## As reference when we have to switch to cmake, which still fails to build so..
#{
#	'repo_type' : 'archive',
#	# 'download_locations' : [
#		# { 'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c7b24ed6536f1a10fc9bce7994e55c427b727602e78342821f1f07fb48753d4b' }, ], },
#		# { 'url' : 'https://fossies.org/linux/misc/glib-2.58.2.tar.xz/', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c7b24ed6536f1a10fc9bce7994e55c427b727602e78342821f1f07fb48753d4b' }, ], },
#	# ],
#	'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.3.tar.xz',
#	# 'run_post_patch' : [
#		# 'if [ ! -f "INSTALL" ] ; then touch INSTALL ; fi',
#		# 'echo \'<<EOF\nEXTRA_DIST =\nCLEANFILES =\nEOF\' > gtk-doc.make',
#		# 'sed -i.bak "s/SUBDIRS = . m4macros glib gmodule gthread gobject gio po docs tests subprojects/SUBDIRS = . m4macros glib gmodule gthread gobject gio po subprojects/" Makefile.am',
#		# 'autoreconf -fiv',
#	# ],
#	'conf_system' : 'meson',
#	'build_system' : 'ninja',
#	'source_subfolder' : 'build',
#	'configure_options' : 
#		'--prefix={target_prefix} '
#		'--libdir={target_prefix}/lib '
#		'--default-library=static '
#		'--buildtype=plain '
#		'--backend=ninja '
#		# '-Dbuild_tests=false '
#		# '-Dbuild_tools=false '
#		'--buildtype=release '
#		'-Dinstalled_tests=false '
#		'-Dinternal_pcre=true '
#		'-Diconv=native '#          [libc, gnu, native]
#		'-Dforce_posix_threads=true '
#		'--cross-file={meson_env_file} ./ ..'
#		# --with-pcre=internal --with-threads=posix --disable-fam --disable-shared --disable-libmount
#	,
#	'env_exports' : {
#		'LDFLAGS' : '-liconv',
#	},
#	'patches' : [
#		( 'glib2/0001-Use-CreateFile-on-Win32-to-make-sure-g_unlink-always.patch', '-p1', '..' ),
#		( 'glib2/0001-win32-Make-the-static-build-work-with-MinGW-when-pos.patch', '-p1', '..' ),
#		( 'glib2/0001-disable-some-tests-when-static.patch', '-p1', '..' ),
#		( 'glib2/0001-Revert-tests-W32-ugly-fix-for-sscanf-format.patch', '-p1', '..' ),
#		
#	],
#	'depends_on' : [ 'libffi', 'gettext' ],
#	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	'_info' : { 'version' : '2.58.2', 'fancy_name' : 'glib2' },
#}
# -----------
# OLD before 2022.12.18
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#		{ 'url' : 'https://fossies.org/linux/misc/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#		# glib-2.72.1 fails to locate PCRE (PCRE2) by any method.  Grr.
#	],
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
#		#
#		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#	],
#	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2020.05.12 'pcre', # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
#	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	'_info' : { 'version' : '2.58.1', 'fancy_name' : 'glib2 lib' },
#}


