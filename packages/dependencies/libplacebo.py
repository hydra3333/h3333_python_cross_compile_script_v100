{
	'repo_type' : 'git',
	'url' : 'https://github.com/haasn/libplacebo.git',
	'depth_git' : 0,
	#'branch' : '65e5e17edffaf0b9b1adcd9ba90637a27641e59b', # '65e5e17edffaf0b9b1adcd9ba90637a27641e59b', works # 'dca1913c6ac81c455800868e8c5219626351a959', broken
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'run_post_regexreplace' : [
		'cp -nv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"', # gotta fix this properly at some point.
	],
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=plain '
		'--backend=ninja '
		'--buildtype=release '
		#'-Dvulkan=enabled ' # 2020.10.12 comment out vulkan since it an no longer be statically linked
		#'-Dvulkan-registry={target_prefix}/share/vulkan/registry/vk.xml ' # 2020.10.12 comment out vulkan since it an no longer be statically linked
		#'-Dglslang=enabled '
		#'-Dshaderc=enabled '
		'-Dlcms=enabled '
		'-Dtests=false '
		'-Dbench=false '
		'--cross-file={meson_env_file} ./ ..'
	,
	'depends_on' : [ 'lcms2', 'glslang', 'shaderc', ], # 'vulkan_loader',  2020.10.12 comment out vulkan since it an no longer be statically linked
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libplacebo' },
}
