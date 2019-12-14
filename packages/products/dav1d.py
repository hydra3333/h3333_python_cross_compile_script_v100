{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/dav1d.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
    'run_post_patch' : [
		'sed -i.bak \'s/sdl2_dependency.found()/false/\' ../tools/meson.build' # 2019.12.13 # 2019.08.07 turn off building of tool dav1dplay.exe since it won't link. A Nod to JB MABS.
	],
	'configure_options' : ''
		'--prefix={output_prefix}/dav1d.installed  '    # 2019.12.13 old '--prefix={product_prefix}/dav1d.installed  '
		'--libdir={output_prefix}/dav1d.installed/lib ' # 2019.12.13 old '--libdir={product_prefix}/dav1d.installed/lib '
		'--default-library=static '
		#'--buildtype=plain ' # 2019.12.13
		'--backend=ninja '
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
	,
	'_info' : { 'version' : None, 'fancy_name' : 'dav1d' },
}