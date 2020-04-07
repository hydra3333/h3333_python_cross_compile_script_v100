{ # in ubuntu 18.04.3 : CMake Error at src/CMakeLists.txt:1 (cmake_minimum_required):   CMake 3.11 or higher is required.  You are running version 3.10.2
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/flac.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_64_BIT_WORDS=ON -DBUILD_PROGRAMS=OFF -DINSTALL_MANPAGES=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_64_BIT_WORDS=ON -DBUILD_PROGRAMS=OFF -DINSTALL_PKGCONFIG_MODULES=ON -DINSTALL_MANPAGES=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release', # 2020.04.06 try to fix vamp error. this -> sndfile -> vamp
	'patches': [
		('flac/0001-mingw-fix-2.patch', '-p1', '..'),
		('flac/libFLAC_CMakeLists.txt.patch', '-p1', '..'),
		#('flac/libFLAC++_CMakeLists.txt.patch', '-p1', '..'),
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r'add_subdirectory\("microbench"\)',
				'in_file': '../CMakeLists.txt'
			},
			{
				0: r'add_subdirectory\("utils"\)',
				'in_file': '../src/CMakeLists.txt'
			},
			{
				0: r'    add_subdirectory\("metaflac"\)',
				'in_file': '../src/CMakeLists.txt'
			},
			{
				0: r'    add_subdirectory\("flac"\)',
				'in_file': '../src/CMakeLists.txt'
			},
		],
	},
	'depends_on' : [
		'libogg',
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'flac (library)' },
}
#
# src/libFLAC/CMakeLists.txt   DESTINATION "${CMAKE_INSTALL_DATADIR}/pkgconfig"     DESTINATION "${CMAKE_INSTALL_LIBDIR}/lib/pkgconfig")
# src/libFLAC++/CMakeLists.txt DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig" DESTINATION "${CMAKE_INSTALL_LIBDIR}/lib/pkgconfig")
