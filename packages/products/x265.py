{
	'repo_type' : 'mercurial',
	'url' : 'https://bitbucket.org/multicoreware/x265',
	'rename_folder' : 'x265_hg',
	'source_subfolder' : '_build',
	'configure_options' : 
		'../source {cmake_prefix_options} '
		'-DCMAKE_AR={cross_prefix_full}ar '
		'-DENABLE_SHARED=OFF '
		'-DENABLE_ASSEMBLY=ON '
		'-DEXTRA_LIB="x265_main10.a;x265_main12.a" '
		'-DEXTRA_LINK_FLAGS="-L{offtree_prefix}/libx265_10bit/lib;-L{offtree_prefix}/libx265_12bit/lib" '
		'-DLINKED_10BIT=ON '
		'-DLINKED_12BIT=ON '
        '-DLIBXML_STATIC=ON -DGLIB_STATIC_COMPILATION=ON ' # 2019.12.13
		'-DCMAKE_INSTALL_PREFIX={output_prefix}/x265_hg.installed'
	,
	'conf_system' : 'cmake',
	'depends_on' : [ 'libxml2', 'libx265_multibit_10', 'libx265_multibit_12' ],
	'_info' : { 'version' : 'mercurial (default)', 'fancy_name' : 'x265 (multibit 12/10/8)' },
}
# 2019.12.13 old:
#	'x265_multibit' : {
#		'repo_type' : 'mercurial',
#		'url' : 'https://bitbucket.org/multicoreware/x265',
#		'rename_folder' : 'x265_multibit_hg',
#		'source_subfolder': 'source',
#		'configure_options': '. {cmake_prefix_options} -DCMAKE_AR={cross_prefix_full}ar -DENABLE_SHARED=OFF -DENABLE_ASSEMBLY=ON -DEXTRA_LIB="x265_main10.a;x265_main12.a" -DEXTRA_LINK_FLAGS="-L{offtree_prefix}/libx265_10bit/lib;-L{offtree_prefix}/libx265_12bit/lib" -DLINKED_10BIT=ON -DLINKED_12BIT=ON -DLIBXML_STATIC=ON -DGLIB_STATIC_COMPILATION=ON -DCMAKE_INSTALL_PREFIX={product_prefix}/x265_multibit_hg.installed',
#		'conf_system' : 'cmake',
#		'depends_on' : [ 'libxml2', 'libx265_multibit_10', 'libx265_multibit_12' ],
#		'_info' : { 'version' : 'mercurial (default)', 'fancy_name' : 'x265 (multibit 12/10/8)' },
#	},