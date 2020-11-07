{
	'repo_type' : 'git',
	'url' : 'https://github.com/georgmartius/vid.stab.git', #"Latest commit 97c6ae2  on May 29, 2015" .. master then I guess?
	'depth_git' : 0,
	'branch' : 'e7715fcf329573cdcff5c57d0e4a25f4c3a0cb7f', # commit after this fails per vidstab issue https://github.com/georgmartius/vid.stab/issues/98
	'rename_folder' : 'vidstab_git',
	'conf_system' : 'cmake',
	'configure_options' : '{cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DENABLE_SHARED=OFF -DCMAKE_AR={cross_prefix_full}ar -DUSE_OMP=OFF', #fatal error: omp.h: No such file or directory
	#'patches' : [
	#	('vidstab/94-from-mabs-2020.11.03.patch','-Np1'), # 2020.11.03 per MABS # ,'..'
	#],
	'run_post_regexreplace' : [
		'sed -i.bak "s/SHARED/STATIC/g" CMakeLists.txt',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'vid.stab' },
}
