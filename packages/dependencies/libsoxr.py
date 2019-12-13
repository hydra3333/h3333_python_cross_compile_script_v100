{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://download.videolan.org/contrib/soxr/soxr-0.1.3-Source.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b111c15fdc8c029989330ff559184198c161100a59312f5dc19ddeb9b5a15889' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/soxr/files/soxr-0.1.3-Source.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b111c15fdc8c029989330ff559184198c161100a59312f5dc19ddeb9b5a15889' }, ], },
	],
	'conf_system' : 'cmake',
	#'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release -DWITH_LSR_BINDINGS:bool=ON -DBUILD_LSR_TESTS:bool=OFF -DBUILD_EXAMPLES:bool=OFF -DBUILD_SHARED_LIBS:bool=off -DBUILD_TESTS:BOOL=OFF -DCMAKE_AR={cross_prefix_full}ar', #not sure why it cries about AR # 2019.12.13
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DHAVE_WORDS_BIGENDIAN_EXITCODE:bool=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_LSR_BINDINGS:bool=ON -DBUILD_LSR_TESTS:bool=OFF -DBUILD_EXAMPLES:bool=OFF -DBUILD_SHARED_LIBS:bool=off -DBUILD_TESTS:BOOL=OFF -DCMAKE_AR={cross_prefix_full}ar', #not sure why it cries about AR # 2019.12.13

	'patches' : [ # 2019.12.13 added 2 patches from Alexpux for 0.1.3
		('libsoxr/0001-libsoxr-fix-pc-file-installation.patch','-Np1'), # 2019.12.13
		('libsoxr/0002-libsoxr-fix-documentation-installation.patch','-Np1'), # 2019.12.13
	],
	'depends_on': [ # 2019.12.13
		'libvorbis','gettext', 'libopus', 'libflac', # 2019.12.13
	], # 2019.12.13
    'update_check' : { 'url' : 'https://sourceforge.net/projects/soxr/files/', 'type' : 'sourceforge', 'regex' : r'soxr-(?P<version_num>[\d.]+)-Source\.tar\.xz' },
	'_info' : { 'version' : '0.1.3', 'fancy_name' : 'soxr' },
}
