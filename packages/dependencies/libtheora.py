{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/theora.git',
	'patches' : [
		('theora/theora_remove_rint_1.2.0alpha1.patch', '-p1'),
	],
	'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static --disable-doc --disable-spec --disable-oggtest --disable-vorbistest --disable-examples',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'theora' },
}
