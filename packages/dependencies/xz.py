{
	'repo_type' : 'git',
	'url' : 'https://github.com/xz-mirror/xz.git',
	'depth_git' : 0,
	#'branch' : '6468f7e41a8e9c611e4ba8d34e2175c5dacdbeb4',
	#'url' : 'http://git.tukaani.org/xz.git',
	'custom_cflag' : ' -D_FORTIFY_SOURCE=2 ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all
	#'custom_cflag' : ' -O3 -fstack-protector-all -D_FORTIFY_SOURCE=2 ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all
	#'run_post_regexreplace' : [ # 
	'run_post_regexreplace' : [
		'pwd ; autoreconf -fiv ; pwd', # autoreconf is almost identical to ./autogen.sh
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-assembler --disable-debug --disable-small --enable-threads=posix '
							'--disable-xz --disable-xzdec --disable-lzmadec --disable-lzmainfo --disable-doc '
							'--disable-lzma-links --disable-scripts '
	,
	'depends_on' : [ 'iconv', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'xz' },
}
enable_option_checking
enable_debug
enable_encoders
enable_decoders
enable_match_finders
enable_checks
enable_external_sha256
enable_assembler
enable_small
enable_threads
enable_assume_ram
enable_xz
enable_xzdec
enable_lzmadec
enable_lzmainfo
enable_lzma_links
enable_scripts
enable_doc
enable_symbol_versions
enable_sandbox
enable_path_for_scripts
enable_silent_rules
enable_dependency_tracking
enable_shared
enable_static
with_pic
enable_fast_install
with_aix_soname
with_gnu_ld
with_sysroot
enable_libtool_lock
enable_nls
enable_rpath
with_libiconv_prefix
with_libintl_prefix
enable_largefile
enable_unaligned_access
enable_unsafe_type_punning