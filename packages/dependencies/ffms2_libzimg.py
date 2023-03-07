{
	'repo_type' : 'git',
	'url' : 'https://github.com/sekrit-twc/zimg.git',
	'depth_git' : 0,
	'folder_name' : 'ffms2_zimg',
	'run_post_regexreplace' : [
		'git submodule update --init --recursive --remote ', # 2022.12.18 per DEADSIX27 try to add --remote
		'autoreconf -fiv', # 2020.11.07 from MABS 
	],
	'patches' : [
		('zimg/0001-libm_wrapper-define-__CRT__NO_INLINE-before-math.h-from-MABS.patch', '-Np1' ), # 2020.11.07 from MABS per https://github.com/m-ab-s/media-autobuild_suite/commit/e57877f87abf1a07b79284de257e3cad6bbf7409#diff-adfad29200df8b40f03fd8670a191195ff4f98c0160a7b12ada8caa8cb824c75
	],
	# was pre-2023.03.06:
	#'run_post_regexreplace' : [
	#	'git submodule update --init --recursive --remote ',
	#	#'sh ./autogen.sh',
	#	'autoreconf -fiv',
	#],
	#'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-x86simd -disable-testapp --disable-example --disable-unit-test --disable-debug', # 2019.12.13
	'configure_options' : '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --enable-shared --disable-static --enable-x86simd -disable-testapp --disable-example --disable-unit-test --disable-debug', # 2019.12.13
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zimg' },
}
