{
	'repo_type' : 'git',
	'url' : 'https://github.com/libarchive/libarchive.git',
	'conf_system' : 'cmake',
	'source_subfolder' : '_build',
	'configure_options' : '.. {cmake_prefix_options} -DCMAKE_INSTALL_PREFIX={target_prefix} -DBUILD_SHARED_LIBS=0 -DCMAKE_BUILD_TYPE=Release '
		'-DENABLE_NETTLE=ON '
		'-DENABLE_OPENSSL=OFF '
		'-DENABLE_LIBB2=ON '
		'-DENABLE_LZ4=ON '
		'-DENABLE_LZO=ON '
		'-DENABLE_LZMA=ON '
		'-DENABLE_ZSTD=ON '
		'-DENABLE_ZLIB=ON '
		'-DZLIB_WINAPI_EXITCODE=0 '
		'-DZLIB_WINAPI_EXITCODE__TRYRUN_OUTPUT="" '
		'-DENABLE_BZip2=ON '
		'-DENABLE_LIBXML2=ON '
		'-DENABLE_EXPAT=ON '
		'-DENABLE_PCREPOSIX=ON '
		'-DENABLE_LibGCC=ON '
		'-DENABLE_CNG=ON '
		'-DENABLE_TAR=ON '
		'-DENABLE_TAR_SHARED=OFF '
		'-DENABLE_CPIO=ON '
		'-DENABLE_CPIO_SHARED=OFF '
		'-DENABLE_CAT=ON '
		'-DENABLE_CAT_SHARED=OFF '
		'-DENABLE_XATTR=ON '
		'-DENABLE_ACL=ON '
		'-DENABLE_ICONV=ON '
		'-DENABLE_TEST=OFF '
		'-DENABLE_COVERAGE=OFF '
		'-DENABLE_INSTALL=ON '
		'-DLIBXML2_LIBRARIES="-lxml2 -lz -llzma -liconv -lws2_32"'
	,
	'depends_on' : [
		'iconv', 'bzip2', 'expat', 'zlib', 'xz', 'lzo', 'bzip2', 'libnettle', 'libxml2', 'expat', 'pcre', 'pcre2', 'libcrypt',
	],
	'patches': [
		('libarchive/0001-libarchive-mingw-workaround.patch', '-p1', '..')
	],
	'regex_replace': {
		'post_install': [
			{
				0: r'^Libs: -L\${{libdir}} -larchive([^\n]+)?',
				1: r'Libs: -L${{libdir}} -larchive -lnettle -lxml2 -llzma -lbcrypt -lbz2 -lz -liconv -lcharset -llzo2 -lws2_32\1',
				'in_file': '{pkg_config_path}/libarchive.pc'
			},
			{
				0: r'Libs.private:  [^\n]+',
				1: r'Libs.private: -lnettle -lxml2 -llzma -lbcrypt -lbz2 -lz -liconv -lcharset -llzo2 -lws2_32',
				'in_file': '{pkg_config_path}/libarchive.pc'
			}
		]
	},
	'_info' : { 'version' : None, 'fancy_name' : 'libarchive' },
}
# 2019.12.13 old:
#	'libarchive': {
#		'repo_type' : 'git',
#		'url' : 'https://github.com/libarchive/libarchive.git',
#		'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static --disable-bsdtar --disable-bsdcat --disable-bsdcpio --without-openssl', #--without-xml2 --without-nettle
#		'depends_on' : [
#			'bzip2', 'expat', 'zlib', 'xz', 'lzo'
#		],
#		'run_post_install' : [
#			'sed -i.bak \'s/Libs: -L${{libdir}} -larchive/Libs: -L${{libdir}} -larchive -llzma -lbcrypt -lz/\' "{pkg_config_path}/libarchive.pc"', # libarchive complaints without this.
#		],
#		'_info' : { 'version' : 'git (master)', 'fancy_name' : 'libarchive' },
#	},
#
#OPTION(ENABLE_NETTLE "Enable use of Nettle" ON)
#OPTION(ENABLE_OPENSSL "Enable use of OpenSSL" ON)
#OPTION(ENABLE_LIBB2 "Enable the use of the system LIBB2 library if found" ON)
#OPTION(ENABLE_LZ4 "Enable the use of the system LZ4 library if found" ON)
#OPTION(ENABLE_LZO "Enable the use of the system LZO library if found" OFF)
#OPTION(ENABLE_LZMA "Enable the use of the system LZMA library if found" ON)
#OPTION(ENABLE_ZSTD "Enable the use of the system zstd library if found" ON)
#OPTION(ENABLE_ZLIB "Enable the use of the system ZLIB library if found" ON)
#OPTION(ENABLE_BZip2 "Enable the use of the system BZip2 library if found" ON)
#OPTION(ENABLE_LIBXML2 "Enable the use of the system libxml2 library if found" ON)
#OPTION(ENABLE_EXPAT "Enable the use of the system EXPAT library if found" ON)
#OPTION(ENABLE_PCREPOSIX "Enable the use of the system PCREPOSIX library if found" ON)
#OPTION(ENABLE_LibGCC "Enable the use of the system LibGCC library if found" ON)
## CNG is used for encrypt/decrypt Zip archives on Windows.
#OPTION(ENABLE_CNG "Enable the use of CNG(Crypto Next Generation)" ON)
#OPTION(ENABLE_TAR "Enable tar building" ON)
#OPTION(ENABLE_TAR_SHARED "Enable dynamic build of tar" FALSE)
#OPTION(ENABLE_CPIO "Enable cpio building" ON)
#OPTION(ENABLE_CPIO_SHARED "Enable dynamic build of cpio" FALSE)
#OPTION(ENABLE_CAT "Enable cat building" ON)
#OPTION(ENABLE_CAT_SHARED "Enable dynamic build of cat" FALSE)
#OPTION(ENABLE_XATTR "Enable extended attribute support" ON)
#OPTION(ENABLE_ACL "Enable ACL support" ON)
#OPTION(ENABLE_ICONV "Enable iconv support" ON)
#OPTION(ENABLE_TEST "Enable unit and regression tests" ON)
#OPTION(ENABLE_COVERAGE "Enable code coverage (GCC only, automatically sets ENABLE_TEST to ON)" FALSE)
#OPTION(ENABLE_INSTALL "Enable installing of libraries" ON)
