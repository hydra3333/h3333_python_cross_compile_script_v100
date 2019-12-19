{
	'repo_type' : 'git',
	'url' : 'https://github.com/sekrit-twc/zimg.git',
	#'branch' : 'd0f9cdebd34b0cb032f79357660bd0f6f23069ee', # '3aae2066e5b8df328866ba7e8636d8901f42e8e7',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-x86simd', # 2019.12.13
	'_info' : { 'version' : None, 'fancy_name' : 'zimg' },
}
# 2019.12.13 old:
#	'libzimg' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/sekrit-twc/zimg.git',
#		#'branch' : 'd0f9cdebd34b0cb032f79357660bd0f6f23069ee', # '3aae2066e5b8df328866ba7e8636d8901f42e8e7',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-x86simd', # 2018.11.23 added --enable-x86simd per Alexpux
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zimg' },
#	},