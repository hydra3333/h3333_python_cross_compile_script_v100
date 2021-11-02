# 2021.07.21 TRY TO BUILD BASED ON RDP';S with meson
{
	'repo_type' : 'archive',
	'download_locations' : [ # https://fossies.org/linux/misc/
		{ 'url' : 'https://download.gnome.org/sources/glib/2.64/glib-2.64.3.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fe9cbc97925d14c804935f067a3ad77ef55c0bbe9befe68962318f5a767ceb22' }, ], },
	],
	'patches' : [
		('glib2/glib-2.64.3_mingw-static.patch', '-Np1') # add , ".."),  only when using 'source_subfolder' : 'build',
	],
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	#'source_subfolder' : 'build',
	'custom_ldflag' : ' {original_cflags} -L${target_prefix}/lib -pthread -DGLIB_STATIC_COMPILATION -lintl -liconv -lintl ', #  # For some reason the frexp configure checks fail without this as math.h isn't found when cross-compiling;
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'-Dinternal_pcre=true '
		'-Dforce_posix_threads=true '
		'--cross-file={meson_env_file} . build' # either ./ ..  only when using 'source_subfolder' : 'build', or  . build if not using 'source_subfolder' : 'build'
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
	'_info' : { 'version' : '2.69.3', 'fancy_name' : 'glib2 lib' },
}
#
# rdp'S BUILD OF GLIB:
#
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

