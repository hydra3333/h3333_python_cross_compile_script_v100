{
	'repo_type' : 'git',
	'url' : 'https://github.com/file/file.git',
	'rename_folder' : 'libfile.git',
	'patches' : [
		( 'libfile/file-win32.patch', '-p1' ),
	],
	'configure_options' : '{autoconf_prefix_options} --enable-fsect-man5',
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_patch' : [
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c',
		'autoreconf -fiv' 
	],
	'depends_on' : [ 'mingw-libgnurx', 'libfile_local' ], # 2019.12.13
	'flipped_path' : True,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'file' },
}