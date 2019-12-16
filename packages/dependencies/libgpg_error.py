{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
		#'repo_type' : 'archive',
		#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.32.tar.bz2',
		'repo_type' : 'git',
		'recursive_git' : True,
		'url' : 'git://git.gnupg.org/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-rpath --disable-doc --disable-tests --with-libiconv-prefix={target_prefix}', # --with-libintl=no --with-libpth=no',
		'custom_cflag' : ' -D_FORTIFY_SOURCE=2 ', # 2019.12.13 it fails to build with anythinf other than this, eg it crashes with -O3 and -fstack-protector-all
		'run_post_patch' : (
			'autoreconf -fiv',
		),
		'depends_on' : (
			'iconv', 
		),
		'_info' : { 'version' : 'git master', 'fancy_name' : 'libgpg-error for libaacs' },
}
# 2019.12.13 old:
#	'libgpg_error' : { # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
#		'repo_type' : 'git',
#		'recursive_git' : True,
#		'url' : 'git://git.gnupg.org/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-rpath --disable-doc --disable-tests --with-libiconv-prefix={target_prefix}', # --with-libintl=no --with-libpth=no',
#		'run_post_patch' : (
#			'autoreconf -fiv',
#		),
#		'depends_on' : (
#			'iconv', 
#		),
#		'_info' : { 'version' : 'git master', 'fancy_name' : 'libgpg-error for libaacs' },
#	},