{ # https://fossies.org/linux/misc/
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/2.9.0/harfbuzz-2.9.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3e1c2e1d2c65d56364fd16d1c41a06b2a35795496f78dfff635c2b7414b54c5a' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.9.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '3e1c2e1d2c65d56364fd16d1c41a06b2a35795496f78dfff635c2b7414b54c5a' }, ], }, # https://fossies.org/linux/misc/
		# 2022.05.06 hmm, 2.9.0 to 4.2.1 is a big jump, it may not work.
		{ 'url' : 'https://github.com/harfbuzz/harfbuzz/releases/download/4.2.1/harfbuzz-4.2.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'bd17916513829aeff961359a5ccebba6de2f4bf37a91faee3ac29c120e3d7ee1' }, ], }, # https://github.com/harfbuzz/harfbuzz/releases
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-4.2.1.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'bd17916513829aeff961359a5ccebba6de2f4bf37a91faee3ac29c120e3d7ee1' }, ], }, # https://fossies.org/linux/misc/
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
	#'_info' : { 'version' : '2.9.0', 'fancy_name' : 'harfbuzz (with freetype2)' },
	'_info' : { 'version' : '4.2.1', 'fancy_name' : 'harfbuzz (with freetype2)' },
}
