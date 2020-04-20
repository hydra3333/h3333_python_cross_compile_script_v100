{
	'repo_type' : 'git',
	'depth_git': 0,
	'url' : 'https://bitbucket.org/mpyne/game-music-emu.git',
	#'branch' : '97527b20a40e6a8ddc272e0c503fea254a0b8eb2', # 2020.04.20 COMMENTED OUT # 2020.03.19 try latest git master # 97527b20a40e6a8ddc272e0c503fea254a0b8eb2 works
	'conf_system' : 'cmake',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_UBSAN=OFF',
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'game-music-emu' },
}
# 2019.12.13 old:
#	'libgme_game_music_emu' : {
#		'repo_type' : 'git',
#		'url' : 'https://bitbucket.org/mpyne/game-music-emu.git',
#		'branch' : 'a8da3a1992d2e099201392d630d99ef2c3f070ee', # 2019.11.11
#		'conf_system' : 'cmake',
#		'configure_options': '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_UBSAN=OFF',
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'game-music-emu' },
#	},