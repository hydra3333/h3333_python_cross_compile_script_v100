{
	'is_dep_inheriter' : True,
	'run_post_regex' : [
	#'run_pre_depends_on' : [
		'echo "#"',
		'echo "#"',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "#"',
		'echo "#"',
		'echo "IF YOU NEED TO RE-RUN BUILDING FREETYPE/HARFBUZZ/"',
		'echo "THEN YOU *** MUST MUST MUST *** DO THESE COMMANDS FIRST:"',
		'echo "#"',
		'echo "#"',
		'echo "rm -vfR x86_64/freetype2_git"',
		'echo "rm -vf  {pkg_config_path}/freetype2.pc"',
		'echo "rm -vf  {target_prefix}/lib/libfreetype.a"',
		'echo "rm -vfR {target_prefix}/include/freetype2"',
		'echo "#"',
		'echo "rm -vfR x86_64/harfbuzz-with-freetype"',
		'echo "rm -vf  {pkg_config_path}/harfbuzz.pc"',
		'echo "rm -vf  {target_prefix}/lib/libharfbuzz.a"',
		'echo "rm -vfR {target_prefix}/include/harfbuzz"',
		'echo "#"',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "#"',
		'echo "#"',
	],
	'depends_on' : [ 'zlib', 'bzip2', 'libpng', 'freetype_lib', 'harfbuzz_lib-with-freetype', ], # 'freetype_lib-with-harfbuzz' ],
}
#rm -vfR x86_64/freetype2_git
#rm -vf  {pkg_config_path}/freetype2.pc
#rm -vf  {target_prefix}/lib/libfreetype.a
#rm -vfR {target_prefix}/include/freetype2
#rm -vfR x86_64/harfbuzz-with-freetype
#rm -vf  {pkg_config_path}/harfbuzz.pc
#rm -vf  {target_prefix}/lib/libharfbuzz.a
#rm -vfR {target_prefix}/include/harfbuzz
#
#
#rm -vfR ~/Desktop/_working/workdir/x86_64/freetype2_git
#rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libfreetype.a
#rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/freetype2.pc
#rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/freetype2
#rm -vfR ~/Desktop/_working/workdir/x86_64/harfbuzz-with-freetype
#rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libharfbuzz.a
#rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/harfbuzz.pc
#rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/harfbuzz

