{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/libpng/files/libpng16/1.6.37/libpng-1.6.37.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca' },	], },
		{ 'url' : 'https://fossies.org/linux/misc/libpng-1.6.37.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca' }, ],	},
	],
	'conf_system' : 'cmake',
	# 'custom_cflag' : '-fno-asynchronous-unwind-tables',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release '
						'-DPNG_SHARED=OFF -DPNG_STATIC=ON -DPNG_TESTS=OFF -DPNG_BUILD_ZLIB=ON -DPNG_FRAMEWORK=OFF '
						'-DPNG_HARDWARE_OPTIMIZATIONS=ON -DPNG_DEBUG=OFF '
						'-DBUILD_SHARED_LIBS=OFF -DBUILD_BINARY=OFF  '
						
	'patches' : [
		('libpng/libpng-1.6.37-apng.patch', '-p1'),
	],
	'run_post_patch' : [
		'pwd ; sh ./autogen.sh ; pwd',
	],
	'depends_on' : [ 'zlib', ],
	'update_check' : { 'url' : 'https://sourceforge.net/projects/libpng/files/libpng16/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '1.6.37', 'fancy_name' : 'libpng' },
}
