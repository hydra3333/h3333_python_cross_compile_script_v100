{
	'repo_type' : 'git', # 2020.10.14 move from xvid.com to MABS-maintained mirror git
	'url' : 'https://github.com/m-ab-s/xvid.git',
	#'depth_git' : 0,
	#'branch' : '',
	#'recursive_git' : True, 
	'source_subfolder' : 'xvidcore/build/generic',
	'patches' : [
		('xvid/MABS-lighde-2020.10.14.patch','-p1','../../..'), # 2020.05.11 per MABS # 
	],
	'configure_options' : '--host={target_host} --prefix={target_prefix}',
	'run_post_install' : [
		'ls -al {target_prefix}/lib/*xvidcore*',
		'rm -vf {target_prefix}/lib/libxvidcore.a',
		'ls -al {target_prefix}/lib/*xvidcore*',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'Xvid core' },
}
#{
#	'repo_type' : 'archive',
#	'download_locations' : [
#		{ 'url' : 'https://downloads.xvid.com/downloads/xvidcore-1.3.7.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'aeeaae952d4db395249839a3bd03841d6844843f5a4f84c271ff88f7aa1acff7' }, ], },
#	],
#	'folder_name' : 'xvidcore',
#	'rename_folder' : 'xvidcore-1.3.7',
#	'source_subfolder' : 'build/generic',
#	'configure_options' : '--host={target_host} --prefix={target_prefix}',
#	'run_post_install' : [
#		'rm -v {target_prefix}/lib/xvidcore.dll.a',
#		'mv -v {target_prefix}/lib/xvidcore.a {target_prefix}/lib/libxvidcore.a',
#	],
#	# last i checked their website (xvid one) had some shitty DDoS protection or w/e, which needs shitty JS to verify, so no way to parse the site.
#	#'update_check' : { 'url' : 'https://labs.xvid.com/source/', 'type' : 'httpindex', 'regex' : r'xvidcore-(?P<version_num>[\d.]+)\.tar\.gz' },
#	'_info' : { 'version' : '1.3.7', 'fancy_name' : 'xvidcore' },
#}

