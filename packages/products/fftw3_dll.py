{
	'repo_type' : 'archive',
	'do_not_bootstrap' : True,
	'needs_configure' : False,
	'needs_make' : False,
	'needs_make_install' : False,
	'recursive_git' : False,
	'is_dep_inheriter' : True, # try without, for it to be a product and the script runs
	'depends_on' : [
		'fftw3_dll_single', 'fftw3_dll_double', 'fftw3_dll_ldouble', # 'fftw3_dll_quad' missing library 
		#                                                            # *** Warning: This system cannot link to static lib archive
		#	                                                         # (snip)/libquadmath.la.
		#	                                                         # *** I have the capability to make that library automatically link in when
		#	                                                         # *** you link to this library.  But I can only do this if you have a
		#	                                                         # *** shared version of the library, which you do not appear to have.
	],
	'_info' : { 'version' : '3.3.10', 'fancy_name' : 'fftw3 shared DLLs' },
}
