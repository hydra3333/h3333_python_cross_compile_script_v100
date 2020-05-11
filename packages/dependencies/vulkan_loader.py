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
	#'regex_replace': {
	#	'post_install': [
	#		{
	#			0: r'(?:[^\r\n]+)?libdir=(?:[^\r\n]+)?',
	#			'in_file': '{pkg_config_path}/vulkan.pc',
	#			'out_file': '{pkg_config_path}/vulkan.pc'
	#		},
	#		{
	#			0: r'exec_prefix=([^\r\n]+)',
	#			1: r'prefix={{target_prefix}}\nexec_prefix=\1\nlibdir=${{exec_prefix}}/lib\n',
	#			'in_file': '{pkg_config_path}/vulkan.pc',
	#			'out_file': '{pkg_config_path}/vulkan.pc'
	#		},
	#		{
	#			0: r'-lvulkan$',
	#			1: r'-lvulkan-1.dll',
	#			'in_file': '{pkg_config_path}/vulkan.pc',
	#			'out_file': '{pkg_config_path}/vulkan.pc'
	#		},
	#	]
	#},
	#'run_post_install' : [
	#	##'cp -fv "{target_prefix}/lib/libvulkan-1.dll.a" "{target_prefix}/lib/libvulkan-1.a"',
		#'cp -fv "{target_prefix}/lib/pkgconfig/vulkan.pc" "{target_prefix}/lib/pkgconfig/vulkan.pc.orig"',
		#'sed -i.bak \'s/-lvulkan/-lvulkan-1.dll/g\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
		#'sed -i.bak \'s/-lvulkan-1.dll-1.dll/-lvulkan-1.dll/g\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
		#'diff -U 5 "{target_prefix}/lib/pkgconfig/vulkan.pc.orig" "{target_prefix}/lib/pkgconfig/vulkan.pc" && echo "NO difference" || echo "YES differences!"',
		#'cat "{target_prefix}/lib/pkgconfig/vulkan.pc"',
	#],
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', ],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader' },
}
