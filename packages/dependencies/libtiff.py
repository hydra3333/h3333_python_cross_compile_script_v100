{
# 2021.01.31 we could consider adding libdeflate for libtiff : https://github.com/ebiggers/libdeflate/tags
	'repo_type' : 'archive',
	'download_locations' : [
		#{ 'url' : 'https://download.osgeo.org/libtiff/tiff-4.1.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5d29f32517dadb6dbcd1255ea5bbc93a2b54b94fbf83653b4d65c7d6775b8634' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/tiff-4.1.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5d29f32517dadb6dbcd1255ea5bbc93a2b54b94fbf83653b4d65c7d6775b8634' }, ], },
		#{ 'url' : 'https://download.osgeo.org/libtiff/tiff-4.2.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'eb0484e568ead8fa23b513e9b0041df7e327f4ee2d22db5a533929dfc19633cb' }, ], },
		#{ 'url' : 'https://fossies.org/linux/misc/tiff-4.2.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'eb0484e568ead8fa23b513e9b0041df7e327f4ee2d22db5a533929dfc19633cb' }, ], },
		{ 'url' : 'https://download.osgeo.org/libtiff/tiff-4.3.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0e46e5acb087ce7d1ac53cf4f56a09b221537fc86dfc5daaad1c2e89e1b37ac8' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/tiff-4.3.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : '0e46e5acb087ce7d1ac53cf4f56a09b221537fc86dfc5daaad1c2e89e1b37ac8' }, ], },
	],
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'custom_cflag' : '-O3 -fstack-protector-all', # 2019.12.13 remove fortify_source so that it builds
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release',
	'regex_replace': {
		'post_install': [
			{
				0: r'Libs: -L[^\n]+',
				1: r'Libs: -L${{libdir}} -ltiff -lwebp -llzma -ljpeg -lz',
				'in_file': '{pkg_config_path}/libtiff-4.pc'
			}
		]
	},
	'depends_on' : [
		'zlib', 'libjpeg-turbo', 'libwebp',
	],
	'update_check' : { 'url' : 'https://download.osgeo.org/libtiff/?C=M;O=D', 'type' : 'httpindex', 'regex' : r'tiff-(?P<version_num>[\d.]+)\.tar\.gz' },
	#'_info' : { 'version' : '4.1.0', 'fancy_name' : 'libtiff' },
	'_info' : { 'version' : '4.3.0', 'fancy_name' : 'libtiff' },
}
# 2019.12.13 old:
# none
#
# fails to build, with
#FAILED: libtiff/CMakeFiles/tiffxx.dir/tif_stream.cxx.obj 
#/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-g++ --sysroot=/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32  -DNEED_LIBPORT -D_FILE_OFFSET_BITS=64 -I../libtiff -Ilibtiff -I/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include -O3  -fstack-protector-all  -D_FORTIFY_SOURCE=2 -O3 -DNDEBUG -MD -MT libtiff/CMakeFiles/tiffxx.dir/tif_stream.cxx.obj -MF libtiff/CMakeFiles/tiffxx.dir/tif_stream.cxx.obj.d -o libtiff/CMakeFiles/tiffxx.dir/tif_stream.cxx.obj -c ../libtiff/tif_stream.cxx
#In file included from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/ext/string_conversions.h:43,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/bits/basic_string.h:6493,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/string:55,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/bits/locale_classes.h:40,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/bits/ios_base.h:41,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/ios:42,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/ostream:38,
#                 from /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/iostream:39,
#                 from ../libtiff/tif_stream.cxx:29:
#/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/cstdio:175:11: error: '::snprintf' has not been declared
#  175 |   using ::snprintf;
#      |           ^~~~~~~~
#/home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/include/c++/9.2.0/cstdio:185:22: error: '__gnu_cxx::snprintf' has not been declared
#  185 |   using ::__gnu_cxx::snprintf;
#      |                      ^~~~~~~~
#[7/125] Building C object libtiff/CMakeFiles/tiff.dir/tif_color.c.obj
#[8/125] Building C object libtiff/CMakeFiles/tiff.dir/tif_compress.c.obj
#[9/125] Building C object libtiff/CMakeFiles/tiff.dir/tif_dir.c.obj
#ninja: build stopped: subcommand failed.
#[21:52:51][ERROR] Error [1] running process: 'ninja -j 4 ' in '/home/u/Desktop/_working/workdir/x86_64/tiff-4.1.0/_build'
#[21:52:51][ERROR] You can try deleting the product/dependency folder: '/home/u/Desktop/_working/workdir/x86_64/tiff-4.1.0/_build' and re-run the script
#

