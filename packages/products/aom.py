{
	'repo_type' : 'git',
	'url' : 'https://aomedia.googlesource.com/aom',
	'depth_git': 0,
	#'branch': 'acc2adf9195ff4c5d061132d860d2fe38b28aa55', # 2020.03.19 comment out
	#'rename_folder' : 'aom_git',
	'conf_system' : 'cmake',
	'source_subfolder' : 'build',
	#
	# BUILD system configuration options can be found at the top of the CMakeLists.txt file found in the root of the AV1 repository, 
	# AV1 CODEC CONFIGURATION options can currently be found in the file build/cmake/aom_config_defaults.cmake.
	#
    # 2019.12.13 note: we make this a 64 bit build only with -DAOM_TARGET_CPU=x86_64 ... some may not prefer this.
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={output_prefix}/aom_git.installed '
		'-DAOM_TARGET_CPU={bit_name2} ' # '-DAOM_TARGET_CPU=x86_64 ' 
		'-DARCH_X86_64=1 '
		'-DCONFIG_GCC=1 '
		'-DCONFIG_RUNTIME_CPU_DETECT=1 '
		'-DBUILD_SHARED_LIBS=0 '
		'-DCONFIG_STATIC=1 '
		'-DCONFIG_SHARED=0 '
		'-DFORCE_HIGHBITDEPTH_DECODING=1 '
		'-DCONFIG_AV1_HIGHBITDEPTH=1 '
		'-DHAVE_PTHREAD_H=1 '
		#'-DENABLE_CCACHE=1 '
		#'-DCONFIG_LPF_MASK=1 ' # 2020.05.10 removed per https://bugs.chromium.org/p/aomedia/issues/detail?id=2684#c6
		'-DCONFIG_LIBYUV=1 '
		'-DCONFIG_MULTITHREAD=1 '
		'-DCONFIG_PIC=1 '
		'-DCONFIG_COEFFICIENT_RANGE_CHECKING=1 '
		'-DCONFIG_DENOISE=1 '
		'-DCONFIG_WEBM_IO=1 '
		'-DCONFIG_SPATIAL_RESAMPLING=1 '
		'-DENABLE_NASM=ON ' # YASM is preferred (default) # 2019.12.13 no, NASM is.
		'-DCONFIG_AV1_DECODER=1 '
		'-DCONFIG_AV1_ENCODER=1 '
		#'-DCONFIG_ANALYZER=1 '
		#'-DCONFIG_ACCOUNTING=1 '
		#'-DCONFIG_INSPECTION=1 '
		'-DENABLE_TOOLS=1 '
		'-DENABLE_EXAMPLES=1 '
		'-DENABLE_DOCS=1 '
		'-DENABLE_TESTS=0 '
		'-DENABLE_TESTDATA=0 '
		'-DAOM_EXTRA_C_FLAGS="{original_cflags}" '
		'-DAOM_EXTRA_CXX_FLAGS="{original_cflags}" '
		'-DLIBXML_STATIC=1 '
		'-DGLIB_STATIC_COMPILATION=1 '
	,
	'depends_on' : [ 'libxml2', ], # 2019.12.13 # 2020.05.12 removed 'glib2', 
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'aom-av1' },
}
