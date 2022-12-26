{
	'repo_type' : 'git',
	'url' : 'https://github.com/cisco/openh264.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'source_subfolder' : '_build',
	#'patches' : [  # 2022.12.18 from deadsix27
	#	( 'openh264/0001-openh264-static-only.patch', '-p1', ".." ),  # 2022.12.18 from deadsix27
	#],  # 2022.12.18 from deadsix27
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--backend=ninja '
		'-Dtests=disabled '
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
	,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'openh264' },
}