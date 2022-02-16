{
	'repo_type' : 'git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	'depth_git' : 0,
	'branch' : 'f7711d228c3c32395460c82498c60a9f730d0239', # '6468f7e41a8e9c611e4ba8d34e2175c5dacdbeb4',
	#'url' : 'http://git.tukaani.org/xz.git',
	'custom_cflag' : '-D_FORTIFY_SOURCE=2', # 2019.12.13 it fails to build with anythinf other than this, eg it crashes with -O3 and -fstack-protector-all
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc', # 2019.12.13 --disable-shared --enable-static
	'depends_on' : [ 'iconv', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'xz' },
}
