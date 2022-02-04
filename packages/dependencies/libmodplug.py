{
	'repo_type' : 'git',
	'url': 'https://github.com/Konstanty/libmodplug.git',
    #'download_locations' : [ # 2019.12.13 this was the pre-GIT download location
	#	#UPDATECHECKS: https://sourceforge.net/projects/modplug-xmms/files/libmodplug/
	#	{ "url" : "https://ftp.openbsd.org/pub/OpenBSD/distfiles/libmodplug-0.8.9.0.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "457ca5a6c179656d66c01505c0d95fafaead4329b9dbaa0f997d00a3508ad9de" }, ], },
	#	{ "url" : "https://sourceforge.net/projects/modplug-xmms/files/libmodplug/0.8.9.0/libmodplug-0.8.9.0.tar.gz", "hashes" : [ { "type" : "sha256", "sum" : "457ca5a6c179656d66c01505c0d95fafaead4329b9dbaa0f997d00a3508ad9de" }, ], },
	#],
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DMODPLUG_STATIC=1 -DBUILD_SHARED_LIBS=0',  # 2019.12.13
	'source_subfolder': '_build',
	#
	# 2022.02.04 change to be similar to RDP's
	#'patches': [
	#	('modplug/0001-modplug-mingw-workaround.patch', '-p1', '..'), # to avoid setting -DLIBMODPLUG_STATIC
	#],
    #'run_post_install': ( # 2019.12.13 perhaps not needed in latest git ?
	#	'sed -i.bak \'s/-lmodplug.*/-lmodplug -lstdc++/\' "{pkg_config_path}/libmodplug.pc"', # huh ?? c++?  # 2019.12.13
	#),
    'run_post_install': ( # 2022.02.04 perhaps not needed in latest git ? Do it similar to RDP anyway
		'sed -i.bak \'s/__declspec(dllexport)//\' "{target_prefix}/include/libmodplug/modplug.h"', #strip DLL import/export directives
		'sed -i.bak \'s/__declspec(dllimport)//\' "{target_prefix}/include/libmodplug/modplug.h"', #strip DLL import/export directives
		'sed -i.bak \'s/__declspec(dllexport)//\' "{target_prefix}/include/libmodplug/stdafx.h"', #strip DLL import/export directives
		'sed -i.bak \'s/__declspec(dllimport)//\' "{target_prefix}/include/libmodplug/stdafx.h"', #strip DLL import/export directives
	),
	'regex_replace': {
		'post_patch': [
			{
				# Will they ever realise that WIN32 is True on MinGW as well where we need pkg-config files and so on?
				# Use MSVC or a combination of MINGW/WINDOWS/WIN32
				0: r'if \(NOT WIN32\)',
				1: r'if (NOT MSVC)',
				'in_file': '../CMakeLists.txt'
			},
		],
	},
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libmodplug' },
}
