{
	'repo_type' : 'archive',
	'folder_name' : 'mingw-libgnurx-2.5.1',
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/mingw/files/Other/UserContributed/regex/mingw-regex-2.5.1/mingw-libgnurx-2.5.1-src.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '7147b7f806ec3d007843b38e19f42a5b7c65894a57ffc297a76b0dcd5f675d76' }, ], },
	],
	'configure_options' : '{autoconf_prefix_options} ', # --disable-shared --enable-static --enable-fsect-man5 # static fixed by patches below
	'cpu_count' : '1', 
	'needs_make' : False,
	'needs_make_install' : False,
	'run_post_configure' : [
		'make -f Makefile.mingw-cross-env -j 1 TARGET={target_host} bin_PROGRAMS= sbin_PROGRAMS= noinst_PROGRAMS= install-static'
		#'{cross_prefix_bare}ranlib libregex.a'
		#'make -f "Makefile.mingw-cross-env" libgnurx.a V=1'
	],
	'patches' : [
		( 'libgnurx/mingw-libgnurx-static.patch', '-p1' ),
		( 'libgnurx/libgnurx-1-build-static-lib.patch', '-p1' ),
	],
	'update_check' : { 'url' : 'https://sourceforge.net/projects/mingw/files/Other/UserContributed/regex/', 'type' : 'sourceforge', 'regex' : r'mingw-regex-(?P<version_num>[\d.]+)', },
	'_info' : { 'version' : '2.5.1', 'fancy_name' : 'mingw-libgnurx' },
}
# 2019.12.13 old:
#	'mingw-libgnurx' : {
#		'repo_type' : 'archive',
#		'folder_name' : 'mingw-libgnurx-2.5.1',
#		'download_locations' : [
#			#UPDATECHECKS: https://sourceforge.net/projects/mingw/files/Other/UserContributed/regex/
#			{ "url" : "https://sourceforge.net/projects/mingw/files/Other/UserContributed/regex/mingw-regex-2.5.1/mingw-libgnurx-2.5.1-src.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "7147b7f806ec3d007843b38e19f42a5b7c65894a57ffc297a76b0dcd5f675d76" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix}', # --disable-shared --enable-static --enable-fsect-man5
#		'cpu_count' : '1', #...
#		'needs_make' : False,
#		'needs_make_install' : False,
#		'run_post_configure' : [
#			'make -f Makefile.mingw-cross-env -j 1 TARGET={target_host} bin_PROGRAMS= sbin_PROGRAMS= noinst_PROGRAMS= install-static'
#			#'{cross_prefix_bare}ranlib libregex.a'
#			#'make -f "Makefile.mingw-cross-env" libgnurx.a V=1'
#		],
#		'patches' : [
#			( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/mingw-libgnurx-static.patch', '-p1' ),
#			( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libgnurx-1-build-static-lib.patch', '-p1' ),
#		],
#		'_info' : { 'version' : '2.5.1', 'fancy_name' : 'mingw-libgnurx' },
#	},