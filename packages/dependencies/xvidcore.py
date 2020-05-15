{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://downloads.xvid.com/downloads/xvidcore-1.3.7.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'aeeaae952d4db395249839a3bd03841d6844843f5a4f84c271ff88f7aa1acff7' }, ], },
		#{ 'url' : 'https://downloads.xvid.com/downloads/xvidcore-1.3.5.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '5e6b58b13c247fe7a9faf9b95517cc52bc4b59a44b630cab20aae0c7f654f77e' }, ], },
	],
	'folder_name' : 'xvidcore',
	'rename_folder' : 'xvidcore-1.3.7',
	'source_subfolder' : 'build/generic',
	'configure_options' : '--host={target_host} --prefix={target_prefix}',
	# 'run_post_configure' : [
	# 	'sed -i.bak "s/-mno-cygwin//" platform.inc',
	# ],
	'run_post_install' : [
		'rm -v {target_prefix}/lib/xvidcore.dll.a',
		'mv -v {target_prefix}/lib/xvidcore.a {target_prefix}/lib/libxvidcore.a',
	],
	# last i checked their website (xvid one) had some shitty DDoS protection or w/e, which needs shitty JS to verify, so no way to parse the site.
	#'update_check' : { 'url' : 'https://labs.xvid.com/source/', 'type' : 'httpindex', 'regex' : r'xvidcore-(?P<version_num>[\d.]+)\.tar\.gz' },
	'_info' : { 'version' : '1.3.7', 'fancy_name' : 'xvidcore' },
}
