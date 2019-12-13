{
	'repo_type' : 'git',
	'url' : 'https://code.videolan.org/videolan/dav1d.git',
	'conf_system' : 'meson',
	'build_system' : 'ninja',
	'rename_folder' : 'libdav1d_git',
	'source_subfolder' : 'build',
	'configure_options' :
		'--prefix={target_prefix} '
		'--libdir={target_prefix}/lib '
		'--default-library=static '
		'--buildtype=plain '
		'--backend=ninja '
		'-Denable_tests=false '
		'-Denable_tools=false '
		'--buildtype=release '
		'--cross-file={meson_env_file} ./ ..'
  ,
	'_info' : { 'version' : None, 'fancy_name' : 'dav1d (library)' },
}