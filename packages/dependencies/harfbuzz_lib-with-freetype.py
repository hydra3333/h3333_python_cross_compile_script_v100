{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
		{ 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.7.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '49e481d06cdff97bf68d99fa26bdf785331f411614485d892ea4c78eb479b218' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.6.7.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '49e481d06cdff97bf68d99fa26bdf785331f411614485d892ea4c78eb479b218' }, ], },
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
	'update_check' : { 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'harfbuzz-(?P<version_num>[\d.]+)\.tar\.xz' },
	'_info' : { 'version' : '2.6.7', 'fancy_name' : 'harfbuzz (with freetype2)' },
}
