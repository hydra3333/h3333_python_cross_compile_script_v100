{
	'repo_type' : 'archive',
	'do_not_bootstrap' : True,
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	'recursive_git' : False,
	'is_dep_inheriter' : True, # try without, for it to be a product and the script runs
	'depends_on' : [
		'fftw3_dll_single', 'fftw3_dll_double', 'fftw3_dll_ldouble', 'fftw3_dll_quad', 
	],
	'_info' : { 'version' : '3.3.8', 'fancy_name' : 'fftw3 shared DLLs' },
}
# 2019.12.13 old:
#	'fftw3_dll' : { # create the FFTW DLLs which we can use with things like avisynth etc
#		'is_dep_inheriter' : True,
#		'depends_on' : [
#			'fftw3_dll_single', 'fftw3_dll_double', 'fftw3_dll_ldouble', #'fftw3_dll_quad', 
#		],
#	},