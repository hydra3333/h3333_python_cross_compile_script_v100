{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=summary
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://fossies.org/linux/misc/libgcrypt-1.10.1.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ef14ae546b0084cd84259f61a55e07a38c3b53afc0f546bffcef2f01baffe9de' }, ], },
	#],
	'repo_type' : 'git',
	'recursive_git' : True,
	'depth_git' : 0,
	'url' : 'git://git.gnupg.org/libgcrypt.git',
	#'url' : 'https://git.gnupg.org/source/libgcrypt.git',
	##'branch' : 'tags/libgcrypt-1.10.1',  # 1.9.3 onward fails 2021.09.18 on commit d2b3d046fc66a3166dc0c003a430ce756532ff74
	'branch' : '833a904faf2b90a1b1d1b58e1e9a12f2e8e2378c', # 2023.02.23
	'rename_folder' : 'libgcrypt',
	'patches' : [
		#('libgcrypt/libgcrypt.patch', '-p1'),	# 2021.09.18 undo commit d2b3d046fc66a3166dc0c003a430ce756532ff74
		('libgcrypt/libgcrypt-2022.02.16.patch', '-p1'),	# 2022.02.16
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
	#'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libgcrypt for libaacs' },
	#'_info' : { 'version' : '1.10.1', 'fancy_name' : 'libgcrypt for libaacs' },
}
