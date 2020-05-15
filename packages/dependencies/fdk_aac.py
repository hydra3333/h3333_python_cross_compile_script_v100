{
	'repo_type' : 'git',
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'url' : 'https://github.com/mstorsjo/fdk-aac.git',
	# Note does not like to be compiled without optimisations: error: inlining failed in call to always_inline 'void fft_4(FIXP_DBL*)': indirect function call with a yet undetermined callee
	# So make sure to empty the cflags or enable optimisations when your global c(xx)flags are defaulting to -0g/0:
	# 'custom_cflag': '',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'fdk-aac' },
}
