{
	'repo_type' : 'git',
	'url' : 'https://github.com/json-c/json-c.git',
	'depth_git': 0,
	'conf_system' : 'cmake',
	#
	#'branch': '2327b23d8e9111ad7d0df7452546c611c0e7ad7e', # this works with -D_FORTIFY_SOURCE=2
	#'source_subfolder' : 'json-c-build',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_RDRAND=ON -DENABLE_THREADING=ON -DDISABLE_WERROR=ON',
	#
	'branch': 'json-c-0.14-20200419', # see https://github.com/json-c/json-c/issues/604
	'source_subfolder' : 'json-c-build',
	#'custom_cflag' : ' -O3 -fstack-protector-all ', # 2020.05.13 json-c hates -D_FORTIFY_SOURCE=2 and it crashes the build ... except when we add the "sed" edit below.
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_STATIC_LIBS=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_RDRAND=ON -DENABLE_THREADING=ON -DDISABLE_WERROR=ON',
	#
	# per https://github.com/json-c/json-c/issues/604 :
	# perhaps try changing the the #if near the start of snprintf_compat.h 
	# from
	#if !defined(HAVE_SNPRINTF) && defined(_MSC_VER)
	# to be something like:
	#if !defined(HAVE_SNPRINTF) && (defined(_MSC_VER) || defined(__MINGW32__))
	'run_post_regexreplace' : [ # 'run_post_patch' : [ # 2020.04.08
		'cp -fv "../snprintf_compat.h" "../snprintf_compat.h-orig"',
		'sed -i \'s/#if !defined(HAVE_SNPRINTF) \&\& defined(_MSC_VER)/#if !defined(HAVE_SNPRINTF) \&\& (defined(_MSC_VER) \|\| defined(__MINGW32__))/g\' "../snprintf_compat.h"',
		'diff -U 5  "../snprintf_compat.h-orig" "../snprintf_compat.h" && echo "NO difference" || echo "YES differences!"',
	],
	#
	'depends_on' : [ 'dlfcn-win32', ], # 2020.05.13 noticed it depended on dlfcn-win32 during building it
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'json-c' },
}
