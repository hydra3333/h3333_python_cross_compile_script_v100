{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=summary # This DAMN thing fails to build with "versioninfo.rc.in:21: syntax error" if not built directly from a GIT clone
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818

	#'repo_type' : 'archive',
	#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.3.tar.bz2',
	'repo_type' : 'git',
	'recursive_git' : True,
	'depth_git' : 0, # 2019.12.13 otherwise too shallow for the specfified commit to fetch
	'url' : 'git://git.gnupg.org/libgcrypt.git',
	#'branch' : '7c2943309d14407b51c8166c4dcecb56a3628567', # 2020.03.19 try git master # 7c2943309d14407b51c8166c4dcecb56a3628567 works with no errors
	'rename_folder' : 'libgcrypt_for_aacs_git',
	'configure_options': '--host={target_host} --prefix={output_prefix}/libaacs_dll_git.installed --with-gpg-error-prefix={output_prefix}/libaacs_dll_git.installed --enable-threads=windows --disable-asm --disable-doc ',
	'custom_cflag' : ' {original_fortify_source_trim} ', # 2019.12.13 this does not like -O3 -fstack-protector-all ... use one or more of {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim}
	'run_post_regexreplace' : (
		##'./autogen.sh --find-version',
		'autoreconf -fiv',
	),
	'depends_on' : (
		'libgpg_error_for_libaacs', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libgcrypt for libaacs' },
}
