{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-tools',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Tools.git',
	'depth_git': 0,
	#'branch': 'main', # 2023.01.12 address more 'merican embedded racism
	'branch': '64ba112ffb1fed55f1514e209db8ddbafbd7b9ae', # 2023.01.12 address more 'merican embedded racism
	'recursive_git' : True,
	#'needs_make' : False,
	#'needs_make_install' : False,
	#'needs_configure' : False,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
		'-DCMAKE_BUILD_TYPE=release '
		'-DSKIP_SPIRV_TOOLS_INSTALL=OFF '
		'-DSPIRV_TOOLS_BUILD_STATIC=ON '
		'-DSPIRV_SKIP_EXECUTABLES=ON '
		'-DSPIRV_SKIP_TESTS=ON '
		'-DSKIP_SPIRV_HEADERS_INSTALL=ON '
	,
	#
	# If SPIR-V Tools is configured as a standalone project, then 
	# download the googletest source into the 
	# <spirv-dir>/external/googletest 
	# directory before configuring and building the project.
	'run_post_regexreplace' : [
		'pwd',
		'!SWITCHDIR|../external',
		'ln -snf {inTreePrefix}/spirv-headers/ spirv-headers',
		'pwd',
		'ls -al',
		'!SWITCHDIR|../_build',
		#'if [ -d "../external/googletest" ] ; then rm -fvR "../external/googletest" ; fi',
		#'if [ -d "../external/effcee" ] ; then rm -fvR "../external/effcee" ; fi',
		#'if [ -d "../external/re2" ] ; then rm -fvR "../external/re2" ; fi',
		#'git clone https://github.com/google/googletest.git          ../external/googletest',
		#'git clone https://github.com/google/effcee.git              ../external/effcee',
		#'git clone https://github.com/google/re2.git                 ../external/re2',
	],
	'depends_on' : [ 'spirv-headers', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV Tools' },
}