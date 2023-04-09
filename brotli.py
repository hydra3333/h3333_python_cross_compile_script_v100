{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/brotli',
	# 'depth_git': 0,
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
		'sed -i.bak "s/-lbrotlienc/-lbrotlicommon -lbrotlienc/" "{pkg_config_path}/libbrotlienc.pc"', 
		'cat "{pkg_config_path}/libbrotlienc.pc"', 
		'sed -i.bak "s/-lbrotlidec/-lbrotlicommon -lbrotlidec/" "{pkg_config_path}/libbrotlidec.pc"', 
		'cat "{pkg_config_path}/libbrotlidec.pc"', 
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : None, 'fancy_name' : 'brotli' },
}
