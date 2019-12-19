{
	'repo_type' : 'git',
	'url' : 'git://git.ghostscript.com/mujs.git',
	'needs_configure' : False,
	'build_options' : '{make_prefix_options} prefix={target_prefix} HAVE_READLINE=no',
	'install_options' : '{make_prefix_options} prefix={target_prefix} HAVE_READLINE=no',
	'run_post_patch' : [
		'sed -i.bak \'s/install -m 755 $(OUT)\/mujs $(DESTDIR)$(bindir)/install -m 755 $(OUT)\/mujs.exe $(DESTDIR)$(bindir)/g\' Makefile',
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mujs' },
}