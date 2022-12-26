{
	'repo_type' : 'none',
	'folder_name' : 'decklink_headers',
	'run_post_regexreplace' : [
		'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/DeckLinkAPI.h ; fi', # 2019.12.13 copied from deadsix27
		'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/DeckLinkAPI_i.c ; fi', # 2019.12.13 copied form deadsix27
		'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/DeckLinkAPIVersion.h ; fi', # 2019.12.13 copied form deadsix27
		'if [ ! -f "already_done" ] ; then cp -fv "DeckLinkAPI.h" "{target_prefix}/include/DeckLinkAPI.h" ; fi',
		'if [ ! -f "already_done" ] ; then cp -fv "DeckLinkAPI_i.c" "{target_prefix}/include/DeckLinkAPI_i.c" ; fi',
		'if [ ! -f "already_done" ] ; then cp -fv "DeckLinkAPIVersion.h" "{target_prefix}/include/DeckLinkAPIVersion.h" ; fi',
		'if [ ! -f "already_done" ] ; then touch  "already_done" ; fi',
	],
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	'_info' : { 'version' : '10.11.2', 'fancy_name' : 'Decklink SDK Headers' },
}
