{ # 2019.12.13 use holywu fork of L-SMASH-Works
		'repo_type' : 'git',
		'url' : 'https://github.com/HolyWu/L-SMASH-Works.git', # 2019.11.19 swap to HolyWu's fork as it seems more updated
		'depth_git' : 0,
		#'branch' : '86f757d4096de3abdd1970202dc33fbaa8c8b640',
		'source_subfolder' : 'VapourSynth',
		'env_exports' : {
			'PKGCONFIG' : 'pkg-config',
		},
		'conf_system' : 'meson',
		'build_system' : 'ninja',
		'source_subfolder' : 'VapourSynth/build', # 'VapourSynth', # 'build',
		'configure_options' :
			'--prefix={target_prefix} '
			'--libdir={target_prefix}/lib '
			#'--extra-libs="-lssp" '
			'-D__USE_MINGW_ANSI_STDIO=1 '
			'--default-library=static '
			'--backend=ninja '
			'--buildtype=release '
			'--cross-file={meson_env_file} ./ ..'
		,
		'depends_on' : ['libffmpeg', 'libl-smash'],
		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'liblsw' },
}