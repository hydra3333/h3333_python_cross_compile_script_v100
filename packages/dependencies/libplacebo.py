{
	'repo_type' : 'git',
	'url' : 'https://github.com/haasn/libplacebo.git', # https://github.com/haasn/libplacebo.git 
	'depth_git' : 0,
	#'branch' : '65e5e17edffaf0b9b1adcd9ba90637a27641e59b',
    'recursive_git' : True,
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : '_build',
	'patches' : [
		#('libplacebo/115-from-MABS.patch', '-p1', '..'),	# 2022.01.02 revert patch per MABS
	],
	#'run_post_regexreplace' : [
	#	'cp -fuv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"', # gotta fix this properly at some point.
	#],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'--backend=ninja '
		'-Dvulkan=enabled ' # 2021.11.01 it finds it better without this
		'-Dvulkan-registry={target_prefix}/share/vulkan/registry/vk.xml '  # 2021.10.30 re-try vulkan
		'-Dglslang=enabled ' # 2021.11.01 it finds it better without this
		'-Dshaderc=disabled ' # 2021.11.01 it finds it better without this
		#'-Dd3d11=enabled ' # 2022.06.28 from MABS
		'-Dd3d11=disabled ' # 2022.06.28 from MABS
		'-Dlcms=enabled '
		'-Dtests=false '
		'-Dbench=false '
		'-Ddemos=false ' # 2021.04.09 try this from MABS
		'-Dfuzz=false '
		'-Dunwind=disabled '
		'--cross-file={meson_env_file} ./ ..'
	,
	#'depends_on' : [ 'lcms2', 'spirv-tools', 'glslang', 'shaderc', 'vulkan_from_windows_dll' ], # 'vulkan_loader',
	'run_post_regexreplace' : [
		'pwd',
		'sed -i.bak "s/shaderc = dependency(\'shaderc\',/shaderc = dependency(\'shaderc_static\',/" ../src/meson.build',
		'sed -i.bak "s/cross = dependency(\'spirv-cross-c-shared\',/cross = dependency(\'spirv-cross\',/" ../src/meson.build',
		'if [ ! -d "{target_prefix}/share" ] ; then mkdir -pv "{target_prefix}/share" ; fi',
		'if [ ! -d "{target_prefix}/share/vulkan" ] ; then mkdir -pv "{target_prefix}/share/vulkan" ; fi',
		'if [ ! -d "{target_prefix}/share/vulkan/registry" ] ; then mkdir -pv "{target_prefix}/share/vulkan/registry" ; fi',
	],
	'depends_on' : [ 'lcms2', 'glslang', 'shaderc', 'vulkan_from_windows_dll' ],  # 'vulkan_loader', # 2022.06.28 'spirv-tools' dependency is in glslang
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libplacebo' },
}
