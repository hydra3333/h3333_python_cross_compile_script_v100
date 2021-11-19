{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
	#'repo_type' : 'archive',
	#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.43.tar.bz2',
	#
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'git://git.gnupg.org/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
	##'url' : 'https://dev.gnupg.org/source/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
	#
	'custom_cflag' : ' ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all -D_FORTIFY_SOURCE=2 
	'run_post_regexreplace' : (
		'autoreconf -fiv', # https://dev.gnupg.org/T5696
		'./autogen.sh --force --build-w64 --prefix={target_prefix}', # -prefix={target_prefix},	# https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=README.GIT;hb=HEAD https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=README;hb=HEAD
	),
	'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-rpath --disable-doc --disable-tests --with-libiconv-prefix={target_prefix}', # --with-libintl=no --with-libpth=no',
	'depends_on' : (
		'iconv', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'libgpg-error for libaacs' },
}