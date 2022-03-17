# 2021.10.30 this and its patches are completely different to deadsix27 ... if this does not work then perhaps reconcile.
#            note: one of deadsix27 patches appears to be "older" in part(s)
{ # in ubuntu 18.04.3 : CMake Error at src/CMakeLists.txt:1 (cmake_minimum_required):   CMake 3.11 or higher is required.  You are running version 3.10.2
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/flac.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'run_post_patch' : [
		'sh autogen.sh --no-symlink',
	],
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_PROGRAMS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_64_BIT_WORDS=ON -DBUILD_PROGRAMS=OFF -DINSTALL_PKGCONFIG_MODULES=ON -DINSTALL_MANPAGES=OFF -DBUILD_SHARED_LIBS=OFF -DWITH_OGG=ON -DHAVE_SQLITE3=ON -DBUILD_DOCS=OFF -DWITH_STACK_PROTECTOR=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.4 -DCMAKE_BUILD_TYPE=Release', # 2020.04.06 try to fix vamp error. this -> sndfile -> vamp
	'patches': [
		('flac/0001-mingw-fix-2020.05.14.patch', '-p1', '..'), # 2020.05.11 from deadsix27
		('flac/0001-mingw-fix-src-CMakeLists-2020.05.14.patch', '-p1', '..'), # 2020.05.11 from deadsix27
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r'add_subdirectory\("microbench"\)',
				'in_file': '../CMakeLists.txt'
			},
            # {
			# 	0: r'add_definitions\(-DHAVE_CONFIG_H\)',
			# 	1: r'add_definitions\(-DHAVE_CONFIG_H -D_FORTIFY_SOURCE=0\)',
			# 	'in_file': '../src/CMakeLists.txt'
			# },
		],
	},
	'depends_on' : [
		'libogg', 'sqlite3',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'flac (library)' },
}
