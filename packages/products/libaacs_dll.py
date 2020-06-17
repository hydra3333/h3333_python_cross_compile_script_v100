{ # 2019.12.13 # http://code.videolan.org/?p=libaacs.git # https://vlc-bluray.whoknowsmy.name/
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818

	'repo_type' : 'git',
	'recursive_git' : True,
	#'url' : 'https://git.videolan.org/git/libaacs.git',
	'url' : 'https://code.videolan.org/videolan/libaacs.git',
	'depth_git' : 0, # 2019.12.13 otherwise too shallow for the specfified commit to fetch
	# 'branch' : 'f263376b1e6570556031f420b9df08373e346d76', # 2020.03.19 try latest GIT instead of this branch # f263376b1e6570556031f420b9df08373e346d76 works for combo libaacs/libgcrypt/libgpg_error
	'rename_folder' : 'libaacs_dll_git',
	#'configure_options': '--host={target_host} --prefix={target_prefix} --with-libgcrypt-prefix={target_prefix} --with-gpg-error-prefix={target_prefix} --disable-shared --enable-static',
	'configure_options': '--host={target_host} --prefix={output_prefix}/libaacs_dll_git.installed --with-libgcrypt-prefix={output_prefix}/libaacs_dll_git.installed --with-gpg-error-prefix={output_prefix}/libaacs_dll_git.installed ',
	'run_post_regexreplace' : (
		#'autoreconf -fiv',
	),
	'run_post_install' : (
		'strip -s {output_prefix}/libaacs_dll_git.installed/bin/libaacs-0.dll',
		'strip -s {output_prefix}/libaacs_dll_git.installed/bin/libgcrypt-20.dll',
		'strip -s {output_prefix}/libaacs_dll_git.installed/bin/libgpg-error-0.dll',
	),
	'depends_on' : (
		'libgcrypt_for_libaacs', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libbaacs for libbluray' },
}
