{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/lame/files/lame/3.100/lame-3.100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/lame-3.100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e' }, ], },
	],
	'patches' : ( # 2019.12.13
		('liblame/0002-07-field-width-fix.all.patch','-Np1'), # 2019.12.13
		('liblame/0005-no-gtk.all.patch','-Np1'), # 2019.12.13
		('liblame/0006-dont-use-outdated-symbol-list.patch','-Np1'), # 2019.12.13
		('liblame/0007-revert-posix-code.patch','-Np1'), # 2019.12.13
		('liblame/0008-skip-termcap.patch','-Np1'), # 2019.12.13
	), # 2019.12.13
	'run_post_regexreplace' : ( # 2019.12.13
		'autoreconf -fiv', # 2019.12.13
	), # 2019.12.13
    'configure_options': '{autoconf_prefix_options} --build=x86_64-linux-gnu --target={target_host} --disable-shared --enable-static --enable-nasm --disable-frontend', # 2019.12.13
	'update_check' : { 'url' : 'https://sourceforge.net/projects/lame/files/lame/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '3.100', 'fancy_name' : 'LAME (library)' },
}
# 2019.12.13 old:
#	'liblame' : {
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://sourceforge.net/projects/lame/files/lame/
#			{ "url" : "https://sourceforge.net/projects/lame/files/lame/3.100/lame-3.100.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/lame-3.100.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e" }, ], },
#		],
#		'folder_name' : 'liblame_3.100',
#		'patches' : (
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/lame-from-AlexPux/0002-07-field-width-fix.all.patch','-Np1'),
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/lame-from-AlexPux/0005-no-gtk.all.patch','-Np1'),
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/lame-from-AlexPux/0006-dont-use-outdated-symbol-list.patch','-Np1'),
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/lame-from-AlexPux/0007-revert-posix-code.patch','-Np1'),
#			# tgetent() crashes under mingw64, not sure why
#			('https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/lame-from-AlexPux/0008-skip-termcap.patch','-Np1'),
#		),
#		'run_post_regexreplace' : (
#			'autoreconf -fiv',
#		),																					   
#		'configure_options': '--build=x86_64-linux-gnu --host={target_host} --target={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-nasm --disable-frontend', # 2018.11.23
#		'_info' : { 'version' : '3.100', 'fancy_name' : 'LAME 3.100 (library)' },
#	},