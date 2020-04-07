{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/Vulkan-Loader.git',
	#'depth_git' : 0,
	#'branch' : 'tags/v1.2.135',
	'recursive_git' : True, 
	'configure_options' : 
		'.. {cmake_prefix_options} -DVULKAN_HEADERS_INSTALL_DIR={target_prefix} '
		'-DCMAKE_BUILD_TYPE=Release '
		'-DBUILD_TESTS=OFF '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DBUILD_TESTS=OFF ' 
		'-DENABLE_STATIC_LOADER=ON ' # 2020.04.07 By default, the loader is built as a dynamic library. This allows it to be built as a static library, instead.
		'-DBUILD_STATIC_LOADER=OFF ' # 2020.04.07 comment out since "Note that this will only work on MacOS and is not supported"
	,
	'env_exports' : { # 2019.12.13 add -D_POSIX_C_SOURCE
		'CFLAGS'   : ' -O3',
		'CXXFLAGS' : ' -O3',
		'CPPFLAGS' : ' -O3',
		'LDFLAGS'  : ' -O3',
	},
	# 'cpu_count': 1,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'patches' : [
		# ('vulkan/0001-mingw-workarounds.patch','-p1','..'),
		('vulkan/0001-mingw-workarounds-2020.04.07.patch','-p1','..'),
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
	'run_post_install' : [
	#	##'cp -fv "{target_prefix}/lib/libvulkan-1.dll.a" "{target_prefix}/lib/libvulkan-1.a"',
		'cp -fv "{target_prefix}/lib/pkgconfig/vulkan.pc" "{target_prefix}/lib/pkgconfig/vulkan.pc.orig"',
		'sed -i.bak \'s/-lvulkan/-lvulkan-1.dll/g\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
		'sed -i.bak \'s/-lvulkan-1.dll-1.dll/-lvulkan-1.dll/g\' "{target_prefix}/lib/pkgconfig/vulkan.pc"',
		'diff -U 5 "{target_prefix}/lib/pkgconfig/vulkan.pc.orig" "{target_prefix}/lib/pkgconfig/vulkan.pc" && echo "NO difference" || echo "YES differences!"',
		'cat "{target_prefix}/lib/pkgconfig/vulkan.pc"',
	],
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', ],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Vulkan Loader' },
}
