{ # 2019.12.13 use holywu fork of L-SMASH-Works 
	'repo_type' : 'git',
	'url' : 'https://github.com/HolyWu/L-SMASH-Works.git', # 2019.11.19 swap to HolyWu's fork as it seems more updated
	'depth_git' : 0,
	#'branch' : 'ab66a24f255dc89c03eb955c1a996a12d9c7595a', # 2020.08.21 this commit works per https://github.com/HolyWu/L-SMASH-Works/issues/11 (space between 
	#'branch' : 'TAGS/20200728',
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'VapourSynth/build', # 'VapourSynth', # 'build',
	'run_post_regexreplace' : [
		#'ls -al',
		#'ls -al ..',
		'cp -fv "../lsmashsource.h" "../lsmashsource.h.old"',
		'sed -i.BAK \'s;<VapourSynth.h>;"VapourSynth.h";g\' "../lsmashsource.h"',
		'diff -U 5 "../lsmashsource.h.old" "../lsmashsource.h" && echo "NO difference" || echo "YES differences!"',
		'cp -fv "../meson.build" "../meson.build.old"',
		'sed -i.BAK "s;vapoursynth_dep =;includes = include_directories(\'../include\')\\n\\nvapoursynth_dep =;g" "../meson.build"',
		'sed -i.BAK \'s;dependencies: deps,;dependencies : deps,\\ninclude_directories : includes,;g\' "../meson.build"', # 2020.09.10 removed a space prior to : to fix an upstream commit
		'diff -U 5 "../meson.build.old" "../meson.build" && echo "NO difference" || echo "YES differences!"',
		'sleep 3',
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
