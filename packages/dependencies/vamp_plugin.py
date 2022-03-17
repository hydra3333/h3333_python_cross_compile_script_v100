{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/sources/vamp-plugin-sdk-2.9.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b72a78ef8ff8a927dc2ed7e66ecf4c62d23268a5d74d02da25be2b8d00341099' }, ], }, # 2019.12.13
		{ 'url' : 'https://code.soundsoftware.ac.uk/attachments/download/2588/vamp-plugin-sdk-2.9.0.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'b72a78ef8ff8a927dc2ed7e66ecf4c62d23268a5d74d02da25be2b8d00341099' }, ], },
	],
	'run_post_regexreplace' : [
		'cp -fv build/Makefile.mingw64 Makefile',
		'autoreconf -fiv',
	],
	'patches' : [
		('vamp/vamp-plugin-sdk-2.7.1.patch','-p0'), #They rely on M_PI which is gone since c99 or w/e, give them a self defined one and hope for the best.
	],
	'configure_options' : 'sdkstatic --host={target_host} --prefix={target_prefix}--libdir={target_prefix}/lib --disable-programs ',
	'build_options' : '{make_prefix_options} sdkstatic  --host={target_host} --prefix={target_prefix} --libdir={target_prefix}/lib --disable-programs ', # for DLL's add 'sdk rdfgen' # 2022.03.17 try 'configure' instead if just build 
	'needs_make_install' : False, # doesnt s support xcompile installing
	'run_post_build' : [ # lets install it manually then I guess?
		'cp -fv libvamp-sdk.a "{target_prefix}/lib/"',
		'cp -fv libvamp-hostsdk.a "{target_prefix}/lib/"',
		'cp -frv vamp-hostsdk/ "{target_prefix}/include/"',
		'cp -frv vamp-sdk/ "{target_prefix}/include/"',
		'cp -frv vamp/ "{target_prefix}/include/"',
		'cp -fv pkgconfig/vamp.pc.in "{target_prefix}/lib/pkgconfig/vamp.pc"',
		'cp -fv pkgconfig/vamp-hostsdk.pc.in "{target_prefix}/lib/pkgconfig/vamp-hostsdk.pc"',
		'cp -fv pkgconfig/vamp-sdk.pc.in "{target_prefix}/lib/pkgconfig/vamp-sdk.pc"',
		'sed -i.bak \'s/\%PREFIX\%/{target_prefix_sed_escaped}/\' "{pkg_config_path}/vamp.pc"',
		'sed -i.bak \'s/\%PREFIX\%/{target_prefix_sed_escaped}/\' "{pkg_config_path}/vamp-hostsdk.pc"',
		'sed -i.bak \'s/\%PREFIX\%/{target_prefix_sed_escaped}/\' "{pkg_config_path}/vamp-sdk.pc"',
	],
	'depends_on' : ['libsndfile',],
	'update_check' : { 'url' : 'https://vamp-plugins.org/develop.html', 'type' : 'httpregex', 'regex' : r'.*<ul><li>Download the <b>Vamp plugin SDK<\/b> \(version (?P<version_num>[\d.]+)\):.*' },
	# { 'url' : 'https://code.soundsoftware.ac.uk/projects/vamp-plugin-sdk/files/', 'type' : 'httpindex', 'regex' : r'	vamp-plugin-sdk-(?P<version_num>[\d.]+)\.tar\.gz', },
	'_info' : { 'version' : '2.9.0', 'fancy_name' : 'vamp-plugin-sdk' },
}
