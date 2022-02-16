{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=summary # This DAMN thing fails to build with "versioninfo.rc.in:21: syntax error" if not built directly from a GIT clone
																									 
	#'repo_type' : 'archive',
	#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.3.tar.bz2',
	'repo_type' : 'git',
	'recursive_git' : True,
	'depth_git' : 0,
	'url' : 'git://git.gnupg.org/libgcrypt.git',
	##'branch' : 'tags/libgcrypt-1.9.2',  # 1.9.3 onward fails 2021.09.18 on commit d2b3d046fc66a3166dc0c003a430ce756532ff74
	#'branch' : '',
	'patches' : [
		#('libgcrypt/libgcrypt.patch', '-p1'),	# 2021.09.18 undo commit d2b3d046fc66a3166dc0c003a430ce756532ff74
		('libgcrypt-2022.02.16.patch', '-p1'),	# 2022.02.16
	],
	'custom_cflag' : ' {original_fortify_source_trim} ', # 2019.12.13 this does not like -O3 -fstack-protector-all ... use one or more of {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim}
	'run_post_regexreplace' : (
		'autoreconf -fiv', # https://dev.gnupg.org/T5696
		#'./autogen.sh --force --build-w64 --prefix={target_prefix}',	  # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=README.GIT;hb=HEAD https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=README;hb=HEAD
	),
	'configure_options': '--host={target_host} --prefix={target_prefix} --with-gpg-error-prefix={target_prefix} --disable-shared --enable-static --disable-doc --enable-threads=windows ', # --disable-asm 
	'depends_on' : (
		'libgpg_error', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libgcrypt for libaacs' },
}
