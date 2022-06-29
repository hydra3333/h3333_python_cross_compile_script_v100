{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-tools',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Tools.git',
	'depth_git': 0,
	'recursive_git' : True,
	#'branch': '323a81fc5e30e43a04e5e22af4cba98ca2a161e6', # 2020.03.19 comment out
	#'needs_make' : False,
	#'needs_make_install' : False,
	#'needs_configure' : False,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DSKIP_SPIRV_TOOLS_INSTALL=ON '
		'-DSPIRV_TOOLS_BUILD_STATIC=ON '
		'-DSPIRV_SKIP_EXECUTABLES=ON '
		'-DSPIRV_SKIP_TESTS=ON '
		'-DSKIP_SPIRV_HEADERS_INSTALL=ON '
	,
	'depends_on' : [ 'spirv-headers', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV Tools' },
}
