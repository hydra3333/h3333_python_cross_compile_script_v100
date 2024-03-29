#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

sudo apt -y update
#sudo apt -y full-upgrade
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager certifi # install latest certificatess for python requests.get

sudo pip3 install --upgrade pip-review
sudo pip3 check
sudo pip-review
#sudo pip-review --auto --continue-on-fail

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

rm -frv /home/u/Desktop/_working/workdir/win64_output

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

#rm -fv ./debug.log
#echo "# `date`" >>./debug.log
#echo 'find . -iname "*.exe" -print -delete '>>./debug.log
#find . -iname "*.exe" -print -delete 2>&1 | tee -a ./debug.log

#cd ~/Desktop
#sudo chmod a=rwx -R *.sh
#./cross_compiler_v100_003.py --force --debug --products --dependencies -pl ffmpeg_static_non_free_opencl,x265_multibit
#./cross_compiler_v100_003.py --force --debug -p x265_multibit
# only use --force if ity's already been fully built, 
# or it breaks if you use it the first time
./cross_compiler_v100_003.py list -p 2>&1 | tee -a ./debug.log
./cross_compiler_v100_003.py list -d 2>&1 | tee -a ./debug.log

./Remove_ffmpeg_3333_related_files.sh
rm -fv ./ffmpeg.log
# ensure forced rebuild of libplacebo and all its dependencies including shaderc, glslang, spirv
./cross_compiler_v100_003.py --allforce --debug -d libplacebo 2>&1 | tee -a ./ffmpeg.log
./cross_compiler_v100_003.py --force --debug -p ffmpeg 2>&1 | tee -a ./ffmpeg.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done ffmpeg_static_non_free_opencl press any key to continue"

rm -fv ./x264.log
./cross_compiler_v100_003.py --force --debug -p x264 2>&1 | tee -a ./x264.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done x264 press any key to continue"
#
#
rm -fv ./x265.log
./cross_compiler_v100_003.py --force --debug -p x265 2>&1 | tee -a ./x265.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done x265 press any key to continue"


rm -fv ./mp4box.log
./cross_compiler_v100_003.py --force --debug -p mp4box 2>&1 | tee -a ./mp4box.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done mp4box press any key to continue"


rm -fv ./lame.log
./cross_compiler_v100_003.py --force --debug -p lame 2>&1 | tee -a ./lame.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done lame press any key to continue"


rm -fv ./aom.log
./cross_compiler_v100_003.py --force --debug -p aom 2>&1 | tee -a ./aom.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done aom press any key to continue"


rm -fv ./sox.log
./cross_compiler_v100_003.py --force --debug -p sox 2>&1 | tee -a ./sox.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done sox press any key to continue"


rm -fv ./vpx.log
./cross_compiler_v100_003.py --force --debug -p vpx 2>&1 | tee -a ./vpx.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done vpx press any key to continue"


rm -fv ./webp.log
./cross_compiler_v100_003.py --force --debug -d libwebp 2>&1 | tee -a ./webp.log
./cross_compiler_v100_003.py --force --debug -p webp 2>&1 | tee -a ./webp.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done webp press any key to continue"


rm -fv ./mediainfo.log
./cross_compiler_v100_003.py --force --debug -p mediainfo 2>&1 | tee -a ./mediainfo.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done mediainfo press any key to continue"


rm -fv ./dav1d.log
./cross_compiler_v100_003.py --force --debug -p dav1d 2>&1 | tee -a ./dav1d.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done dav1d press any key to continue"

rm -fv ./fftw3_dll.log
./cross_compiler_v100_003.py --force --debug -d fftw3_dll_single 2>&1 | tee -a ./fftw3_dll.log
./cross_compiler_v100_003.py --force --debug -d fftw3_dll_double 2>&1 | tee -a ./fftw3_dll.log
./cross_compiler_v100_003.py --force --debug -d fftw3_dll_ldouble 2>&1 | tee -a ./fftw3_dll.log
#./cross_compiler_v100_003.py --force --debug -p fftw3_dll_quad 2>&1 | tee -a ./fftw3_dll.log
./cross_compiler_v100_003.py --force --debug -p fftw3_dll 2>&1 | tee -a ./fftw3_dll.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done fftw3_dll press any key to continue"

# mpv after ffmpeg when everything is built to fullest extent
rm -fv ./mpv.log
#./cross_compiler_v100_003.py --force --debug -p mpv 2>&1 | tee -a ./mpv.log
./cross_compiler_v100_003.py --allforce --debug -p mpv 2>&1 | tee -a ./mpv.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done mpv press any key to continue"

rm -fv ./libaacs_dll.log
#./cross_compiler_v100_003.py --force --debug -p libaacs_dll 2>&1 | tee -a ./libaacs_dll.log
./cross_compiler_v100_003.py --allforce --debug -p libaacs_dll 2>&1 | tee -a ./libaacs_dll.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done libaacs_dll press any key to continue"

