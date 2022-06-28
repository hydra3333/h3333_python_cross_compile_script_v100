{
	'repo_type' : 'git',
	#'depth_git' : 0,
	'branch' : 'main',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Headers.git',
	'recursive_git' : True,
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix}',
	'conf_system' : 'cmake',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan headers' },
}
