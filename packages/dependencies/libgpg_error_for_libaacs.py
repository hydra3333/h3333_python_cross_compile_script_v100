{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818
		#'repo_type' : 'archive',
		#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.32.tar.bz2',
		'repo_type' : 'git',
		'recursive_git' : True,
		'url' : 'git://git.gnupg.org/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
		'rename_folder' : 'libgpg-error_for_aacs_git',
		'configure_options': '--host={target_host} --prefix={output_prefix}/libaacs_dll_git.installed --disable-rpath --disable-doc --disable-tests ', #--with-libiconv-prefix={target_prefix}', # --with-libintl=no --with-libpth=no',
		'custom_cflag' : ' ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all -D_FORTIFY_SOURCE=2 
		'run_post_regexreplace' : (
			'autoreconf -fiv',
			'./autogen.sh --build-w64 --prefix={output_prefix}/libaacs_dll_git.installed',
		),
		'depends_on' : (
			'iconv', 
		),
		'update_check' : { 'type' : 'git', },
		'_info' : { 'version' : 'git master', 'fancy_name' : 'libgpg-error for libaacs' },
}
