{
	#LDFLAGS='-lm'
	'repo_type' : 'svn',
	'url' : 'svn://svn.code.sf.net/p/xavs/code/trunk',
	'folder_name' : 'xavs_svn',
	'configure_options' : '{autoconf_prefix_options} --cross-prefix={cross_prefix_bare}',
	'run_post_install' : [
		'rm -f NUL', # uh???
	],
	'packages' : {
		'arch' : [ 'yasm' ],
	},
	'_info' : { 'version' : 'svn (master)', 'fancy_name' : 'xavs' },
}