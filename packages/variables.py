{
	'ffmpeg_config' : # the base for all ffmpeg configurations.
		'--arch={bit_name2} '
		#'--target-os=mingw32 '
		'--target-os={target_OS} ' # 2019.12.13 to enable mingw64 for 64-bit target ... {bit_name3} won't yield "mingw32" 
		'--cross-prefix={cross_prefix_bare} '
		'--pkg-config=pkg-config '
		'--pkg-config-flags=--static '
		'--disable-shared --enable-static ' # 2019.10.31 - I ENFORCE NOTHING BUT STATIC, disable shared !
		'--disable-w32threads '
		'--enable-pthreads ' # 2019.12.13
		'--enable-cross-compile '
		'--target-exec=wine '
		'--enable-runtime-cpudetect '
		'--enable-gpl '
		'--enable-version3 '
		'--extra-version="Hydra3333/python_cross_compile_script_v100" '

		# Misc.
		'--enable-pic '
		'--enable-bzlib '
		'--enable-zlib '
		'--enable-lzma '
		'--enable-fontconfig '
		'--enable-libfontconfig '
		'--enable-libfreetype '
		'--enable-libfribidi '
		'--enable-libbluray '
		'--enable-libcdio '
		'--enable-avisynth ' # 2019.12.13 reconsider this, possibly disable it
		'--enable-vapoursynth ' #maybe works?
		'--enable-librtmp '
		'--enable-libcaca '
		'--enable-iconv '
		'--enable-libxml2 '
		'--enable-gmp '
		'--enable-gnutls ' # nongpl: openssl,libtls(libressl)
		#'--enable-avresample ' # deprecated. 2018.11.23 ... but LSW depends on it # 2019.11.19 HolyWu's lsw does not need avresample as it uses libswresample

		# Video/Picture Libs
		'--enable-libzimg '
		'--enable-libx264 '
		#'--enable-libopenh264 ' # 2019.12.13 disable libopenh264
		'--enable-libx265 '
		# '--enable-libkvazaar ' #2019.12.13 disable libkvazaar
		'--enable-libvpx '
		'--enable-libdav1d '
		#'--enable-libaom '
		'--disable-libaom ' # 2021.02.26 because libaom breaks now
		'--enable-libxvid '
		'--enable-gray '

		# Audio Libs
		'--enable-libopus '
		'--enable-libmp3lame '
		'--enable-libvorbis '
		'--enable-libtheora '
		'--enable-libspeex '
		'--enable-libsoxr '
		'--enable-librubberband '

		# Subtitle/OCR Libs:
		'--enable-libass '
		#'--enable-libtesseract ' # 2020.06.27 comment out as no longer required
		#'--enable-liblensfun ' # 2020.05.12 comment out so we do not have to build glib2

		# Image libs
		'--enable-libwebp '

		# HW Decoders
		'--enable-ffnvcodec '
		'--enable-cuvid '
		#'--enable-cuda-nvcc ' # 2019.10.31 MADE IT TO FREE # 2019.12.13 added it back in
		'--enable-cuda-llvm ' # test 2020.03.10
		'--enable-opengl '
		'--enable-d3d11va '
		'--enable-nvenc '
		'--enable-nvdec '
		'--enable-dxva2 '
		'--enable-libmfx '
		'--enable-amf '
		'--enable-opencl ' # 2019.12.13, added it, not sure why it wasn't in any of the configs ? depends on opencl_non_icd or opencl_icd
		'--enable-opengl '
		#'--enable-vulkan --enable-filter=scale_vulkan --enable-filter=avgblur_vulkan --enable-filter=chromaber_vulkan --enable-filter=overlay_vulkan '  # 2020.10.12 pith off vulcan since vulkan_loader can no longer be statically linked
		'--extra-cflags="-DFRIBIDI_LIB_STATIC" ' # 2020.06.20 per https://github.com/fribidi/fribidi/issues/146#issuecomment-646991416 # --extra-libs="-lfribidi"
		'--extra-libs="-lpsapi -lintl -liconv -lssp" ' # 2019.12.13 add  -lssp for -fstack-protector-all, #2020.10.12 moved here from ffmpeg_extra_config
	,

	'ffmpeg_nonfree': '--enable-nonfree --enable-libfdk-aac --enable-decklink', # --enable-cuda-sdk # nonfree stuff

	'ffmpeg_extra_config' :
		'--enable-libtwolame '
		'--enable-libzvbi '
		'--enable-libgsm '
		'--enable-libopencore-amrnb '
		'--enable-libopencore-amrwb '
		'--enable-libvo-amrwbenc '
		'--enable-libsnappy '
		'--enable-frei0r '
		'--enable-filter=frei0r '
		'--enable-libsrt '
		'--enable-libbs2b '
		#'--enable-libwavpack ' # 'libwavpack' deleted from ffmpeg 2020.10.04
		'--enable-libilbc '
		'--enable-libgme '
		'--enable-libflite '
		'--enable-sdl2 ' # 2020.05.13 renabled. Removed '--disable-sdl2 ' # 2020.05.13 removed SDL2 '--enable-sdl2 '
		#'--enable-libdavs2 '
		#'--enable-libxavs '
		#'--enable-libxavs2 '
		'--enable-libopenmpt '
		'--enable-libmysofa '
		'--enable-libvidstab '
		'--enable-libmodplug '
		'--disable-schannel ' # 2019.12.13 deadsix27 had this commented out, un-comment it
		#'--disable-gcrypt '
		#'--enable-ladspa ' # 2019.12.13 deadsix27 had this commented out, review it later
		# '--enable-libcodec2 ' # Requires https://github.com/traviscross/freeswitch/tree/master/libs/libcodec2, too lazy to split that off.
		# '--enable-libvmaf '
		# '--extra-libs="-lpsapi" '
		# '--extra-libs="-liconv" ' # -lschannel #-lsecurity -lz -lcrypt32 -lintl -liconv -lpng -loleaut32 -lstdc++ -lspeexdsp -lpsapi
		# '--extra-cflags="-DLIBTWOLAME_STATIC" '
		# '--extra-cflags="-DMODPLUG_STATIC" '
		'--extra-cflags="-DLIBTWOLAME_STATIC" ' # 2019.12.13 addded back in
		'--extra-cflags="-DMODPLUG_STATIC"  ' # 2019.12.13 addded back in
		'--extra-cflags="-DLIBXML_STATIC" ' # 2019.12.13 addded back in
		'--extra-cflags="-DGLIB_STATIC_COMPILATION" ' # 2019.12.13 addded back in
	,
	'ffmpeg_tiny_config' : # the base for all ffmpeg configurations.
		'--arch={bit_name2} '
		#'--target-os=mingw32 '
		'--target-os={target_OS} ' # 2019.12.13 to enable mingw64 for 64-bit target ... {bit_name3} won't yield "mingw32" 
		'--cross-prefix={cross_prefix_bare} '
		'--pkg-config=pkg-config '
		'--pkg-config-flags=--static '
		'--disable-shared --enable-static ' # 2019.10.31 - I ENFORCE NOTHING BUT STATIC, disable shared !
		'--disable-w32threads '
		'--enable-pthreads ' # 2019.12.13
		'--enable-cross-compile '
		'--target-exec=wine '
		'--enable-runtime-cpudetect '
		'--enable-gpl '
		'--enable-version3 '
		'--extra-version=Hydra3333/python_cross_compile_script_v100 '
		#
		'--enable-libxml2 '
		'--enable-libx264 '
		'--enable-libx265 '
		'--enable-libvpx '
		#'--enable-libaom '
		'--disable-libaom ' # 2021.02.26 because libaom breaks now
		'--enable-libxvid '
		'--enable-libopus '
		'--enable-libmp3lame '
		'--enable-libvorbis '
		'--enable-libtheora '
		'--enable-libsoxr '
		'--enable-librubberband '
		'--enable-libwebp '
		'--enable-ffnvcodec '
		'--enable-cuvid '
		#'--enable-cuda-nvcc ' # 2019.10.31 MADE IT TO FREE # 2019.12.13 added it back in
		'--enable-cuda-llvm ' # test 2020.03.10
		'--enable-d3d11va '
		'--enable-nvenc '
		'--enable-nvdec '
		'--enable-dxva2 '
		'--enable-opencl ' # 2019.12.13, added it, not sure why it wasn't in any of the configs ? depends on opencl_non_icd or opencl_icd
		#'--enable-vulkan --enable-filter=scale_vulkan --enable-filter=avgblur_vulkan --enable-filter=chromaber_vulkan --enable-filter=overlay_vulkan '  # 2020.10.12 pith off vulcan since vulkan_loader can no longer be statically linked
		'--enable-nonfree --enable-libfdk-aac '
		#
		'--enable-libtwolame '
		'--enable-libwavpack '
		'--extra-libs="-lpsapi -lintl -liconv -lssp" ' # 2019.12.13 add  -lssp for -fstack-protector-all
		'--extra-cflags="-DLIBTWOLAME_STATIC" ' # 2019.12.13 addded back in
		'--extra-cflags="-DLIBXML_STATIC" ' # 2019.12.13 addded back in
		'--extra-cflags="-DGLIB_STATIC_COMPILATION" ' # 2019.12.13 addded back in
	,
}