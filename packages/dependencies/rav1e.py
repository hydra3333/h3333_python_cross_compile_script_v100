#type: ignore
{
	'repo_type' : 'git',
	'url' : 'https://github.com/xiph/rav1e',
	'depth_git': 1,
	'rename_folder' : 'rav1e_lib',
	'needs_configure' : False,
	'needs_make_install' : False,
	'build_system' : 'rust',
    #'cpu_count': '',
	#'run_post_regexreplace' : [	
	#	'rm -fv Cargo.lock',
	#	'wget "https://github.com/xiph/rav1e/releases/download/v0.6.4/Cargo.lock"',
	#],
	'build_options' : 
        'cinstall -v '
        # '--manifest-path ./dolby_vision/Cargo.toml '
        '--prefix {target_prefix} '
		'--default-toolchain=stable '
        '--library-type staticlib '
        '--crt-static '
        '--target {rust_target} '
        '--release '
		'--frozen '
		'--offline '
		'--locked '
    ,
	'env_exports' : {
		"CC": "gcc",
		"CXX": "g++",
		"PKG_CONFIG_LIBDIR": "",
		"PKG_CONFIG_PATH": "",
		"TARGET_CC": "{cross_prefix_bare}gcc",
		"TARGET_LD": "{cross_prefix_bare}ld",
		"TARGET_CXX": "{cross_prefix_bare}g++",
		"CROSS_COMPILE": "1",
	},
	'_info' : { 'version' : None, 'fancy_name' : 'rav1e_lib' },
}
# Alexpux msys2/mingw64 does it this way (relies on cargo being fully pre-installed):
#
# Maintainer: Christoph Reiter <reiter.christoph@gmail.com>
#_realname=rav1e
#pkgbase=mingw-w64-${_realname}
#pkgname="${MINGW_PACKAGE_PREFIX}-${_realname}"
#pkgver=0.5.1
#pkgrel=3
#pkgdesc='An AV1 encoder focused on speed and safety (mingw-w64)'
#arch=('any')
#mingw_arch=('mingw32' 'mingw64' 'ucrt64' 'clang64')
#url=https://github.com/xiph/rav1e/
#license=(BSD)
#depends=("${MINGW_PACKAGE_PREFIX}-gcc-libs")
#makedepends=("${MINGW_PACKAGE_PREFIX}-nasm"
#             "${MINGW_PACKAGE_PREFIX}-rust"
#             "${MINGW_PACKAGE_PREFIX}-cargo-c")
#source=("${_realname}-${pkgver}.tar.gz"::"https://github.com/xiph/rav1e/archive/v${pkgver}.tar.gz"
#         https://github.com/xiph/rav1e/releases/download/v${pkgver}/Cargo.lock)
##https://github.com/xiph/rav1e/archive/refs/tags/v0.6.4.tar.gz
##https://github.com/xiph/rav1e/releases/download/v0.6.4/Cargo.lock
#sha256sums=('7b3060e8305e47f10b79f3a3b3b6adc3a56d7a58b2cb14e86951cc28e1b089fd'
#            '6baeb4e72ee86dd4c3d6c9acfcfac6a2e58a580101eb181daced09199a136868')
#
#prepare() {
#  cp Cargo.lock "${_realname}-${pkgver}"
#  cd "${srcdir}/${_realname}-${pkgver}"
#
#  cargo fetch \
#    --locked
#}

#build() {
#  cd "${srcdir}/${_realname}-${pkgver}"
#
#  cargo build \
#    --release \
#    --frozen \
#    --offline
#  MSYS2_ARG_CONV_EXCL="--prefix=" \
#    cargo capi build \
#      --release \
#      --frozen \
#      --library-type=cdylib \
#      --prefix="${MINGW_PREFIX}"
#}
#
#check() {
#  cd "${srcdir}/${_realname}-${pkgver}"#
#  cargo test \
#    --release \
#    --frozen
#}
#
#package() {
#  cd "${srcdir}/${_realname}-${pkgver}"
#  cargo install \
#    --frozen \
#    --offline \
#    --no-track \
#    --path . \
#    --root "${pkgdir}${MINGW_PREFIX}"
#  MSYS2_ARG_CONV_EXCL="--prefix=" \
#    cargo capi install \
#      --release \
#      --frozen \
#      --library-type=cdylib \
#      --prefix="${MINGW_PREFIX}" \
#      --destdir="${pkgdir}"
#
#  # Workaround for import lib
#  mv ${pkgdir}${MINGW_PREFIX}/lib/{,lib}rav1e.dll.a
#  rm -f ${pkgdir}${MINGW_PREFIX}/lib/*.def
#  install -Dm644 LICENSE PATENTS -t "${pkgdir}${MINGW_PREFIX}/share/licenses/${_realname}/"
#}
