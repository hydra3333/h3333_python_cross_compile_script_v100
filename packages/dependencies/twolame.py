{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://github.com/njh/twolame/releases/download/0.4.0/twolame-0.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d' }, ], },
		{ 'url' : 'https://sourceforge.net/projects/twolame/files/twolame/0.4.0/twolame-0.4.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d' }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static CPPFLAGS=-DLIBTWOLAME_STATIC',
	#'custom_cflag' : '',
	'depends_on' : ['libsndfile', ],
	'patches': [
		('twolame/0001-mingw32-does-not-need-handholding.all.patch', '-p1'), # 2019.12.13
		('twolame/0001-twolame-mingw-workaround_and_add-missing-TL_API.patch', '-p1'), # 2019.12.13 combined those 2 patches
	],
	'update_check' : { 'url' : 'https://github.com/njh/twolame/releases/', 'type' : 'githubreleases', 'name_or_tag' : 'tag_name' },
	'_info' : { 'version' : '0.4.0', 'fancy_name' : 'twolame' },
}
# 2019.12.13 old:
#	'twolame' : { 
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://github.com/njh/twolame/releases/
#			{ "url" : "https://github.com/njh/twolame/releases/download/0.4.0/twolame-0.4.0.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d" }, ], },
#			{ "url" : "https://sourceforge.net/projects/twolame/files/twolame/0.4.0/twolame-0.4.0.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d" }, ], },
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static CPPFLAGS=-DLIBTWOLAME_STATIC', # ?? remove CPPFLAGS=-DLIBTWOLAME_STATIC' ??
#		'patches' : ( # 2019.11.02 from Alexpux  https://github.com/msys2/MINGW-packages/tree/master/mingw-w64-twolame for 0.4.0
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/twolame-from-Alexpux/0001-mingw32-does-not-need-handholding.all.patch','-Np1'),
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/twolame-from-Alexpux/0002-Add-missing-TL_API.patch','-Np1'),
#		),
#		'_info' : { 'version' : '0.4.0', 'fancy_name' : 'twolame' },
#	},