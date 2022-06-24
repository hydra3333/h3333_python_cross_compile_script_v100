{
	'repo_type' : 'git',
	'url' : 'https://github.com/sekrit-twc/zimg.git',
	'branch' : 'c9a15ec4f86adfef6c7cede8dae79762d34f2564', # 2022.06.24 per MABS, commits after ths one break, cpuinfo broken
	'patches' : [
		('zimg/0001-libm_wrapper-define-__CRT__NO_INLINE-before-math.h-from-MABS.patch', '-Np1' ), # 2020.11.07 from MABS per https://github.com/m-ab-s/media-autobuild_suite/commit/e57877f87abf1a07b79284de257e3cad6bbf7409#diff-adfad29200df8b40f03fd8670a191195ff4f98c0160a7b12ada8caa8cb824c75
	],
	'run_post_patch' : [
		#'autoreconf -fiv', # 2020.11.07 from MABS 
		'sh ./autogen.sh',
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --enable-x86simd -disable-testapp --disable-example --disable-unit-test --disable-debug', # 2019.12.13
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'zimg' },
}
