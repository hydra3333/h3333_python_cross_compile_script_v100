{
	'repo_type' : 'git',
	'url' : 'https://github.com/erikd/libsamplerate.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DLIBSAMPLERATE_EXAMPLES=OFF -DBUILD_TESTING=OFF -DLIBSAMPLERATE_TESTS=OFF -DBUILD_SHARED_LIBS=0 -DLIBSAMPLERATE_ENABLE_SANITIZERS=OFF -DCMAKE_BUILD_TYPE=Release -DHAVE_SQLITE3=ON ',
	'run_post_regexreplace' : [
		'sh ./autogen.sh',
	],
	'depends_on' : [
		'libflac', 'fftw3', 'libopus', 'sqlite3',
	], # 2019.12.13 chanaged fftw to fftw3
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libsamplerate' },
}
