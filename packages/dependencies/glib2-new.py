{ # 2020.10.21 be more like RDP for later versions of glib2
	#'repo_type' : 'archive',
	#'download_locations' : [
		#{ 'url' : 'https://download.gnome.org/sources/glib/2.69/glib-2.69.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f92f34057a091fc8638d91f10cece842cb8618e9a1090b0ddb19cc15a21bf39c' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/glib-2.69.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'f92f34057a091fc8638d91f10cece842cb8618e9a1090b0ddb19cc15a21bf39c' }, ], },
		#{ 'url' : 'https://download.gnome.org/sources/glib/2.69/glib-2.69.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '47af2c6e06becee44d447ae7d1212dbab255b002b5141d9b62a4357c0ecc058f' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/glib-2.69.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '47af2c6e06becee44d447ae7d1212dbab255b002b5141d9b62a4357c0ecc058f' }, ], },
	#],
	'repo_type' : 'git',
	'depth_git' : 0,
	'url' : 'https://github.com/GNOME/glib.git', # this is a reasonably up to date mirror
	'branch' : 'tags/2.69.3',
	'folder_name' : 'glib2',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'env_exports' : {
		'CFLAGS'   : '{original_cflags} -pthread -DGLIB_STATIC_COMPILATION ',
		'CXXFLAGS' : '{original_cflags} -pthread -DGLIB_STATIC_COMPILATION ',
		'CPPFLAGS' : '{original_cflags} -pthread -DGLIB_STATIC_COMPILATION ',
		'LDFLAGS'  : '{original_cflags} -pthread -DGLIB_STATIC_COMPILATION -L{target_prefix}/lib ', # 2020.10.21 per RDP we add "-L{target_prefix}/lib"
		#'PKGCONFIG' : 'pkg-config', # 2020.10.21 try this since it seems to be failing in glib2
	},
	
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir=lib '
		'--includedir=include '
		'--default-library=static '
		'--backend=ninja '
		'--buildtype=release '
		'-Dinternal_pcre=false ' #'-Dinternal_pcre=true '
		'-Dforce_posix_threads=true '
		'-Diconv=external ' # 2020.10.21 try this
		'-Dlibmount=disabled ' # 2020.10.21 try this
		'-Dman=false ' # 2020.10.21 try this
		'-Dfam=false '
		'-Dinstalled_tests=false '
		'--cross-file={meson_env_file} ./ ..' ,
	'patches' : [
		#('glib2/disable_libmount-make-UTF-yes.patch', '-Np0', '..'), # 2020.10.21 no longer works on v2.6x+
		('glib2/rdp-glib-2.64.3_mingw-static.patch', '-Np1', '..'), # note Np1, if fails, try adding ", '..')"
		#('glib2/glib2-debug-patch-2020.10.21.patch', '-Np1', '..'), # note Np1, MY TEMPORARY DEBUG PATCH ON TOP OF PRIOR PATCHES for meson.build
	],
	'run_post_patch' : [
		'ls -al "../"',
		'cp -fv "../meson.build" "../meson.build.orig_post_patch"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_prefix=\' + glib_prefix)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_bindir=\' + glib_bindir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_libdir=\' + glib_libdir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_libexecdir=\' + glib_libexecdir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_datadir=\' + glib_datadir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_pkgdatadir=\' + glib_pkgdatadir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_includedir=\' + glib_includedir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_pkgconfigreldir=\' + glib_pkgconfigreldir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;message(\'glib_charsetaliasdir=\' + glib_charsetaliasdir)\\ninstalled_tests_metadir =;g" "../meson.build"',
		'sed -i.bak "s;installed_tests_metadir =;\\ninstalled_tests_metadir =;g" "../meson.build"',
		'diff -U 5 "../meson.build.orig_post_patch" "../meson.build" && echo "NO difference" || echo "YES differences!"',
		#
		'/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/pkg-config --modversion libelf',
		'/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/pkg-config --cflags libelf',
		'pkg-config --modversion libelf',
		'pkg-config --cflags libelf',
	],
	'run_post_install' : [
		'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"',
		#'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "glib-2.0.pc"',
		'sed -i.bak \'s/-lglib-2.0.*$/-lglib-2.0 -lintl -liconv -lintl -pthread -lws2_32 -lwinmm -lm -liconv -lole32/\' "glib-2.0.pc"', # per RDP
		'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc" && echo "NO difference" || echo "YES differences!"',
		#
		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"',
		#'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "{pkg_config_path}/glib-2.0.pc"',
		'sed -i.bak \'s/-lglib-2.0.*$/-lglib-2.0 -lintl -liconv -lintl -pthread -lws2_32 -lwinmm -lm -liconv -lole32/\' "{pkg_config_path}/glib-2.0.pc"', # per RDP
		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc" && echo "NO difference" || echo "YES differences!"',
	],
	
	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], #  'pcre',
	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '2.69.3', 'fancy_name' : 'glib2 lib' },
}
