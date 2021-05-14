{ # AviSynth+
# FFmpeg can read AviSynth scripts as input. 
# To enable support, pass --enable-avisynth to configure after installing the headers provided by AviSynth+. 
# AviSynth+ can be configured to install only the headers by either passing -DHEADERS_ONLY:bool=on 
# to the normal CMake-based build system, or by using the supplied GNUmakefile.
# For Windows, supported AviSynth variants are AviSynth 2.6 RC1 or higher for 32-bit builds and AviSynth+ r1718 or higher for 32-bit and 64-bit builds.
# In 2016, AviSynth+ added support for building with GCC. However, due to the eccentricities of Windows’ calling conventions, 
# 32-bit GCC builds of AviSynth+ are not compatible with typical 32-bit builds of FFmpeg.
# By default, FFmpeg assumes compatibility with 32-bit MSVC builds of AviSynth+ since that is the most widely-used and entrenched build configuration. 
# Users can override this and enable support for 32-bit GCC builds of AviSynth+ by passing -DAVSC_WIN32_GCC32 to --extra-cflags when configuring FFmpeg.
# 64-bit builds of FFmpeg are not affected, and can use either MSVC or GCC builds of AviSynth+ without any special flags.
# AviSynth(+) is loaded dynamically. 
# Distributors can build FFmpeg with --enable-avisynth, and the binaries will work regardless of the end user having AviSynth installed. 
# If/when an end user would like to use AviSynth scripts, then they can install AviSynth(+) and FFmpeg will be able to find and use it to open scripts.
	'repo_type' : 'git',
	#'depth_git' : 0,
	#'branch' : '',											
	'url' : 'https://github.com/AviSynth/AviSynthPlus',
	'source_subfolder' : 'avisynth-build',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DHEADERS_ONLY:bool=on ',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Avisynth+ (Headers only)' },
}
