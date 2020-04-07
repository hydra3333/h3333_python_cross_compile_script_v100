{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/flac.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	#'configure_options' : '--host={target_host} --prefix={output_prefix}/flac_git.installed --disable-shared --enable-static',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_64_BIT_WORDS=ON -DBUILD_PROGRAMS=ON -DINSTALL_PKGCONFIG_MODULES=ON -DINSTALL_MANPAGES=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release', # 2020.04.06 try to fix vamp error. this -> sndfile -> vamp
	'patches': [
		('flac/0001-mingw-fix-2.patch', '-p1', '..'),
		('flac/libFLAC_CMakeLists.txt.patch', '-p1', '..'),
		#('flac/libFLAC++_CMakeLists.txt.patch', '-p1', '..'),
	],
	#'regex_replace': {
	#	'post_patch': [
			#{
			#	0: r'add_subdirectory\("microbench"\)',
			#	'in_file': '../CMakeLists.txt'
			#},
			#{
			#	0: r'add_subdirectory\("utils"\)',
			#	'in_file': '../src/CMakeLists.txt'
			#},
			#{
			#	0: r'    add_subdirectory\("metaflac"\)',
			#	'in_file': '../src/CMakeLists.txt'
			#},
			#{
			#	0: r'    add_subdirectory\("flac"\)',
			#	'in_file': '../src/CMakeLists.txt'
			#},
	#	],
	#},
	'depends_on' : [
		'libogg',
	],
	'packages' : {
		'ubuntu' : [ 'docbook-to-man' ],
	},
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'FLAC' },
}
