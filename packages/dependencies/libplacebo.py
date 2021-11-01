{
	'repo_type' : 'git',
	'url' : 'https://github.com/haasn/libplacebo.git', # https://github.com/haasn/libplacebo.git
	'depth_git' : 0,
	#'branch' : '65e5e17edffaf0b9b1adcd9ba90637a27641e59b',
    'recursive_git' : True,
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	#'run_post_regexreplace' : [
	#	'cp -fuv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"', # gotta fix this properly at some point.
	#],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=release '
		'--backend=ninja '
		'--buildtype=release '
		#'-Dvulkan=enabled ' # 2021.11.01 it finds it better without this
		'-Dvulkan-registry={target_prefix}/share/vulkan/registry/vk.xml '  # 2021.10.30 re-try vulkan
		#'-Dglslang=enabled ' # 2021.11.01 it finds it better without this
		#'-Dshaderc=enabled ' # 2021.11.01 it finds it better without this
		'-Dlcms=enabled '
		'-Dtests=false '
		'-Dbench=false '
		'-Ddemos=false ' # 2021.04.09 try this from MABS
		'--cross-file={meson_env_file} ./ ..'
	,
	#'depends_on' : [ 'lcms2', 'spirv-tools', 'glslang', 'shaderc', ], # 2021.10.30 add spirv-tools # 'vulkan_loader',	2020.10.12 comment out vulkan since it an no longer be statically linked
	'depends_on' : [ 'lcms2', 'spirv-tools', 'glslang', 'shaderc', 'vulkan_loader' ], # 2021.10.30 re-try 'vulkan_loader'
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libplacebo' },
}
