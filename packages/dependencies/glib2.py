{ # 2019.12.13 glib3 failed to buid, fox it
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
	],
	# 2019.12.13 changed to use my configure which worked.
	#'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --with-threads=posix --disable-fam --enable-gc-friendly --disable-man --disable-gtk-doc --with-pcre=external --with-libiconv --disable-libmount --disable-selinux', # 2019.12.13
	 'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --with-threads=posix --enable-gc-friendly --disable-fam --disable-man --disable-gtk-doc --with-pcre=system   --with-libiconv --disable-libmount --disable-selinux ', # ??? --with-pcre=internal # 2019.04.13 --disable-libelf 

	'run_post_patch' : [
		'if [ ! -f "INSTALL" ] ; then touch INSTALL ; fi',
		'echo \'<<EOF\nEXTRA_DIST =\nCLEANFILES =\nEOF\' > gtk-doc.make',
		'sed -i.bak "s/SUBDIRS = . m4macros glib gmodule gthread gobject gio po docs tests subprojects/SUBDIRS = . m4macros glib gmodule gthread gobject gio po subprojects/" Makefile.am', # remove docs and tests
		'autoreconf -fiv', # 2019.12.13
		'rm -fv ./configure',  # 2019.12.13
		'./autogen.sh NOCONFIGURE=1', # 2019.12.13
		#'autoreconf -fiv', # 2019.12.13
	],
	'patches' : [
		( 'glib2/0001-Use-CreateFile-on-Win32-to-make-sure-g_unlink-always.patch', '-p1' ),
		( 'glib2/0001-win32-Make-the-static-build-work-with-MinGW-when-pos.patch', '-p1' ),
        ( 'glib2/disable_libmount-make-UTF-yes.patch', '-p1' ),  # 2019.12.13
		( 'glib2/0001-disable-some-tests-when-static.patch', '-p1' ),
		( 'glib2/0001-Revert-tests-W32-ugly-fix-for-sscanf-format.patch', '-p1' ),
	],
    'run_post_install' : [ # 2019.12.13 addded all of run_post_install
		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv/\' "glib-2.0.pc"', # 2019.12.13
		'sed -s -i.bak2 \'s/ -lgiowin32//g\' "glib-2.0.pc"', # 2019.12.13
		'sed -s -i.bak3 \'s/ -llgnulib//g\' "glib-2.0.pc"', # 2019.12.13
		'sed -s -i.bak4 \'s/ -lcharset//g\' "glib-2.0.pc"', # 2019.12.13
		#
		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv/\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
		'sed -s -i.bak2 \'s/ -lgiowin32//g\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
		'sed -s -i.bak3 \'s/ -llgnulib//g\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
		'sed -s -i.bak4 \'s/ -lcharset//g\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
	],
	#'depends_on' : [ 'libffi','gettext', 'libelf' ],  # 2019.12.13
    'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '2.58.3', 'fancy_name' : 'glib2 lib' },
}
# 2019.12.13 old:
#	'libglib2' : { # UN-uperseded 2019.05.12 # superseded 2019.05.12
#		#'repo_type' : 'git',
#		#'url' : 'https://gitlab.gnome.org/GNOME/glib.git',
#		#'branch' : 'tags/2.58.3',
#		####'branch' : 'tags/2.60.1', # 2019.05.05
#		'repo_type' : 'archive',
#		'download_locations' : [
#			{ 'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#			{ 'url' : 'https://fossies.org/linux/misc/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#		],
#		'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --with-threads=posix --enable-gc-friendly --disable-fam --disable-man --disable-gtk-doc --with-pcre=system --with-libiconv --disable-libmount --disable-selinux ', # ??? --with-pcre=internal # 2019.04.13 --disable-libelf 
#		'patches' : [
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libglib2-from-Alexpux-2_58_0/0001-Use-CreateFile-on-Win32-to-make-sure-g_unlink-always.patch', '-Np1'), 
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libglib2-from-Alexpux-2_58_0/0001-win32-Make-the-static-build-work-with-MinGW-when-pos.patch', '-Np1'), 
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libglib2-from-Alexpux-2_58_0/disable_libmount-make-UTF-yes.patch', '-Np0' ), # 2018.08.10 mine # TODO: CHECK THIS PATCH
#			# ('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libglib2-from-Alexpux-2_58_0/0001-glib2-mr-226.patch', '-Np1' ), # 2018.08.31 this patch is already implemented in 2.58.0 ... for same as -D_FILE_OFFSET_BITS=64 per alexpux
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libglib2-from-Alexpux-2_58_0/0001-disable-some-tests-when-static.patch', '-p1' ),              # 2019.04.13
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libglib2-from-Alexpux-2_58_0/0001-Revert-tests-W32-ugly-fix-for-sscanf-format.patch', '-p1' ), # 2019.04.13
#		],
#		'run_post_patch' : [
#			'rm -fv ./configure',
#			'./autogen.sh NOCONFIGURE=1',
#			'autoreconf -fiv',
#		],
#		'run_post_install' : [
#			'sed -s -i.bak1 \'s/-lintl/-lintl -liconv/\' "glib-2.0.pc"',
#			'sed -s -i.bak2 \'s/ -lgiowin32//g\' "glib-2.0.pc"',
#			'sed -s -i.bak3 \'s/ -llgnulib//g\' "glib-2.0.pc"',
#			'sed -s -i.bak4 \'s/ -lcharset//g\' "glib-2.0.pc"',
#			#
#			'sed -s -i.bak1 \'s/-lintl/-lintl -liconv/\' "{pkg_config_path}/glib-2.0.pc"',
#			'sed -s -i.bak2 \'s/ -lgiowin32//g\' "{pkg_config_path}/glib-2.0.pc"',
#			'sed -s -i.bak3 \'s/ -llgnulib//g\' "{pkg_config_path}/glib-2.0.pc"',
#			'sed -s -i.bak4 \'s/ -lcharset//g\' "{pkg_config_path}/glib-2.0.pc"',
#			#
#			#'sed -i.bak \'s/$(cygpath -m \${MINGW_PREFIX})/\${MINGW_PREFIX}/g\' "{pkg_config_path}/glib-2.0.pc"', # TODO: CHANGE MINGW_PREFIX TO SOMETHING ELSE ...
#			#'sed -i.bak \'s/$(cygpath -m \${MINGW_PREFIX})/\${MINGW_PREFIX}/g\' "glib-2.0.pc"', # TODO: CHANGE MINGW_PREFIX TO SOMETHING ELSE ...
#			#'sed -i.bak \'s/$(cygpath -m ${MINGW_PREFIX})/${MINGW_PREFIX}/g" "{target_prefix}/bin/glib-gettextize" # TODO: CHANGE MINGW_PREFIX TO SOMETHING ELSE ...
#		],
#		'depends_on' : [ 'iconv', 'gettext', 'pcre', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2017.23.11 not 'libmount'
#		'_info' : { 'version' : '(git tags/2.58.3)', 'fancy_name' : 'libglib2' },
#	},
