{
	'repo_type' : 'git',
	'rename_folder' : 'spirv-tools',
	'url' : 'https://github.com/KhronosGroup/SPIRV-Tools.git',
	'depth_git': 0,
	'recursive_git' : True,
	#'branch': '323a81fc5e30e43a04e5e22af4cba98ca2a161e6', # 2020.03.19 comment out
	#'needs_make' : False,
	#'needs_make_install' : False,
	#'needs_configure' : False,
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : 
		'.. {cmake_prefix_options} '
		'-DCMAKE_INSTALL_PREFIX={target_prefix} '
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
	#
	'run_post_regexreplace' : [
		'pwd',
		#'if [ -d "../external/spirv-headers" ] ; then rm -fvR "../external/spirv-headers" ; fi',
		#'git clone https://github.com/KhronosGroup/SPIRV-Headers.git ../external/spirv-headers',
		'!SWITCHDIR|../external',
		'ln -snf {inTreePrefix}/spirv-headers_likeMABS/ spirv-headers',
		'!SWITCHDIR|../_build',
		'if [ -d "../external/googletest" ] ; then rm -fvR "../external/googletest" ; fi',
		'if [ -d "../external/effcee" ] ; then rm -fvR "../external/effcee" ; fi',
		'if [ -d "../external/re2" ] ; then rm -fvR "../external/re2" ; fi',
		'git clone https://github.com/google/googletest.git          ../external/googletest',
		'git clone https://github.com/google/effcee.git              ../external/effcee',
		'git clone https://github.com/google/re2.git                 ../external/re2',
	],
	'depends_on' : [ 'spirv-headers_likeMABS', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'SPIRV-Tools' },
}