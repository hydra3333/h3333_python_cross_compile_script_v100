{
	'repo_type' : 'git',
	'url' : 'https://github.com/fribidi/fribidi.git',
	'branch': 'f503e576c8345dd32d7438569346d6ca9aa50044', # 2020.02.15
	'depth_git': 2, # 2020.02.15
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : 'build',
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=plain '
		'--backend=ninja '
		'-Ddocs=false '
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
	,
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libfribidi' },
}