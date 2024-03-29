{
	'repo_type' : 'none',
	'folder_name' : 'opencl_non_icd',
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	#'run_pre_depends_on' : [ # run_pre_depends_on causes this to run even though is_dep_inheriter is true
	'run_post_regexreplace' : [
		#'echo ""',
		#'ls -al',
		#'rm -fv "./OpenCL.dll ./libOpenCL.a ./OpenCL.def ./already_ran_make_install"',
		#'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/OpenCL.dll?raw=true" --retry 50 -L --output "./OpenCL.dll"',
		#'ls -al',
		#'echo "1. cross_prefix_full={cross_prefix_full}"',
		#'echo "2. cross_prefix_bare={cross_prefix_bare}"',
		#'echo "3. mingw_binpath={mingw_binpath}"',
		#'ls -al "{mingw_binpath}"',
		#'echo ""',
		#'ls -al "{cross_prefix_full}dlltool"',
		#'ls -al "{mingw_binpath}/gendef"',
		#'echo ""',
		#'{mingw_binpath}/gendef OpenCL.dll',
		#'echo ""',
		#'{cross_prefix_full}dlltool -l libOpenCL.a -d OpenCL.def -k -A',
		#'echo ""',
		#'ls -al',
		'rm -fv "./OpenCL.dll ./libOpenCL.a ./OpenCL.def ./already_ran_make_install"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/OpenCL.def?raw=true" --retry 50 -L --output "./OpenCL.def"',
		'curl -4 "https://github.com/hydra3333/h3333_python_cross_compile_script_v100/blob/master/sources/libOpenCL.a?raw=true" --retry 50 -L --output "./libOpenCL.a"',
		'cp -fv "libOpenCL.a" "{target_prefix}/lib/libOpenCL.a"',     # 2020.04.28
		'cp -fv "libOpenCL.a" "{target_prefix}/lib/libOpenCL.dll.a"', # 2020.04.28
		'echo ""',
		'echo ""',
		'echo ""',
		'echo "To create a new libOpenCL.a after a new nvidia driver is installed on a Win10x64 PC,"',
		'echo "1. Copy C:\Windows\System32\OpenCL.dll to a vm with mingw etc installed into folder ~/Desktop/OpenCL/"',
		'echo "2. /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/gendef OpenCL.dll"',
		'echo "3. /home/u/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-dlltool -l libOpenCL.a -d OpenCL.def -k -A"',
		'echo "4. Copy/upload/commit resulting libOpenCL.a and libOpenCL.def into sources folder in the git"',
		'echo ""',
		'echo ""',
		'echo ""',
		'touch already_ran_make_install',
	],
	'depends_on' : [ 'opencl_headers' ],	
	'_info' : { 'version' : 'windows/system32/OpenCL.dll', 'fancy_name' : 'OpenCL-non-ICD' }, # 2020.04.28
}
