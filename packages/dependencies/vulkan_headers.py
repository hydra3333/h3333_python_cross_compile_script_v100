{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Headers.git',
	'depth_git' : 0,
	#'branch' : 'main',
	'branch' : 'e8b8e06d092ab406b097907ecaae1a8aae9c7d53',	# 2023.02.19 fix upstream change which breaks libplacebo
	#'branch' : 'tags/sdk-1.3.236.0', # 2022.12.21 workaround per https://github.com/m-ab-s/media-autobuild_suite/issues/2345 see in vulkan_loader.py
	# 2022.12.25 undo 'branch' : 'tags/sdk-1.3.236.0' per https://git.videolan.org/?p=ffmpeg.git;a=commit;h=eb0455d64690eed0068e5cb202f72ecdf899837c
	'recursive_git' : True,
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_INSTALL_LIBDIR={target_prefix}/lib ',
	'conf_system' : 'cmake',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan headers' },
}
