{
	'repo_type' : 'git',
	'url' : 'https://github.com/json-c/json-c.git',
	'depth_git': 0,
	'conf_system' : 'cmake',
	'branch': 'json-c-0.14-20200419', # see https://github.com/json-c/json-c/issues/604
	'source_subfolder' : 'json-c-build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=OFF -DBUILD_STATIC_LIBS=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_RDRAND=ON -DENABLE_THREADING=ON -DDISABLE_WERROR=ON',
	#
	# per https://github.com/json-c/json-c/issues/604 : 2020.05.15 fixed in commit d414d3eabc34269fb1f53b32be4547fab2a9a225
	#'run_post_regexreplace' : [ # 'run_post_patch' : [ # 2020.05.13 json-c hates -D_FORTIFY_SOURCE=2 and it crashes the build ... except when we add the "sed" 
	#	'cp -fv "../snprintf_compat.h" "../snprintf_compat.h-orig"',
	#	'sed -i \'s/#if !defined(HAVE_SNPRINTF) \&\& defined(_MSC_VER)/#if !defined(HAVE_SNPRINTF) \&\& (defined(_MSC_VER) \|\| defined(__MINGW32__))/g\' "../snprintf_compat.h"',
	#	'diff -U 5  "../snprintf_compat.h-orig" "../snprintf_compat.h" && echo "NO difference" || echo "YES differences!"',
	#],
	'depends_on' : [ 'dlfcn-win32', ], # 2020.05.13 noticed it depended on dlfcn-win32 during building it
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'json-c' },
}
