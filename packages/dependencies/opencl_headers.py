{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-Headers.git',
	'run_post_patch' : [
		#'if [ ! -f "already_ran_make_install" ] ; then if [ ! -d "{target_prefix}/include/CL" ] ; then mkdir "{target_prefix}/include/CL" ; fi ; fi', # 2019.12.13 commented out
        if [ ! -d "{target_prefix}/include/CL" ] ; then mkdir -pv "{target_prefix}/include/CL" ; fi   # 2019.12.13 always try to create the folder
		#'if [ ! -f "already_ran_make_install" ] ; then cp -rfv CL/*.h "{target_prefix}/include/CL/" ; fi', # 2019.12.13 always commented out
        'cp -rfv CL/*.h "{target_prefix}/include/CL/"', # 2019.12.13 always copy the file
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'needs_make' : False,
	'needs_make_install' : False,
	'needs_configure' : False,
	'_info' : { 'version' : None, 'fancy_name' : 'OpenCL Headers for OpenCL ICD Loader' },
}
