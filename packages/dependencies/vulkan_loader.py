{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	'depth_git' : 0,
	##'branch' : 'tags/v1.3.218',
	#'branch' : 'e91cfe1cf9c540597e969f3b01b16384ec4b9c50',
	# Hmmm ... 2020.10.11 STATIC LINKING NO LONGER POSSIBLE PER https://github.com/KhronosGroup/Vulkan-Loader/commit/0c0ac2c6c458acdb8ca28902fc990342902fc0a3#diff-4a527f83a3a4ca7e1d70adb26a35b72e
	#'recursive_git' : True, 
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DENABLE_WERROR=OFF ' # 2022.04.08
		'-DBUILD_LOADER=ON '
		'-DBUILD_STATIC_LOADER=ON '     # 2021.10.30 per deadsix27
		'-DENABLE_STATIC_LOADER=ON '    # 2021.10.30 per deadsix27
		'-DCMAKE_ASM_COMPILER="$(command -v nasm)" ' # 2022.04.08 back in
		'-DUSE_MASM=OFF '                # 2021.10.30 per deadsix27
		'-DUNIX=OFF '                 # 2020.05.11 per MABS # 2020.10.12 comment out
		'-DBUILD_TESTS=OFF '
		'-DUSE_CCACHE=OFF ' # 2020.05.11 per MABS 
		#'-DSTRSAFE_NO_DEPRECATE=ON ' # 2020.08.21 per MABS
		'-DUSE_UNSAFE_C_GEN=ON ' # 2020.10.10 per MABS https://github.com/m-ab-s/media-autobuild_suite/commit/7034e948ca14323514fca98c83adc1ec7720909e
	,
	'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'CXXFLAGS' : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'CPPFLAGS' : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'LDFLAGS'  : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
	},
	'patches' : [
		#('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-2022.06.28.patch', '-Np1', '..'),
		#('vulkan/vulkan-0002-pc-remove-CMAKE_CXX_IMPLICIT_LINK_LIBRARIES-MABS-2022.06.28.patch', '-Np1', '..'),
		('vulkan/vulkan-1001-cross-compile-static-linking-hacks-exMABSupdated-2022.07.09-CMakeLists_txt.patch', '-Np1', '..'),
		#('vulkan/vulkan-1002-cross-compile-static-linking-hacks-exMABSupdated-2022.07.09-loader_h.patch', '-Np1', '..'),
		('vulkan/vulkan-1003-cross-compile-static-linking-hacks-exMABSupdated-2022.07.09-loader.rc_in.patch', '-Np1', '..'),
		('vulkan/vulkan-1004-cross-compile-static-linking-hacks-exMABSupdated-2022.07.09-loader_windows_c.patch', '-Np1', '..'),
		('vulkan/vulkan-1005-cross-compile-static-linking-hacks-exMABSupdated-2022.07.09-vk_loader_platform_h.patch', '-Np1', '..'),
	],
	'run_post_patch' : [ 
		'sed -i.bak \'s/ pthread m)/ pthread m cfgmgr32)/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27
		'sed -i.bak \'s/ -lshlwapi -lcfgmgr32"/ -lcfgmgr32 -lpthread -lm -lshlwapi -lglslang"/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27 # 2020.10.11 libglslang
		'sed -i.bak "s/\@VULKAN_LIB_SUFFIX\@//" ../loader/vulkan.pc.in',
	],
	'regex_replace': {
		'post_install': [
			#{
			#	0: r'(?:[^\r\n]+)?libdir=(?:[^\r\n]+)?',
			#	'in_file': '{pkg_config_path}/vulkan.pc',
			#	'out_file': '{pkg_config_path}/vulkan.pc'
			#},
			#{
			#	0: r'exec_prefix=([^\r\n]+)',
			#	1: r'prefix={{target_prefix}}\nexec_prefix=\1\nlibdir=${{exec_prefix}}/lib\n',
			#	'in_file': '{pkg_config_path}/vulkan.pc',
			#	'out_file': '{pkg_config_path}/vulkan.pc'
			#},
			#{
			#	0: r'-lvulkan$',
			#	1: r'-lvulkan-1',
			#	'in_file': '{pkg_config_path}/vulkan.pc',
			#	'out_file': '{pkg_config_path}/vulkan.pc'
			#},
		]
	},
	'run_post_install' : [ 
		#'cat {pkg_config_path}/vulkan.pc',
		'sed -i.bak "s;/Lib;/lib;g" "{pkg_config_path}/vulkan.pc"',
		'sed -i.bak "s/-lvulkan-1/-lvulkan/g" "{pkg_config_path}/vulkan.pc"',
		'cat {pkg_config_path}/vulkan.pc',
		'ls -al {target_prefix}/lib/libvulkan*',
		#'cp -fv "{target_prefix}/lib/libvulkan.dll.a" "{target_prefix}/lib/libvulkan.a"',
		#'ls -al {target_prefix}/lib/libvulkan*',
		#'cp -fv "{target_prefix}/lib/libvulkan-1.dll.a" "{target_prefix}/lib/libvulkan.a"',
		#'cp -fv "{target_prefix}/lib/libvulkan-1.dll.a" "{target_prefix}/lib/libvulkan-1.a"',
		#'cp -fv "{target_prefix}/lib/libvulkan-1.dll.a" "{target_prefix}/lib/libvulkan-1.dll.a"',
		'ls -al {target_prefix}/lib/libvulkan*',
	],
	#'depends_on' : [ 'glslang', 'spirv-headers', 'spirv-tools', 'spirv-cross', 'shaderc', 'vulkan_headers', 'vulkan-d3dheaders', ], # 2020.10.11 libglslang
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', ], # MABS/DEADSIX27 VULKAN depends only on these
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader' },
}
