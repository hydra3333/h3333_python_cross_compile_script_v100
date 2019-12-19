{
	'repo_type' : 'git',
	'recursive_git' : True,
	'url' : 'https://code.videolan.org/videolan/libbluray',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-examples --disable-doxygen-doc --disable-bdjava-jar --enable-udf', #--without-libxml2 --without-fontconfig .. optional.. I guess
	'patches' : [
		('libbluray/libbluray_git_remove_strtok_s.patch', '-p1'),
	],
	'run_post_install' : [ # 2019.12.13
	#	'sed -i.bak \'s/-lbluray.*$/-lbluray -lfreetype -lexpat -lz -lbz2 -lxml2 -lws2_32 -lgdi32 -liconv/\' "{pkg_config_path}/libbluray.pc"', # fix undefined reference to `xmlStrEqual' and co  # 2019.12.13
		'sed -i.bak \'s/-lbluray.*$/-lbluray -lfreetype -lexpat -lz -lbz2 -lxml2 -lws2_32 -lgdi32 -liconv -laacs/\' "{pkg_config_path}/libbluray.pc"', # fix undefined reference to `xmlStrEqual' and co # 2018.11.23 add -laacs  # 2019.12.13
	], # 2019.12.13
	'depends_on' : [
		'freetype', 'libaacs', 'libcdio-paranoia'  # 2019.12.13 added libaacs
	],
	'_info' : { 'version' : None, 'fancy_name' : 'libbluray' },
}
# 2019.12.13 old:
#	'libbluray' : {
#		'repo_type' : 'git',
#		'recursive_git' : True,
#		#'url' : 'https://git.videolan.org/git/libbluray.git',
#		'url' : 'https://code.videolan.org/videolan/libbluray.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-examples --disable-doxygen-doc --disable-bdjava-jar --enable-udf', #--without-libxml2 --without-fontconfig .. optional.. I guess # 2018.11.23 enable examples
#		'patches' : (
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/libbluray_git_remove_strtok_s.patch', '-p1'),
#		),
#		'run_post_install' : (
#			'sed -i.bak \'s/-lbluray.*$/-lbluray -lfreetype -lexpat -lz -lbz2 -lxml2 -lws2_32 -lgdi32 -liconv -laacs/\' "{pkg_config_path}/libbluray.pc"', # fix undefined reference to `xmlStrEqual' and co # 2018.11.23 add -laacs
#		),
#		'depends_on' : (
#			'freetype', 'libaacs', 'libcdio-paranoia' # 2018.11.23 added libaacs 'libaacs', 'libcdio-paranoia'
#		),
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libbluray' },
#	},