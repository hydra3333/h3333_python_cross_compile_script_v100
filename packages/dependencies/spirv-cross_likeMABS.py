{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-cross',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Cross.git',
	'depth_git': 0,
	'recursive_git' : True,
	# 2022.06.28 for now, stay with cmake not meson which MABS creates
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
		# MABS
		#'-DSPIRV_CROSS_ENABLE_CPP=OFF '
		'-DSPIRV_CROSS_C_API_CPP=ON '
		'-DSPIRV_CROSS_C_API_GLSL=ON '
		'-DSPIRV_CROSS_C_API_HLSL=ON '
		'-DSPIRV_CROSS_C_API_MSL=ON '
		'-DSPIRV_CROSS_C_API_REFLECT=ON '
		# non-MABS 2022.06.28
		'-DSPIRV_CROSS_ENABLE_GLSL=ON '
		'-DSPIRV_CROSS_ENABLE_HLSL=ON '
		'-DSPIRV_CROSS_ENABLE_MSL=ON '
		'-DSPIRV_CROSS_ENABLE_CPP=ON '
		'-DSPIRV_CROSS_ENABLE_REFLECT=ON '
		'-DSPIRV_CROSS_ENABLE_C_API=ON '
		'-DSPIRV_CROSS_ENABLE_UTIL=ON '
		'-DSPIRV_CROSS_EXCEPTIONS_TO_ASSERTIONS=ON '
		'-DSPIRV_CROSS_FORCE_PIC=ON '
		'-DSPIRV_CROSS_SKIP_INSTALL=OFF '
	,
	#'conf_system' : 'meson',
	#'build_system' : 'ninja',
	#'source_subfolder' : '_build',
	#'configure_options' :
	#	'--prefix={target_prefix} '
	#	'--libdir={target_prefix}/lib '
	#	'--default-library=static '
	#	#'--strip '
	#	'--backend=ninja '
	#	'--buildtype=release '
	#	'--cross-file={meson_env_file} ./ ..'
	'patches' : [
		('spirv-cross/0001-add-a-basic-Meson-build-system-for-use-as-a-subproje-MABS-2022.06.28.patch', '-Np1', '..'),
	],
	#'run_post_patch' : [
		#'ls -al "{target_prefix}/lib/pkgconfig/spirv-cross.pc"',
		#'rm -fv "{target_prefix}/lib/pkgconfig/spirv-cross.pc"',
		#'ls -al "{target_prefix}/lib/pkgconfig/spirv-cross.pc"',
	#],
	'run_post_install' : [
		# 2022.06.28 the next line is to create a .pc ... if SHOULD not be needed any more ??? 
		"echo 'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include/spirv_cross\nName: spirv-cross-c-shared\nDescription: C API for SPIRV-Cross\nVersion:\nLibs: -L${{libdir}} -lspirv-cross-c -lspirv-cross-cpp -lspirv-cross-reflect -lspirv-cross-glsl -lspirv-cross-hlsl -lspirv-cross-msl -lspirv-cross-core -lstdc++\nCflags: -I${{includedir}}' > {target_prefix}/lib/pkgconfig/spirv-cross.pc",
		#'echo "It should have created a .pc file {target_prefix}/lib/pkgconfig/spirv-cross.pc" IF NOT then create it in run_post_install',
		'ls -al "{target_prefix}/lib/pkgconfig/spirv-cross.pc"', # 2022.06.28 it should have created a .pc file
		'cat "{target_prefix}/lib/pkgconfig/spirv-cross.pc"', # 2022.06.28 it should have created a .pc file
	],
	'run_post_patch' : [ 
		'sed -i.bak "s/0.13.0/0.48.0/" ../meson.build',
	],
	'depends_on' : [ 'spirv-headers_likeMABS', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV-Cross' },
}
