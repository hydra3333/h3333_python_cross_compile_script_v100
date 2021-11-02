{ # 2020.10.21 be more like RDP for later versions of glib2
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	#{ 'url' : 'https://download.gnome.org/sources/glib/2.64/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fe9cbc97925d14c804935f067a3ad77ef55c0bbe9befe68962318f5a767ceb22' }, ], }, # 2020.10.21 try this version
	#	{ 'url' : 'https://download.gnome.org/sources/glib/2.66/glib-2.66.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ec390bed4e8dd0f89e918f385e8d4cfd7470b1ef7c1ce93ec5c4fc6e3c6a17c4' }, ], }, # 2020.10.21 try this version
	#	{ 'url' : 'https://fossies.org/linux/misc/glib-2.66.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ec390bed4e8dd0f89e918f385e8d4cfd7470b1ef7c1ce93ec5c4fc6e3c6a17c4' }, ], }, # 2020.10.21 try this version
	#],
	'repo_type' : 'git',
	'depth_git' : 0,
	'url' : 'https://github.com/GNOME/glib.git', # this is a reasonably up to date mirror
	'branch' : 'tags/2.64.3',
	#'branch' : 'tags/2.66.2',
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
		#('glib2/glib2-debug-patch-2020.10.21.patch', '-Np1', '..'), # note Np1, MY TEMPORARY DEBUG PATCH ON TOP OF PRIOR PATCHES for meson.build
		('glib2/rdp-glib-2.64.3_mingw-static.patch', '-Np1', '..'), # note Np1, if fails, try adding ", '..')"
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
	'_info' : { 'version' : '2.66.2', 'fancy_name' : 'glib2 lib' },
}
#
# rdp'S BUILD OF GLIB:
#build_glib() {
#  export CPPFLAGS="$CPPFLAGS -DLIBXML_STATIC -liconv" # gettext build...
#  generic_download_and_make_and_install  https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz
#  reset_cppflags
#  generic_download_and_make_and_install  https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz # also dep
#  download_and_unpack_file https://gitlab.gnome.org/GNOME/glib/-/archive/2.64.3/glib-2.64.3.tar.gz
#  cd glib-2.64.3
#    apply_patch  file://$patch_dir/glib-2.64.3_mingw-static.patch -p1
#    export CPPFLAGS="$CPPFLAGS -pthread -DGLIB_STATIC_COMPILATION"
#    export CXXFLAGS="$CFLAGS" # Not certain this is needed, but it doesn't hurt
#    export LDFLAGS="-L${mingw_w64_x86_64_prefix}/lib" # For some reason the frexp configure checks fail without this as math.h isn't found when cross-compiling; no negative impact for native builds
#    local meson_options="--prefix=${mingw_w64_x86_64_prefix} --libdir=${mingw_w64_x86_64_prefix}/lib --buildtype=release --default-library=static -Dinternal_pcre=true -Dforce_posix_threads=true . build"
#    if [[ $compiler_flavors != "native" ]]; then
#      get_local_meson_cross_with_propeties # Need to add flags to meson properties; otherwise ran into some issues
#      meson_options+=" --cross-file=meson-cross.mingw.txt"
#    fi
#    do_meson "$meson_options"
#    do_ninja_and_ninja_install
#    if [[ $compiler_flavors == "native" ]]; then
#      sed -i.bak 's/-lglib-2.0.*$/-lglib-2.0 -pthread -lm -liconv/' $PKG_CONFIG_PATH/glib-2.0.pc
#    else
#      sed -i.bak 's/-lglib-2.0.*$/-lglib-2.0 -lintl -pthread -lws2_32 -lwinmm -lm -liconv -lole32/' $PKG_CONFIG_PATH/glib-2.0.pc
#    fi
#    reset_cppflags
#    unset CXXFLAGS
#    unset LDFLAGS
#  cd ..
#}
#
# 2021.07.21 TRY TO BUILD BASED ON RDP';S with meson
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://download.gnome.org/sources/glib/2.64/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fe9cbc97925d14c804935f067a3ad77ef55c0bbe9befe68962318f5a767ceb22' }, ], },
#		{ 'url' : 'https://fossies.org/linux/misc/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fe9cbc97925d14c804935f067a3ad77ef55c0bbe9befe68962318f5a767ceb22' }, ], },
#		#{ 'url' : 'https://download.gnome.org/sources/glib/2.69/glib-2.69.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
#		#{ 'url' : 'https://fossies.org/linux/misc/glib-2.69.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
#	],
#	'patches' : [
#		('glib2/glib-2.64.3_mingw-static.patch', '-Np1', ".."), 
#	],
#	'conf_system' : 'meson',
#	'build_system' : 'ninja',
#	'source_subfolder' : 'build',
#	'custom_cflag'  : ' {original_cflags} -L${target_prefix}/lib -pthread -DGLIB_STATIC_COMPILATION -lintl -liconv -lintl ',
#	'custom_ldflag' : ' {original_cflags} -L${target_prefix}/lib -pthread -DGLIB_STATIC_COMPILATION -lintl -liconv -lintl ', #  # For some reason the frexp configure checks fail without this as math.h isn't found when cross-compiling;
#		'configure_options' :
#		'--prefix={target_prefix} '
#		'--libdir={target_prefix}/lib '
#		'--default-library=static '
#		'--buildtype=release '
#		'-Dinternal_pcre=true '
#		'-Dforce_posix_threads=true '
#		'--cross-file={meson_env_file} ./ ..'   # or . build
#	,
#	'run_post_install' : [
#		'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-pthread -lm -lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-pthread -lm -lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#	],
#	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2020.05.12 'pcre', # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
#	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.69/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	#'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	'_info' : { 'version' : '2.69.0', 'fancy_name' : 'glib2 lib' },
#	#'_info' : { 'version' : '2.58.3', 'fancy_name' : 'glib2 2.58.3 lib' },
#}

