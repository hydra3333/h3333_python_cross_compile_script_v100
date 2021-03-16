{
	'repo_type' : 'git',
	'url' : 'https://github.com/breakfastquay/rubberband.git',
	'depth_git' : 0,
	#'branch' : 'default',
	'branch' : '57d680a8e3a6523a4151315f99dfa7fa60260c7e', # this is athe last commit which has aconfigure. meson builds fail to build :(
	'download_header' : [
		'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/ladspa.h',
		#'https://www.ladspa.org/ladspa_sdk/ladspa.h.txt',
	],
	'env_exports' : {
		'AR': '{cross_prefix_bare}ar',
		'CC': '{cross_prefix_bare}gcc',
		'PREFIX': '{target_prefix}',
		'RANLIB': '{cross_prefix_bare}ranlib',
		'LD': '{cross_prefix_bare}ld',
		'STRIP': '{cross_prefix_bare}strip',
		'CXX': '{cross_prefix_bare}g++',
		'PKG_CONFIG': 'pkg-config --static'
	},
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static ', # 2019.12.13
	'build_options' : '{make_prefix_options}',
	'needs_make_install' : False,
	'run_post_build' : [
		'cp -fv lib/* "{target_prefix}/lib"',
		'cp -frv rubberband "{target_prefix}/include"',
		'cp -fv rubberband.pc.in "{pkg_config_path}/rubberband.pc"',
		'sed -i.bak "s|%PREFIX%|{target_prefix_sed_escaped}|" "{pkg_config_path}/rubberband.pc"',
		'sed -i.bak \'s/-lrubberband *$/-lrubberband -lfftw3 -lsamplerate -lstdc++/\' "{pkg_config_path}/rubberband.pc"',
	],
	'depends_on' : [
		'libsamplerate', 'libopus', 'libogg', 'libvorbis', 'libflac', 'libsndfile', 'vamp_plugin', 'fftw3', # 2019.12.13 also changed fft3 to fftw3
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (default)', 'fancy_name' : 'rubberband' },
}
#{
#	'repo_type' : 'git',
#	'url' : 'https://github.com/breakfastquay/rubberband.git',
#	'depth_git' : 0,
#	'branch' : 'default',
#    'conf_system' : 'meson',
#	'build_system' : 'ninja',
#    'source_subfolder' : 'build',
#	'download_header' : [
#		'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/ladspa.h',
#		#'https://www.ladspa.org/ladspa_sdk/ladspa.h.txt',
#	],
#	'env_exports' : {
#		'AR': '{cross_prefix_bare}ar',
#		'CC': '{cross_prefix_bare}gcc',
#		'PREFIX': '{target_prefix}',
#		'RANLIB': '{cross_prefix_bare}ranlib',
#		'LD': '{cross_prefix_bare}ld',
#		'STRIP': '{cross_prefix_bare}strip',
#		'CXX': '{cross_prefix_bare}g++',
#		'PKG_CONFIG': 'pkg-config --static'
#	},
#   	'configure_options' :
#		'--prefix={target_prefix} '
#		'--libdir={target_prefix}/lib '
#		'--default-library=static '
#		'--backend=ninja '
#		'-Dfft=fftw '
#		'-Dresampler=libsamplerate '
#		'-Dno_shared=true '
#		'--buildtype=release '
#		'--cross-file={meson_env_file} ./ ..'
#	,
#	'run_post_build' : [
#		'ls -al',
#		'ls -al ..',
#		'cp -fv lib/* "{target_prefix}/lib"',
#		'cp -frv rubberband "{target_prefix}/include"',
#		'cp -fv rubberband.pc.in "{pkg_config_path}/rubberband.pc"',
#		'sed -i.bak "s|%PREFIX%|{target_prefix_sed_escaped}|" "{pkg_config_path}/rubberband.pc"',
#		'sed -i.bak \'s/-lrubberband *$/-lrubberband -lfftw3 -lsamplerate -lstdc++/\' "{pkg_config_path}/rubberband.pc"',
#	],
#	'depends_on' : [
#		'libsamplerate', 'libopus', 'libogg', 'libvorbis', 'libflac', 'libsndfile', 'vamp_plugin', 'fftw3', # 2019.12.13 also changed fft3 to fftw3
#	],
#	'update_check' : { 'type' : 'git', },
#	'_info' : { 'version' : 'git (default)', 'fancy_name' : 'rubberband' },
#}