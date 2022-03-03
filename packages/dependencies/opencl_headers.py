{
	'repo_type' : 'git',
	'url' : 'https://github.com/KhronosGroup/OpenCL-Headers.git',
	'branch' : 'main',
	# 2020.10.15 commit https://github.com/KhronosGroup/OpenCL-Headers/commit/9fac4e9866a961f66bdd72fa2bff50145512f972
	#            changed default header version to 3.0 if CL_TARGET_OPENCL_VERSION is not defined
	'run_post_regexreplace' : [
		'if [ ! -d "{target_prefix}/include/CL" ] ; then mkdir -pv "{target_prefix}/include/CL" ; fi',   # 2019.12.13 always try to create the folder
		'cp -rfv CL/*.h "{target_prefix}/include/CL/"', # 2019.12.13 always copy the files
		'ls -al "{target_prefix}/include/CL/"', # 2019.12.13 always copy the files
		#'wget https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/additional_headers/WDK-10.0.18362.0/windows.management.deployment.h', # 2020.04.27
		#'cp -fv "windows.management.deployment.h" "{target_prefix}/include"',
		#'ls -al "{target_prefix}/include/windows.management.deployment.h"',
		'if [ ! -f "already_ran_make_install" ] ; then touch already_ran_make_install ; fi',
	],
	'needs_make' : False,
	'needs_make_install' : False,
	'needs_configure' : False,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'OpenCL Headers for OpenCL ICD Loader' },
}
