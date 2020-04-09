{
	'repo_type' : 'none',
	'folder_name' : 'vulkan_d3dheaders',
	'run_post_regexreplace' : [
		'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/d3dukmdt.h ; fi',
		'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/d3dkmthk.h ; fi',
		'if [ ! -f "already_done" ] ; then cp -fv "d3dkmthk.h" "{target_prefix}/include/d3dkmthk.h" ; fi',
		'if [ ! -f "already_done" ] ; then cp -fv "d3dukmdt.h" "{target_prefix}/include/d3dukmdt.h" ; fi',
		'if [ ! -f "already_done" ] ; then touch  "already_done" ; fi',
	],
	'needs_make' : False,
	'needs_make_install' : False,
	'needs_configure' : False,
	'_info' : { 'version' : '1.0', 'fancy_name' : 'Modified D3D headers from the Wine package to satisfy vulkan-loader compilation' },
}
# 2019.12.13 old:
#	'vulkan-d3dheaders' : { # 2019.08
#		'repo_type' : 'none',
#		'folder_name' : 'vulkan_d3dheaders',
#		'run_post_regexreplace' : [
#			'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/additional_headers/d3dukmdt.h ; fi',
#			'if [ ! -f "already_done" ] ; then wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/additional_headers/d3dkmthk.h ; fi',
#			'if [ ! -f "already_done" ] ; then cp -fv "d3dkmthk.h" "{target_prefix}/include/d3dkmthk.h" ; fi',
#			'if [ ! -f "already_done" ] ; then cp -fv "d3dukmdt.h" "{target_prefix}/include/d3dukmdt.h" ; fi',
#			'if [ ! -f "already_done" ] ; then touch  "already_done" ; fi',
#		],
#		'needs_make' : False,
#		'needs_make_install' : False,
#		'needs_configure' : False,
#		'_info' : { 'version' : '1.0', 'fancy_name' : 'Modified D3D headers from the Wine package to satisfy vulkan-icd compilation' },
#	},