{
	'repo_type' : 'git',
	'depth_git': 0,
	'url' : 'https://bitbucket.org/mpyne/game-music-emu.git',
	#'branch' : '97527b20a40e6a8ddc272e0c503fea254a0b8eb2', # 2020.04.20 COMMENTED OUT # 2020.03.19 try latest git master # 97527b20a40e6a8ddc272e0c503fea254a0b8eb2 works
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_UBSAN=OFF',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'game-music-emu' },
}
