{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/libpng/files/libpng16/1.6.39/libpng-1.6.39.tar.xz',	'hashes' : [ { 'type' : 'sha256', 'sum' : '1f4696ce70b4ee5f85f1e1623dc1229b210029fa4b7aee573df3e2ba7b036937' },	], },
		{ 'url' : 'https://fossies.org/linux/misc/libpng-1.6.39.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '1f4696ce70b4ee5f85f1e1623dc1229b210029fa4b7aee573df3e2ba7b036937' }, ],	},
	],
	'conf_system' : 'cmake',
	# 'custom_cflag' : '-fno-asynchronous-unwind-tables',
	'configure_options' : '. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_BUILD_TYPE=Release '
						'-DPNG_SHARED=OFF -DPNG_STATIC=ON -DPNG_TESTS=OFF -DPNG_BUILD_ZLIB=ON -DPNG_FRAMEWORK=OFF '
						'-DPNG_HARDWARE_OPTIMIZATIONS=ON -DPNG_DEBUG=OFF '
						'-DBUILD_SHARED_LIBS=OFF -DBUILD_BINARY=OFF  '
						,
	'patches' : [
		('libpng/libpng-1.6.39-apng.patch', '-p1'),
	],
	'run_post_patch' : [
		'pwd ; sh ./autogen.sh ; pwd',
	],
	'depends_on' : [ 'zlib', ],
	'update_check' : { 'url' : 'https://sourceforge.net/projects/libpng/files/libpng16/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '1.6.39', 'fancy_name' : 'libpng' },
}
