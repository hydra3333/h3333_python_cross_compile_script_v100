{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/harfbuzz-2.6.4.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '9413b8d96132d699687ef914ebb8c50440efc87b3f775d25856d7ec347c03c12' }, ], },
	],
	'folder_name' : 'harfbuzz-with-freetype',
	'rename_folder' : 'harfbuzz-with-freetype',
	#'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-shared=no --enable-static=yes --with-freetype --with-fontconfig=no --with-icu=no --with-glib=no --with-gobject=no --disable-gtk-doc-html',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-shared=no --enable-static=yes --with-freetype --with-fontconfig=no --with-icu=no --with-glib=yes --with-gobject=no --disable-gtk-doc-html', # 2019.12.13
	'run_post_install' : [ # 2019.12.13
		'sed -i.bak \'s/Libs: -L${{libdir}} -lharfbuzz.*/Libs: -L${{libdir}} -lharfbuzz -lfreetype/\' "{pkg_config_path}/harfbuzz.pc"',
	],
	'depends_on': [
		'glib2', 'freetype_lib', # 2019.12.13 added these 2 dependencies, renamed libglib2 to glib to accord with deadsix27
	],
    'update_check' : { 'url' : 'https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'harfbuzz-(?P<version_num>[\d.]+)\.tar\.bz2' },
	'_info' : { 'version' : '2.6.4', 'fancy_name' : 'harfbuzz (with freetype2)' },
}
