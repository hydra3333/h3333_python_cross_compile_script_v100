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
