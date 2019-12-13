{
	'repo_type' : 'git',
	'url' : 'https://github.com/OpenVisualCloud/SVT-VP9.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DCPPAN_BUILD=OFF -DCMAKE_BUILD_TYPE=Release',
	'run_post_patch' : [
		'sed -i.bak \'s/#include <Windows.h>/#include <windows.h>/\' ../Source/Lib/Codec/EbThreads.h',
	],
	'_info' : { 'version' : None, 'fancy_name' : 'SVT-VP9' },
}