{
	'repo_type' : 'git',
	'url' : 'https://github.com/file/file.git',
	'depth_git' : 0,
	#'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608', # 2020.03.19 try latest git. 24c9c086cd7c55b7b0a003a145b32466468e2608 works
	'rename_folder' : 'libfile.git',
	'patches' : [
		( 'libfile/file-win32.patch', '-p1' ),
	],
	'configure_options' : '{autoconf_prefix_options} -disable-shared --enable-static --enable-fsect-man5 --disable-silent-rules',
	'depends_on' : [ 'mingw-libgnurx', 'libfile_local' ], # 2020.03.19 added 'libfile_local'
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_regexreplace' : [
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c',
		'autoreconf -fiv' 
	],
	'flipped_path' : True,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'file' },
}
