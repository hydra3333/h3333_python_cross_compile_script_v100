{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=summary # This DAMN thing fails to build with "versioninfo.rc.in:21: syntax error" if not built directly from a GIT clone
	#'repo_type' : 'archive',
	#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.3.tar.bz2',
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'git://git.gnupg.org/libgcrypt.git',
	'branch' : '7c2943309d14407b51c8166c4dcecb56a3628567', # 2019.08.21 see if 900647d96cb7806cd9b2de343e4a4bd66c073fba reverts a build error
	'configure_options': '--host={target_host} --prefix={target_prefix} --with-gpg-error-prefix={target_prefix} --disable-shared --enable-static --disable-doc ',
	'run_post_patch' : (
		#'./autogen.sh --find-version',
		'autoreconf -fiv',
	),
	'depends_on' : (
		'libgpg_error', 
	),
	'_info' : { 'version' : 'git master', 'fancy_name' : 'libgcrypt for libaacs' },
}