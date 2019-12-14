{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
		#'repo_type' : 'archive',
		#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.32.tar.bz2',
		'repo_type' : 'git',
		'recursive_git' : True,
		'url' : 'git://git.gnupg.org/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
		#'branch' : 'a5d4a4b32b11814d673241d62624ecec1d577571', # 2018.12.10 commented out # (A) works for combo libaacs/libgcrypt/libgpg_error # the commit after this broke it 2018.11.28
		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-rpath --disable-doc --disable-tests --with-libiconv-prefix={target_prefix}', # --with-libintl=no --with-libpth=no',
		'run_post_patch' : (
			#'./autogen.sh --force --build-w64 --host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-rpath --disable-doc --disable-tests --with-libiconv-prefix={target_prefix};, # --with-libintl=no --with-libpth=no',
			#'./autogen.sh --find-version',
			'autoreconf -fiv',
		),
		'depends_on' : (
			'iconv', 
		),
		'_info' : { 'version' : 'git master', 'fancy_name' : 'libgpg-error for libaacs' },
}