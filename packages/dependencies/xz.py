{
	'repo_type' : 'git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	#'url' : 'http://git.tukaani.org/xz.git',
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc', # 2019.12.13 --disable-shared --enable-static
	'_info' : { 'version' : None, 'fancy_name' : 'xz' },
}