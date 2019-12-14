{ # 2019.12.13 use holywu fork of L-SMASH-Works
		'repo_type' : 'git',
		#'url' : 'https://github.com/hydra3333/L-SMASH-Works', # 2018.11.27 updated vapoursynth.h # 'https://github.com/VFR-maniac/L-SMASH-Works.git',
		'url' : 'https://github.com/HolyWu/L-SMASH-Works.git', # 2019.11.19 swap to HolyWu's fork as it seems mroe updated
		'source_subfolder' : 'VapourSynth',
		'env_exports' : {
			'PKGCONFIG' : 'pkg-config',
			'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
			'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
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