{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/shaderc.git', # https://github.com/google/shaderc.git
	'depth_git': 0, # 2020.03.11 per deadsix27 stay on last working commit
	'branch' : 'main',  # 2020.06.22 they've changed the trunk from master to main (a US political race thing against the word, apparently)
	'recursive_git' : True,
	'configure_options' :
		'cmake .. {cmake_prefix_options} '
		'-GNinja ' # 2021.11.01 per MABS
		'-DCMAKE_BUILD_TYPE=Release '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DSHADERC_SKIP_INSTALL=OFF '
		'-DSHADERC_SKIP_TESTS=ON '
		'-DSHADERC_SKIP_EXAMPLES=ON '
		'-DSHADERC_ENABLE_SHARED_CRT=OFF '
		'-DSHADERC_ENABLE_SPVC=ON '
		'-DSHADERC_ENABLE_WERROR_COMPILE=OFF ' # 2021.11.01 per MABS
		# 2022.06.26 
		'-DSHADERC_SKIP_COPYRIGHT_CHECK=ON '
        '-DENABLE_EXCEPTIONS=ON '
		'-DENABLE_CTEST=OFF '
		'-DENABLE_GLSLANG_BINARIES=OFF '
		'-DSPIRV_SKIP_EXECUTABLES=ON '
		'-DSPIRV_TOOLS_BUILD_STATIC=ON '
		'-DBUILD_SHARED_LIBS=OFF '
		'-DSKIP_GLSLANG_INSTALL=N '
		'-DSKIP_SPIRV_HEADERS_INSTALL=ON '
		'-DSKIP_SPIRV_CROSS_INSTALL=ON '
		'-DSKIP_SPIRV_TOOLS_INSTALL=ON '
		'-DSKIP_GOOGLETEST_INSTALL=ON '
	,
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
	#'needs_make_install' : False,
	'build_options' : '',
	'run_post_patch' : [ # 2020.04.08 eveything else uses run_post_regexreplace instead of run_post_patch, shaderc depends on run_post_patch
		'!SWITCHDIR|../third_party',
		'ln -snf {inTreePrefix}/glslang/ glslang',
		'ln -snf {inTreePrefix}/spirv-headers/ spirv-headers',
		'ln -snf {inTreePrefix}/spirv-tools/ spirv-tools',
		'ln -snf {inTreePrefix}/spirv-cross spirv-cross',
		'!SWITCHDIR|../_build',
		"sed -i 's/add_subdirectory(examples)/#add_subdirectory(examples)/g' ../CMakeLists.txt",
		"sed -i 's/--check/#--check/g' ../CMakeLists.txt",
		"sed -i 's/printed_count += 1/#printed_count += 1/g' ../utils/add_copyright.py", # 2021.02.27 grr since it fails with glslang, ignore errors
		'if [ -f "{target_prefix}/lib/libshaderc.a" ] ; then rm -fv "{target_prefix}/lib/libshaderc.a" ; fi',
		'if [ -f "{target_prefix}/lib/libshaderc_combined.a" ] ; then rm -fv "{target_prefix}/lib/libshaderc_combined.a" ; fi',
		'if [ -d "{target_prefix}/include/shaderc" ] ; then rm -fvR "{target_prefix}/include/shaderc" ; fi',
		'if [ -d "{target_prefix}/include/libshaderc_util" ] ; then rm -fvR "{target_prefix}/include/libshaderc_util" ; fi',
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r'#define snprintf sprintf_s',
				'in_file': '../third_party/glslang/glslang/Include/Common.h'
			},
		],
	},
	'run_post_build' : [
		'cp -frv "../libshaderc/include/shaderc" "{target_prefix}/include/"',
		'cp -frv "../libshaderc_util/include/libshaderc_util" "{target_prefix}/include/"',
		'cp -frv "libshaderc/libshaderc_combined.a" "{target_prefix}/lib/libshaderc_combined.a"',
		'cp -frv "libshaderc/libshaderc.a" "{target_prefix}/lib/libshaderc.a"',
	],
	#
	'patches' : [
		('shaderc/0001-third_party-set-INSTALL-variables-as-cache-MABS-2022.06.28.patch', '-Np1', '..'),
		('shaderc/0002-shaderc_util-add-install-MABS-2022.06.28.patch',' -Np1', '..'),
	],
	'depends_on' : [ 'spirv-headers', 'spirv-cross', 'spirv-tools', 'glslang', ],

	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'shaderc' },
}
