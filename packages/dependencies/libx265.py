{ # 2019.12.13 make it the same as multibit
	#'repo_type' : 'mercurial',
	#'url' : 'https://bitbucket.org/multicoreware/x265',
	#'rename_folder' : 'libx265_hg',
	#'source_subfolder' : '_build',
	#'configure_options' : 
	#	'../source {cmake_prefix_options} '
	#	'-DCMAKE_INSTALL_PREFIX={target_prefix} '
	#	'-DENABLE_ASSEMBLY=ON '
	#	'-DENABLE_CLI:BOOL=OFF '
	#	'-DENABLE_SHARED=OFF '
	#	'-DCMAKE_AR={cross_prefix_full}ar'
	#,
	#'conf_system' : 'cmake',
	#'depends_on' : [ 'libxml2' ],
	#'run_post_install' : [
	#	'sed -i.bak \'s|-lmingwex||g\' "{pkg_config_path}/x265.pc"',
	#],
	#'_info' : { 'version' : None, 'fancy_name' : 'x265 (library)' },
	#
	'is_dep_inheriter' : True,
	'depends_on' : [
		'libx265_multibit',
	],
	
}