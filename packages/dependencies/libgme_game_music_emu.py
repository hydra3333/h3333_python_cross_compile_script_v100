{
	'repo_type' : 'git',
	'depth_git': 0,
	'url' : 'https://bitbucket.org/mpyne/game-music-emu.git',
	'branch' : '97527b20a40e6a8ddc272e0c503fea254a0b8eb2', # 2019.12.13 a different commit to mine
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_UBSAN=OFF',
	'_info' : { 'version' : None, 'fancy_name' : 'game-music-emu' },
}