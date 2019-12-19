{
	'repo_type' : 'git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	#'url' : 'http://git.tukaani.org/xz.git',
	'custom_cflag' : '-D_FORTIFY_SOURCE=2', # 2019.12.13 it fails to build with anythinf other than this, eg it crashes with -O3 and -fstack-protector-all
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc', # 2019.12.13 --disable-shared --enable-static
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'xz' },
}
# 2019.12.13 old:
#	'xz' : { #lzma
#		'repo_type' : 'git',
#		'url' : 'https://github.com/xz-mirror/xz.git',
#		#'url' : 'http://git.tukaani.org/xz.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'xz' },
#	},
