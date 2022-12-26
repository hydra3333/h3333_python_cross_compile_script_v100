{
	'repo_type' : 'git',
	'url' : 'https://github.com/yt-dlp/yt-dlp',
	'install_options' : 'yt-dlp DESTDIR="{output_prefix}/yt-dlp_git.installed"',
	#'run_post_install' : [
	#	'mv -fv "{output_prefix}/yt-dlp_git.installed/bin/yt-dlp" "{output_prefix}/yt-dlp_git.installed/bin/yt-dlp.py"',
	#],
	'run_post_build' : [
		'mkdir -pv "{output_prefix}/yt-dlp_git.installed/bin"',
		'cp -fv yt-dlp "{output_prefix}/yt-dlp_git.installed/bin/"',
		'cp -fv yt-dlp "{output_prefix}/yt-dlp_git.installed/bin/yt-dlp.py"',
	],
	'build_options' : 'yt-dlp',
	'needs_configure' : False,
	#'needs_make_install' : False,
	'_info' : { 'version' : 'git (master)', 'fancy_name' : 'yt-dlp' },
}
