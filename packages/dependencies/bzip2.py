{
	'repo_type' : 'git',
    'url': 'https://github.com/libarchive/bzip2.git',
    'source_subfolder': '_build',
	'regex_replace': {
		'post_patch': [
			{
				0: r'ARCHIVE_OUTPUT_NAME bz2_static\)',
				1: r'ARCHIVE_OUTPUT_NAME bz2)',
				'in_file': '../CMakeLists.txt'
			},

		],
	},
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_STATIC_LIB=ON -DENABLE_SHARED_LIB=OFF -DENABLE_LIB_ONLY=ON',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'BZip2 (library)' },
}
