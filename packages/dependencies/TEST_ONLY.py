{ # per https://github.com/curl/curl/issues/5219#issuecomment-612574575 issues with gcc10 and curl
	'repo_type' : 'git',
	'depth_git' : 0,
	'url' : 'https://github.com/hydra3333/TEST_ONLY.git',
	'needs_make' :False,
	'needs_make_install' :False,
	'needs_configure' :False,
	'run_post_regexreplace' : [ # {bit_name2}-{bit_name_win}-gcc
		'echo "#{bit_name2}-{bit_name_win}-gcc"',
		'echo "#{cross_prefix_bare}"',
		'echo "#{cross_prefix_bare}gcc"',
		'echo "#{cross_prefix_bare}ar"',
		#'##{cross_prefix_bare}x86_64-w64-mingw32-windres ',
		#'##{cross_prefix_bare}x86_64-w64-mingw32-ranlib ',
		'rm -vf shared.o',
		'rm -vf shared2.o',
		'rm -vf libshared.a',
		'rm -vf program.exe',
		'{cross_prefix_bare}gcc -c -o shared.o shared.c',
		'{cross_prefix_bare}gcc -c -o shared2.o shared2.c',
		'{cross_prefix_bare}ar rcs libshared.a shared.o shared2.o',
		'{cross_prefix_bare}gcc -Wall  -L. program.c -o program.exe -lshared',
	],
	#'depends_on' : [ '', ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'none', 'fancy_name' : 'TEST_ONLY' },
}
