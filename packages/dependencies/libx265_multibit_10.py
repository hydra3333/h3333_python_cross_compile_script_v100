{
	#'repo_type' : 'git',
	#'url' : 'https://bitbucket.org/multicoreware/x265_git',
	#'folder_name': 'libx265_multilib_hg_10_bit',
	#'depth_git': 0,
    'repo_type' : 'mercurial',                        # 2021.10.30 per deadsix27
	'url' : 'http://hg.videolan.org/x265/',           # 2021.10.30 per deadsix27
	'rename_folder' : 'libx265_multilib_hg_10_bit',   # 2021.10.30 per deadsix27
	'source_subfolder' : '_build',
	'configure_options' : 
		'../source {cmake_prefix_options} '
		'-DCMAKE_AR={cross_prefix_full}ar '
		'-DENABLE_ASSEMBLY=ON '
		'-DHIGH_BIT_DEPTH=ON '
		'-DENABLE_HDR10_PLUS=ON ' # 2020.06.09
		'-DEXPORT_C_API=OFF '
		'-DENABLE_SHARED=OFF '
		'-DENABLE_CLI=OFF '
		'-DCMAKE_INSTALL_PREFIX={offtree_prefix}/libx265_10bit '
		'-DLIBXML_STATIC=ON ' # 2019.12.13
		'-DGLIB_STATIC_COMPILATION=ON ' # 2019.12.13
		'-DENABLE_HDR10_PLUS=ON ' # 2020.07.27
	,
	'run_post_install' : [
        'if [ ! -d "{offtree_prefix}/libx265_10bit/lib" ]; then mkdir -pv –m777 "{offtree_prefix}/libx265_10bit/lib"; fi ;',
		'mv -fv "{offtree_prefix}/libx265_10bit/lib/libx265.a" "{offtree_prefix}/libx265_10bit/lib/libx265_main10.a"'
	],
	'conf_system' : 'cmake',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x265 (library (10))' },
}
