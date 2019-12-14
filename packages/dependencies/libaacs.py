{ # 2019.12.13 # http://code.videolan.org/?p=libaacs.git # https://vlc-bluray.whoknowsmy.name/
	'repo_type' : 'git',
	'recursive_git' : True,
	#'url' : 'https://git.videolan.org/git/libaacs.git',
	'url' : 'https://code.videolan.org/videolan/libaacs.git',
	'branch' : 'f263376b1e6570556031f420b9df08373e346d76', # works for combo libaacs/libgcrypt/libgpg_error
	'configure_options': '--host={target_host} --prefix={target_prefix} --with-libgcrypt-prefix={target_prefix} --with-gpg-error-prefix={target_prefix} --disable-shared --enable-static',
	'run_post_patch' : (
		'autoreconf -fiv',
	),
	'depends_on' : (
		'libgcrypt', 
	),
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libbaacs for libbluray' },
}