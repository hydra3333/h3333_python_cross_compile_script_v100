{
	'repo_type' : 'git',
	'url' : 'https://github.com/kcat/openal-soft.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	#'custom_cflag' : '-O3', # native tools have to use the same march as end product else it fails*
	'configure_options' :
		'.. {cmake_prefix_options} -DCMAKE_TOOLCHAIN_FILE=XCompile.txt -DEXTRA_INSTALLS=OFF -DHOST={target_host}'
		' -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_INSTALL_BINDIR={target_prefix}/bin -DCMAKE_INSTALL_DATADIR={target_prefix}/share -DCMAKE_INSTALL_INCLUDEDIR={target_prefix}/include -DCMAKE_INSTALL_LIBDIR={target_prefix}/lib -DCMAKE_FIND_ROOT_PATH=' # 2022.12.18 from deadsix27
		' -DLIBTYPE=STATIC -DALSOFT_UTILS=OFF -DALSOFT_BACKEND_PIPEWIRE=OFF -DALSOFT_EXAMPLES=OFF',
	#'patches' : [
	#	('openal/0001-mingwfixes.patch', '-p1','..'),
	#	#('openal/0001-versioned-w32-dll.mingw.patch', '-p1','..'), # 2022.12.18 from deadsix27
	#	## ('openal/0002-w32ize-portaudio-loading.mingw.patch', '-p1'), # 2022.12.18 from deadsix27
	#	#('openal/0003-openal-not-32.mingw.patch', '-p1','..'), # 2022.12.18 from deadsix27
	#	#('openal/0004-disable-OSS-windows.patch', '-p1','..'), # 2022.12.18 from deadsix27
	#],
	#'run_post_regexreplace' : [ # 2022.12.18 from deadsix27, comment out all these perhaps the updated patch fixes them
	#	"sed -i.bak 's/CMAKE_INSTALL_PREFIX \"\${{CMAKE_FIND_ROOT_PATH}}\"/CMAKE_INSTALL_PREFIX ""/' ../XCompile.txt",
	#	"sed -i.bak 's/FIND_PACKAGE(DSound)/OPTION(ALSOFT_BACKEND_DSOUND \"Enable DirectSound backend\" ON)\\nSET(HAVE_DSOUND 1)\\nSET(BACKENDS  \"${{BACKENDS}} DirectSound${{IS_LINKED}},\")\\nSET(ALC_OBJS  ${{ALC_OBJS}} Alc\/backends\/dsound.cpp Alc\/backends\/dsound.h)/g' ../CMakeLists.txt",
	#],
	#'run_post_install' : [
	#	"sed -i.bak 's/^Libs: -L\${{libdir}} -lopenal $/Libs: -L\${{libdir}} -lopenal -lwinmm -latomic -lm -lole32 -lstdc++/' '{pkg_config_path}/openal.pc'", #issue with it not using pkg-config option "--static" or so idk?
	#],
	'install_options' : 'DESTDIR={target_prefix}',
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'openal-soft' },
}