{
	'repo_type' : 'git',
	'url' : 'https://github.com/erikd/libsndfile.git',
	'depth_git' : 0,
	#'branch' : '4bdd7414602946a18799b514001b0570e8693a47', # 2020.04.20 COMMENTED OUT # see if this fixes vamp build error
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_PROGRAMS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DENABLE_BOW_DOCS=OFF -DENABLE_PACKAGE_CONFIG=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_STATIC_RUNTIME=ON -DHAVE_SQLITE3=OFF -DHAVE_ALSA_ASOUNDLIB_H=OFF -DENABLE_EXTERNAL_LIBS=ON ', # -DENABLE_EXPERIMENTAL=ON -DENABLE_EXTERNAL_LIBS=ON ', 
	'depends_on' : [ 'libogg', 'libvorbis', 'libflac', 'libsamplerate', 'libopus', 'libspeex' ], # 2019.12.13
	# 'run_post_install' : [ # -lspeex
	# 	'sed -i.bak \'s/Libs: -L${{libdir}} -lsndfile/Libs: -L${{libdir}} -lsndfile -lopus -lFLAC -lvorbis -lvorbisenc -logg/\' "{pkg_config_path}/sndfile.pc"',  # -lssp
	# ],
	'regex_replace': {
		'post_install': [
			{
				0: r'^Requires:([\n\r\s]+)?$',
				1: r'Requires: opus flac vorbis vorbisenc ogg speex\1', # 2019.12.13
				'in_file': '{pkg_config_path}/sndfile.pc'
			},
		],
	},
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libsndfile' },
}
