{	# SHADERC has commit reviisions specified in file DEPS.
	# eg the glslang version where sometimes glslang is ahead of shaderc and it breaks things when they are not compatible.
	# So ... find the relevant compatible commit(s) and save them
	#
	
	#'is_dep_inheriter' : True, 
	'repo_type' : 'none',
	'folder_name' : 'shaderc_commit_dependencies',
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	#
	#'run_pre_depends_on' : [ # run_pre_depends_on causes this to run even though is_dep_inheriter is true
	'run_post_regexreplace' : [	# not using is_dep_inheriter and run_pre_depends_on allows the system to create the folder etc for us
		#'pwd',
		#'ls -al',
		#'!SWITCHDIR|x86_64',
		#'if [ ! -d "shaderc_commit_dependencies" ]; then mkdir -pv shaderc_commit_dependencies ; fi',
		#'!SWITCHDIR|shaderc_commit_dependencies',
		#'pwd ; ls -al',
		'if [ -f "DEPS" ] ; then rm -fv DEPS ; fi',
		'wget https://raw.githubusercontent.com/google/shaderc/main/DEPS',
		#'cat ./DEPS',
		#
		'if [ -f "./glslang_revision.txt" ] ; then rm -f ./glslang_revision.txt ; fi',
		'if [ -f "./glslang_revision.commit" ] ; then rm -f ./glslang_revision.commit ; fi',
		'grep "\'glslang_revision\':" ./DEPS >> ./glslang_revision.commit',
		'sed -i "s/  \'glslang_revision\': \'//g" ./glslang_revision.commit',
		'sed -i "s/\',//g" ./glslang_revision.commit',
		'cp -fv ./glslang_revision.commit ./glslang_revision.txt',
		'sed -i "s/^/export glslang_revision=/" ./glslang_revision.txt',
		'chmod +x ./glslang_revision.txt',
		'chmod +x ./glslang_revision.commit',
		'cat ./glslang_revision.commit ; cat ./glslang_revision.txt',
		#
		'if [ -f "./spirv_headers_revision.txt" ] ; then rm -f ./spirv_headers_revision.txt ; fi',
		'if [ -f "./spirv_headers_revision.commit" ] ; then rm -f ./spirv_headers_revision.commit ; fi',
		'grep "\'spirv_headers_revision\':" ./DEPS >> ./spirv_headers_revision.commit',
		'sed -i "s/  \'spirv_headers_revision\': \'//g" ./spirv_headers_revision.commit',
		'sed -i "s/\',//g" ./spirv_headers_revision.commit',
		'cp -fv ./spirv_headers_revision.commit ./spirv_headers_revision.txt',
		'sed -i "s/^/export spirv_headers_revision=/" ./spirv_headers_revision.txt',
		'chmod +x ./spirv_headers_revision.txt',
		'chmod +x ./spirv_headers_revision.commit',
		'cat ./spirv_headers_revision.commit ; cat ./spirv_headers_revision.txt',
		#
		'if [ -f "./spirv_tools_revision.txt" ] ; then rm -f ./spirv_tools_revision.txt ; fi',
		'if [ -f "./spirv_tools_revision.commit" ] ; then rm -f ./spirv_tools_revision.commit ; fi',
		'grep "\'spirv_tools_revision\':" ./DEPS >> ./spirv_tools_revision.commit',
		'sed -i "s/  \'spirv_tools_revision\': \'//g" ./spirv_tools_revision.commit',
		'sed -i "s/\',//g" ./spirv_tools_revision.commit',
		'cp -fv ./spirv_tools_revision.commit ./spirv_tools_revision.txt',
		'sed -i "s/^/export spirv_tools_revision=/" ./spirv_tools_revision.txt',
		'chmod +x ./spirv_tools_revision.txt',
		'chmod +x ./spirv_tools_revision.commit',
		'cat ./spirv_tools_revision.commit ; cat ./spirv_tools_revision.txt',
		#
		#'cat {inTreePrefix}/glslang_revision.txt',
		#'!CMD(cat {inTreePrefix}/glslang_revision.txt)CMD! ; export',
		#'cat {inTreePrefix}/spirv_headers_revision.txt',
		#'!CMD(cat {inTreePrefix}/spirv_headers_revision.txt)CMD! ; export',
		#'cat {inTreePrefix}/spirv_tools_revision.txt',
		#'!CMD(cat {inTreePrefix}/spirv_tools_revision.txt)CMD! ; export',
		#'printenv',
		#
		'if [ -f "already_done" ] ; then rm -fv  "already_done" ; fi',
		'touch  "already_done"',
		#'pwd',
		#'ls -al',
		#'!SWITCHDIR|..',
		#'!SWITCHDIR|..',
		#'pwd',
		#'ls -al',
		#--------------------------------------
		#--------------------------------------
		#
		# To pass a variable to parent process:
		#	child process:
		#		echo ${variable} >/tmp/file
		#	parent process:
		#		read variable </tmp/file
		#--------------------------------------
		#--------------------------------------
	],
	#'depends_on' : [ , ],
	'_info' : { 'version' : 'see shaderc file DEPS', 'fancy_name' : 'shaderc_commit_dependencies' }, # 2022.02.04
}