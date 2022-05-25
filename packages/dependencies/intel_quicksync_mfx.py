{ #  # 2022.05.25 comment out intel_quicksync_mfx since ffmpeg quicksync no longer detects https://github.com/lu-zero/mfx_dispatch.git as valid.
	'repo_type' : 'git',
	'url' : 'https://github.com/lu-zero/mfx_dispatch.git',
	'do_not_bootstrap' : True,
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'configure_options' : '{autoconf_prefix_options}  --disable-shared --enable-static --without-libva_drm --without-libva_x11',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'intel_quicksync_mfx' },
}
