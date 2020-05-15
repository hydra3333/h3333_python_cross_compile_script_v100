{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/vorbis.git',
	#'depth_git' : 0,
	#'branch' : '30c490373b740f357d219c9e9672698d739f11f3', # 2020.04.08 something broke after this commit :(
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF ',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DINSTALL_CMAKE_PACKAGE_MODULE=ON ',
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
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'vorbis' },
}
