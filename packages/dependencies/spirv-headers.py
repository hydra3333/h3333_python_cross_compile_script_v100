{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-headers',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Headers.git',
	#'depth_git': 0,
	'recursive_git' : True,
	#'branch': 'main', # 2023.01.12 address more 'merican embedded racism
	'branch': '!CMD(cat "shaderc_commit_dependencies/spirv_headers_revision.commit")CMD!', # 2023.02.04
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
	'depends_on' : [ 'shaderc_commit_dependencies', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV Headers' },
}