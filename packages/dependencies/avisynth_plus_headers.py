{
	'repo_type' : 'git',
	#'depth_git' : 0,
	#'branch' : '',											
	'url' : 'https://github.com/AviSynth/AviSynthPlus',
	'source_subfolder' : 'avisynth-build',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DHEADERS_ONLY:bool=on ',
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Avisynth+ (Headers only)' },
}
