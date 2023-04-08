{
# 2021.01.31 we could consider adding libdeflate for libtiff : https://github.com/ebiggers/libdeflate/tags
	'repo_type' : 'git',
	'url' : 'https://gitlab.com/libtiff/libtiff.git',
	#'repo_type' : 'archive',
	#'download_locations' : [
	#	{ 'url' : 'https://download.osgeo.org/libtiff/tiff-4.4.0.tar.xz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '49307b510048ccc7bc40f2cba6e8439182fe6e654057c1a1683139bf2ecb1dc1' }, ], },
	#	{ 'url' : 'https://fossies.org/linux/misc/tiff-4.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '49307b510048ccc7bc40f2cba6e8439182fe6e654057c1a1683139bf2ecb1dc1' }, ], },
	#],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'custom_cflag' : '-O3 -fstack-protector-all', # 2019.12.13 remove fortify_source so that it builds
	#'configure_options' : '.. {cmake_prefix_options} -DWebP_LIBRARIES=-lsharpyuv -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release', # 2022.12.18 from deadsix27
	'configure_options' : '.. {cmake_prefix_options} -Dtiff-tools=OFF -Dtiff-docs=OFF -Dtiff-contrib=OFF -Dtiff-tests=OFF -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release', # 2022.12.18 from deadsix27
    #'patches' : [ # 2022.12.18 from deadsix27
	#	('tiff/tiff1.patch', '-p1', ".."),
	#],
	'regex_replace': {
		'post_install': [
			{
				0: r'Libs: -L[^\n]+',
				#1: r'Libs: -L${{libdir}} -ltiff -lwebp -llzma -ljpeg -lz -',  # 2022.12.18 from deadsix27
				1: r'Libs: -L${{libdir}} -ltiff -lwebp -llzma -ljpeg -lz',
				'in_file': '{pkg_config_path}/libtiff-4.pc'
			}
		]
	},
	'run_post_regexreplace' : [
		'pwd ; cd .. ; sh ./autogen.sh ; cd _build ; pwd',
	],
	'depends_on' : [
		'zlib', 'libjpeg-turbo', 'libwebp',
	],
	#'update_check' : { 'url' : 'https://download.osgeo.org/libtiff/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'tiff-(?P<version_num>[\d.]+)\.tar\.gz' }, # problematic since optional rcx at the end of version numbers :(
	#'_info' : { 'version' : '4.4.0', 'fancy_name' : 'libtiff' },
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libtiff' },
}
