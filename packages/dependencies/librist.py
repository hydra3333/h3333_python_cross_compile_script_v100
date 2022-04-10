{ # 2021.08.27 per MABS.  add this '--enable-librist ' to ffmpeg
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/rist/librist.git',
	#'depth_git': 0,
	#'branch': '',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	
	'run_justbefore_patch' : [
		'pwd; sed -i.bak0 "s/cjson_lib = dependency(\'libcjson\', required: false)/cjson_lib = dependency(\'cJSON\', required: false)/" ../meson.build ; pwd',
	],
	'patches' : [
		('rist/0001-Workaround-fixes-for-cJSON-symbol-collision-2022.02.04.patch', '-p1', '..')
	],
	'run_post_patch' : [
        'if [ -d "{target_prefix}/include/librist" ] ; then rm -fvR "{target_prefix}/include/librist" ; fi',    # per MABS
	],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'-Dhave_mingw_pthreads=true -Dtest=false -Ddisable_json=true -Dbuilt_tools=false '  # -D_FILE_OFFSET_BITS=64 ?????????
		'--cross-file={meson_env_file} ./ ..'
	,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'librist' },
}
#
# from MABS:
#do_vcs "https://code.videolan.org/rist/librist.git"; then
#do_patch "https://raw.githubusercontent.com/m-ab-s/mabs-patches/master/librist/0001-Workaround-fixes-for-cJSON-symbol-collision.patch" am
#do_uninstall include/librist "${_check[@]}"
#extracommands=("-Ddisable_json=true")
#[[ $standalone = y ]] || extracommands+=("-Dbuilt_tools=false")
#do_mesoninstall global -Dhave_mingw_pthreads=true -Dtest=false "${extracommands[@]}"