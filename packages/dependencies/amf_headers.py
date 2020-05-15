{
	'repo_type' : 'git',
	'url' : 'https://github.com/DeadSix27/AMF',
	'rename_folder' : 'amd_media_framework_headers',
	'depth_git': 1,
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	'run_post_regexreplace' : [
		'if [ ! -f "already_done" ] ; then if [ ! -d "{target_prefix}/include/AMF" ]; then mkdir -p "{target_prefix}/include/AMF" ; fi ; fi',
		'if [ ! -f "already_done" ] ; then pwd ; fi',
		'if [ ! -f "already_done" ] ; then cp -av "amf/public/include/." "{target_prefix}/include/AMF" ; fi',
		'if [ ! -f "already_done" ] ; then touch  "already_done" ; fi',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'AMF (headers)' },
}
