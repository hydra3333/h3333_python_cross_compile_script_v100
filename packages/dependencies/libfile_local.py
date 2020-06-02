{
	'repo_type' : 'git',
	'depth_git' : 0,
	'branch' : 'd33b9a8d633c76878168bb85f5c993af36e52e58', # 2020.06.02
	'url' : 'https://github.com/file/file.git',
	'rename_folder' : 'libfile_local.git',
	'configure_options' : '--prefix={target_prefix} --disable-shared --enable-static --enable-fsect-man5 --disable-silent-rules',
	'needs_make' : False,
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_regexreplace' : [
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c',
		'autoreconf -fiv' 
	],
	'depends_on' : [ 'mingw-libgnurx', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libfile (bootstrap)' },
}
