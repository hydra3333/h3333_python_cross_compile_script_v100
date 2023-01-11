{
	'repo_type' : 'git',
	'url' : 'https://github.com/ArtifexSoftware/mujs.git', # this seems to be as up to date as #'url' : http://git.ghostscript.com/mujs.git
	'recursive_git' : True,
	'depth_git' : 0,
	'branch' : 'bb6a85a31c46f82577bacc1cc21d3c3b9df02b82', # 2023.01.11 see https://bugs.ghostscript.com/show_bug.cgi?id=706322
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
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : None, 'fancy_name' : 'mujs' },
}
