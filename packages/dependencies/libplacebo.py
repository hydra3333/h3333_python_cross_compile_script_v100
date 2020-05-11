{
	'repo_type' : 'git',
	'url' : 'https://github.com/haasn/libplacebo.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	#'run_post_regexreplace' : [
	#	'cp -nv "/usr/bin/pkg-config" "{cross_prefix_full}pkg-config"', # gotta fix this properly at some point.
	#],
	'warnings' : [
		'libplacebo for some reason can\'t detect Vulkan via pkg-config with new meson versions...',
		'one way to work around this (until I figure out why... or haasn does... if its even an issue on his side'
		'is to just install an old version by running: \'pip install meson==0.49.0 \'',
		'2020.05.11 h3333: well, I am not willing to live with an old meson version so try below without, or maybe also with custom_ldflag although likely that will not work.'
	],
	'custom_ldflag' : ' {original_cflags} -lvulkan ', # 2020.05.11 try this in addition to -Dvulkan=enabled below 
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=plain '
		'--backend=ninja '
		'--buildtype=release '
		'-Dvulkan=enabled '  # 2020.05.11 deadsix27 added this, let's try it in addition to the ldflags
		'--cross-file={meson_env_file} ./ ..'
	,
	'depends_on' : [ 'lcms2', 'shaderc', 'vulkan_loader' ], # 2020.04.11 added back 'vulkan_loader' per deadsix27. perhaps need to re-remove, we'll see
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libplacebo' },
}