{ # 2019.12.13 # http://code.videolan.org/?p=libaacs.git # https://vlc-bluray.whoknowsmy.name/
  # 2020.06.20 https://code.videolan.org/videolan/libaacs browse here
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'https://code.videolan.org/videolan/libaacs.git',
	'depth_git' : 0, # 2019.12.13 otherwise too shallow for the specfified commit to fetch
	#'branch' : '9bceea3f0a022010aa15e898bbb1d47f2af45052', # 2020.03.19 try latest GIT instead of this branch # f263376b1e6570556031f420b9df08373e346d76 works for combo libaacs/libgcrypt/libgpg_error
	'rename_folder' : 'libaacs_git',
	'custom_ldflag' : ' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -L{target_prefix}/lib ',
	'configure_options': '--host={target_host} --prefix={target_prefix} --with-libgcrypt-prefix={target_prefix} --with-gpg-error-prefix={target_prefix} --disable-shared --enable-static',
	'run_post_regexreplace' : (
		'autoreconf -fiv',
	),
	'depends_on' : (
		'libgcrypt', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libbaacs for libbluray' },
}
