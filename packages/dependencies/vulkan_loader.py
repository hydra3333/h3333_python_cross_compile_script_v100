{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	#'depth_git' : 0,
	#'branch' : 'tags/v1.2.135',
	# Hmmm ... 2020.10.11 STATIC LINKING NO LONGER POSSIBLE PER https://github.com/KhronosGroup/Vulkan-Loader/commit/0c0ac2c6c458acdb8ca28902fc990342902fc0a3#diff-4a527f83a3a4ca7e1d70adb26a35b72e
	'recursive_git' : True, 
	'configure_options' : 
		'.. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DBUILD_LOADER=ON '
		'-DBUILD_TESTS=OFF '
		'-DUSE_CCACHE=OFF ' # 2020.05.11 per MABS 
		#'-DCMAKE_ASM_COMPILER="$(command -v nasm)" ' # 2020.05.11 per MABS but without the .exe
		#'-DSTRSAFE_NO_DEPRECATE=ON ' # 2020.08.21 per MABS
		'-DUNIX=OFF '                 # 2020.05.11 per MABS # 2020.10.12 comment out
		'DUSE_MASM=OFF '                # 2021.10.30 per deadsix27
		#'-DBUILD_STATIC_LOADER=ON '   # Hmmm ... 2020.10.11 STATIC LINKING NO LONGER POSSIBLE
		'-DBUILD_STATIC_LOADER=ON '     # 2021.10.30 per deadsix27
		#'-DENABLE_STATIC_LOADER=ON '  # Hmmm ... 2020.10.11 STATIC LINKING NO LONGER POSSIBLE
		'-DENABLE_STATIC_LOADER=ON '    # 2021.10.30 per deadsix27
		'-DUSE_UNSAFE_C_GEN=ON ' # 2020.10.10 per MABS https://github.com/m-ab-s/media-autobuild_suite/commit/7034e948ca14323514fca98c83adc1ec7720909e
	,
	'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'CXXFLAGS' : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'CPPFLAGS' : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
		'LDFLAGS'  : ' -O3 -D_POSIX_C_SOURCE -DSTRSAFE_NO_DEPRECATE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE # 2020.08.21 per MABS -DSTRSAFE_NO_DEPRECATE
	},
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'patches' : [
		#('vulkan/0001-mingw-workarounds-2020.04.08.patch','-p1','..'),
		('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-2020.10.10.patch','-p1','..'), # 2020.05.11 per MABS # 
		# 2021.10.30 hmmmmm, if building with vulkan fails then refer this updated patch from deadsix27 :  patches/vulkan/0001-mingw-workarounds.patch 
	],
	'run_post_patch' : [ 
		'sed -i.bak \'s/ pthread m)/ pthread m cfgmgr32)/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27
		'sed -i.bak \'s/ -lshlwapi -lcfgmgr32"/ -lcfgmgr32 -lpthread -lm -lshlwapi -lglslang"/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27 # 2020.10.11 libglslang
	],
	'run_post_install' : [ 
		'cp -fv "{target_prefix}/lib/libvulkan.dll.a" "{target_prefix}/lib/libvulkan.a"', # Hmmm ... 2020.10.11 STATIC LINKING NO LONGER POSSIBLE so do this
	],
	'depends_on' : [ 'glslang', 'vulkan_headers', 'vulkan-d3dheaders', ], # 2020.10.11 libglslang
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader' },
}
