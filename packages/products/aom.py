{
	'repo_type' : 'git',
	'url' : 'https://aomedia.googlesource.com/aom',
	'depth_git': 100,
	'branch': 'acc2adf9195ff4c5d061132d860d2fe38b28aa55',
	'conf_system' : 'cmake',
	'source_subfolder' : 'build',
    # 2019.12.13 note: we make this a 64 bit build only with -DAOM_TARGET_CPU=x86_64 ... some may not prefer this.
	#'configure_options' : # 2019.12.13 commented out
	#	'.. {cmake_prefix_options} '
	#	'-DCMAKE_INSTALL_PREFIX={output_prefix}/aom_git.installed '
	#	'-DBUILD_SHARED_LIBS=0 '
	#	'-DENABLE_DOCS=0 '
	#	'-DENABLE_TESTS=0 '
	#	'-DENABLE_TOOLS=1 '
	#	'-DENABLE_CCACHE=1 '
	#	'-DCONFIG_LPF_MASK=1 '
	#	'-DENABLE_EXAMPLES=1 '
	#	'-DENABLE_TESTDATA=0 '
	#	'-DCONFIG_AV1_DECODER=1 '
	#	'-DCONFIG_AV1_ENCODER=1 '
	#	'-DCONFIG_PIC=1 '
	#	'-DCONFIG_SPATIAL_RESAMPLING=1 '
	#	'-DENABLE_NASM=off ' # YASM is preferred (default)
	#	'-DCONFIG_STATIC=1 '
	#	'-DCONFIG_SHARED=0'
	#,
	'configure_options': '.. {cmake_prefix_options} ' 
		'-DCMAKE_INSTALL_PREFIX={output_prefix}/aom_git.installed '
        '-DAOM_TARGET_CPU=x86_64 ' 
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
        '-DCONFIG_COEFFICIENT_RANGE_CHECKING=0 '
		'-DCONFIG_RUNTIME_CPU_DETECT=1 '
        '-DCONFIG_WEBM_IO=1 '
		'-DCONFIG_SPATIAL_RESAMPLING=1 '
        '-DENABLE_NASM=on '
		'-DCONFIG_AV1=1 '
		'-DCONFIG_AV1_DECODER=1 '
        '-DCONFIG_AV1_ENCODER=1 '
        '-DENABLE_TOOLS=1 '
        '-DENABLE_EXAMPLES=1 '
        '-DENABLE_DOCS=1 '
        '-DCONFIG_INSTALL_DOCS=1 '
		'-DCONFIG_INSTALL_BINS=1 '
        '-DCONFIG_INSTALL_LIBS=0 '
		'-DCONFIG_INSTALL_SRCS=0 '
        '-DCONFIG_UNIT_TESTS=0 '
        '-DENABLE_TESTS=0 '
        '-DENABLE_TESTDATA=0 '
        '-DAOM_EXTRA_C_FLAGS="{original_cflags}" '
        '-DAOM_EXTRA_CXX_FLAGS="{original_cflags}" '
		'-DLIBXML_STATIC=1 '
        '-DGLIB_STATIC_COMPILATION=1 '
	,
    'depends_on' : [ 'glib2', 'libxml2' ], # 2019.12.13
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'aom-av1' },
}
# 2019.12.13 old:
#	'aom' : {
#		'repo_type' : 'git',
#		'url' : 'https://aomedia.googlesource.com/aom', # https://aomedia-review.googlesource.com/q/status:merged
#		#'branch' : 'd759facf0fd6af16d9d4a137076782d522242c1e', # 2019.08.15 this following commit  a7091f15ee7df7f7b38d54d2baf89ccbe5d3427f  broke building :(
#		'conf_system' : 'cmake',
#		'source_subfolder' : 'build',
#		# note: we make this a 64 bit build only with -DAOM_TARGET_CPU=x86_64 ... some may not prefer this.
#		'configure_options': '.. {cmake_prefix_options} ' 
#			'-DAOM_TARGET_CPU=x86_64 -DAOM_EXTRA_C_FLAGS="{original_cflags}" -DAOM_EXTRA_CXX_FLAGS="{original_cflags}" ' # 2018.11.23 add these options # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'-DLIBXML_STATIC=1 -DGLIB_STATIC_COMPILATION=1 -DENABLE_EXAMPLES=1 ' # 2018.11.23 add these options
#			'-DCMAKE_INSTALL_PREFIX={product_prefix}/aom_git.installed '
#			'-DCONFIG_LOWBITDEPTH=0 -DFORCE_HIGHBITDEPTH_DECODING=1 -DCONFIG_HIGHBITDEPTH=1 ' # 2019.10.22 per https://aomedia.googlesource.com/aom/+/refs/heads/master/build/cmake/aom_configure.cmake#28
#			'-DCONFIG_AV1=1 -DHAVE_PTHREAD=1 -DBUILD_SHARED_LIBS=0 -DENABLE_DOCS=1 -DCONFIG_INSTALL_DOCS=1 '
#			'-DCONFIG_INSTALL_BINS=1 -DCONFIG_INSTALL_LIBS=0 '
#			'-DCONFIG_INSTALL_SRCS=0 -DCONFIG_UNIT_TESTS=0 -DENABLE_TESTS=0 -DENABLE_TESTDATA=0 '
#			'-DCONFIG_AV1_DECODER=1 -DCONFIG_AV1_ENCODER=1 -DENABLE_CCACHE=1 -DCONFIG_LPF_MASK=1 -DENABLE_TOOLS=1 -DENABLE_EXAMPLES=1 '
#			'-DCONFIG_MULTITHREAD=1 -DCONFIG_PIC=1 -DCONFIG_COEFFICIENT_RANGE_CHECKING=0 '
#			'-DCONFIG_RUNTIME_CPU_DETECT=1 -DCONFIG_WEBM_IO=1 '
#			'-DCONFIG_SPATIAL_RESAMPLING=1 -DENABLE_NASM=on' # 2018.11.23 enable nasm
#		,
#		'depends_on' : [ 'libxml2' ],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'aom-av1' },
#	},
	


