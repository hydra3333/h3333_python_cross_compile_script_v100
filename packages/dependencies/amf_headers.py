{
	'repo_type' : 'git',
	'url' : 'https://github.com/GPUOpen-LibrariesAndSDKs/AMF',	# 2023.01.28, use this, deaqdsix27's source is well out of date
	'rename_folder' : 'AMF_headers',
	'depth_git': 1,
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	'run_post_regexreplace' : [
		'if [ ! -d "{target_prefix}/include/AMF" ]; then mkdir -p "{target_prefix}/include/AMF" ; fi',
		'pwd',
		'!SWITCHDIR|amf/public/include',
		'pwd',
		# use install, per MABS
		'install -D -p -v -t "{target_prefix}/include/AMF/core" core/*.h',
		'install -D -p -v -t "{target_prefix}/include/AMF/components" components/*.h',
		'!SWITCHDIR|../../..',
		'pwd',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'AMF (headers)' },
}
