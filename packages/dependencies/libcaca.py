{
	'repo_type' : 'git',
	'url' : 'https://github.com/cacalabs/libcaca.git',
	'run_post_configure' : [
		'sed -i.bak "s/int vsnprintf/int vnsprintf_disabled/" "caca/string.c"',
		'sed -i.bak "s/int vsnprintf/int vnsprintf_disabled/" "caca/figfont.c"',
		'sed -i.bak "s/__declspec(dllexport)//g" cxx/caca++.h',
		'sed -i.bak "s/__declspec(dllexport)//g" caca/caca.h',
		'sed -i.bak "s/__declspec(dllexport)//g" caca/caca0.h',
		'sed -i.bak "s/__declspec(dllimport)//g" caca/caca.h',
		'sed -i.bak "s/__declspec(dllimport)//g" caca/caca0.h',
	],
	'run_post_install' : [
		"sed -i.bak 's/-lcaca *$/-lcaca -lz/' \"{pkg_config_path}/caca.pc\"",
	],
	'configure_options' : '{autoconf_prefix_options} --libdir={target_prefix}/lib --disable-shared --enable-static --disable-cxx --disable-csharp --disable-java --disable-python --disable-ruby --disable-imlib2 --disable-doc --disable-examples', # 2019.12.13
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcaca' },
}
