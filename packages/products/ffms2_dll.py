{
	'repo_type' : 'git',
	'url' : 'https://github.com/FFMS/ffms2', 
	'depth_git' : 0,
	'rename_folder' : 'ffms2_dll',
	'run_post_regexreplace' : [
		'rm -fv ./configure',
		'if [ ! -d "src/config" ]; then mkdir -p src/config ; fi',
		'autoreconf -fiv',
		'./configure --help=recursive',
	],
	'configure_options': '--host={target_host} --prefix={output_prefix}/ffms2_dll.installed --disable-shared --enable-static --with-zlib={target_prefix}/lib',
	'custom_ldflag' : ' {original_cflags} -L{target_prefix}/lib -lzimg ',
	'depends_on': [
		'libzimg', 'libffmpeg_extra',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git master', 'fancy_name' : 'ffms2_dll' },
}