{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/opus.git',
	'depth_git': 0,
	'strip_cflags': ['-ffast-math', ],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DOPUS_X86_MAY_HAVE_SSE=1 -DOPUS_X86_MAY_HAVE_SSE2=1 -DOPUS_X86_MAY_HAVE_SSE4_1=1 -DOPUS_X86_MAY_HAVE_AVX=1 -DOPUS_X86_PRESUME_SSE=1 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=0 -DBUILD_TESTING=0 -DOPUS_CUSTOM_MODES=1 -DOPUS_BUILD_PROGRAMS=0 -DOPUS_INSTALL_PKG_CONFIG_MODULE=1',
	'patches' : [
		#('https://github.com/hydra3333/opus/commit/505d0cf2dc259b94c7d3b52b2df676cb02d38923.patch', '-p1', '..'),
        ('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/patches/opus/fix_OPUS_LIBRARY_VERSION-from-deadsix27.patch', '-p1', '..'),
	],
	'custom_cflag' : '{original_cflags}', # 2019.12.13 add -fstack-protector-all -D_FORTIFY_SOURCE=2
	'env_exports' : { # 2019.12.13
		'PKGCONFIG' : 'pkg-config', # 2019.12.13
		'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2 # 2019.12.13
		'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2 # 2019.12.13
		'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2 # 2019.12.13
		'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2 # 2019.12.13
	},
	'regex_replace': {
		'post_install': [
			{
				0: r'^(Libs: -L).+ (-lopus)([\n\r\s]+)?$',
				1: r'\1${{libdir}} \2 -lssp\3',
				'in_file': '{pkg_config_path}/opus.pc'
			},
		],
	},
	'_info' : { 'version' : None, 'fancy_name' : 'opus' },
}


