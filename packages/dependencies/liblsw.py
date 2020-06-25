{ # 2019.12.13 use holywu fork of L-SMASH-Works
	'repo_type' : 'git',
	'url' : 'https://github.com/HolyWu/L-SMASH-Works.git', # 2019.11.19 swap to HolyWu's fork as it seems more updated
	'depth_git' : 0,
	#'branch' : 'a2fd2e0c625a33b2f1af356689f2091bb677c9e0', #'86f757d4096de3abdd1970202dc33fbaa8c8b640',
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'VapourSynth/build', # 'VapourSynth', # 'build',
	'run_post_regexreplace' : [
		#'ls -al',
		#'ls -al ..',
		'sed -i.BAK \'s;<VapourSynth.h>;"VapourSynth.h";g\' "../lsmashsource.h"',
		'sed -i.BAK "s;vapoursynth_dep =;includes = include_directories(\'../include\')\\n\\nvapoursynth_dep =;g" "../meson.build"',
		'sed -i.BAK \'s;dependencies : deps,;dependencies : deps,\\ninclude_directories : includes,;g\' "../meson.build"',
		#'sed -iBAK \'s;;;g\' "../"',
	],
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
	'depends_on' : ['vapoursynth_libs', 'libffmpeg_extra', 'libl-smash'],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'liblsw' },
}
