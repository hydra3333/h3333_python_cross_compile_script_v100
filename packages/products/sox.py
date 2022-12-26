{ # 2020.09.27 latest git doesn't work, revert to release ... https://fossies.org/linux/misc/
	#'repo_type' : 'git',
	#'rename_folder' : 'sox_git',
	#'url' : 'git://git.code.sf.net/p/sox/code',
	##'depth_git' : 0,
	##'branch' : '3b6c27419f736c2dfa3b2bf3d34dfe656832c464', # 2020.09.27 after 3b6c27419f736c2dfa3b2bf3d34dfe656832c464 link to vorbis fails
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://downloads.sourceforge.net/project/sox/sox/14.4.2/sox-14.4.2.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b45f598643ffbd8e363ff24d61166ccec4836fea6d3888881b8df53e3bb55f6c' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/sox-14.4.2.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b45f598643ffbd8e363ff24d61166ccec4836fea6d3888881b8df53e3bb55f6c' }, ], },
	],
	'configure_options' : '--host={target_host} --prefix={output_prefix}/sox_git.installed --disable-shared --enable-static --without-gsm --disable-examples', # 2019.12.13
	'env_exports' : { # 2019.12.13
		'LIBS'   : '-lFLAC -lFLAC++',
	},
	'run_post_regexreplace' : [
		'autoreconf -fiv',
		'if [ -f "{target_prefix}/lib/libgsm.a" ] ; then mv -fv {target_prefix}/lib/libgsm.a {target_prefix}/lib/libgsm.a.disabled ; fi',
		'if [ -d "{target_prefix}/include/gsm" ] ; then mv -fv {target_prefix}/include/gsm {target_prefix}/include/gsm.disabled ; fi',
	],
	'run_post_install' : [
		'if [ -f "{target_prefix}/lib/libgsm.a.disabled" ] ; then mv {target_prefix}/lib/libgsm.a.disabled {target_prefix}/lib/libgsm.a ; fi',
		'if [ -f "{target_prefix}/lib/libgsm.a.disabled" ] ; then mv {target_prefix}/lib/libgsm.a.disabled {target_prefix}/lib/libgsm.a ; fi',
		'if [ -d "{target_prefix}/include/gsm.disabled" ] ; then mv {target_prefix}/include/gsm.disabled {target_prefix}/include/gsm ; fi',
	],
	'depends_on' : [
		'libvorbis', 'gettext', 'libsndfile', 'libpng', 'libopus', 'libflac', # 2019.12.13
	],
	'_info' : { 'version' : '14.4.2', 'fancy_name' : 'SoX' },
}
