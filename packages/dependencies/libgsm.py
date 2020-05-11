{
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://src.fedoraproject.org/repo/pkgs/gsm/gsm-1.0.18.tar.gz/sha512/c5b597f68d4a270e1d588f480dcde66fda8302564c687d753f2bd4fc41d246109243e567568da61eddce170f5232d869984743ddf1eea7696d673014a1a453b7/gsm-1.0.18.tar.gz',
		#	'hashes' : [ { 'type' : 'sha256', 'sum' : '04f68087c3348bf156b78d59f4d8aff545da7f6e14f33be8f47d33f4efae2a10' }, ],
		#},
		#{ 'url' : 'http://www.quut.com/gsm/gsm-1.0.18.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '04f68087c3348bf156b78d59f4d8aff545da7f6e14f33be8f47d33f4efae2a10' }, ], },
		{ 'url' : 'http://www.quut.com/gsm/gsm-1.0.19.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4903652f68a8c04d0041f0d19b1eb713ddcd2aa011c5e595b3b8bca2755270f6' }, ], },
		{ 'url' : 'https://ftp.openbsd.org/pub/OpenBSD/distfiles/gsm-1.0.19.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '4903652f68a8c04d0041f0d19b1eb713ddcd2aa011c5e595b3b8bca2755270f6' }, ], },
	],
	'folder_name' : 'gsm-1.0-pl18',
	'patches' : [
		('gsm/gsm-1.0.16.patch', '-p0'),
		('gsm/gsm-1.0.16_Makefile.patch', '-p0'), # toast fails. so lets just patch it out of the makefile..
	],
	'needs_configure' : False,
	'needs_make_install' : False,
	'run_post_build' : [
		'cp -fv lib/libgsm.a {target_prefix}/lib',
		'mkdir -pv {target_prefix}/include/gsm',
		'cp -fv inc/gsm.h {target_prefix}/include/gsm',
	],
	#'cpu_count' : '1',
	'build_options' : '{make_prefix_options} INSTALL_ROOT={target_prefix}',
	'update_check' : { 'url' : 'http://www.quut.com/gsm', 'type' : 'httpregex', 'regex' : r'<a href="http:\/\/www.quut.com/gsm/gsm-(?P<version_num>[\d.]+)\.tar\.gz">sourcecode<\/a>' },
	'_info' : { 'version' : '1.0.19', 'fancy_name' : 'gsm' },
}
