{
	'repo_type' : 'git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	#'patches' :	[ # removed per deadsix27, patch was merged upstream
	#	( 'https://github.com/lu-zero/mfx_dispatch/pull/70.patch', '-p1' ),
	#],
	'url' : 'https://github.com/lu-zero/mfx_dispatch.git',
	'url' : 'https://github.com/lu-zero/mfx_dispatch.git',
	'configure_options' : '{autoconf_prefix_options}  --disable-shared --enable-static --without-libva_drm --without-libva_x11',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'intel_quicksync_mfx' },
}
