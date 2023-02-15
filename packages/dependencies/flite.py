{
	'repo_type' : 'git',
	'url' : 'https://github.com/festvox/flite.git',
	#'depth_git': 0,
	#'branch' : 'tags/v2.2',
	#'patches' : [ # 2022.12.18 per DEADSIX27
	#	('flite/flite_64.diff', '-p0'), # 2022.12.18 per DEADSIX27 however the sed below supersedes the patch
	#], # 2022.12.18 per DEADSIX27
	'configure_options' : '{autoconf_prefix_options} --bindir="{target_prefix}/bin" --disable-shared --enable-static --with-audio=none', # 2019.12.13 --target_os={target_OS}  --bindir=DIR --libdir=DIR --includedir=DIR   
	'run_post_regexreplace' : [
		'sed -i.bak0 "s|#include \<string.h\>|#include \<string.h\>\\n#include \<windows.h\>|g" configure', # 2022.02.18
		#
		'sed -i "s|-DWIN32 -shared|-DWIN64 -static|" configure.in', # 2022.12.18 per DEADSIX27
		#'sed -i.bak2 "s|-DUNDER_WINDOWS -DWIN32|-DUNDER_WINDOWS -DWIN64|g" configure.in',
		'sed -i.bak2 "s|-DWIN32|-DWIN64|g" configure.in', # 2022.12.18
		#
		'sed -i "s|-DWIN32 -shared|-DWIN64 -static|" configure', # 2022.12.18 per DEADSIX27
		#'sed -i.bak2 "s|-DUNDER_WINDOWS -DWIN32|-DUNDER_WINDOWS -DWIN64|g" configure', # 2022.02.18
		'sed -i.bak2 "s|-DWIN32|-DWIN64|g" configure', # 2022.12.18
	],
	'needs_make_install' : False,	# install crashes trying to copy the exe files, so copy the includes and libs manually
	'run_post_build' : [
		'mkdir -pv "{target_prefix}/include/flite"',
		'cp -fv ./include/* "{target_prefix}/include/flite"',
		'cp -fv ./build/{bit_name}-mingw32/lib/*.a "{target_prefix}/lib"',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'flite' },
}
