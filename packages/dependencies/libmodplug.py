{
	'repo_type' : 'git',
	'url': 'https://github.com/Konstanty/libmodplug.git',
	'conf_system' : 'cmake',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DMODPLUG_STATIC=1 -DBUILD_SHARED_LIBS=0',  # 2019.12.13
	'source_subfolder': '_build',
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
