{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/speexdsp.git',
	'run_post_patch' : [ 'autoreconf -fiv', ],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static',
	'_info' : { 'version' : None, 'fancy_name' : 'speexdsp' },
}