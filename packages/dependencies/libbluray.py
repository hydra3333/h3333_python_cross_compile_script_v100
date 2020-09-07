{
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'https://code.videolan.org/videolan/libbluray',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-examples --disable-doxygen-doc --disable-bdjava-jar --enable-udf --enable-dependency-tracking -with-pic', #--without-libxml2 --without-fontconfig --without-freetype ... optional
	'patches' : [
		('libbluray/libbluray_git_remove_strtok_s.patch', '-p1'),
	],
	'run_post_install' : [ # 2019.12.13
	#	'sed -i.bak \'s/-lbluray.*$/-lbluray -lfreetype -lexpat -lz -lbz2 -lxml2 -lws2_32 -lgdi32 -liconv/\' "{pkg_config_path}/libbluray.pc"', # fix undefined reference to `xmlStrEqual' and co  # 2019.12.13
		'sed -i.bak \'s/-lbluray.*$/-lbluray -lfreetype -lexpat -lz -lbz2 -lxml2 -lws2_32 -lgdi32 -liconv -laacs/\' "{pkg_config_path}/libbluray.pc"', # fix undefined reference to `xmlStrEqual' and co # 2018.11.23 add -laacs  # 2019.12.13
	], # 2019.12.13
	'depends_on' : [
		'libxml2', 'freetype', 'libaacs', 'libcdio-paranoia'  # 2019.12.13 added libaacs
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libbluray' },
}
