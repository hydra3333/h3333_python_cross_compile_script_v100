{
	#'repo_type' : 'git',
	#'url' : 'https://bitbucket.org/multicoreware/x265_git',
	#'folder_name': 'x265_git',
	#'depth_git': 0,
	'repo_type' : 'mercurial',					# 2021.10.30 per deadsix27
	'url' : 'http://hg.videolan.org/x265/',		# 2021.10.30 per deadsix27
	'rename_folder' : 'x265_multibit_hg',	 # 2021.10.30 per deadsix27
	'source_subfolder' : '_build',
	'configure_options' : 
		'../source {cmake_prefix_options} '
		'-DCMAKE_AR={cross_prefix_full}ar '
		'-DENABLE_SHARED=OFF '
		'-DENABLE_ASSEMBLY=ON '
		'-DENABLE_SHARED=OFF '
		#'-DENABLE_CLI:BOOL=OFF '
		'-DEXTRA_LIB="x265_main10.a;x265_main12.a" '
		'-DEXTRA_LINK_FLAGS="-L{offtree_prefix}/libx265_10bit/lib;-L{offtree_prefix}/libx265_12bit/lib" '
		'-DLINKED_10BIT=ON '
		'-DLINKED_12BIT=ON '
		'-DCMAKE_INSTALL_PREFIX={output_prefix}/x265.installed'
		'-DLIBXML_STATIC=ON '
		'-DGLIB_STATIC_COMPILATION=ON ' # 2019.12.13
		'-DENABLE_HDR10_PLUS=ON ' # 2020.07.27
	,
	'conf_system' : 'cmake',
	'depends_on' : [ 'libxml2', 'libx265_multibit_10', 'libx265_multibit_12' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'x265 (multibit 12/10/8)' },
}
