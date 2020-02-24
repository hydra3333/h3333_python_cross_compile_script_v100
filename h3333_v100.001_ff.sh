#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x
cd ~/Desktop
if [[ ! -d "meson_git" ]]; then
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	echo "Nothing doing. Run sudo ./h3333_v100_setup.sh first !!!"
	exit
fi
cd ~/Desktop
sudo chmod a=rwx -R *.sh
set +x
#------------------------------------------------------------------------------------------------
set -x
# 2019.11.20 change these 3 lines per documentation 
#            https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#ubuntu-x86_64-run
#            https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#environment-setup
#            but not https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#cross-installation
#                    since there is no target win64 operating system available
export PATH=/usr/local/cuda-10.2/bin:/usr/local/cuda-10.2/nsight-compute-2019.5.0${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
#------------------------------------------------------------------------------------------------

cd ~/Desktop
sudo chmod a=rwx -R *.sh
rm -fR "./_ref"
git clone https://github.com/hydra3333/h3333_python_cross_compile_script_v100.git "./_ref"
sudo chmod a=rwx -R *.sh
mkdir -pv "./_working"
rsync -rvtI "./_ref/" "./_working"
sudo chmod a=rwx -R *.sh
cd "./_working"
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
sudo chmod a=rwx -R *.sh
#find . -iname "*.exe" -print -delete 

rm -fv ./debug-ff.log
#echo "# `date`" >>./debug-ff.log
#echo 'find . -iname "*.exe" -print -delete '>>./debug-ff.log
#find . -iname "*.exe" -print -delete 2>&1 | tee -a ./debug-ff.log

#cd ~/Desktop
#sudo chmod a=rwx -R *.sh
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
./cross_compiler_v100_001.py --force --debug -p ffmpeg 2>&1 | tee -a ./debug-ff.log
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
sudo chmod a=rwx -R *.sh
rm -fv ./exe.log
echo find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe"
echo find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll"

cd ~/Desktop
sudo chmod a=rwx -R *.sh
rm -frv ./exe_x64_py/* 2>&1 | tee -a ./exe.log
mkdir -pv exe_x64_py 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git.installed/bin/ffmpeg.exe            ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git.installed/bin/ffprobe.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git.installed/bin/ffplay.exe            ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvextract.exe    ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvinfo.exe       ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvmerge.exe      ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvpropedit.exe   ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/x265_hg.installed/bin/x265.exe                ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/x264_git.installed/bin/x264.exe               ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/mp4box_git.installed/bin/MP4Box.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/dav1d.installed/bin/dav1d.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/aom_git.installed/bin/aomdec.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/aom_git.installed/bin/aomenc.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/sox_git.installed/bin/sox.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/vpx_git.installed/bin/vpxdec.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/vpx_git.installed/bin/vpxenc.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/lame-3.100.installed/bin/lame.exe             ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/mediainfo_git.installed/bin/mediainfo.exe     ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/webp.installed/bin/webpinfo.exe               ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/webp.installed/bin/cwebp.exe                  ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/webp.installed/bin/dwebp.exe                  ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/fftw3_dll/bin/libfftw3l-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/fftw3_dll/bin/libfftw3f-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/fftw3_dll/bin/libfftw3-3.dll                  ./exe_x64_py/ 2>&1 | tee -a ./exe.log

exit
