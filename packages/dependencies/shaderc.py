{
	'repo_type' : 'git',
	'url' : 'https://github.com/google/shaderc.git', # https://github.com/google/shaderc.git
	'depth_git': 0,
	'branch' : 'main',
	'recursive_git' : True,
	'source_subfolder' : '_build',
	'conf_system' : 'cmake',
	'configure_options' :
		'cmake .. {cmake_prefix_options} '
		'-GNinja ' # 2021.11.01 per MABS
		'-DCMAKE_BUILD_TYPE=Release '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DSHADERC_SKIP_INSTALL=OFF '
		'-DSHADERC_SKIP_TESTS=ON '
		'-DSHADERC_SKIP_EXAMPLES=ON '
		'-DSHADERC_SKIP_COPYRIGHT_CHECK=ON '
		'-DSHADERC_ENABLE_WERROR_COMPILE=OFF ' # 2021.11.01 per MABS
		'-DSHADERC_ENABLE_SHARED_CRT=OFF '
		'-DSHADERC_ENABLE_SPVC=ON '
		# 2022.06.26 
        '-DENABLE_EXCEPTIONS=ON '
		'-DENABLE_CTEST=OFF '
		'-DENABLE_GLSLANG_BINARIES=OFF '
		'-DSPIRV_SKIP_EXECUTABLES=ON '
		'-DSPIRV_TOOLS_BUILD_STATIC=ON '
		'-DBUILD_SHARED_LIBS=OFF '
		'-DSKIP_GLSLANG_INSTALL=ON '
		'-DSKIP_SPIRV_HEADERS_INSTALL=ON '
		'-DSKIP_SPIRV_CROSS_INSTALL=ON '
		'-DSKIP_SPIRV_TOOLS_INSTALL=ON '
		'-DSKIP_GOOGLETEST_INSTALL=ON '
	,
	'build_options' : '', # 2022.12.18 per DEADSIX27
	'run_post_patch' : [ # 2020.04.08 eveything else uses run_post_regexreplace instead of run_post_patch, shaderc depends on run_post_patch
		'!SWITCHDIR|../third_party',
		#'ln -snf {inTreePrefix}/glslang/ glslang',
		'ln -snf {inTreePrefix}/glslang_static_git/ glslang',
		'ls -al glslang/',
		'ln -snf {inTreePrefix}/spirv-headers/ spirv-headers',
		'ls -al spirv-headers/',
		'ln -snf {inTreePrefix}/spirv-tools/ spirv-tools',
		'ls -al spirv-tools/',
		'ln -snf {inTreePrefix}/spirv-cross spirv-cross',
		'ls -al spirv-cross/',
		'!SWITCHDIR|../_build',
		"sed -i 's/add_subdirectory(examples)/#add_subdirectory(examples)/g' ../CMakeLists.txt",
		"sed -i 's/--check/#--check/g' ../CMakeLists.txt",
		"sed -i 's/printed_count += 1/#printed_count += 1/g' ../utils/add_copyright.py", # 2021.02.27 grr since it fails with glslang, ignore errors
		'if [ -f "{target_prefix}/lib/libshaderc.a" ] ; then                rm -fv "{target_prefix}/lib/libshaderc.a" ; fi',
		'if [ -f "{target_prefix}/lib/libshaderc_combined.a" ] ; then       rm -fv "{target_prefix}/lib/libshaderc_combined.a" ; fi',
		'if [ -f "{target_prefix}/lib/pkgconfig/shaderc_shared.pc" ] ; then rm -fv "{target_prefix}/lib/pkgconfig/shaderc_shared.pc" ; fi',
		'if [ -f "{target_prefix}/lib/pkgconfig/shaderc.pc" ] ; then        rm -fv "{target_prefix}/lib/pkgconfig/shaderc.pc"; fi',
		'if [ -d "{target_prefix}/include/shaderc" ] ; then                 rm -fvR "{target_prefix}/include/shaderc" ; fi',
		'if [ -d "{target_prefix}/include/libshaderc_util" ] ; then         rm -fvR "{target_prefix}/include/libshaderc_util" ; fi',
		# The next sed's removes dependence on 3rd party commit numbers and instead relies on latest git heads
		# 2022.09.05 SHADERC depends on GLSLANG ... GLSLANG is "ahead" of SHADERC 
		#            and there is a mismatch, so we affix GLSLANG to a KNOWN GOOD COMMIT
		#            both in glslang.py and here in shaderc.py at 'glslang_revision'
		'sed -i "s/\'glslang_revision\':.*/\'glslang_revision\': \'1fb2f1d7896627d62a289439a2c3e750e551a7ab\',/g" ../DEPS',  # 2022.12.18 per DEADSIX27
		'sed -i "s/\'spirv_headers_revision\':.*/\'spirv_headers_revision\': \'\',/g" ../DEPS',
		'sed -i "s/\'spirv_tools_revision\':.*/\'spirv_tools_revision\': \'\',/g" ../DEPS',
	],
	'regex_replace': {
		'post_patch': [
			{
				0: r'#define snprintf sprintf_s',
				'in_file': '../third_party/glslang/glslang/Include/Common.h'
			},
		],
	},
	'run_post_install' : [
		'cp -frv "../libshaderc/include/shaderc" "{target_prefix}/include/"',
		'cp -frv "../libshaderc_util/include/libshaderc_util" "{target_prefix}/include/"',
		'cp -frv "{target_prefix}/lib/pkgconfig/shaderc.pc" "{target_prefix}/lib/pkgconfig/shaderc_shared.pc"', # save a copy of shaderc.pc (it is "shared" by default)
		'cp -frv "{target_prefix}/lib/pkgconfig/shaderc_static.pc" "{target_prefix}/lib/pkgconfig/shaderc.pc"', # make shaderc.pc the "static" version by copying the static, overwriting the "shared" default one
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