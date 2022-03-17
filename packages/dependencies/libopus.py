{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/opus.git',
	'depth_git': 0,
	'strip_cflags': ['-ffast-math', ],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DOPUS_X86_MAY_HAVE_SSE=1 -DOPUS_X86_MAY_HAVE_SSE2=1 -DOPUS_X86_MAY_HAVE_SSE4_1=1 -DOPUS_X86_MAY_HAVE_AVX=1 -DOPUS_X86_PRESUME_SSE=1 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=0 -DBUILD_TESTING=0 -DOPUS_CUSTOM_MODES=1 -DOPUS_BUILD_PROGRAMS=0 -DOPUS_INSTALL_PKG_CONFIG_MODULE=1 -DHAVE_SQLITE3=ON',
	'regex_replace': {
		'post_install': [
			{
				0: r'^(Libs: -L).+ (-lopus)([\n\r\s]+)?$',
				1: r'\1${{libdir}} \2 -lssp\3',
				'in_file': '{pkg_config_path}/opus.pc'
			},
		],
	},
	'run_post_regexreplace' : [
		'sh ./autogen.sh',
	],
	#'depends_on' : [ 'glib2' ], # 2020.05.12 removed 'glib2', 
	'depends_on' : [ 
		'sqlite3',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'opus' },
}
