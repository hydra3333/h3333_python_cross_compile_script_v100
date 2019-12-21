{
	'repo_type' : 'git',
	'url' : 'https://github.com/file/file.git',
	'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608',
	#'branch' : '4020d6819dd155ab2780ce6daa9e18e76621a190',
	'depth_git' : 0,
	'rename_folder' : 'libfile.git',
	'patches' : [
		( 'libfile/file-win32.patch', '-p1' ),
	],
	'configure_options' : '{autoconf_prefix_options} -disable-shared --enable-static --enable-fsect-man5',
	'needs_make' : True,
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_patch' : [
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c',
		'autoreconf -fiv' 
	],
	'depends_on' : [ 'mingw-libgnurx', 'libfile_local' ],
	'flipped_path' : True,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'file' },
}
# 2019.12.13 old:
#	'libfile' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/file/file.git',
#		#'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608', #'bf8b5f2cf7ce59ae2170e7f2fb026182c4dddcdc', # 2019.10.04 commented out
#		'rename_folder' : 'libfile.git',
#		'patches' : [
#			( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/file-win32.patch', '-p1' ),
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-fsect-man5',
#		'depends_on' : [ 'mingw-libgnurx', 'libfile_local' ], # 2019.10.04 
#		'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
#		'run_post_patch' : [ 
#			'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c', # 2019.10.04
#			'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c', # 2019.10.04
#			'autoreconf -fiv' 
#		],
#		'flipped_path' : True,
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'file' },
#	},