{
	'repo_type' : 'git',
	'url': 'https://github.com/libffi/libffi.git',
	'rename_folder' : 'libffi_git', # 2019.12.13
	'run_post_patch' : [ # 2019.12.13
		#'./autogen.sh', # 2019.12.13
		'autoreconf -fiv', # 2019.12.13
	], # 2019.12.13
    #'configure_options': '{autoconf_prefix_options} --disable-doc', # 2019.12.13
    'configure_options': '{autoconf_prefix_options} --disable-shared --enable-static --enable-portable-binary --enable-purify-safety --disable-doc', # 2019.12.13
	'depends_on' : [ # 2019.12.13
		'gettext', # 2019.12.13
	], # 2019.12.13
    '_info' : { 'version' : '3.3', 'fancy_name' : 'libffi' },
}