# 2021.10.30 this and its patches are completely different to deadsix27 ... if this does not work then perhaps reconcile.
#            note: one of deadsix27 patches appears to be "older" in part(s)
{ # in ubuntu 18.04.3 : CMake Error at src/CMakeLists.txt:1 (cmake_minimum_required):   CMake 3.11 or higher is required.  You are running version 3.10.2
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/flac.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	#'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=OFF -DBUILD_PROGRAMS=OFF -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.3 -DCMAKE_BUILD_TYPE=Release',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} '
								'-DENABLE_64_BIT_WORDS=ON -DBUILD_PROGRAMS=OFF -DBUILD_UTILS=OFF -DINSTALL_PKGCONFIG_MODULES=ON -DINSTALL_MANPAGES=OFF -DBUILD_SHARED_LIBS=OFF '
								'-DWITH_OGG=ON -DBUILD_DOCS=OFF -DWITH_STACK_PROTECTOR=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF -DVERSION=1.3.4 '
								'-DCMAKE_BUILD_TYPE=Release',
#	'patches': [
#		('flac/0001-mingw-fix-2020.05.14.patch', '-p1', '..'), # 2020.05.11 from deadsix27
#		('flac/0001-mingw-fix-src-CMakeLists-2020.05.14.patch', '-p1', '..'), # 2020.05.11 from deadsix27
#	],
	'run_post_patch' : [
		#'sed -i.bak "s/#elif defined(_WIN32)/#elif defined(_MSC_VER)/" ../include/FLAC++/export.h',
		#'diff -U 5 "../include/FLAC++/export.h.bak" "../include/FLAC++/export.h"  && echo "NO difference" || echo "YES differences!"',
		#'sed -i.bak "s/#elif defined(_WIN32)/#elif defined(_MSC_VER)/" ../include/FLAC/export.h',
		#'diff -U 5 "../include/FLAC/export.h.bak" "../include/FLAC/export.h"  && echo "NO difference" || echo "YES differences!"',
		#'sed -i.bak "s/Libs: -L${libdir} -lFLAC/Libs: -L${libdir} -lFLAC -lssp/" ../src/libFLAC++/flac++.pc.in',
		#'diff -U 5 "../src/libFLAC++/flac++.pc.in.bak" "../src/libFLAC++/flac++.pc.in"  && echo "NO difference" || echo "YES differences!"',
		#'sed -i.bak "s/Libs: -L${libdir} -lFLAC/Libs: -L${libdir} -lFLAC -lssp/" ../src/libFLAC/flac.pc.in',
		#'diff -U 5 "../src/libFLAC/flac.pc.in.bak" "../src/libFLAC/flac.pc.in"  && echo "NO difference" || echo "YES differences!"',
		#
		#
		'sed -i.bak "s|__declspec(dllimport)||g" ../include/FLAC++/export.h',
		'diff -U 5 "../include/FLAC++/export.h.bak" "../include/FLAC++/export.h"  && echo "NO difference" || echo "YES differences!"',
		'sed -i.bak "s|__declspec(dllimport)||g" ../include/FLAC/export.h',
		'diff -U 5 "../include/FLAC/export.h.bak" "../include/FLAC/export.h"  && echo "NO difference" || echo "YES differences!"',
		'sed -i.bak \'s|add_subdirectory("microbench")||g\' ../CMakeLists.txt',
		'diff -U 5 "../CMakeLists.txt.bak" "../CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"',
		'cp -fv ../src/CMakeLists.txt ../src/CMakeLists.txt.orig',
		'sed -i.bak "s|add_subdirectory(utils/flacdiff)||g"  ../src/CMakeLists.txt',
		'sed -i.bak "s|add_subdirectory(utils/flactimer)||g" ../src/CMakeLists.txt',
		'diff -U 5 "../src/CMakeLists.txt.orig" "../src/CMakeLists.txt"  && echo "NO difference" || echo "YES differences!"',
		#
		'pwd ; cd .. ; sh ./autogen.sh --no-symlink ; cd _build ; pwd',
	],
	'run_post_install' : [
		'sed -i.bak "s|__declspec(dllimport)||g" {target_prefix}/include/FLAC++/export.h',
		'diff -U 5 "{target_prefix}/include/FLAC++/export.h.bak" "{target_prefix}/include/FLAC++/export.h"  && echo "NO difference" || echo "YES differences!"',
		'sed -i.bak "s|__declspec(dllimport)||g" {target_prefix}/include/FLAC/export.h',
		'diff -U 5 "{target_prefix}/include/FLAC/export.h.bak" "{target_prefix}/include/FLAC/export.h"  && echo "NO difference" || echo "YES differences!"',
	],
	'depends_on' : [
		'libogg',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'flac (library)' },
}
