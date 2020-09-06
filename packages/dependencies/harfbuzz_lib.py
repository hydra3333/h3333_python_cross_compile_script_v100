{ # 2020.04.10 NOT USED
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/archive/2.7.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e95ee43b6bd0d3d1307e2aacf0f9c0050e5baceb21988b367b833028114aa569' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.7.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e95ee43b6bd0d3d1307e2aacf0f9c0050e5baceb21988b367b833028114aa569' }, ], }, # https://fossies.org/linux/misc/
		{ 'url' : 'https://github.com/harfbuzz/harfbuzz/archive/2.7.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b8c048d7c2964a12f2c80deb6634dfc836b603dd12bf0d0a3df1627698e220ce' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.7.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b8c048d7c2964a12f2c80deb6634dfc836b603dd12bf0d0a3df1627698e220ce' }, ], }, # https://fossies.org/linux/misc/
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
	'_info' : { 'version' : '2.7.1', 'fancy_name' : 'harfbuzz' },
}

