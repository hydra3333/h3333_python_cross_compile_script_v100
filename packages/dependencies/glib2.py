# 2021.07.21 TRY TO BUILD BASED ON RDP';S with meson
{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://download.gnome.org/sources/glib/2.64/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
		{ 'url' : 'https://download.gnome.org/sources/glib/2.69/glib-2.69.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/glib-2.69.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
	],
	'patches' : [
		('glib2/glib-2.64.3_mingw-static.patch', '-Np1'), 
	],
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'custom_cflag'  : ' {original_cflags} -L${target_prefix}/lib -pthread -DGLIB_STATIC_COMPILATION -lintl -liconv -lintl ',
	'custom_ldflag' : ' {original_cflags} -L${target_prefix}/lib -pthread -DGLIB_STATIC_COMPILATION -lintl -liconv -lintl ', #  # For some reason the frexp configure checks fail without this as math.h isn't found when cross-compiling;
		'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'-Dinternal_pcre=true '
		'-Dforce_posix_threads=true '
		'--cross-file={meson_env_file} ./ ..'   # or . build
	,
	'run_post_install' : [
		'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"', # 2019.12.13
		'sed -s -i.bak1 \'s/-lintl/-pthread -lm -lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
		'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"', # 2019.12.13
		'sed -s -i.bak1 \'s/-lintl/-pthread -lm -lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
	],
	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2020.05.12 'pcre', # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.69/" lang="">(?P<version_num>[\d.]+)<\/a>' },
	#'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
	'_info' : { 'version' : '2.69.0', 'fancy_name' : 'glib2 lib' },
	#'_info' : { 'version' : '2.58.3', 'fancy_name' : 'glib2 2.58.3 lib' },
}
#
#
#
# 2020.10.22 see glib2-new for an attempt at a later version
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://download.gnome.org/sources/glib/2.58/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#		{ 'url' : 'https://fossies.org/linux/misc/glib-2.58.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '8f43c31767e88a25da72b52a40f3301fefc49a665b56dc10ee7cc9565cbe7481' }, ], },
#		#{ 'url' : 'https://download.gnome.org/sources/glib/2.69/glib-2.69.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
#		#{ 'url' : 'https://fossies.org/linux/misc/glib-2.69.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1cdb3fd8610f3c57b6622e5cd68e0a3210561d80b0eceb971eb51fb8b63dbfae' }, ], },
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
#		('glib2/glib-2.64.3_mingw-static.patch', '-Np1'), 
#		('glib2/disable_libmount-make-UTF-yes.patch', '-Np0' ), # 2019.12.13 also note Np0
#		('glib2/0001-disable-some-tests-when-static.patch', '-Np1' ),              # 2019.12.13
#		('glib2/0001-Revert-tests-W32-ugly-fix-for-sscanf-format.patch', '-Np1' ), # 2019.12.13
#	],
#	# 2020.05.12 comment out all of the run_post_install, to be more like deadsix27
#	'custom_ldflag' : ' {original_cflags} -lintl -liconv -lintl ',
#	'run_post_install' : [ # 2019.12.13 addded all of run_post_install
#		'cp -fv "glib-2.0.pc" "glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "glib-2.0.pc"', # 2019.12.13
#	#	#'sed -s -i.bak2 \'s/ -lgiowin32//g\' "glib-2.0.pc"', # 2019.12.13
#	#	#'sed -s -i.bak3 \'s/ -llgnulib//g\' "glib-2.0.pc"', # 2019.12.13
#	#	#'sed -s -i.bak4 \'s/ -lcharset//g\' "glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "glib-2.0.pc.orig" "glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#	#	#
#		'cp -fv "{pkg_config_path}/glib-2.0.pc" "{pkg_config_path}/glib-2.0.pc.orig"', # 2019.12.13
#		'sed -s -i.bak1 \'s/-lintl/-lintl -liconv -lintl/\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
#	#	#'sed -s -i.bak2 \'s/ -lgiowin32//g\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
#	#	#'sed -s -i.bak3 \'s/ -llgnulib//g\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
#	#	#'sed -s -i.bak4 \'s/ -lcharset//g\' "{pkg_config_path}/glib-2.0.pc"', # 2019.12.13
#		'diff -U 5 "{pkg_config_path}/glib-2.0.pc.orig" "{pkg_config_path}/glib-2.0.pc"  && echo "NO difference" || echo "YES differences!"', # 2019.12.13
#	],
#	'depends_on' : [ 'iconv', 'gettext', 'pcre2', 'libffi', 'zlib', 'python3_libs', 'libelf' ], # 2020.05.12 'pcre', # 2019.12.13 added my stuff, removed 'pcre' ... testing if pcre2 is good enough
#	#'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.59/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	'update_check' : { 'url' : 'https://developer.gnome.org/glib/', 'type' : 'httpregex', 'regex' : r'<a class="doc-link" href="2.58/" lang="">(?P<version_num>[\d.]+)<\/a>' },
#	#'_info' : { 'version' : '2.69.0', 'fancy_name' : 'glib2 lib' },
#	'_info' : { 'version' : '2.58.3', 'fancy_name' : 'glib2 2.58.3 lib' },
#}
#
#
#
#
# rdp'S BUILD OF GLIB:
#build_glib() {
# 
#  export CPPFLAGS="$CPPFLAGS -DLIBXML_STATIC -liconv" # gettext build...
#  
#  generic_download_and_make_and_install  https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz
#  reset_cppflags
#  
#  generic_download_and_make_and_install  https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz # also dep
#  download_and_unpack_file https://gitlab.gnome.org/GNOME/glib/-/archive/2.64.3/glib-2.64.3.tar.gz
#  
#  cd glib-2.64.3
#    
#	apply_patch  file://$patch_dir/glib-2.64.3_mingw-static.patch -p1
#    
#	export CPPFLAGS="$CPPFLAGS -pthread -DGLIB_STATIC_COMPILATION"
#    export CXXFLAGS="$CFLAGS" # Not certain this is needed, but it doesn't hurt
#    export LDFLAGS="-L${mingw_w64_x86_64_prefix}/lib" # For some reason the frexp configure checks fail without this as math.h isn't found when cross-compiling; no negative impact for native builds
#    
#	local meson_options="--prefix=${mingw_w64_x86_64_prefix} --libdir=${mingw_w64_x86_64_prefix}/lib --buildtype=release --default-library=static -Dinternal_pcre=true -Dforce_posix_threads=true . build"
#    if [[ $compiler_flavors != "native" ]]; then
#      get_local_meson_cross_with_propeties # Need to add flags to meson properties; otherwise ran into some issues
#      meson_options+=" --cross-file=meson-cross.mingw.txt"
#    fi
#    do_meson "$meson_options"
#    do_ninja_and_ninja_install
#    
#	if [[ $compiler_flavors == "native" ]]; then
#      sed -i.bak 's/-lglib-2.0.*$/-lglib-2.0 -pthread -lm -liconv/' $PKG_CONFIG_PATH/glib-2.0.pc
#    else
#      sed -i.bak 's/-lglib-2.0.*$/-lglib-2.0 -lintl -pthread -lws2_32 -lwinmm -lm -liconv -lole32/' $PKG_CONFIG_PATH/glib-2.0.pc
#    fi
#    
#	reset_cppflags
#    unset CXXFLAGS
#    unset LDFLAGS
#  cd ..
#}

