{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
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
		"echo 'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include\nName: harfbuzz\nDescription: HarfBuzz text shaping library\nVersion:\nLibs: -L${{libdir}} -lharfbuzz\nRequires: freetype2\nCflags: -I${{includedir}}/harfbuzz' > {target_prefix}/lib/pkgconfig/harfbuzz.pc",
	],
	# 'configure_options' : '{autoconf_prefix_options} --with-freetype --with-fontconfig=no --with-icu=no --with-glib=no --with-gobject=no --disable-gtk-doc-html',
	'update_check' : { 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'harfbuzz-(?P<version_num>[\d.]+)\.tar\.bz2' },
	'_info' : { 'version' : '2.6.4', 'fancy_name' : 'harfbuzz (with freetype2)' },
}
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
#		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
#	],
#	'folder_name' : 'harfbuzz-with-freetype',
#	'rename_folder' : 'harfbuzz-with-freetype',
#	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-shared=no --enable-static=yes --with-freetype --with-fontconfig=no --with-icu=no --with-glib=yes --with-gobject=no --disable-gtk-doc-html --enable-introspection', # 2019.12.13
#	'run_post_install' : [ # 2019.12.13
#		'sed -i.bak \'s/Libs: -L${{libdir}} -lharfbuzz.*/Libs: -L${{libdir}} -lharfbuzz -lfreetype/\' "{pkg_config_path}/harfbuzz.pc"',
#	],
#	'depends_on': [
#		'glib2', 'freetype_lib', # 2019.12.13 added these 2 dependencies, renamed libglib2 to glib to accord with deadsix27
#	],
#    'update_check' : { 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'harfbuzz-(?P<version_num>[\d.]+)\.tar\.bz2' },
#	'_info' : { 'version' : '2.6.4', 'fancy_name' : 'harfbuzz (with freetype2)' },
#}
# 2019.12.13 old:
#	'harfbuzz_lib-with-freetype' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D
#			{ "url" : "https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.4.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/harfbuzz-2.6.4.tar.xz", "hashes" : [ { "type" : "sha256", "sum" : "9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12" }, ], },
#	],
#		'folder_name' : 'harfbuzz-lib-with-freetype',
#		'rename_folder' : 'harfbuzz-lib-with-freetype',
#		'run_post_install': [
#			'sed -i.bak \'s/Libs: -L${{libdir}} -lharfbuzz.*/Libs: -L${{libdir}} -lharfbuzz -lfreetype/\' "{pkg_config_path}/harfbuzz.pc"',
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --with-freetype --with-fontconfig=no --disable-shared --enable-shared=no --enable-static=yes --enable-introspection --with-icu=no --with-glib=yes --with-gobject=no --disable-gtk-doc-html', # 3018.11.23
#		'depends_on': [
#			'libglib2', 'freetype_lib', # 2019.04.13 added 'freetype_lib'
#		],
#		'_info' : { 'version' : '2.6.4', 'fancy_name' : 'harfbuzz (with freetype2)' },
#	},
