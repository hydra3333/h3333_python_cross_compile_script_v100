{
	'repo_type' : 'git',
	'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608',
	'url' : 'https://github.com/file/file.git',
	'rename_folder' : 'libfile_local.git',
	'configure_options' : '--prefix={target_prefix} --disable-shared --enable-static --enable-fsect-man5',
	'needs_make' : False,
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_patch' : [ 'autoreconf -fiv' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : None, 'fancy_name' : 'libfile (bootstrap)' },
}
#{
#	'repo_type' : 'git',
#	'url' : 'https://github.com/file/file.git',
#	'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608',
#	#'branch' : '4020d6819dd155ab2780ce6daa9e18e76621a190',
#	'depth_git' : 0,	
#	'rename_folder' : 'libfile_local.git',
#	'patches' : [
#		( 'libfile/file-win32.patch', '-p1' ),
#	],
#	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-fsect-man5',
#	'needs_make' : False,
#	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
#	'run_post_patch' : [ 
#		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',
#		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c',
#		'autoreconf -fiv' ],
#	'depends_on' : [ 'mingw-libgnurx', ],
#	'update_check' : { 'type' : 'git', },
#	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libfile_local (bootstrap)' },
#}
#
# 2019.12.13 old:
#	'libfile_local' : { # the local variant is for bootstrapping, please make sure to always keep both at the same commit, otherwise it could fail.
#		'repo_type' : 'git',
#		#'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608', #'bf8b5f2cf7ce59ae2170e7f2fb026182c4dddcdc', # '4091ea8660a4355b0379564dc901e06bdcdc8c50', #'42d9a8a34607e8b0336b4c354cd5e7e7692bfec7',
#		'url' : 'https://github.com/file/file.git',
#		'rename_folder' : 'libfile_local.git',
#		'configure_options' : '--prefix={target_prefix} --disable-shared --enable-static --enable-fsect-man5',
#		'needs_make' : False,
#		'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
#		'run_post_patch' : [ 'autoreconf -fiv' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libfile (bootstrap)' },
#	},
