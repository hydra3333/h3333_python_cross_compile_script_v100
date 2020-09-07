{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://github.com/harfbuzz/harfbuzz/archive/2.7.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e95ee43b6bd0d3d1307e2aacf0f9c0050e5baceb21988b367b833028114aa569' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.7.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'e95ee43b6bd0d3d1307e2aacf0f9c0050e5baceb21988b367b833028114aa569' }, ], }, # https://fossies.org/linux/misc/
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/archive/2.7.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b8c048d7c2964a12f2c80deb6634dfc836b603dd12bf0d0a3df1627698e220ce' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.7.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b8c048d7c2964a12f2c80deb6634dfc836b603dd12bf0d0a3df1627698e220ce' }, ], }, # https://fossies.org/linux/misc/
	],
	# 'run_post_install' : [
		# 'sed -i.bak \'s/Libs: -L${{libdir}} -lharfbuzz.*/Libs: -L${{libdir}} -lharfbuzz -lfreetype/\' "{pkg_config_path}/harfbuzz.pc"',
	# ],
	'folder_name' : 'harfbuzz-with-freetype',
	'rename_folder' : 'harfbuzz-with-freetype',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DHB_HAVE_FREETYPE=ON '
		'-DHB_HAVE_ICU=OFF '
		'-DHB_HAVE_GLIB=OFF '
		'-DHB_BUILD_TESTS=OFF '
	,
	'run_post_install' : [
		#"echo 'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include\nName: harfbuzz\nDescription: HarfBuzz text shaping library\nVersion:\nLibs: -L${{libdir}} -lharfbuzz\nRequires: freetype2\nCflags: -I${{includedir}}/harfbuzz' > {target_prefix}/lib/pkgconfig/harfbuzz.pc",
		"echo 'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include\nName: harfbuzz\nDescription: HarfBuzz text shaping library\nVersion: 2.6.4\nLibs: -L${{libdir}} -lharfbuzz\nRequires: freetype2\nCflags: -I${{includedir}}/harfbuzz' > {target_prefix}/lib/pkgconfig/harfbuzz.pc",
	],
	'update_check' : { 'url' : 'https://github.com/harfbuzz/harfbuzz/releases', 'type' : 'githubreleases', 'name_or_tag' : 'name' },
	#'update_check' : { 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'harfbuzz-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '2.7.1', 'fancy_name' : 'harfbuzz (with freetype2)' },
	#'_info' : { 'version' : '2.7.2', 'fancy_name' : 'harfbuzz (with freetype2)' },
}
