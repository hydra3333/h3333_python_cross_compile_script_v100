{
	'repo_type' : 'git',
	'rename_folder' : 'sox_git',
	'url' : 'git://git.code.sf.net/p/sox/code',
	'configure_options' : '--host={target_host} --prefix={output_prefix}/sox_git.installed --disable-shared --enable-static --without-gsm --disable-examples', # 2019.12.13
	'env_exports' : { # 2019.12.13
		'LIBS'   : '-lFLAC -lFLAC++',
	},
	'run_post_patch' : [
		'autoreconf -fiv',
		'if [ -f "{target_prefix}/lib/libgsm.a" ] ; then mv {target_prefix}/lib/libgsm.a {target_prefix}/lib/libgsm.a.disabled ; fi',
		'if [ -d "{target_prefix}/include/gsm" ] ; then mv {target_prefix}/include/gsm {target_prefix}/include/gsm.disabled ; fi',
	],
	'run_post_install' : [
		'if [ -f "{target_prefix}/lib/libgsm.a.disabled" ] ; then mv {target_prefix}/lib/libgsm.a.disabled {target_prefix}/lib/libgsm.a ; fi',
		'if [ -d "{target_prefix}/include/gsm.disabled" ] ; then mv {target_prefix}/include/gsm.disabled {target_prefix}/include/gsm ; fi',
	],
	'depends_on' : [
		'libvorbis', 'gettext', 'libsndfile', 'libpng', 'libopus', 'libflac', # 2019.12.13
	],
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SoX' },
}
# 2019.12.13 old:
#	'sox' : { # https://sourceforge.net/p/sox/code/ci/master/tree/
#		'repo_type' : 'git',
#		'rename_folder' : 'sox_git',
#		'url' : 'git://git.code.sf.net/p/sox/code',
#		'configure_options': '--host={target_host} --prefix={product_prefix}/sox_git.installed --disable-shared --enable-static --without-gsm --disable-examples ',
#		'env_exports' : {
#			'LIBS'   : '-lFLAC -lFLAC++',
#		},
#		'run_post_patch' : (
#			'autoreconf -fiv',
#			'if [ -f "{target_prefix}/lib/libgsm.a" ] ; then mv -fv {target_prefix}/lib/libgsm.a {target_prefix}/lib/libgsm.a.disabled ; fi',
#			'if [ -d "{target_prefix}/include/gsm" ] ; then mv -fv {target_prefix}/include/gsm {target_prefix}/include/gsm.disabled ; fi',
#		),
#		'run_post_install' : (
#			'if [ -f "{target_prefix}/lib/libgsm.a.disabled" ] ; then mv -fv {target_prefix}/lib/libgsm.a.disabled {target_prefix}/lib/libgsm.a ; fi',
#			'if [ -d "{target_prefix}/include/gsm.disabled" ] ; then mv -fv {target_prefix}/include/gsm.disabled {target_prefix}/include/gsm ; fi',
#		),
#		'depends_on': [
#			'libvorbis', 'gettext', 'libopus', 'libflac',
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SoX' },
#	},