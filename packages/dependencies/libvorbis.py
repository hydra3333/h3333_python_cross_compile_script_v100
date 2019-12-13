{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/vorbis.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release',
	#'run_post_install': ( # 2019.12.13 see if it still needss this
	#	'sed -i.bak \'s/Libs: -L${{libdir}} -lvorbisenc/Libs: -L${{libdir}} -lvorbisenc -lvorbis -logg/\' "{pkg_config_path}/vorbisenc.pc"',  # 2019.12.13 see if it still needs this, probably not
	#	'sed -i.bak \'s/Libs: -L${{libdir}} -lvorbis/Libs: -L${{libdir}} -lvorbis -logg/\' "{pkg_config_path}/vorbis.pc"',  # 2019.12.13 see if it still needs this, probably not
	#),
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
	'_info' : { 'version' : None, 'fancy_name' : 'vorbis' },
}
