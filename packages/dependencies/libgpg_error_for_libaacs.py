{ # 2019.12.13 # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
  # see https://forum.videolan.org/viewtopic.php?f=32&t=127218&p=432818&hilit=compile+libaacs#p432818
	#'repo_type' : 'archive',
	#'download_locations' : [ 
	#	{ 'url' : 'https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.45.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : '570f8ee4fb4bff7b7495cff920c275002aea2147e9a1d220c068213267f80a26' }, ], },
	#	# in WIn10 use powershell to find the sha256 of a file https://www.youtube.com/watch?v=YM2CE6zKvoo&t=57
	#	# in linux: sha256sum filename
	#],
	#
	'repo_type' : 'git',
	'recursive_git' : True,
	'depth_git' : 0,
	#'branch' : '745d333cf7b5b6fee62e3b26c8a2ccc004e017da',	# 2023.01.08 re-try without affix to this commit # 2022.10.16 commits after 745d333cf7b5b6fee62e3b26c8a2ccc004e017da	fail to build
	#'url' : 'git://git.gnupg.org/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
	'url' : 'https://dev.gnupg.org/source/libgpg-error.git', # https://git.gnupg.org/ # https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgpg-error.git;a=summary
	#
	'rename_folder' : 'libgpg-error_for_aacs_git',
	'custom_cflag' : ' ', # 2019.12.13 it fails to build with anything other than this, eg it crashes with -O3 and -fstack-protector-all -D_FORTIFY_SOURCE=2 
	'custom_ldflag' : ' -L{output_prefix}/libaacs_dll_git.installed/lib ',
	'run_post_regexreplace' : (
		'autoreconf -fiv', # https://dev.gnupg.org/T5696
		'./autogen.sh --force --build-w64 --prefix={output_prefix}/libaacs_dll_git.installed',
	),
	'configure_options': '--host={target_host} --prefix={output_prefix}/libaacs_dll_git.installed --disable-rpath --disable-doc --disable-tests ', #--with-libiconv-prefix={target_prefix}', # --with-libintl=no --with-libpth=no',
	'depends_on' : (
		'iconv', 
	),
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'libgpg-error for libaacs' },
}
