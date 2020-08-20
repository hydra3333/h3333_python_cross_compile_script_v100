{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	#'depth_git' : 0,
	#'branch' : 'tags/v1.2.135',
	'recursive_git' : True, 
	'configure_options' : 
		'.. {cmake_prefix_options} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DBUILD_TESTS=OFF '
		'-DUSE_CCACHE=OFF ' # 2020.05.11 per MABS 
		'-DSTRSAFE_NO_DEPRECATE=ON ' # 2020.08.21 per MABS
		#'-DCMAKE_ASM_COMPILER="$(command -v nasm)" ' # 2020.05.11 per MABS but without the .exe
		#'-DUNIX=OFF ' # 2020.05.11 per MABS 
		'-DENABLE_STATIC_LOADER=ON ' # 2020.04.07 By default, the loader is built as a dynamic library. This allows it to be built as a static library, instead.
	,
	'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -O3 -D_POSIX_C_SOURCE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE
		'CXXFLAGS' : ' -O3 -D_POSIX_C_SOURCE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE
		'CPPFLAGS' : ' -O3 -D_POSIX_C_SOURCE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE
		'LDFLAGS'  : ' -O3 -D_POSIX_C_SOURCE ', # 2020.04.07 attempted to add -D_POSIX_C_SOURCE
	},
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'patches' : [
		#('vulkan/0001-mingw-workarounds-2020.04.08.patch','-p1','..'),
		('vulkan/vulkan-0001-cross-compile-static-linking-hacks-MABS-shinchiro-2020.05.11.patch','-p1','..'), # 2020.05.11 per MABS # https://raw.githubusercontent.com/shinchiro/mpv-winbuild-cmake/master/packages/vulkan-0001-cross-compile-static-linking-hacks.patch
	],
	'run_post_patch' : [ 
		'sed -i.bak \'s/ pthread m)/ pthread m cfgmgr32)/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27
		'sed -i.bak \'s/ -lshlwapi -lcfgmgr32"/ -lcfgmgr32 -lpthread -lm -lshlwapi"/g\' ../loader/CMakeLists.txt', # 2020.05.11 to align more with deadsix27
	],
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader' },
}
