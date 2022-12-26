{
	'repo_type' : 'git',
	'url' : 'https://github.com/mstorsjo/fdk-aac.git',
	# Note does not like to be compiled without optimisations: error: inlining failed in call to always_inline 'void fft_4(FIXP_DBL*)': indirect function call with a yet undetermined callee
	# So make sure to empty the cflags or enable optimisations when your global c(xx)flags are defaulting to -0g/0:
	# 'custom_cflag': '',
	#'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13
	#'run_post_regexreplace' : [
	#	'autoreconf -fiv',
	#],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'run_post_regexreplace' : [
		'pwd ; cd .. ; sh ./autogen.sh ; cd _build ; pwd',
	],
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_INSTALL_LIBDIR={target_prefix}/lib -DBUILD_SHARED_LIBS=OFF -DBUILD_PROGRAMS=OFF -DCMAKE_BUILD_TYPE=Release',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'fdk-aac' },
}

