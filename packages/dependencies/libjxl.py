#type:ignore
{
	'repo_type' : 'git',
	'url' : 'https://github.com/libjxl/libjxl',
	'depth_git': 0,
	'branch': 'main',
	'conf_system' : 'cmake',
	'build_system' : 'ninja',
    'patches': [
		#('libjxl/0001-Fix-building-on-MinGW.patch', '-p1','..'),
		('https://raw.githubusercontent.com/m-ab-s/mabs-patches/master/libjxl/0001-brotli-add-ldflags.patch', '-p1', '..'),
    ],
	'source_subfolder' : 'build',
	'env_exports' : { # 2020.06.19
		'CFLAGS'   : ' -Wa,-muse-unaligned-vector-move {original_cflags}',
		'CXXFLAGS' : ' -Wa,-muse-unaligned-vector-move {original_cflags}',
		'CPPFLAGS' : ' -Wa,-muse-unaligned-vector-move {original_cflags}',
	},
	'run_post_patch' : [
		'!SWITCHDIR|..',
		'./deps.sh',
		'!SWITCHDIR|build',
		'sed -i.bak \'/add_custom_target\(all_tests/d\' "../CMakeLists.txt"',
		'sed -i.bak \'/add_dependencies\(all_tests/d\' "../CMakeLists.txt"',
		'cat "../CMakeLists.txt"',
	],
	'regex_replace': {
		"post_install": [
			{
				0: r"Cflags: -I\${includedir}\n",
				1: r"Cflags: -I${includedir}  -DJXL_STATIC_DEFINE\n",
				"in_file": "{pkg_config_path}/libjxl.pc",
			},
			{
				0: r"Cflags: -I\${includedir}\n",
				1: r"Cflags: -I${includedir} -DJXL_THREADS_STATIC_DEFINE\n",
				"in_file": "{pkg_config_path}/libjxl_threads.pc",
			},
			{
				0: r"Libs: -L\${libdir} -ljxl\n",
				1: r"Libs: -L${libdir} -ljxl -lstdc++\n",
				"in_file": "{pkg_config_path}/libjxl.pc",
			},
			{
				0: r"Libs: -L\${libdir} -ljxl_threads\n",
				1: r"Libs: -L${libdir} -ljxl_threads -lstdc++\n",
				"in_file": "{pkg_config_path}/libjxl_threads.pc",
			},
		],
	},
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
        '-DBUILD_SHARED_LIBS=false '
		'-DJPEGXL_ENABLE_TOOLS=false '
        '-DJPEGXL_ENABLE_JPEGLI=false '
		'-DJPEGXL_ENABLE_DOXYGEN=false '
		'-DJPEGXL_ENABLE_MANPAGES=false '
		'-DJPEGXL_ENABLE_BENCHMARK=false '
		'-DJPEGXL_ENABLE_EXAMPLES=false '
        '-DJPEGXL_ENABLE_VIEWERS=false '
        '-DJPEGXL_ENABLE_DEVTOOLS=false '
        '-DJPEGXL_ENABLE_SJPEG=true '
		'-DJPEGXL_ENABLE_OPENEXR=true '
		'-DJPEGXL_ENABLE_SKCMS=true '
        '-DJPEGXL_ENABLE_JNI=false '
        '-DJPEGXL_EMSCRIPTEN=false '
        '-DJPEGXL_FORCE_SYSTEM_BROTLI=true '
        '-DJPEGXL_FORCE_SYSTEM_LCMS2=true '
        '-DJPEGXL_FORCE_SYSTEM_HWY=true '
		'-DJPEGXL_ENABLE_JPEGLI_LIBJPEG=true '
		'-DBUILD_TESTING=false '
		'-DJPEGXL_STATIC=true '
		'-DJPEGXL_BUNDLE_LIBPNG=false '
	,
	'depends_on' : [  "libbrotli", "highway", "libpng", "lcms2", "libjpeg-turbo", "zlib" ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git main', 'fancy_name' : 'libjxl' },
}