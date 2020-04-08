{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/vorbis.git',
	'#depth_git' : 0,
	#'branch' : '30c490373b740f357d219c9e9672698d739f11f3', # 2020.04.08 something broke after this commit :(
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF ',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DINSTALL_CMAKE_PACKAGE_MODULE=ON ',
	'patches' : [ # 2020.04.08 TEMPORARY patch since they broke compatibility with commit https://github.com/xiph/vorbis/commit/ffcd784bca8b02606014f2bb43d43a6d5dcfc8ae#commitcomment-38360217
		('https://github.com/xiph/vorbis/pull/62.patch', '-p1', '..'), # temporary; I submitted that patch, I assume it'll get merged soon.
	],
	'regex_replace': {
		'post_install': [
			# {
			# 	0: r'Libs: -L${{libdir}} -lvorbisenc[^\n]+',
			# 	1: r'Libs: -L${{libdir}} -lvorbisenc -lvorbis -logg',
			# 	'in_file': '{pkg_config_path}/vorbisenc.pc'
			# },
			# {
			# 	0: r'Libs: -L${{libdir}} -lvorbis[^\n]+',
			# 	1: r'Libs: -L${{libdir}} -lvorbis -logg',
			# 	'in_file': '{pkg_config_path}/vorbis.pc'
			# }
			{
				0: r'Requires\.private:',
				1: r'Requires:',
				'in_file': '{pkg_config_path}/vorbisenc.pc'
			},
			{
				0: r'Requires\.private:',
				1: r'Requires:',
				'in_file': '{pkg_config_path}/vorbis.pc'
			},
		]
	},
	'depends_on': ['libogg',],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'vorbis' },
}
# 2019.12.13 old:
#	'libvorbis' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/xiph/vorbis.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
#		'run_post_install': (
#			'sed -i.bak \'s/Libs: -L${{libdir}} -lvorbisenc/Libs: -L${{libdir}} -lvorbisenc -lvorbis -logg/\' "{pkg_config_path}/vorbisenc.pc"', # dunno why ffmpeg doesnt work with Requires.private
#			'sed -i.bak \'s/Libs: -L${{libdir}} -lvorbis/Libs: -L${{libdir}} -lvorbis -logg/\' "{pkg_config_path}/vorbis.pc"', # dunno why ffmpeg doesnt work with Requires.private
#		),
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'vorbis' },
#	},