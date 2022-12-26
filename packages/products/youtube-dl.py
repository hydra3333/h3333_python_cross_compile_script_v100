{ # let's see if deadsix27 can get it to build :)
	'repo_type' : 'git',
	'url' : 'https://github.com/rg3/youtube-dl.git',
	'install_options' : 'youtube-dl PREFIX="{output_prefix}/youtube-dl_git.installed"',
	'run_post_regexreplace' : [
		'sed -i.bak \'s/pandoc.*/touch youtube-dl.1/g\' Makefile', # "disables" doc, the pandoc requirement is so annoyingly big..
	],
	'run_post_install' : [
		#'if [ -f "{output_prefix}/youtube-dl_git.installed/bin/youtube-dl" ] ; then mv "{output_prefix}/youtube-dl_git.installed/bin/youtube-dl" "{output_prefix}/youtube-dl_git.installed/bin/youtube-dl.py" ; fi',
		'mv -fv "{output_prefix}/youtube-dl_git.installed/bin/youtube-dl" "{output_prefix}/youtube-dl_git.installed/bin/youtube-dl.py"',
	],
	'build_options' : 'youtube-dl',
	'patches' : [
		( 'https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/patches/youtube-dl/youtube-dl.patch', '-p1' ),
	],
	'needs_configure' : False,
	'update_check' : { 'type' : 'git', },
	'_info' : { 'version' : None, 'fancy_name' : 'youtube-dl' },
}
