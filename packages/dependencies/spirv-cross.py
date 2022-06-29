{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-cross',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Cross.git',
	'depth_git': 0,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DSPIRV_CROSS_SHARED=OFF '
		'-DSPIRV_CROSS_STATIC=ON '
		'-DSPIRV_CROSS_ENABLE_TESTS=OFF '
		#'-DSPIRV_CROSS_SHARED=OFF -DSPIRV_CROSS_STATIC=ON -DSPIRV_CROSS_CLI=OFF -DSPIRV_CROSS_ENABLE_TESTS=OFF -DSPIRV_CROSS_FORCE_PIC=ON -DSPIRV_CROSS_ENABLE_CPP=OFF ' from GYAN
		# 2022.06.26 the rest are from gyan
		'-DSPIRV_CROSS_CLI=OFF '
		'-DSPIRV_CROSS_FORCE_PIC=ON '
		'-DSPIRV_CROSS_ENABLE_CPP=OFF '
	,
	'run_post_install' : [
        "mkdir -pv {target_prefix}/lib/pkgconfig",
		"echo 'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include/spirv_cross\nName: spirv-cross-c-shared\nDescription: C API for SPIRV-Cross\nVersion:\nLibs: -L${{libdir}} -lspirv-cross-c -lspirv-cross-cpp -lspirv-cross-reflect -lspirv-cross-glsl -lspirv-cross-hlsl -lspirv-cross-msl -lspirv-cross-core -lstdc++\nCflags: -I${{includedir}}' > {target_prefix}/lib/pkgconfig/spirv-cross.pc",
	],
	'depends_on' : [ 'spirv-headers', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV Cross' },

}
