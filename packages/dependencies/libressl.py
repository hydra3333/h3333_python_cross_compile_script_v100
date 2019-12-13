{
	'repo_type' : 'git',
	'url' : 'https://github.com/libressl-portable/portable.git',
	'folder_name' : 'libressl_git',
	'configure_options' : '{autoconf_prefix_options} --disable-hardening',
	# 'patches' : [
		# ( 'https://raw.githubusercontent.com/shinchiro/mpv-winbuild-cmake/master/packages/libressl-0001-ignore-compiling-test-and-man-module.patch', '-p1' ),
		# ( 'https://raw.githubusercontent.com/shinchiro/mpv-winbuild-cmake/master/packages/libressl-0002-tls-revert-Add-tls-tls_keypair.c-commit.patch', '-p1' ),
		# ( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/patches/ressl/libressl-0001-rename-timegm-for-mingw-compat.patch', '-p1' ),
	# ],
	'_info' : { 'version' : None, 'fancy_name' : 'libressl' },
}
