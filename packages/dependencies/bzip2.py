{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/bzip2-1.0.8.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269' }, ], },
	],
	'patches' : [
		('bzip2/bzip2-1.0.6-gcc8.patch', '-p0'),
	],
	'custom_cflag' : '{original_cflags}',
	'needs_configure' : False,
	'needs_make' : True,
	'needs_make_install' : False,
	'build_options' : '{make_prefix_options} libbz2.a bzip2 bzip2recover install',

	'update_check' : { 'url' : 'ftp://sourceware.org/pub/bzip2/', 'type' : 'ftpindex', 'regex' : r'bzip2-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.0.8', 'fancy_name' : 'BZip2 (library)' },
}
# 2019.12.13 old:
#	'bzip2' : { # ftp://sourceware.org/pub/bzip2/
#		'repo_type' : 'archive',
#		'download_locations' : [
#			{ "url" : "https://fossies.org/linux/misc/bzip2-1.0.8.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269" }, ], },
#		],
#		'patches' : (
#			#('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/bzip2/bzip2_cross_compile.diff', '-p0'),
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/bzip2/bzip2-1.0.6-gcc8.patch', '-p0'),
#		),
#		"needs_configure": False,
#		"needs_make": True,
#		"needs_make_install": False,
#		'build_options': '{make_prefix_options} libbz2.a bzip2 bzip2recover install',
#		'_info' : { 'version' : '1.0.8', 'fancy_name' : 'BZip2 (library)' },
#	},