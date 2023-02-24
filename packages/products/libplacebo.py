{
	'repo_type' : 'git',
	'url' : 'https://github.com/haasn/libplacebo.git', # https://github.com/haasn/libplacebo.git 
	'depth_git' : 0,
	#'branch' : '82023b9e9d683499329b2d5c502eafaf5f6c8ef2',	# 2023.02.19 ... libplacebo breaks cross-compilation after this commit
	'recursive_git' : True,
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : '_build',
	'patches' : [
		#('libplacebo/115-from-MABS.patch', '-p1', '..'),	# 2022.01.02 revert patch per MABS
	],
	#'run_post_patch' : [ # 2022.12.18 per DEADSIX27
		###	'cp -fuv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"', # gotta fix this properly at some point.
		## 'cp -nv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"', # gotta fix this properly at some point.
		#'!SWITCHDIR|../', # 2022.12.18 per DEADSIX27
        #'cd ..', # 2022.12.18 per DEADSIX27
        #'git submodule update --init', # 2022.12.18 per DEADSIX27
        #'!SWITCHDIR|build', # 2022.12.18 per DEADSIX27
	#],
	'custom_ldflag' : ' {original_cflag_trim} {original_stack_protector_trim} {original_fortify_source_trim} -L{target_prefix}/lib ',
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'--backend=ninja '
		'-Dvulkan=enabled '
		'-Dvulkan-registry={target_prefix}/share/vulkan/registry/vk.xml '  # 2021.10.30 re-try vulkan
		'-Dglslang=enabled ' # 2021.11.01 it finds it better without this
		'-Dshaderc=disabled ' # 2021.11.01 it finds it better without this
		#'-Dd3d11=enabled ' # 2022.12.18 try to re-enable it
		'-Dd3d11=disabled ' # 2022.12.18 try to re-enable it
		#'-Dopengl=enabled ' # 2022.12.18 leave opengl disabled
		'-Dlcms=enabled '
		'-Dtests=false '
		'-Dbench=false '
		'-Ddemos=false ' # 2021.04.09 try this from MABS
		'-Dfuzz=false '
		'-Dunwind=disabled '
		'--cross-file={meson_env_file} ./ ..'
	,
	'run_post_regexreplace' : [
		#'pwd ; cd .. ; git submodule update --remote --recursive --init ; cd _build ; pwd',
		#'pwd ; meson --wipe --prefix={target_prefix} --libdir={target_prefix}/lib --default-library=static --buildtype=release --backend=ninja --cross-file={meson_env_file} ./ .. ; pwd',
		'sed -i.bak "s/shaderc = dependency(\'shaderc\',/shaderc = dependency(\'shaderc_static\',/" ../src/meson.build',
		'sed -i.bak "s/cross = dependency(\'spirv-cross-c-shared\',/cross = dependency(\'spirv-cross\',/" ../src/meson.build',
		'if [ ! -d "{target_prefix}/share" ] ; then mkdir -pv "{target_prefix}/share" ; fi',
		'if [ ! -d "{target_prefix}/share/vulkan" ] ; then mkdir -pv "{target_prefix}/share/vulkan" ; fi',
		'if [ ! -d "{target_prefix}/share/vulkan/registry" ] ; then mkdir -pv "{target_prefix}/share/vulkan/registry" ; fi',
	],
	#'depends_on' : [ 'lcms2', 'spirv-tools', 'glslang', 'shaderc', 'vulkan_from_windows_dll' ], # 'vulkan_loader',
	'depends_on' : [ 'vulkan_headers', 'vulkan-d3dheaders', 'vulkan_from_windows_dll' , 'lcms2', 'libepoxy', 'spirv-headers', 'spirv-tools', 'spirv-cross', 'glslang', 'shaderc', ], # 2022.12.18 ad libepoxy for opengl # 'vulkan_loader', # 2022.06.28 'spirv-tools' dependency is in glslang
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libplacebo' },
}
