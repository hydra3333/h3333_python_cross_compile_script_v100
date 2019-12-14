{
	'repo_type' : 'git',
	'url' : 'https://github.com/pkuvcl/davs2.git',
	'source_subfolder' : 'build/linux',
	'configure_options' : '{autoconf_prefix_options} --cross-prefix={cross_prefix_bare} --enable-static --disable-shared --disable-cli --disable-win32thread --enable-strip --enable-opencl', # 2019.12.13 try to add opencl
	'install_target' : 'install-lib-static',
    'depends_on' : [ 'opencl_icd' ], # 2019.12.13
	'_info' : { 'version' : None, 'fancy_name' : 'davs2' },
}