{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	#'depth_git' : 0,
	#'branch' : 'tags/v1.1.127',
	'recursive_git' : True, 
	'configure_options' : 
		'.. {cmake_prefix_options} -DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DBUILD_TESTS=OFF '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DBUILD_TESTS=OFF ' #-DENABLE_STATIC_LOADER=ON 
	,
	# 'cpu_count': 1,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'patches' : [
		# ('vulkan/0001-fix-cross-compiling.patch', '-p1', '..'),
		('vulkan/0001-mingw-workarounds.patch','-p1','..'),
	],
	'regex_replace': {
		'post_install': [
			{
				0: r'(?:[^\r\n]+)?libdir=(?:[^\r\n]+)?',
				'in_file': '{pkg_config_path}/vulkan.pc',
				'out_file': '{pkg_config_path}/vulkan.pc'
			},
			{
				0: r'exec_prefix=([^\r\n]+)',
				1: r'prefix={{target_prefix}}\nexec_prefix=\1\nlibdir=${{exec_prefix}}/lib\n',
				'in_file': '{pkg_config_path}/vulkan.pc',
				'out_file': '{pkg_config_path}/vulkan.pc'
			},
		]
	},
	#'run_post_install' : [
	#	'sed -i.bak \'s/Libs: -L${{libdir}} -lvulkan/Libs: -L${{libdir}} -lvulkan -lshlwapi -lcfgmgr32/\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
	#	'sed -i.bak \'s/Libs.private:  -lshlwapi/Libs.private: -lvulkan -lshlwapi -lcfgmgr32/\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
	#],
	'depends_on' : [ 'vulkan_headers', ], # 'vulkan-d3dheaders' ],
	'_info' : { 'version' : 'git (tags/v1.1.127)', 'fancy_name' : 'Vulkan Loader' },
}
# 2019.12.13 old:
#	'vulkan_loader' : { # 2019.11.27 use shared loading (like OpenCL) per deadsix27 https://github.com/DeadSix27/python_cross_compile_script/commit/107bcefc4f2c56abd22079ff5196090d49e49a12
#		'repo_type' : 'git',
#		'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
#		'branch' : 'tags/v1.1.127', #'v1.1.106',
#		#'recursive_git' : True, 
#		'configure_options': '.. {cmake_prefix_options} -DVULKAN_HEADERS_INSTALL_DIR={target_prefix} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_ASM_COMPILER={mingw_binpath}/{cross_prefix_bare}as -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF ', # 2019.11.27 removed  -DENABLE_STATIC_LOADER=ON ',
#		'conf_system' : 'cmake',
#		'source_subfolder' : '_build',
#		'patches' : [
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/vulkan-from-deadsix27/0001-fix-cross-compiling-old.patch','-p1','..'],
#		],
#		'run_post_install' : [
#			'sed -i.bak \'s/Libs: -L${{libdir}} -lvulkan/Libs: -L${{libdir}} -lvulkan -lshlwapi -lcfgmgr32/\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
#			'sed -i.bak \'s/Libs.private:  -lshlwapi/Libs.private: -lvulkan -lshlwapi -lcfgmgr32/\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
#		],
#		'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader (shared like OpenCL)' },
#	},
