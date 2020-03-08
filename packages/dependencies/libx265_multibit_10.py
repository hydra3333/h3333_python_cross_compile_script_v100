{
	'repo_type' : 'git',
	'url' : 'https://bitbucket.org/multicoreware/x265_git',
	'folder_name': 'x265_multilib_10_git',
	'depth_git': 0,
	'source_subfolder' : '_build',
	'configure_options' : 
		'../source {cmake_prefix_options} '
		'-DCMAKE_AR={cross_prefix_full}ar '
		'-DENABLE_ASSEMBLY=ON '
		'-DHIGH_BIT_DEPTH=ON '
		'-DEXPORT_C_API=OFF '
		'-DENABLE_SHARED=OFF '
		'-DENABLE_CLI=OFF '
		'-DCMAKE_INSTALL_PREFIX={offtree_prefix}/libx265_10bit '
        '-DLIBXML_STATIC=ON ' # 2019.12.13
        '-DGLIB_STATIC_COMPILATION=ON ' # 2019.12.13
	,
	'run_post_install' : [
		'mv -fv "{offtree_prefix}/libx265_10bit/lib/libx265.a" "{offtree_prefix}/libx265_10bit/lib/libx265_main10.a"'
	],
	'conf_system' : 'cmake',
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x265 (library (10))' },
}
# 2019.12.13 old:
#	'libx265_multibit_10' : {
#		'repo_type' : 'mercurial',
#		'url' : 'https://bitbucket.org/multicoreware/x265',
#		'rename_folder' : 'libx265_hg_10bit',
#		'source_subfolder' : 'source',
#		'configure_options': '. {cmake_prefix_options} -DCMAKE_AR={cross_prefix_full}ar -DENABLE_ASSEMBLY=ON -DHIGH_BIT_DEPTH=ON -DEXPORT_C_API=OFF -DENABLE_SHARED=OFF -DENABLE_CLI=OFF -DCMAKE_INSTALL_PREFIX={offtree_prefix}/libx265_10bit -DLIBXML_STATIC=ON -DGLIB_STATIC_COMPILATION=ON ', # 2018.11.23 added  -DLIBXML_STATIC=ON -DGLIB_STATIC_COMPILATION=ON 
#		'run_post_install' : [
#			'mv -fv "{offtree_prefix}/libx265_10bit/lib/libx265.a" "{offtree_prefix}/libx265_10bit/lib/libx265_main10.a"'
#		],
#		'conf_system' : 'cmake',
#		'_info' : { 'version' : 'mercurial (default)', 'fancy_name' : 'x265 (library (10))' },
#	},