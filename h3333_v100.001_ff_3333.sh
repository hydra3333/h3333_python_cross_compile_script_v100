#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

sudo apt install -y locales
sudo locale-gen en_AU.UTF-8
sudo update-locale LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'
export LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'

cd ~/Desktop
if [[ ! -d "meson_git" ]]; then
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	exit
fi
cd ~/Desktop
sudo chmod -R a=rwx *.sh
sudo chmod -R a=rwx *.py
set +x
#------------------------------------------------------------------------------------------------
set -x
# 2019.11.20 change these 3 lines per documentation 
#            https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#ubuntu-x86_64-run
#            https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#environment-setup
#            but not https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#cross-installation
#                    since there is no target win64 operating system available
#
#export PATH=/usr/local/cuda-10.2/bin:/usr/local/cuda-10.2/nsight-compute-2019.5.0${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
#------------------------------------------------------------------------------------------------

cd ~/Desktop
sudo chmod -R a=rwx *.sh
sudo chmod -R a=rwx *.py
rm -fR ./_ref
git clone https://github.com/hydra3333/h3333_python_cross_compile_script_v100.git ./_ref
sudo chmod a=rwx ./_ref
sudo chmod -R a=rwx *.sh
sudo chmod -R a=rwx *.py
sudo chmod -R a=rwx ./_ref
mkdir -pv ./_working
sudo chmod a=rwx ./_working
rsync -rvtI ./_ref/ ./_working
sudo chmod -R a=rwx ./_working/*.sh
sudo chmod -R a=rwx ./_working/*.py
sudo chmod -R a=rwx ./_working
cd ./_working
rm -fv ~/Desktop/_working/*.yaml

#git fetch origin
#git reset --hard origin/master
#ls -al
#git clean -ffdx
#git submodule foreach --recursive git clean -ffdx
#git reset --hard
#git submodule foreach --recursive git reset --hard
#git submodule update --init --recursive
#ls -al

#cd ~/Desktop
sudo chmod -R a=rwx *.sh
sudo chmod -R a=rwx *.py
#find . -iname "*.exe" -print -delete 

rm -fv ./debug-ff.log
#echo "# `date`" >>./debug-ff.log
#echo 'find . -iname "*.exe" -print -delete '>>./debug-ff.log
#find . -iname "*.exe" -print -delete 2>&1 | tee -a ./debug-ff.log

rm -vfR ~/Desktop/_working/workdir/x86_64/Vulkan-Headers_git
rm -vfR ~/Desktop/_working/workdir/x86_64/vulkan_d3dheaders
rm -vfR ~/Desktop/_working/workdir/x86_64/Vulkan-Loader_git
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/bin/libvulkan.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/bin/libvulkan.dll.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libvulkan.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libvulkan.dll.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/vulkan.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/vulkan
rm -vfR ~/Desktop/_working/workdir/x86_64/freetype*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libfreetype.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/freetype2.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/freetype2
rm -vfR ~/Desktop/_working/workdir/x86_64/harfbuzz*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libharfbuzz.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/harfbuzz.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/harfbuzz
rm -vfR ~/Desktop/_working/workdir/x86_64/gettext*
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextlib.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextlib.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextpo.a
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextpo.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/libgettextsrc.la
rm -vf  ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/lib/pkgconfig/gettext.pc
rm -vfR ~/Desktop/_working/workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/include/gettext-po.h

#cd ~/Desktop
#sudo chmod -R a=rwx *.sh
#sudo chmod -R a=rwx *.py
#./cross_compiler_v100_001.py --force --debug --products --dependencies -pl ffmpeg_min
#./cross_compiler_v100_001.py --force --debug -p x265_multibit
# only use --force if ity's already been fully built, 
# or it breaks if you use it the first time
./cross_compiler_v100_001.py list -p 2>&1 | tee -a ./debug-ff.log
./cross_compiler_v100_001.py list -d 2>&1 | tee -a ./debug-ff.log

echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
./cross_compiler_v100_001.py --force --debug -p ffmpeg_3333 2>&1 | tee -a ./debug-ff.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
#read -p "done ffmpeg press any key to continue"

echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log
echo "# `date` ###################################################################################" >>./debug-ff.log




set -x
sudo chmod -R a=rwx *.sh
sudo chmod -R a=rwx *.py
rm -fv ./exe.log
echo find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe"
echo find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll"

cd ~/Desktop
sudo chmod -R a=rwx *.sh
sudo chmod -R a=rwx *.py
rm -frv ./exe_x64_py/* 2>&1 | tee -a ./exe.log
mkdir -pv ./exe_x64_py 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git_3333.installed/bin/ffmpeg.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git_3333.installed/bin/ffprobe.exe          ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git_3333.installed/bin/ffplay.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log

ls -al ./exe_x64_py/  2>&1 | tee -a ./exe.log

ls -al ./exe_x64_py/

exit
