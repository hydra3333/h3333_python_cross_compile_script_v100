{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=summary # This DAMN thing fails to build with "versioninfo.rc.in:21: syntax error" if not built directly from a GIT clone
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818
	#'repo_type' : 'archive',
	#'url' : 'https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.3.tar.bz2',
	'repo_type' : 'git',
	'recursive_git' : True,
	'depth_git' : 0, # 2019.12.13 otherwise too shallow for the specfified commit to fetch
	'url' : 'git://git.gnupg.org/libgcrypt.git',
	#'branch' : 'tags/libgcrypt-1.9.2',  # 1.9.3 onward fails 2021.09.18 on commit d2b3d046fc66a3166dc0c003a430ce756532ff74
	'branch' : '5e0187d84fc16d9ff0fbb0ccd4348657fea90d36',  # works: '5e0187d84fc16d9ff0fbb0ccd4348657fea90d36' breaks on and after: '3bacdac611b9eb3bd5ae8d78156b1110e77e9518'
	'rename_folder' : 'libgcrypt_for_aacs_git',
	'patches' : [
		('libgcrypt/libgcrypt.patch', '-p1'),   # 2021.09.18 undo commit d2b3d046fc66a3166dc0c003a430ce756532ff74
	],
	'configure_options': '--host={target_host} --prefix={output_prefix}/libaacs_dll_git.installed --with-gpg-error-prefix={output_prefix}/libaacs_dll_git.installed --disable-doc --enable-threads=windows ', # --disable-asm 
	'custom_cflag' : ' {original_fortify_source_trim} ', # 2019.12.13 this does not like -O3 -fstack-protector-all ... use one or more of {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim}
	'run_post_regexreplace' : (
		'autoreconf -fiv', # https://dev.gnupg.org/T5696
		#'./autogen.sh --force --build-w64',     # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=README.GIT;hb=HEAD https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=README;hb=HEAD
	),
	'depends_on' : (
		'libgpg_error_for_libaacs', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libgcrypt for libaacs' },
}
