#type:ignore
{
	'repo_type' : 'git',
    'url': 'https://github.com/libarchive/bzip2.git',
    'source_subfolder': '_build',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_STATIC_LIB=ON -DENABLE_SHARED_LIB=OFF -DENABLE_LIB_ONLY=ON',
	'regex_replace': {
		'post_patch': [
			{
				0: r'ARCHIVE_OUTPUT_NAME bz2_static\)',
				1: r'ARCHIVE_OUTPUT_NAME bz2)',
				'in_file': '../CMakeLists.txt'
			},
		],
	},
	'update_check' : { 'url' : 'ftp://sourceware.org/pub/bzip2/', 'type' : 'ftpindex', 'regex' : r'bzip2-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.0.8', 'fancy_name' : 'BZip2 (library)' },
}