{	# SHADERC has commit reviisions specified in file DEPS.
	# eg the glslang version where sometimes glslang is ahead of shaderc and it breaks things when they are not compatible.
	# So ... find the relevant compatible commit(s) and save them
	#
	'is_dep_inheriter' : True,
	'recursive_git' : False,
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	#
	'run_pre_depends_on' : [
		'pwd',
		'!SWITCHDIR|x86_64_products',
		'if [ ! -d "shaderc_commit_dependencies" ]; then mkdir -pv shaderc_commit_dependencies ; fi',
		'!SWITCHDIR|shaderc_commit_dependencies',
		'pwd',
		'if [ -f "DEPS" ] ; then rm -fv DEPS ; fi',
		'wget https://raw.githubusercontent.com/google/shaderc/main/DEPS',
		'cat ./DEPS',
		#
		'if [ -f "./glslang_revision.txt" ] ; then rm -fv ./glslang_revision.txt ; fi',
		'grep "\'glslang_revision\':" ./DEPS >> ./glslang_revision.txt',
		'sed -i "s/  \'glslang_revision\': \'/export glslang_revision=/g" ./glslang_revision.txt',
		'sed -i "s/\',//g" ./glslang_revision.txt',
		'chmod +x ./glslang_revision.txt',
		#'cat ./glslang_revision.txt',
		#
		'if [ -f "./spirv_headers_revision.txt" ] ; then rm -fv ./spirv_headers_revision.txt ; fi',
		'grep "\'spirv_headers_revision\':" ./DEPS >> ./spirv_headers_revision.txt',
		'sed -i "s/  \'spirv_headers_revision\': \'/export spirv_headers_revision=/g" ./spirv_headers_revision.txt',
		'sed -i "s/\',//g" ./spirv_headers_revision.txt',
		'chmod +x ./spirv_headers_revision.txt',
		'cat ./spirv_headers_revision.txt',
		##
		'if [ -f "./spirv_tools_revision.txt" ] ; then rm -fv ./spirv_tools_revision.txt ; fi',
		'grep "\'spirv_tools_revision\':" ./DEPS >> ./spirv_tools_revision.txt',
		'sed -i "s/  \'spirv_tools_revision\': \'/export spirv_tools_revision=/g" ./spirv_tools_revision.txt',
		'sed -i "s/\',//g" ./spirv_tools_revision.txt',
		'chmod +x ./spirv_tools_revision.txt',
		#'cat ./spirv_tools_revision.txt',
		#
		#'cat ./glslang_revision.txt',
		#'!CMD(cat ./glslang_revision.txt)CMD! ; export',
		#'cat ./spirv_headers_revision.txt',
		#'!CMD(cat ./spirv_headers_revision.txt)CMD! ; export',
		#'cat ./spirv_tools_revision.txt',
		#'!CMD(cat ./spirv_tools_revision.txt)CMD! ; export',
		#'printenv',
		#
		'cat ../shaderc_commit_dependencies/glslang_revision.txt',
		'cat ../shaderc_commit_dependencies/spirv_headers_revision.txt',
		'cat ../shaderc_commit_dependencies/spirv_tools_revision.txt',
		#
		'if [ -f "already_done" ] ; then rm -fv  "already_done" ; fi',
		'touch  "already_done"',
		'!SWITCHDIR|..',
		'!SWITCHDIR|..',
		'pwd',
	],
	#
	#'env_exports' : {
	#	'glslang_revision': '!CMD(cat ./glslang_revision.txt)CMD!',
	#	'spirv_tools_revision': '!CMD(cat ./spirv_tools_revision.txt)CMD!',
	#	'spirv_headers_revision': '!CMD(cat ./spirv_headers_revision.txt)CMD!',
	#}
}