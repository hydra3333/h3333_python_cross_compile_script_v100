{
	'repo_type' : 'git',
	'url' : 'git://git.ghostscript.com/mujs.git',
	'needs_configure' : False,
	'build_options' : '{make_prefix_options} prefix={target_prefix} HAVE_READLINE=no',
	'install_options' : '{make_prefix_options} prefix={target_prefix} HAVE_READLINE=no',
	'regex_replace': {
		'post_patch': [
			{
				0: r'install -m 755 \$\(OUT\)\/mujs',
				1: r'install -m 755 $(OUT)/mujs.exe',
				'in_file': 'Makefile'
			},
		],
		'post_install': [ # hardcode version because master builds use hashes and mpv checks for actual version, could probably edit the git describe command in the Makefile, but this will do.
			{
				0: r'^Version:([\n\r\s]+)?[^\n]+$',
				1: r'Version: 1.0.6',
				'in_file': '{pkg_config_path}/mujs.pc'
			},
		],
	},
	'_info' : { 'version' : None, 'fancy_name' : 'mujs' },
}
# 2020.01.10 was:
#{
#	'repo_type' : 'git',
#	'url' : 'git://git.ghostscript.com/mujs.git',
#	'needs_configure' : False,
#	'build_options' : '{make_prefix_options} prefix={target_prefix} HAVE_READLINE=no',
#	'install_options' : '{make_prefix_options} prefix={target_prefix} HAVE_READLINE=no',
#	'run_post_patch' : [
#		'sed -i.bak \'s/install -m 755 $(OUT)\/mujs $(DESTDIR)$(bindir)/install -m 755 $(OUT)\/mujs.exe $(DESTDIR)$(bindir)/g\' Makefile',
#	],
#	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'mujs' },
#}
