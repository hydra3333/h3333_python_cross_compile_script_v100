{
	'repo_type' : 'git',
	'url' : 'https://github.com/OpenMPT/openmpt.git',
	#'depth_git' : 0,
	#'branch' : '91bad3bd24045dab4d0d9ad952f02a391a059c7d', # 2020.08.21 the following commit kills cross compiling
	# 'source_subfolder' : '_build',
	'needs_configure' : False,
	'build_options' : 'CONFIG=mingw64-win64 TEST=0 SHARED_LIB=0 STATIC_LIB=1 EXAMPLES=0 ', # https://bugs.openmpt.org/view.php?id=1354#c4423 remove MODERN=1
	'install_options' : 'CONFIG=mingw64-win64 TEST=0 SHARED_LIB=0 STATIC_LIB=1 EXAMPLES=0 MODERN=1 PREFIX={target_prefix}',
	# 'configure_path' : '../build/autotools/configure',
	# 'run_post_regexreplace' : [
		# '!SWITCHDIR|../build/autotools',
		# 'autoreconf -fiv',
		# '!SWITCHDIR|../../_build',
	# ],
	# 'configure_options' : '--prefix={target_prefix} --host={target_host}',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'openmpt' },
}
