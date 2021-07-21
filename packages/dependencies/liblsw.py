{
	'repo_type' : 'git',
	'url' : 'https://github.com/VFR-maniac/L-SMASH-Works.git', # no longer builds: 'https://github.com/HolyWu/L-SMASH-Works.git',
	'depth_git' : 0,
    'source_subfolder' : 'VapourSynth', # 'VapourSynth', # 'build',
	'env_exports' : {
		'PKGCONFIG' : 'pkg-config',
	},
	'run_post_regexreplace' : [
		#'ls -al',
		#'ls -al ..',
		'cp -fv "lsmashsource.h" "lsmashsource.h.old"',
		'sed -i.BAK \'s;<VapourSynth.h>;"VapourSynth.h";g\' "lsmashsource.h"',
		'diff -U 5 "lsmashsource.h.old" "lsmashsource.h" && echo "NO difference" || echo "YES differences!"',
		#'cp -fv "../meson.build" "../meson.build.old"',
		#'sed -i.BAK "s;vapoursynth_dep =;includes = include_directories(\'../include\')\\n\\nvapoursynth_dep =;g" "../meson.build"',
		#'sed -i.BAK \'s;dependencies : deps,;dependencies : deps,\\ninclude_directories : includes,;g\' "../meson.build"', # 2020.09.10 prior to : to fix an upstream commit - in case we change commit brancges
		#'sed -i.BAK \'s;dependencies: deps,;dependencies: deps,\\ninclude_directories : includes,;g\' "../meson.build"',   # 2020.09.10 removed a space prior to : to fix an upstream commit
		#'diff -U 5 "../meson.build.old" "../meson.build" && echo "NO difference" || echo "YES differences!"',
		'sleep 3',
	],
    #'custom_ldflag' : ' -O3 -fno-stack-protector -D_FORTIFY_SOURCE=0 -lssp ', 
    #'custom_cflag'  : ' -O3 -fno-stack-protector -D_FORTIFY_SOURCE=0 -lssp ', 
	'configure_options' : '--prefix={target_prefix} --cross-prefix={cross_prefix_bare} --target-os=mingw --extra-cflags=" -lssp " --extra-ldflags==" -lssp ', # --disable-shared --enable-static
	'depends_on' : ['vapoursynth_libs', 'libffmpeg_extra', 'libl-smash'],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'liblsw (VFR-maniac)' },
}
#
#build_lsw() {
#   # Build L-Smash-Works, which are plugins based on lsmash
#   #build_ffmpeg static # dependency, assume already built
#   build_lsmash # dependency
#   do_git_checkout https://github.com/VFR-maniac/L-SMASH-Works.git lsw
#   cd lsw/VapourSynth
#     do_configure "--prefix=$mingw_w64_x86_64_prefix --cross-prefix=$cross_prefix --target-os=mingw"
#     do_make_and_make_install
#     # AviUtl is 32bit-only
#     if [ "$bits_target" = "32" ]; then
#       cd ../AviUtl
#       do_configure "--prefix=$mingw_w64_x86_64_prefix --cross-prefix=$cross_prefix"
#       do_make
#     fi
#   cd ../..
#}
#
#
#
#{ # 2019.12.13 use holywu fork of L-SMASH-Works 
#	'repo_type' : 'git',
#	'url' : 'https://github.com/HolyWu/L-SMASH-Works.git', # 2019.11.19 swap to HolyWu's fork as it seems more updated
#	'depth_git' : 0,
#	'branch' : 'ab66a24f255dc89c03eb955c1a996a12d9c7595a', # 2020.08.21 this commit works per https://github.com/HolyWu/L-SMASH-Works/issues/11 (space between dependencies and :)
#	'env_exports' : {
#		'PKGCONFIG' : 'pkg-config',
#	},
#	'conf_system' : 'meson',
#	'build_system' : 'ninja',
#	'source_subfolder' : 'VapourSynth/build', # 'VapourSynth', # 'build',
#	'run_post_regexreplace' : [
#		#'ls -al',
#		#'ls -al ..',
#		'cp -fv "../lsmashsource.h" "../lsmashsource.h.old"',
#		'sed -i.BAK \'s;<VapourSynth.h>;"VapourSynth.h";g\' "../lsmashsource.h"',
#		'diff -U 5 "../lsmashsource.h.old" "../lsmashsource.h" && echo "NO difference" || echo "YES differences!"',
#		'cp -fv "../meson.build" "../meson.build.old"',
#		'sed -i.BAK "s;vapoursynth_dep =;includes = include_directories(\'../include\')\\n\\nvapoursynth_dep =;g" "../meson.build"',
#		'sed -i.BAK \'s;dependencies : deps,;dependencies : deps,\\ninclude_directories : includes,;g\' "../meson.build"', # 2020.09.10 prior to : to fix an upstream commit - in case we change commit brancges
#		'sed -i.BAK \'s;dependencies: deps,;dependencies: deps,\\ninclude_directories : includes,;g\' "../meson.build"',   # 2020.09.10 removed a space prior to : to fix an upstream commit
#		#'sed .-iBAK "s;if host_machine.system() == \'windows\';if host_machine.system() == \'windows\' or host_machine.system() == \'mingw\';g" "../meson.build"',
#		'diff -U 5 "../meson.build.old" "../meson.build" && echo "NO difference" || echo "YES differences!"',
#		'sleep 3',
#		#'sed -iBAK \'s;;;g\' "../"',
#	],
#	'configure_options' :
#		'--prefix={target_prefix} '
#		'--libdir={target_prefix}/lib '
#		#'--extra-libs="-lssp" '
#		'-D__USE_MINGW_ANSI_STDIO=ON '
#		'--default-library=static '
#		'--backend=ninja '
#		'--buildtype=release '
#		'--cross-file={meson_env_file} ./ ..'
#	,
#	'depends_on' : ['vapoursynth_libs', 'libffmpeg_extra', 'libl-smash'],
#	'update_check' : { 'type' : 'git', },
#	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'liblsw' },
#}
