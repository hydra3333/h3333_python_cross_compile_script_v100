{
	'repo_type' : 'git',
	'url' : 'https://github.com/erikd/libsndfile.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DENABLE_PACKAGE_CONFIG=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_PROGRAMS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DENABLE_BOW_DOCS=OFF -DENABLE_STATIC_RUNTIME=ON -DENABLE_EXPERIMENTAL=ON -DENABLE_EXTERNAL_LIBS=ON -DHAVE_SQLITE3=OFF -DHAVE_ALSA_ASOUNDLIB_H=OFF ', 
	'depends_on' : [ 'libspeex', 'libogg', 'libvorbis', 'libflac', 'libsamplerate', 'libopus' ], # 2019.12.13
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
	'_info' : { 'version' : None, 'fancy_name' : 'libsndfile' },
}
# 2019.12.13 old:
#	'libsndfile' : { 
#		'repo_type' : 'git',
#		'url' : 'https://github.com/erikd/libsndfile.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-sqlite --disable-test-coverage --enable-external-libs --enable-experimental', # --enable-sqlite 
#		'run_post_patch': [
#			'autoreconf -fiv -I M4',
#		],
#		'env_exports' : {
#			'PKGCONFIG' : 'pkg-config',
#			'CFLAGS'   : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CXXFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'CPPFLAGS' : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#			'LDFLAGS'  : '{original_cflags}', # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		},
#		'run_post_install' : [
#			'sed -i.bak \'s/Libs: -L${{libdir}} -lsndfile/Libs: -L${{libdir}} -lsndfile -lopus -lFLAC -lFLAC++ -lvorbis -lvorbisenc -logg -lspeex/\' "{pkg_config_path}/sndfile.pc"', #issue with rubberband not using pkg-config option "--static" or so idk?
#			#'sed -i.bak \'s/Libs: -L${{libdir}} -lsndfile/Libs: -L${{libdir}} -lsndfile -lopus -lvorbis -lvorbisenc -logg -lspeex/\' "{pkg_config_path}/sndfile.pc"', #issue with rubberband not using pkg-config option "--static" or so idk?
#		],
#		'custom_cflag' : '{original_cflags}', # 2019.10.19 D_FORTIFY_SOURCE=0' # 2019.11.10 add -fstack-protector-all -D_FORTIFY_SOURCE=2
#		'depends_on': [ 'libspeex', 'libopus', 'libogg', 'libvorbis', 'libflac', ],
#		'packages': {
#			'arch' : [ 'autogen' ],
#		},
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libsndfile' },
#	},
#
#option (BUILD_SHARED_LIBS "Build shared libraries" OFF)
#if (BUILD_SHARED_LIBS AND BUILD_TESTING)
#	set (BUILD_TESTING OFF)
#	message ("Build testing required static libraries. To prevent build errors BUILD_TESTING disabled.")
#endif ()
#option (BUILD_PROGRAMS "Build programs" ON)
#option (BUILD_EXAMPLES "Build examples" ON)
#option (ENABLE_CPACK "Enable CPack support" ON)
#option (ENABLE_EXPERIMENTAL "Enable experimental code" OFF)
#option (ENABLE_BOW_DOCS "Enable black-on-white html docs" OFF)
#if (MSVC OR MINGW)
#	option (ENABLE_#STATIC_RUNTIME "Enable static runtime" OFF)
#endif ()
#option (ENABLE_PACKAGE_CONFIG "Generate and install package config file" ON)
#cmake_dependent_option (BUILD_REGTEST "Build regtest" ON "SQLITE3_FOUND" OFF)
#cmake_dependent_option (ENABLE_EXTERNAL_LIBS "Enable FLAC, Vorbis, and Opus codecs" ON "VORBISENC_FOUND;FLAC_FOUND;OPUS_FOUND" OFF)
#cmake_dependent_option (ENABLE_CPU_CLIP "Enable tricky cpu specific clipper" ON "CPU_CLIPS_POSITIVE;CPU_CLIPS_NEGATIVE" OFF)
#cmake_dependent_option (ENABLE_COMPATIBLE_LIBSNDFILE_NAME "Set DLL name to libsndfile-1.dll (canonical name), sndfile.dll otherwise" OFF "WIN32;NOT MINGW;BUILD_SHARED_LIBS" OFF)
#set (HAVE_EXTERNAL_XIPH_LIBS ${ENABLE_EXTERNAL_LIBS})
#set (HAVE_SQLITE3 ${BUILD_REGTEST})
#set (HAVE_ALSA_ASOUNDLIB_H ${ALSA_FOUND})
#set (HAVE_SNDIO_H ${SNDIO_FOUND})
#set (ENABLE_EXPERIMENTAL_CODE ${ENABLE_EXPERIMENTAL})
#set (HAVE_SPEEX ${ENABLE_EXPERIMENTAL})
#set (HAVE_OPUS ${ENABLE_EXPERIMENTAL})
#add_feature_info (BUILD_SHARED_LIBS BUILD_SHARED_LIBS "build shared libraries")
#add_feature_info (ENABLE_EXTERNAL_LIBS ENABLE_EXTERNAL_LIBS "enable FLAC, Vorbis, and Opus codecs")
#add_feature_info (ENABLE_EXPERIMENTAL ENABLE_EXPERIMENTAL "enable experimental code")
#add_feature_info (BUILD_TESTING BUILD_TESTING "build tests")
#add_feature_info (BUILD_REGTEST BUILD_REGTEST "build regtest")
#add_feature_info (ENABLE_CPACK ENABLE_CPACK "enable CPack support")
#add_feature_info (ENABLE_CPU_CLIP ENABLE_CPU_CLIP "Enable tricky cpu specific clipper")
#add_feature_info (ENABLE_BOW_DOCS ENABLE_BOW_DOCS "enable black-on-white html docs")
#add_feature_info (ENABLE_PACKAGE_CONFIG ENABLE_PACKAGE_CONFIG "generate and install package config file")
#if (MSVC OR MINGW)
#	add_feature_info (ENABLE_STATIC_RUNTIME ENABLE_STATIC_RUNTIME "Enable static runtime")
#endif ()