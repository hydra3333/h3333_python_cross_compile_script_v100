{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Headers.git',
	'depth_git' : 0,
	'branch' : 'tags/v1.1.127',
	'recursive_git' : True,
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix}',
	'conf_system' : 'cmake',
	'_info' : { 'version' : 'git (tags/v1.1.127)', 'fancy_name' : 'Vulkan headers' },
}
# 2019.12.13 old:
#	'vulkan_headers' : {
#		'repo_type' : 'git',
#		'branch' : 'tags/v1.1.127',
#		'url' : 'https://github.com/KhronosGroup/Vulkan-Headers.git',
#		'recursive_git' : True,
#		'configure_options': '. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix}',
#		'conf_system' : 'cmake',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan headers' },
#	},
