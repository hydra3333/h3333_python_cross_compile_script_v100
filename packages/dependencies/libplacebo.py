{
	'repo_type' : 'git',
	'url' : 'https://github.com/haasn/libplacebo.git',
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
		'-Dvulkan=enabled ' # 2020.05.14 added back
		#'-Dglslang=enabled '
		#'-Dshaderc=enabled '
		'-Dlcms=enabled '
		'-Dtests=false '
		'-Dbench=false '
		'--cross-file={meson_env_file} ./ ..'
	,
	'depends_on' : [ 'lcms2', 'glslang', 'shaderc', 'vulkan_loader', ], # 2020.05.14 added back 'vulkan_loader' 
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libplacebo' },
}