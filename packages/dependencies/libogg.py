{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/ogg.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release -DINSTALL_DOCS=OFF -DHAVE_SQLITE3=ON',
	'run_post_regexreplace' : [
		'sh ./autogen.sh',
	],
	'depends_on' : [
		'sqlite3',
	],
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'ogg' },
}
