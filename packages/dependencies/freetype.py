{
	'is_dep_inheriter' : True,
	
	'run_pre_depends_on' : [
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "IF YOU NEED TO RE-RUN BUILDING FREETYPE/HARFBUZZ/"',
		'echo "THEN YOU *** MUST MUST MUST *** DO THESE COMMANDS FIRST:"',
		'echo "rm -vf  {pkg_config_path}/freetype2.pc"',
		'echo "rm -vf  {target_prefix}/lib/libfreetype.a"',
		'echo "rm -vfR {target_prefix}/include/freetype2"',
		'echo "rm -vf  {pkg_config_path}/harfbuzz.pc"',
		'echo "rm -vf  {target_prefix}/lib/libharfbuzz.a"',
		'echo "rm -vfR {target_prefix}/include/harfbuzz"',
		'echo "rm -vfR x86_64/freetype2_git"',
		'echo "rm -vfR x86_64/harfbuzz-with-freetype"',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
		'echo "WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING "',
	],
	'depends_on' : [ 'zlib', 'bzip2', 'libpng', 'freetype_lib', 'harfbuzz_lib-with-freetype', ], # 'freetype_lib-with-harfbuzz' ],
}
# 2019.12.13 old:
#	'freetype' : {
#		'is_dep_inheriter' : True,
#		'depends_on' : [ 'bzip2', 'freetype_lib', 'harfbuzz_lib-with-freetype', ], # 'freetype_lib-with-harfbuzz' ],
#	},