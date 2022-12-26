{
	'repo_type' : 'git',
	'url' : 'https://github.com/breakfastquay/rubberband.git',
	'depth_git' : 0,
	#'branch': 'e90f377600d6097c6e37d0824f98bf60f77a0841',
	'branch': 'default', # "default" is another 'merican race/colour word mis-use/move away from master as a plain word # fatal: reference is not a tree: cc13a41fd5888a0c1f9f1b6525e32810b584f6ea
	'download_header' : [
		# at https://www.ladspa.org/ladspa_sdk/download.html 
		# 2022.09.26 http://www.ladspa.org/download/ladspa_sdk_1.17.tgz
		#'https://raw.githubusercontent.com/DeadSix27/python_cross_compile_script/master/additional_headers/ladspa.h',
		'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/ladspa.h', 
	],
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	# building the command-line utility aborts, so do not build it see if '-Dcmdline=disabled ' works
	#'run_post_regexreplace' : [  # 2022.12.18 per DEADSIX27 see if 
	#	# building the command-line utility aborts, so do not build it
	#	'sed -i \'s|if have_sndfile|\#if have_sndfile # building the command-line utility aborts, so do not build it\\nif false|\' ../meson.build',
	#],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static --strip '
		'--buildtype=release '
		'--backend=ninja '
		'-Dtests=disabled '
        '-Dcmdline=disabled '
		'-Dresampler=libsamplerate '
		'-Dfft=fftw '
		#'-Ddefault_library=static ' # 2022.12.18 per DEADSIX27. "ERROR: Got argument default_library as both -Ddefault_library and --default-library. Pick one."
		#'-Dno_shared=true '
		#'-DUSE_PTHREADS=true '
		#'-Dhave_posix_memalign=true '
		#'-Dhave_fftw3=true '
		#-Dextra_include_dirs=???
		#-Dextra_lib_dirs=???
		'--cross-file={meson_env_file} ./ ..'
	,
	'depends_on' : [
		'libsamplerate', 'libopus', 'libogg', 'libvorbis', 'libflac', 'libsndfile', 'vamp_plugin', 'fftw3',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'rubberband' },
}
#make: unrecognized option '--host=x86_64-w64-mingw32'
#make: unrecognized option '--prefix=/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32'
#make: unrecognized option '--libdir=/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib'
#make: unrecognized option '--disable-programs'
#Usage: make [options] [target] ...
