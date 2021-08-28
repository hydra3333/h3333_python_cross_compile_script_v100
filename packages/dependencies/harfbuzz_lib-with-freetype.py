{
	'repo_type' : 'archive', # https://fossies.org/linux/misc/
	'download_locations' : [
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/2.7.2/harfbuzz-2.7.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b8c048d7c2964a12f2c80deb6634dfc836b603dd12bf0d0a3df1627698e220ce' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.7.2.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b8c048d7c2964a12f2c80deb6634dfc836b603dd12bf0d0a3df1627698e220ce' }, ], }, # https://fossies.org/linux/misc/
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/2.7.4/harfbuzz-2.7.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6ad11d653347bd25d8317589df4e431a2de372c0cf9be3543368e07ec23bb8e7' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.7.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '6ad11d653347bd25d8317589df4e431a2de372c0cf9be3543368e07ec23bb8e7' }, ], }, # https://fossies.org/linux/misc/
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/2.8.1/harfbuzz-2.8.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4124f663ec4bf4e294d9cf230668370b4249a48ff34deaf0f06e8fc82d891300' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.8.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4124f663ec4bf4e294d9cf230668370b4249a48ff34deaf0f06e8fc82d891300' }, ], }, # https://fossies.org/linux/misc/
        { 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/2.9.0/harfbuzz-2.9.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3e1c2e1d2c65d56364fd16d1c41a06b2a35795496f78dfff635c2b7414b54c5a' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.9.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3e1c2e1d2c65d56364fd16d1c41a06b2a35795496f78dfff635c2b7414b54c5a' }, ], }, # https://fossies.org/linux/misc/
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
	'_info' : { 'version' : '2.9.0', 'fancy_name' : 'harfbuzz (with freetype2)' },
}
