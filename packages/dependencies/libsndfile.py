{
	'repo_type' : 'git',
	'url' : 'https://github.com/erikd/libsndfile.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_PROGRAMS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DENABLE_BOW_DOCS=OFF -DENABLE_STATIC_RUNTIME=ON -DCMAKE_BUILD_TYPE=Release', # 2019.12.13 perhaps -DENABLE_TEST_COVERAGE=OFF
	'depends_on' : [ 'libspeex', 'libogg', 'libvorbis', 'libflac', 'libsamplerate', 'libopus' ], # 2019.12.13
	# 'run_post_install' : [ # -lspeex
	# 	'sed -i.bak \'s/Libs: -L${{libdir}} -lsndfile/Libs: -L${{libdir}} -lsndfile -lopus -lFLAC -lvorbis -lvorbisenc -logg/\' "{pkg_config_path}/sndfile.pc"',  # -lssp
	# ],
    'custom_cflag' : '{original_cflags}', # 2019.12.13
	'regex_replace': {
		'post_install': [
			{
				0: r'^Requires:([\n\r\s]+)?$',
				1: r'Requires: opus flac vorbis vorbisenc ogg speex\1', # 2019.12.13
				'in_file': '{pkg_config_path}/sndfile.pc'
			},
		],
	},
	'_info' : { 'version' : None, 'fancy_name' : 'libsndfile' },
}