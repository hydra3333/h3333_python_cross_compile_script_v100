{ # 2021.08.27 per MABS.  add this '--enable-librist ' to ffmpeg
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/rist/librist.git',
	#'depth_git': 0,
	#'branch': '',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'patches' : [
		('rist/0001-Workaround-fixes-for-cJSON-symbol-collision.patch', '-p1', '..')
	],
	'run_post_patch' : [
        'if [ -d "{target_prefix}/include/librist" ] ; then rm -fvR "{target_prefix}/include/librist" ; fi',    # per MABS
	],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'-Dhave_mingw_pthreads=true -Dtest=false -Ddisable_json=true -Dbuilt_tools=false '
		'--cross-file={meson_env_file} ./ ..'
	,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'librist' },
}
