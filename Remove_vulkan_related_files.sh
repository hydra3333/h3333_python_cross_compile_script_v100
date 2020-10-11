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

rm -vfR ~/Desktop/_working/workdir/x86_64/Vulkan-Headers_git
rm -vfR ~/Desktop/_working/workdir/x86_64/vulkan_d3dheaders
rm -vfR ~/Desktop/_working/workdir/x86_64/Vulkan-Loader_git

rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/bin/libvulcan.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libvulcan.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libvulkan.dll.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/vulcan.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/vulcan



