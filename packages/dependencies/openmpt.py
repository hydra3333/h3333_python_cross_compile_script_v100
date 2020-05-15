{
	'repo_type' : 'git',
	'url' : 'https://github.com/OpenMPT/openmpt.git',
	# 'source_subfolder' : '_build',
	'needs_configure' : False,
	'build_options' : 'CONFIG=mingw64-win64 TEST=0 SHARED_LIB=0 STATIC_LIB=1 EXAMPLES=0 MODERN=1',
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
