{
	'repo_type' : 'git',
	'depth_git' : 0,
	'branch' : '24c9c086cd7c55b7b0a003a145b32466468e2608',
	'url' : 'https://github.com/file/file.git',
	'rename_folder' : 'libfile_local.git',
	'configure_options' : '--prefix={target_prefix} --disable-shared --enable-static --enable-fsect-man5 --disable-silent-rules',
	'needs_make' : False,
	'env_exports' : { 'TARGET_CFLAGS' : '{original_cflags}' },
	'run_post_patch' : [
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/seccomp.c',
		'sed -i.bak "s/#ifdef FIONREAD/#ifdef __linux__ /" src/compress.c',
		'autoreconf -fiv' 
	],
	'depends_on' : [ 'mingw-libgnurx', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git', 'fancy_name' : 'libfile (bootstrap)' },
}
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
