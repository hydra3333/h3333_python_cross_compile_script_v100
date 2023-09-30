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
	'run_post_patch': [
		'sed -i.bak "s/INSTALL(FILES \"docs/#INSTALL(FILES \"docs/g" "CMakeLists.txt"',
		'sed -i.bak "s/  DESTINATION \"\$\{SHARE_INSTALL_PREFIX\}\/man\/man3\/#  DESTINATION \"\$\{SHARE_INSTALL_PREFIX\}\/man\/man3\/g" "CMakeLists.txt"',
		'cat "CMakeLists.txt"', 
	],
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
