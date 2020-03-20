{
	'repo_type' : 'git',
	'url' : 'https://aomedia.googlesource.com/aom',
	'depth_git': 0,
	#'branch': 'acc2adf9195ff4c5d061132d860d2fe38b28aa55', # 2020.03.19 try git master # acc2adf9195ff4c5d061132d860d2fe38b28aa55 works
	'rename_folder' : 'libaom_git',
	'conf_system' : 'cmake',
	'source_subfolder' : 'build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DAOM_TARGET_CPU={bit_name2} ' # '-DAOM_TARGET_CPU=x86_64 ' 
		'-DBUILD_SHARED_LIBS=0 '
		'-DCONFIG_STATIC=1 '
		'-DCONFIG_SHARED=0 '
        '-DCONFIG_LOWBITDEPTH=0 '
		'-DFORCE_HIGHBITDEPTH_DECODING=1 '
		'-DCONFIG_HIGHBITDEPTH=1 '
		'-DHAVE_PTHREAD=1 '
		'-DENABLE_CCACHE=1 '
		'-DCONFIG_LPF_MASK=1 '
		'-DCONFIG_MULTITHREAD=1 '
		'-DCONFIG_PIC=1 '
		'-DCONFIG_COEFFICIENT_RANGE_CHECKING=0 ' # 2019.12.13
        '-DCONFIG_RUNTIME_CPU_DETECT=1 '
		'-DCONFIG_WEBM_IO=1 '
		'-DCONFIG_SPATIAL_RESAMPLING=1 '
		'-DENABLE_NASM=on ' # YASM is preferred (default) # 2019.12.13 no, NASM is. change -DENABLE_NASM=off 
		'-DCONFIG_AV1=1 '
		'-DCONFIG_AV1_DECODER=1 '
		'-DCONFIG_AV1_ENCODER=1 '
		'-DENABLE_TOOLS=0 '
		'-DENABLE_EXAMPLES=0 '
		'-DENABLE_DOCS=0 '
        '-DCONFIG_INSTALL_DOCS=1 '
		'-DCONFIG_INSTALL_BINS=1 '
        '-DCONFIG_INSTALL_LIBS=1 '
		'-DCONFIG_INSTALL_SRCS=0 '
		'-DCONFIG_UNIT_TESTS=0 '
		'-DENABLE_TESTS=0 '
		'-DENABLE_TESTDATA=0 '
		'-DAOM_EXTRA_C_FLAGS="{original_cflags}" '
        '-DAOM_EXTRA_CXX_FLAGS="{original_cflags}" '
		'-DLIBXML_STATIC=1 '
		'-DGLIB_STATIC_COMPILATION=1 '
	,
	'depends_on' : [ 'glib2', 'libxml2' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libaom-av1' },
}
# 2019.12.13 old:
#	'libaom' : {
#		'repo_type' : 'git',
#		'url' : 'https://aomedia.googlesource.com/aom', # https://aomedia-review.googlesource.com/q/status:merged
#		'conf_system' : 'cmake',
#		'source_subfolder' : 'build',
#		'configure_options': '.. {cmake_prefix_options} '
#			'-DAOM_TARGET_CPU=x86_64 -DAOM_EXTRA_C_FLAGS="{original_cflags}" -DAOM_EXTRA_CXX_FLAGS="{original_cflags}" ' # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'-DCMAKE_INSTALL_PREFIX={target_prefix} '
#			'-DCONFIG_LOWBITDEPTH=0 -DFORCE_HIGHBITDEPTH_DECODING=1 -DCONFIG_HIGHBITDEPTH=1 ' # 2019.10.22 per https://aomedia.googlesource.com/aom/+/refs/heads/master/build/cmake/aom_configure.cmake#28
#			'-DCONFIG_AV1=1 -DHAVE_PTHREAD=1 -DBUILD_SHARED_LIBS=0 -DENABLE_DOCS=1 -DCONFIG_INSTALL_DOCS=1 '
#			'-DCONFIG_INSTALL_BINS=0 -DCONFIG_INSTALL_LIBS=1 '
#			'-DCONFIG_INSTALL_SRCS=1 -DCONFIG_UNIT_TESTS=0 -DENABLE_TESTS=0 -DENABLE_TESTDATA=0 -DENABLE_EXAMPLES=0 '
#			'-DCONFIG_AV1_DECODER=1 -DCONFIG_AV1_ENCODER=1 -DENABLE_CCACHE=1 -DCONFIG_LPF_MASK=1 -DENABLE_TOOLS=0 -DENABLE_EXAMPLES=0 '
#			'-DCONFIG_MULTITHREAD=1 -DCONFIG_PIC=1 -DCONFIG_COEFFICIENT_RANGE_CHECKING=0 '
#			'-DCONFIG_RUNTIME_CPU_DETECT=1 -DCONFIG_WEBM_IO=1 '
#			'-DCONFIG_SPATIAL_RESAMPLING=1 -DENABLE_NASM=on'
#			'-DLIBXML_STATIC=1 -DGLIB_STATIC_COMPILATION=1 ' # 2018.11.23 add nasm, and change some settings
#		,
#		'depends_on' : [ 'libxml2' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libaom' },
#	},