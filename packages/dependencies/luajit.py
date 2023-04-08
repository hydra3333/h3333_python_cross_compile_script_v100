{
	'repo_type' : 'git',
	#'url' : 'http://luajit.org/git/luajit-2.0.git',
	'url' : 'https://repo.or.cz/luajit-2.0.git',
	#'depth_git': 0,
	'depth_git': 1,
	'branch': 'v2.1',
	'needs_configure' : False,
	'install_options' : 'CROSS={cross_prefix_bare} HOST_CC="gcc -m{bit_num}" TARGET_SYS=Windows BUILDMODE=static FILE_T=luajit.exe PREFIX={target_prefix}',
	'build_options' : 'CROSS={cross_prefix_bare} HOST_CC="gcc -m{bit_num}" TARGET_SYS=Windows BUILDMODE=static amalg',
	'depends_on': [ 'libdl' ],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'LuaJIT2' },
}