#rm -fv ./mkvtoolnix.log
#./cross_compiler_v100_003.py --force --debug -p mkvtoolnix 2>&1 | tee -a ./mkvtoolnix.log
#exit_status=$?
#echo "exit_status='$exit_status'"
#if [ $exit_status -ne 0 ]; then
#    echo "Error $exit_status detected"
#	exit $exit_status
#fi
sleep 5s
#read -p "done mkvtoolnix press any key to continue"


#rm -fv ./youtube-dl.log
#./cross_compiler_v100_003.py --force --debug -p youtube-dl 2>&1 | tee -a ./youtube-dl.log
#exit_status=$?
#echo "exit_status='$exit_status'"
#if [ $exit_status -ne 0 ]; then
#    echo "Error $exit_status detected"
#	exit $exit_status
#fi
sleep 5s
#read -p "done youtube-dl press any key to continue"

./Remove_ffmpeg_3333_related_files.sh
rm -fv ./ffmpeg_3333.log
#./cross_compiler_v100_003.py --force --debug -p ffmpeg_3333 2>&1 | tee -a ./ffmpeg_3333.log
./cross_compiler_v100_003.py --allforce --debug -p ffmpeg_3333 2>&1 | tee -a ./ffmpeg_3333.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
sleep 5s
#read -p "done ffmpeg_3333 press any key to continue"


set -x
sudo chmod a=rwx -R *.sh
rm -fv ./exe.log
echo find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe"
echo find /home/u/Desktop/_working -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working -iname "*.dll"

cd ~/Desktop
echo "start of tail -n 20 ~/Desktop/_working/ffmpeg.log"
tail -n 20 ~/Desktop/_working/ffmpeg.log
echo "end of tail -n 20 ~/Desktop/_working/ffmpeg.log"
echo "start of tail -n 20 ~/Desktop/_working/x264.log"
tail -n 20 ~/Desktop/_working/x264.log
echo "end of tail -n 20 ~/Desktop/_working/x264.log"
echo "start of tail -n 20 ~/Desktop/_working/x265.log"
tail -n 20 ~/Desktop/_working/x265.log
echo "end of tail -n 20 ~/Desktop/_working/x265.log"
echo "start of tail -n 20 ~/Desktop/_working/mp4box.log"
tail -n 20 ~/Desktop/_working/mp4box.log
echo "end of tail -n 20 ~/Desktop/_working/mp4box.log"
echo "start of tail -n 20 ~/Desktop/_working/mediainfo.log"
tail -n 20 ~/Desktop/_working/mediainfo.log
echo "end of tail -n 20 ~/Desktop/_working/mediainfo.log"
echo "start of tail -n 20 ~/Desktop/_working/ffmpeg_3333.log"
tail -n 20 ~/Desktop/_working/ffmpeg_3333.log
echo "end of tail -n 20 ~/Desktop/_working/ffmpeg_3333.log"

cd ~/Desktop
sudo chmod a=rwx -R *.sh
#rm -frv ./exe_x64_py/* 2>&1 | tee -a ./exe.log
mkdir -pv ./exe_x64_py 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git.installed/bin/ffmpeg.exe           ./exe_x64_py/ffmpeg_OpenCL.exe 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git.installed/bin/ffprobe.exe          ./exe_x64_py/ffprobe_OpenCL.exe 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git.installed/bin/ffplay.exe           ./exe_x64_py/ffplay_OpenCL.exe 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git_3333.installed/bin/ffmpeg.exe      ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git_3333.installed/bin/ffprobe.exe     ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/ffmpeg_git_3333.installed/bin/ffplay.exe      ./exe_x64_py/ 2>&1 | tee -a ./exe.log

#cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvextract.exe   ./exe_x64_py/ 2>&1 | tee -a ./exe.log
#cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvinfo.exe      ./exe_x64_py/ 2>&1 | tee -a ./exe.log
#cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvmerge.exe     ./exe_x64_py/ 2>&1 | tee -a ./exe.log
#cp -fv /home/u/Desktop/_working/workdir/win64_output/mkvtoolnix_git.installed/bin/mkvpropedit.exe  ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/x265.installed/bin/x265.exe                   ./exe_x64_py/ 2>&1 | tee -a ./exe.log
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
cp -fv /home/u/Desktop/_working/workdir/win64_output/mpv_git.installed/bin/mpv.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/fftw3_dll/bin/libfftw3l-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/fftw3_dll/bin/libfftw3f-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/fftw3_dll/bin/libfftw3-3.dll                  ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/workdir/win64_output/libaacs_dll_git.installed/bin/libaacs-0.dll      ./exe_x64_py/libaacs.dll 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/libaacs_dll_git.installed/bin/libgcrypt-20.dll   ./exe_x64_py/libgcrypt.dll 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/libaacs_dll_git.installed/bin/libgcrypt-20.dll   ./exe_x64_py/libgcrypt-20.dll 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/workdir/win64_output/libaacs_dll_git.installed/bin/libgpg-error-0.dll ./exe_x64_py/libgpg-error.dll 2>&1 | tee -a ./exe.log

ls -al ./exe_x64_py/  2>&1 | tee -a ./exe.log

ls -al ./exe_x64_py/

exit
