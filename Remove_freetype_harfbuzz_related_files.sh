#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

echo "#"
echo "# Remove freetype/harfbuzz related files so that ffmpeg rebuilds correctly when rebuilding freetype/harfbuzz"
echo "# Remove freetype/harfbuzz related files so that ffmpeg rebuilds correctly when rebuilding freetype/harfbuzz"
echo "#"

set -x

sudo apt install -y locales
sudo locale-gen en_AU.UTF-8
sudo update-locale LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'
export LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'

cd ~/Desktop
rm -fv  ~/Desktop/_working/*.yaml

rm -vfR ~/Desktop/_working/workdir/x86_64/freetype2_git
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libfreetype.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/freetype2.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/freetype2

rm -vfR ~/Desktop/_working/workdir/x86_64/harfbuzz-with-freetype
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libharfbuzz.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/harfbuzz.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/harfbuzz
