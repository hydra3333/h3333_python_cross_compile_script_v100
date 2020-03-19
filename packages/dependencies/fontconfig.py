{
	'repo_type' : 'git',
	'do_not_bootstrap' : True,
	'url' : 'https://gitlab.freedesktop.org/fontconfig/fontconfig.git',
	'folder_name' : 'fontconfig_git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --enable-libxml2 --disable-docs --disable-silent-rules --with-expat',
	'patches' : [
		('fontconfig/0001-fontconfig-remove-tests.patch', '-p1' ),
		# ('fontconfig/fontconfig-git-utimes.patch', '-p1' ),
		# ('fontconfig/fontconfig-0001-fix-missing-bracket.patch', '-p1' ),
	],
	'run_post_patch' : [
		'autoreconf -fiv',
	],
	'regex_replace': {
		'post_install': [
			{
				0: r'Requires:  freetype2',
				1: r'Requires: harfbuzz libxml-2.0 freetype2',
				'in_file': '{pkg_config_path}/fontconfig.pc'
			},
			{
				0: r'Libs: -L\${{libdir}} -lfontconfig',
				1: r'Libs: -L${{libdir}} -lfontconfig -lfreetype -lharfbuzz -lxml2 -liconv -lintl -liconv ', # 2019.12.13 added a few
				'in_file': '{pkg_config_path}/fontconfig.pc'
			}
		]
	},

	'depends_on' : [
		'expat', 'iconv', 'libxml2', 'freetype', 'bzip2', # 2020.03.19 removed 'json-c' again after trying to add it back
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'fontconfig' },
}
# 2019.12.13 old:
#	'fontconfig' : { # 2018.11.23 combination of deadsix27 and alexpux patching
#		'repo_type' : 'git',
#		'do_not_bootstrap' : True,
#		'cpu_count' : '1', # I had strange build issues with multiple threads..
#		#'branch' : '9b0c093a6a925b71a099f8f4b489d83572c77afe', 
#		'url' : 'https://gitlab.freedesktop.org/fontconfig/fontconfig.git',
#		'folder_name' : 'fontconfig_git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --enable-libxml2 --disable-shared --enable-static --disable-docs --disable-silent-rules',
#		'patches' : [ 
#			#['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig/fontconfig-git-utimes.patch', '-Np1' ], # from deadsix27 2018.11.08 for 648e0cf3d5a53efeab93b24ae37490427d05229d
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig/fontconfig-git-utimes-2019.04.04.patch', '-Np1' ], # they updated fontconfig so a new patch required
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig-from-Alexpux-2_13_1/0001-mingwcompat-remove-tests.patch', '-Np1' ], # 2018.10.22 is equiv to ds27 patch https://raw.githubusercontent.com/DeadSix27/misc_patches/master/fontconfig/0001-fontconfig-remove-tests.patch
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig-from-Alexpux-2_13_1/0001-fix-config-linking.all.patch', '-Np1' ],
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig-from-Alexpux-2_13_1/0002-fix-mkdir.mingw.patch', '-Np1' ],
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig-from-Alexpux-2_13_1/0004-fix-mkdtemp.mingw.patch', '-Np1' ],
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig-from-Alexpux-2_13_1/0005-fix-setenv.mingw.patch', '-Np1' ],
#			['https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v02/master/patches/fontconfig-from-Alexpux-2_13_1/0007-pkgconfig.mingw.patch', '-Np1' ],
#		],
#		'run_post_patch': [
#			'autoreconf -fiv',
#		],
#		'run_post_install': (
#			'sed -i.bak \'s/-L${{libdir}} -lfontconfig[^l]*$/-L${{libdir}} -lfontconfig -lfreetype -lharfbuzz -lxml2 -lintl -liconv/\' "{pkg_config_path}/fontconfig.pc"', # 2018.11.23 -lintl -liconv in that order
#		),
#		'depends_on' : [
#			'iconv', 'gettext', 'libxml2', 'freetype', 'bzip2', 'expat', # 2018.11.23 added 'gettext', 'bzip2', 'expat',
#		],
#		'packages': {
#			'arch' : [ 'gperf' ],
#		},
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'fontconfig' },
#	},