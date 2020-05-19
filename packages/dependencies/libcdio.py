{
	# 2020.05.19 git.savannah.gnu.org is giving a 502 gateway error so try fossies instead until the error resolves
	'repo_type' : 'archive', 
	'download_locations' : [
		{ "url" : "https://fossies.org/linux/privat/libcdio-2.1.0.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "8550e9589dbd594bfac93b81ecf129b1dc9d0d51e90f9696f1b2f9b2af32712b" }, ], },
	],
	#'repo_type' : 'git',
	#'url' : 'https://git.savannah.gnu.org/git/libcdio.git',
	'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-cddb --enable-cpp-progs', #  --enable-maintainer-mode
	'run_post_regexreplace' : [
		'touch doc/version.texi', # took me far to long to come up with and find this workaround
		'touch src/cd-info.1 src/cd-drive.1 src/iso-read.1 src/iso-info.1 src/cd-read.1', # .....
		#'if [ ! -f "configure" ] ; then ./autogen.sh ; fi',
		#'make -C doc stamp-vti', # idk why it needs this... odd thing: https://lists.gnu.org/archive/html/libcdio-devel/2016-03/msg00007.html
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libcdio' },
}
