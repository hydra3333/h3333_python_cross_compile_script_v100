{ # https://fossies.org/linux/misc/
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/4.4.1/harfbuzz-4.4.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c5bc33ac099b2e52f01d27cde21cee4281b9d5bfec7684135e268512478bc9ee' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-4.4.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c5bc33ac099b2e52f01d27cde21cee4281b9d5bfec7684135e268512478bc9ee' }, ], }, # https://fossies.org/linux/misc/
		{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/5.1.0/harfbuzz-5.1.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2edb95db668781aaa8d60959d21be2ff80085f31b12053cdd660d9a50ce84f05' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-5.1.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '2edb95db668781aaa8d60959d21be2ff80085f31b12053cdd660d9a50ce84f05' }, ], }, # https://fossies.org/linux/misc/
	],
	'folder_name' : 'harfbuzz-lib',
	'rename_folder' : 'harfbuzz-lib',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DHB_HAVE_FREETYPE=OFF '
		'-DHB_HAVE_ICU=OFF '
		'-DHB_HAVE_GLIB=OFF '
		'-DHB_BUILD_TESTS=OFF '
	,
	# 'configure_options' : '{autoconf_prefix_options} --without-freetype --with-fontconfig=no --with-icu=no --with-glib=no --with-gobject=no --disable-gtk-doc-html', #--with-graphite2 --with-cairo --with-icu --with-gobject
	'run_post_install' : [
		"echo 'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include/harfbuzz\nName: harfbuzz\nDescription: HarfBuzz text shaping library\nVersion:\nLibs: -L${{libdir}} -lharfbuzz\nCflags: -I${{includedir}}/harfbuzz' > {target_prefix}/lib/pkgconfig/harfbuzz.pc",
	],
	'update_check' : { 'url' : 'https://github.com/harfbuzz/harfbuzz/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	#'update_check' : { 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'harfbuzz-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '5.1.0', 'fancy_name' : 'harfbuzz' },
}

