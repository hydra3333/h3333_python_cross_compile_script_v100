#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

echo "#"
echo "# Remove vulcan related files so that ffmpeg rebuilds correctly when rebuilding vulcan"
echo "# Remove vulcan related files so that ffmpeg rebuilds correctly when rebuilding vulcan"
echo "#"

set -x

sudo apt install -y locales
sudo locale-gen en_AU.UTF-8
sudo update-locale LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'
export LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'

cd ~/Desktop
rm  -fv ~/Desktop/_working/*.yaml

# freetype
rm -vfR ~/Desktop/_working/workdir/x86_64/freetype*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libfreetype.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/freetype2.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/freetype2
#harfbuzz
rm -vfR ~/Desktop/_working/workdir/x86_64/harfbuzz*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libharfbuzz.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/harfbuzz.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/harfbuzz
# vulkan
rm -vfR ~/Desktop/_working/workdir/x86_64/Vulkan-Headers_git
rm -vfR ~/Desktop/_working/workdir/x86_64/vulkan_d3dheaders
rm -vfR ~/Desktop/_working/workdir/x86_64/Vulkan-Loader_git
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/bin/libvulkan.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/bin/libvulkan.dll.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libvulkan.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libvulkan.dll.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/vulkan.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/vulkan
# gettext
rm -vfR ~/Desktop/_working/workdir/x86_64/gettext*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextlib.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextlib.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextpo.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextpo.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextsrc.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/gettext.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/gettext-po.h
# gnutls
rm -vfR ~/Desktop/_working/workdir/x86_64/gnutls*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgnutls.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgnutls.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgnutlsxx.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgnutlsxx.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/gnutls.pc
# libmysofa
rm -vfR ~/Desktop/_working/workdir/x86_64/libmysofa*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libmysofa.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/libmysofa.pc
# soxr
rm -vfR ~/Desktop/_working/workdir/x86_64/soxr*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libsoxr.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libsoxr-lsr.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/soxr.pc
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/soxr-lsr.pc
# libaom
rm -vfR ~/Desktop/_working/workdir/x86_64/libx264*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libx264.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/x264.pc
# libx264
rm -vfR ~/Desktop/_working/workdir/x86_64/libaom*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libaom.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/aom.pc
# srt
rm -vfR ~/Desktop/_working/workdir/x86_64/srt*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libsrt.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libiisrtl.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/srt.pc
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/haisrt.pc
# intel_quicksync_mfx
rm -vfR ~/Desktop/_working/workdir/x86_64/mfx*
rm -vfR  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/mfx
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libmfx.*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/libmfx.pc

