{
	# 'debug_downloadonly': True,
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/lame/files/lame/3.100/lame-3.100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/lame-3.100.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e' }, ], },
	],
	'patches' : [ # 2019.12.13
		('lame/0007-revert-posix-code.patch','-Np1'), # borrowing their file since lame will fix this shortly anyway, its already fixed on svn
		# patchjes from Alexpux follow:
		('lame/0002-07-field-width-fix.all.patch','-p1'), # 
		('lame/0005-no-gtk.all.patch','-p1'), # 
		('lame/0006-dont-use-outdated-symbol-list.patch','-p1'), # 
		('lame/0008-skip-termcap.patch','-p1'), # 
	],
    'run_post_regexreplace' : ( # 2019.12.13
		'autoreconf -fiv',
	),
	'depends_on' : ['iconv'],
	'configure_options' : '--build=x86_64-linux-gnu --host={target_host} --target={target_host} --without-libiconv-prefix --prefix={output_prefix}/lame-3.100.installed --disable-shared --enable-static --enable-nasm', # 2019.12.13
	'update_check' : { 'url' : 'https://sourceforge.net/projects/lame/files/lame/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '3.100', 'fancy_name' : 'LAME3.100' }, # 2019.12.13
}
# 2019.12.13 old:
#	'lame' : {
#		# 'debug_downloadonly': True,
#		'repo_type' : 'archive',
#		'download_locations' : [
#			#UPDATECHECKS: https://sourceforge.net/projects/lame/files/lame/
#			{ "url" : "https://sourceforge.net/projects/lame/files/lame/3.100/lame-3.100.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e" }, ], },
#			{ "url" : "https://fossies.org/linux/misc/lame-3.100.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e" }, ], },
#		],
#		'folder_name' : 'lame_3.100',
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
#		'depends_on' : ['iconv'],
#		'configure_options': '--build=x86_64-linux-gnu --host={target_host} --target={target_host} --without-libiconv-prefix --prefix={product_prefix}/lame-3.100.installed --disable-shared --enable-static --enable-nasm',
#		'_info' : { 'version' : '3.100', 'fancy_name' : 'LAME 3.100' },
#	},