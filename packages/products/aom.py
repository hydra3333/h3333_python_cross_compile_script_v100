{
	'repo_type' : 'git',
	'url' : 'https://aomedia.googlesource.com/aom',
	'conf_system' : 'cmake',
	'source_subfolder' : 'build',
	'configure_options' :
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={output_prefix}/aom_git.installed '
		'-DBUILD_SHARED_LIBS=0 '
		'-DENABLE_DOCS=0 '
		'-DENABLE_TESTS=0 '
		'-DENABLE_TOOLS=1 '
		'-DENABLE_CCACHE=1 '
		'-DCONFIG_LPF_MASK=1 '
		'-DENABLE_EXAMPLES=1 '
		'-DENABLE_TESTDATA=0 '
		'-DCONFIG_AV1_DECODER=1 '
		'-DCONFIG_AV1_ENCODER=1 '
		'-DCONFIG_PIC=1 '
		'-DCONFIG_SPATIAL_RESAMPLING=1 '
		'-DENABLE_NASM=off ' # YASM is preferred (default)
		'-DCONFIG_STATIC=1 '
		'-DCONFIG_SHARED=0'
	,
	'depends_on' : [ 'libxml2' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : None, 'fancy_name' : 'aom-av1' },
}