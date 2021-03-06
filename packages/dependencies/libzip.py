{
	'repo_type' : 'git',
	'url' : 'https://github.com/nih-at/libzip.git',
	'configure_options' : '{autoconf_prefix_options}',
	'patches' : [
		# ('libzip/0001-libzip-git-20170415-fix-static-build.patch','-p1'),
		('libzip/0001-Fix-building-statically-on-mingw64.patch','-p1'),
	],
	'run_post_regexreplace' : [
		'autoreconf -fiv',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libzip' },
}