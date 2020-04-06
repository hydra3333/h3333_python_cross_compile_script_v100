{
	'repo_type' : 'git',
	#'depth_git' : 0,
	#'branch' : '',											
	'url' : 'https://github.com/AviSynth/AviSynthPlus',
	'recursive_git' : True,
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DHEADERS_ONLY:bool=on ',
	'conf_system' : 'cmake',
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'AviSynthPlus headers' },
}
