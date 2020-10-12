{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	#'depth_git' : 0,
	#'branch' : 'tags/v1.2.135',
	'recursive_git' : True, 
	'configure_options' : 
		'.. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DBUILD_LOADER=ON '
		'-DBUILD_TESTS=OFF '
		'-DUSE_CCACHE=OFF ' # 2020.05.11 per MABS 
		#'-DCMAKE_ASM_COMPILER="$(command -v nasm)" ' # 2020.05.11 per MABS but without the .exe
		#'-DSTRSAFE_NO_DEPRECATE=ON ' # 2020.08.21 per MABS
		#'-DUNIX=OFF '                 # 2020.05.11 per MABS # 2020.10.12 comment out
		#'-DBUILD_STATIC_LOADER=ON '   # 2020.10.11 *** TEST *** THIS MAY NOT WORK (?? for apple only ??) # 2020.10.12 comment out
		'-DENABLE_STATIC_LOADER=ON '  # 2020.04.07 By default, the loader is built as a dynamic library. This allows it to be built as a static library, instead.
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
		#('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-shinchiro-2020.05.11.patch','-p1','..'), # 2020.05.11 per MABS # https://raw.githubusercontent.com/shinchiro/mpv-winbuild-cmake/master/packages/vulkan-0001-cross-compile-static-linking-hacks.patch
		#('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-shinchiro-2020.08.21.patch','-p1','..'), # 2020.05.11 per MABS # https://raw.githubusercontent.com/shinchiro/mpv-winbuild-cmake/master/packages/vulkan-0001-cross-compile-static-linking-hacks.patch
		('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-2020.10.10.patch','-p1','..'), # 2020.05.11 per MABS # 
	],
	'run_post_patch' : [ 
		'sed -i.bak \'s/ pthread m)/ pthread m cfgmgr32)/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27
		'sed -i.bak \'s/ -lshlwapi -lcfgmgr32"/ -lcfgmgr32 -lpthread -lm -lshlwapi"/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27
	],
	#'run_post_install' : [ 
	#	'cp -fv "{target_prefix}/lib/libvulkan.dll.a" "{target_prefix}/lib/libvulkan.a"',
	#],
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', ], # 'glslang',  # 2020
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader' },
}
