{
	'repo_type' : 'git',
	'url' : 'https://github.com/file/file.git',
	'depth_git' : 0,
	#'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608',
	'rename_folder' : 'libfile.git',
	'patches' : [
		( 'libfile/file-win32.patch', '-p1' ),
	],
	'configure_options' : '{autoconf_prefix_options} -disable-shared --enable-static --enable-fsect-man5 --disable-silent-rules',
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_patch' : [ # ??? does this go into libfile_local instead ????????????????????????????
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',  # ??? does this go into libfile_local instead ????????????????????????????
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c', # ??? does this go into libfile_local instead ????????????????????????????
		'autoreconf -fiv' 
	],
	'flipped_path' : False, # normal cross-compiling
	'depends_on' : [ 'mingw-libgnurx', 'libfile_local' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'file' },
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
#
#AC_CONFIG_HEADERS([config.h])
#[  --disable-elf            disable builtin ELF support],
#[  --disable-elf-core       disable ELF core file support],
#[AS_HELP_STRING([--disable-zlib], [disable zlib compression support @<:@default=auto@:>@])])
#[AS_HELP_STRING([--disable-bzlib], [disable bz2lib compression support @<:@default=auto@:>@])])
#[AS_HELP_STRING([--disable-xzlib], [disable liblzma/xz compression support @<:@default=auto@:>@])])
#[AS_HELP_STRING([--disable-libseccomp], [disable libseccomp sandboxing @<:@default=auto@:>@])])
#[  --enable-fsect-man5      enable file formats in man section 5],
#[  --disable-warnings	disable compiler warnings],
#if test "$MINGW" = 1; then
#  AC_CHECK_LIB(gnurx,regexec,,AC_MSG_ERROR([libgnurx is required to build file(1) with MinGW]))
#fi