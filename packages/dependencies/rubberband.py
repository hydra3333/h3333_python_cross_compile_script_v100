{
	'repo_type' : 'git',
	'url' : 'https://github.com/breakfastquay/rubberband.git',
	#'branch': 'cc13a41fd5888a0c1f9f1b6525e32810b584f6ea', # fatal: reference is not a tree: cc13a41fd5888a0c1f9f1b6525e32810b584f6ea
	'branch': 'default', # "default" is another 'merican race/colour word mis-use/move away from master as a plain word # fatal: reference is not a tree: cc13a41fd5888a0c1f9f1b6525e32810b584f6ea
    'depth_git' : 0,
	'download_header' : [
		#'https://raw.githubusercontent.com/DeadSix27/python_cross_compile_script/master/additional_headers/ladspa.h',
		'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/ladspa.h',
	],
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	# building the command-line utility aborts, so do not build it
	'run_post_regexreplace' : [
		# building the command-line utility aborts, so do not build it
		'sed -i \'s|if have_sndfile|\#if have_sndfile # building the command-line utility aborts, so do not build it\\nif false|\' ../meson.build',
	],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static --strip '
		'--buildtype=release '
		'--backend=ninja '
		'-Dno_shared=true '
		'-Dresampler=libsamplerate '
		'-Duse_pthreads=true '
		'-Dhave_posix_memalign=true '
		'-Dfft=fftw '
		'-Dhave_fftw3=true '
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
