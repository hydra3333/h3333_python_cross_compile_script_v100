{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-cross',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Cross.git',
	'depth_git': 0,
	'recursive_git' : True,
	'branch': 'main', # 2023.01.29 address more 'merican embedded racism
	# 2022.06.28 for now, stay with cmake not meson which MABS creates
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DSPIRV_CROSS_SHARED=ON '	# 2023.02.25 turn this on for mpv
		'-DSPIRV_CROSS_STATIC=ON '
		'-DSPIRV_CROSS_ENABLE_TESTS=OFF '
		#'-DSPIRV_CROSS_SHARED=OFF -DSPIRV_CROSS_STATIC=ON -DSPIRV_CROSS_CLI=OFF -DSPIRV_CROSS_ENABLE_TESTS=OFF -DSPIRV_CROSS_FORCE_PIC=ON -DSPIRV_CROSS_ENABLE_CPP=OFF ' from GYAN
		# 2022.06.26 the rest are from gyan
		'-DSPIRV_CROSS_CLI=OFF '
		'-DSPIRV_CROSS_FORCE_PIC=ON '
		# MABS
		'-DSPIRV_CROSS_ENABLE_CPP=ON '
		'-DSPIRV_CROSS_C_API_CPP=ON '
		'-DSPIRV_CROSS_C_API_GLSL=ON '
		'-DSPIRV_CROSS_C_API_HLSL=ON '
		'-DSPIRV_CROSS_C_API_MSL=ON '
		'-DSPIRV_CROSS_C_API_REFLECT=ON '
		# non-MABS 2022.06.28
		'-DSPIRV_CROSS_ENABLE_GLSL=ON '
		'-DSPIRV_CROSS_ENABLE_HLSL=ON '
		'-DSPIRV_CROSS_ENABLE_MSL=ON '
		'-DSPIRV_CROSS_ENABLE_REFLECT=ON '
		'-DSPIRV_CROSS_ENABLE_C_API=ON '
		'-DSPIRV_CROSS_ENABLE_UTIL=ON '
		#'-DSPIRV_CROSS_EXCEPTIONS_TO_ASSERTIONS=ON '
		'-DSPIRV_CROSS_SKIP_INSTALL=OFF '
	,
	'patches' : [
		('spirv-cross/0001-add-a-basic-Meson-build-system-for-use-as-a-subproje-MABS-2022.06.28.patch', '-Np1', '..'),
		('https://raw.githubusercontent.com/shinchiro/mpv-winbuild-cmake/master/packages/spirv-cross-0001-static-linking-hacks.patch', '-Np1', '..' ), # 2022.12.18 per DEADSIX27
	],
	'run_post_patch' : [
		'sed -i.bak "s/0.13.0/0.48.0/" ../meson.build',
		'if [   -f "{target_prefix}/lib/pkgconfig/spirv-cross.pc" ] ; then rm -fv "{target_prefix}/lib/pkgconfig/spirv-cross.pc" ; fi', # 2022.12.21 remove .pc before building
	],
	'run_post_install' : [
		# 2022.06.28 the next line is to create a .pc ... if SHOULD not be needed any more ??? 
		'if [ ! -d "{target_prefix}/lib/pkgconfig" ] ; then mkdir -pv "{target_prefix}/lib/pkgconfig" ; fi',
		'if [   -f "{target_prefix}/lib/pkgconfig/spirv-cross.pc" ] ; then cat "{target_prefix}/lib/pkgconfig/spirv-cross.pc" ; fi',
		# me:
		'if [ ! -f "{target_prefix}/lib/pkgconfig/spirv-cross.pc" ] ; then echo \'prefix={target_prefix}\nexec_prefix=${{prefix}}\nlibdir=${{exec_prefix}}/lib\nincludedir=${{prefix}}/include/spirv_cross\nName: spirv-cross-c-static\nDescription: C API for SPIRV-Cross\nVersion:       \nLibs: -L${{libdir}} -lspirv-cross-c -lspirv-cross-cpp -lspirv-cross-reflect -lspirv-cross-glsl -lspirv-cross-hlsl -lspirv-cross-msl -lspirv-cross-core -lstdc++\nCflags: -I${{includedir}}\' > {target_prefix}/lib/pkgconfig/spirv-cross.pc ; fi', # 2022.12.18 per DEADSIX27
		#
		#'if [ ! -f "{target_prefix}/lib/pkgconfig/spirv-cross-c-shared.pc" ] ; then cp -fv {target_prefix}/lib/pkgconfig/spirv-cross.pc {target_prefix}/lib/pkgconfig/spirv-cross-c-shared.pc ; fi',
		#'if [ ! -f "{target_prefix}/lib/pkgconfig/spirv-cross-c-shared.pc" ] ; then sed 's/spirv-cross-c-static/spirv-cross-c-shared/g' {target_prefix}/lib/pkgconfig/spirv-cross-c-shared.pc ; fi',
		#
		'ls -al "{target_prefix}/lib/pkgconfig/spirv-cross.pc"', # 2022.06.28 it should have created a .pc file
		'cat "{target_prefix}/lib/pkgconfig/spirv-cross.pc"', # 2022.06.28 it should have created a .pc file
		#
		'ls -al "{target_prefix}/lib/pkgconfig/spirv-cross-c-shared.pc"', # 2022.06.28 it should have created a .pc file
		'cat "{target_prefix}/lib/pkgconfig/spirv-cross-c-shared.pc"', # 2022.06.28 it should have created a .pc file
	],
	'depends_on' : [ 'spirv-headers', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV Cross' },

}