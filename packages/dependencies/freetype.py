{
	'is_dep_inheriter' : True,
	'run_pre_depends_on' : [
		'rm -vf  {pkg_config_path}/freetype2.pc',
		'rm -vf  {target_prefix}/lib/libfreetype.a',
		'rm -vfR {target_prefix}/include/freetype2',
		'rm -vf  {pkg_config_path}/harfbuzz.pc',
		'rm -vf  {target_prefix}/lib/libharfbuzz.a',
		'rm -vfR {target_prefix}/include/harfbuzz',
		'rm -vfR ../freetype2_git',
		'rm -vfR ../harfbuzz-with-freetype',
	],
	'depends_on' : [ 'zlib', 'bzip2', 'libpng', 'freetype_lib', 'harfbuzz_lib-with-freetype', ], # 'freetype_lib-with-harfbuzz' ],
}
# 2019.12.13 old:
#	'freetype' : {
#		'is_dep_inheriter' : True,
#		'depends_on' : [ 'bzip2', 'freetype_lib', 'harfbuzz_lib-with-freetype', ], # 'freetype_lib-with-harfbuzz' ],
#	},