{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://github.com/njh/twolame/releases/download/0.4.0/twolame-0.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/twolame/files/twolame/0.4.0/twolame-0.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d' }, ], },
	],
    'branch' : 'main',
	# NOTE: ALSO ... This switch by itself without the SEDs prevents build of front-ends : --disable-sndfile
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-sndfile CPPFLAGS=" {original_cflags} -DLIBTWOLAME_STATIC "',
	'patches': [
		('twolame/0001-mingw32-does-not-need-handholding.all.patch', '-p1'), # 2019.12.13
		('twolame/0001-twolame-mingw-workaround_and_add-missing-TL_API.patch', '-p1'), # 2019.12.13 combined those 2 patches
	],
	## building the frontend aborts, so try not build it (this one SED does not manage it)
	# Do the autoreconf AFTER the SED's above
	'run_post_patch' : [
		'sed -i \'s|AC_SUBST(TWOLAME_BIN)|TWOLAME_BIN=""\\nAC_SUBST(TWOLAME_BIN)|\' ./configure.ac',
		'sed -i \'/frontend\/Makefile/d\' ./configure.ac',
		'sed -i \'/simplefrontend\/Makefile/d\' ./configure.ac',
		'sed -i \'/tests\/Makefile/d\' ./configure.ac',
		'sed -i \'s/libtwolame frontend simplefrontend doc tests/libtwolame/\' ./Makefile.am',
		'autoreconf -fiv',
	],
	'depends_on' : ['libsndfile', ],
	'update_check' : { 'url' : 'https://github.com/njh/twolame/releases/', 'type' : 'githubreleases', 'name_or_tag' : 'tag_name' },
	'_info' : { 'version' : '0.4.0', 'fancy_name' : 'twolame' },
}
