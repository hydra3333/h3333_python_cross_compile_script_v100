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
    '_info' : { 'version' : 'git (master), 'fancy_name' : 'libffi' },
}
# 2019.12.13 old:
#	'libffi' : {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/libffi/libffi.git',
#		'rename_folder' : 'libffi_git',
#		'run_post_patch' : [
#			#'./autogen.sh',
#			'autoreconf -fiv',
#		],
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-portable-binary --enable-purify-safety --disable-docs',
#		'patches' : [
#		],
#		'depends_on' : [
#			'gettext',
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libffi' },
#	},