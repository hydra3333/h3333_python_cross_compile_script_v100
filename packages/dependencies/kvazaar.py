{
	'repo_type' : 'git',
	'url' : 'https://github.com/ultravideo/kvazaar.git',
	'configure_options' : '{autoconf_prefix_options}',
	'patches' : [
		( 'kvazaar/0001-mingw-workaround.patch', '-p1' ),
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'kvazaar' },
}