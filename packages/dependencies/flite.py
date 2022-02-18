{
	'repo_type' : 'git',
	'url' : '"https://github.com/festvox/flite.git"',
	#'depth_git': 0,
	#'branch' : 'tags/v2.2',
	'configure_options' : '{autoconf_prefix_options} --bindir="{target_prefix}/bin" --disable-shared --enable-static --with-audio=none', # 2019.12.13 --target_os={target_OS}  --bindir=DIR --libdir=DIR --includedir=DIR   
	'run_post_regexreplace' : [
		'sed -i.bak0 "s|#include \<string.h\>|#include \<string.h\>\\n#include \<windows.h\>|g" configure', # 2022.02.18
		'sed -i.bak2 "s|-DUNDER_WINDOWS -DWIN32|-DUNDER_WINDOWS -DWIN64|g" configure.in', # 2022.02.18
		'sed -i.bak2 "s|-DUNDER_WINDOWS -DWIN32|-DUNDER_WINDOWS -DWIN64|g" configure', # 2022.02.18
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
	#OLD: pre-2022.02.18
	#'repo_type' : 'archive',
	#'download_locations' : [  # http://www.festvox.org/flite/   https://github.com/festvox/flite
		##{ 'url' : 'http://ftp2.za.freebsd.org/pub/FreeBSD/ports/distfiles/flite-1.4-release.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '45c662160aeca6560589f78daf42ab62c6111dd4d244afc28118c4e6f553cd0c' }, ], },
		##{ 'url' : 'http://www.speech.cs.cmu.edu/flite/packed/flite-1.4/flite-1.4-release.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '45c662160aeca6560589f78daf42ab62c6111dd4d244afc28118c4e6f553cd0c' }, ], },
		# http://www.festvox.org/flite/packed/flite-1.4/flite-1.4-release.tar.bz2
		# http://www.festvox.org/flite/packed/flite-2.1/flite-2.1-release.tar.bz2
	#],
	#'patches' : [
	#	('flite/flite_64.diff', '-p0'),
	#],
	#'run_post_regexreplace' : [
	#	'sed -i.bak1 "s|i386-mingw32-|{cross_prefix_bare}|g" configure', # 2019.12.13
	#	'sed -i.bak2 "s|-DWIN32 -shared|-DWIN64 -static|g" configure', # 2019.12.13
	#],	
	#'cpu_count' : '1',
	#'needs_make_install' : False,
	#'configure_options' : '{autoconf_prefix_options} --disable-shared --enable-static', # 2019.12.13 --bindir=DIR --libdir=DIR --includedir=DIR   
	#'run_post_build' : [
	#	'mkdir -pv "{target_prefix}/include/flite"',
	#	'cp -fv include/* "{target_prefix}/include/flite"',
	#	'cp -fv ./build/{bit_name}-mingw32/lib/*.a "{target_prefix}/lib"',
	#],
	#'update_check' : { 'url' : 'http://www.speech.cs.cmu.edu/flite/packed/', 'type' : 'httpindex', 'regex' : r'flite-(?P<version_num>[\d.]+)\/' },	
	#'_info' : { 'version' : '1.4', 'fancy_name' : 'flite' },
