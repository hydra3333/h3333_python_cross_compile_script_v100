{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	'depth_git' : 0,
	'branch' : 'main',
	#'branch' : 'tags/sdk-1.3.236.0', # 2022.12.21 workaround per https://github.com/m-ab-s/media-autobuild_suite/issues/2345 see in vulkan_headers.py
	# 2022.12.25 undo 'branch' : 'tags/sdk-1.3.236.0' per https://git.videolan.org/?p=ffmpeg.git;a=commit;h=eb0455d64690eed0068e5cb202f72ecdf899837c
	#'recursive_git' : True, 
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DUPDATE_DEPS=ON '
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
		'CFLAGS'   : ' -O3 -DVK_ENABLE_BETA_EXTENSIONS -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'CXXFLAGS' : ' -O3 -DVK_ENABLE_BETA_EXTENSIONS -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'CPPFLAGS' : ' -O3 -DVK_ENABLE_BETA_EXTENSIONS -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'LDFLAGS'  : ' -O3 -DVK_ENABLE_BETA_EXTENSIONS -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
	},
	'patches' : [
		('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-2022.11.22.patch', '-Np1', '..'),
		('vulkan/vulkan-0002-pc-remove-CMAKE_CXX_IMPLICIT_LINK_LIBRARIES-MABS-2022.11.22.patch', '-Np1', '..'),
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
