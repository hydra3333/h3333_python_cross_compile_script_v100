{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-headers',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Headers.git',
	#'depth_git': 0,
	'recursive_git' : True,
	#'branch': '204cd131c42b90d129073719f2766293ce35c081', # 2020.03.19 comment out
	#'needs_make' : False,
	#'needs_make_install' : False,
	#'needs_configure' : False,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
	,
	#'run_post_configure' : [
	#	'cmake --build . --target install',
	#],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV Headers' },
}