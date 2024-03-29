{
	'repo_type' : 'git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	'depth_git' : 0,
	#'url' : 'http://git.tukaani.org/xz.git',
	'custom_cflag' : ' -D_FORTIFY_SOURCE=2 ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all
	#'custom_cflag' : ' -O2 -D_FORTIFY_SOURCE=2 ',  # 2022.12.18 per DEADSIX27
	'run_post_regexreplace' : [
		'pwd ; autoreconf -fiv ; pwd', # autoreconf is almost identical to ./autogen.sh
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-assembler --disable-debug --disable-small ' # --enable-threads=posix
							'--disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc '
							'--disable-lzma-links --disable-scripts '
	,
	'depends_on' : [ 'iconv', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'xz' },
}
