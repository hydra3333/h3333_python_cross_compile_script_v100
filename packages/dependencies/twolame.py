{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://github.com/njh/twolame/releases/download/0.4.0/twolame-0.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/twolame/files/twolame/0.4.0/twolame-0.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d' }, ], },
	],
    #'branch' : 'main',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static CPPFLAGS=-DLIBTWOLAME_STATIC',
	'depends_on' : ['libsndfile', ],
	'patches': [
		('twolame/0001-mingw32-does-not-need-handholding.all.patch', '-p1'), # 2019.12.13
		('twolame/0001-twolame-mingw-workaround_and_add-missing-TL_API.patch', '-p1'), # 2019.12.13 combined those 2 patches
	],
	'update_check' : { 'url' : 'https://github.com/njh/twolame/releases/', 'type' : 'githubreleases', 'name_or_tag' : 'tag_name' },
	'_info' : { 'version' : '0.4.0', 'fancy_name' : 'twolame' },
}
