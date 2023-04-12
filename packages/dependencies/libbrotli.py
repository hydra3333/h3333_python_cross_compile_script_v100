{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/brotli',
	# 'depth_git': 0,
	'rename_folder' : 'libbrotli_GIT',
	'conf_system' : 'cmake',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
        '-DBUILD_SHARED_LIBS=false '
		'-DBROTLI_EMSCRIPTEN=false '
	,
	'run_post_install' : [
		'sed -i.bak "s/-lbrotlienc/-lbrotlienc -lbrotlicommon/" "{pkg_config_path}/libbrotlienc.pc"', 
		'cat "{pkg_config_path}/libbrotlienc.pc"', 
		'sed -i.bak "s/-lbrotlidec/-lbrotlidec -lbrotlicommon/" "{pkg_config_path}/libbrotlidec.pc"', 
		'cat "{pkg_config_path}/libbrotlidec.pc"', 
		#'ls -al',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : None, 'fancy_name' : 'libbrotli' },
}
