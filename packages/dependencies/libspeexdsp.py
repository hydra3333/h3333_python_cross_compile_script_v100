{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/speexdsp.git',
	'run_post_regexreplace' : [ 'autoreconf -fiv', ],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'speexdsp' },
}
