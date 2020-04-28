{
	'repo_type' : 'none',
	'folder_name' : 'opencl_non_icd',
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	#'run_pre_depends_on' : [
	#],
	'run_post_regexreplace' : [
		'echo ""',
		'ls -al',
		'rm -fv "./OpenCL.dll ./libOpenCL.a ./OpenCL.def ./already_ran_make_install"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/OpenCL.dll?raw=true" --retry 50 -L --output "./OpenCL.dll"',
		#'ls -al',
		#'echo "1. cross_prefix_full={cross_prefix_full}"',
		#'echo "2. cross_prefix_bare={cross_prefix_bare}"',
		#'echo "3. mingw_binpath={mingw_binpath}"',
		#'ls -al "{mingw_binpath}"',
		#'echo ""',
		#'ls -al "{cross_prefix_full}dlltool"',
		#'ls -al "{mingw_binpath}/gendef"',
		'echo ""',
		'{mingw_binpath}/gendef OpenCL.dll',
		'echo ""',
		'{cross_prefix_full}dlltool -l libOpenCL.a -d OpenCL.def -k -A',
		'echo ""',
		'ls -al',
		'cp -fv "libOpenCL.a" "{target_prefix}/lib/libOpenCL.a"',     # 2020.04.28
		'cp -fv "libOpenCL.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2020.04.28
		'echo ""',
		'touch already_ran_make_install',
	],
	'depends_on' : [ 'opencl_headers' ],	
	'_info' : { 'version' : 'windows/system32/OpenCL.dll', 'fancy_name' : 'OpenCL-non-ICD' }, # 2020.04.28
}
