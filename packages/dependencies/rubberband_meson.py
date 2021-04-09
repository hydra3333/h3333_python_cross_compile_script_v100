{
	'repo_type' : 'git',
	'url' : 'https://github.com/breakfastquay/rubberband.git',
	'depth_git' : 0,
	'branch' : 'default',
    'conf_system' : 'meson',
	'build_system' : 'ninja',
    'source_subfolder' : 'build',
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
   	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--backend=ninja '
		'-Dfft=fftw '
		'-Dresampler=libsamplerate '
		'-Dno_shared=true '
        #'-D_GNU_SOURCE=1 '
        #'-Dextra_include_dirs=/usr/include ' # to fix missing features.h
        #'-Dextra_include_dirs=/usr/include/x86_64-linux-gnu ' # per https://github.com/haskell/unix/issues/49#issuecomment-155227394 after sudo apt-get install --reinstall libc6-dev to solve Fatal error: sys/mman.h: No such file or directory
        '-Dextra_include_dirs=/usr/include,/usr/include/x86_64-linux-gnu ' # per https://github.com/haskell/unix/issues/49#issuecomment-155227394 after sudo apt-get install --reinstall libc6-dev to solve Fatal error: sys/mman.h: No such file or directory
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
	,
	'run_post_build' : [
		'ls -al',
		'ls -al ..',
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