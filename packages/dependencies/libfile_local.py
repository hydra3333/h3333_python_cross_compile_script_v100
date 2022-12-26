{
	'repo_type' : 'git',
	'url' : 'https://github.com/file/file.git',
	#'depth_git' : 0,                 
	#'branch' : '3dc9066f0b59513951626d8596ea67e23a0fd42e', # 2022.12.18 per DEADSIX27 commented out
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
