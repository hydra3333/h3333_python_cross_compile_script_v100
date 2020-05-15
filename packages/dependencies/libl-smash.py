{ # used by liblsw and in turn product x264
		'repo_type' : 'git',
		'url' : 'https://github.com/hydra3333/l-smash', # 2019.12.13 mine is patched #'https://github.com/l-smash/l-smash.git',
		'env_exports' : {
			'PKGCONFIG' : 'pkg-config',
		},
		'configure_options':
			'--prefix={target_prefix} '
			'--cross-prefix={cross_prefix_bare} '
			'--extra-libs="-lssp" ' 
		,
		'build_options': 'install-lib',
		'update_check' : { 'type' : 'git', },
		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libl-smash' },
}
