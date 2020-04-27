#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x
sudo apt update -y
sudo apt upgrade -y

sudo apt-get remove -y python-pip cython # python 
sudo apt autoremove -y
sudo apt install -y python3 python3-pip python3-distutils python3-dev python3-numpy
sudo apt install -y cython3

sudo pip  install progressbar2
sudo pip3 install progressbar2
sudo pip3 install py2exe
sudo pip3 install certifi # install latest certificatess for python requests.get

pip  install progressbar2
pip3 install progressbar2
pip3 install py2exe
pip3 install certifi # install latest certificatess for python requests.get


sudo apt install -y hashalot
sudo apt install -y git git-email
git config --global user.name "hydra3333"
git config --global user.email "hydra3333@gmail.com"
git config --global sendemail.smtpencryption tls
#git config --global sendemail.smtpencryption ssl
git config --global sendemail.smtpserver smtp.gmail.com
# 587 for TLS 465 for SSL
#git config --global sendemail.smtpserverport 465
git config --global sendemail.smtpserverport 587
git config --global sendemail.smtpuser hydra3333@gmail.com
#git config --global sendemail.smtppass ?????
git config --unset sendemail.smtppass
git config --global --unset sendemail.smtppass
#git config --global sendemail.smtpDomain 
git config --global sendemail.to hydra3333@gmail.com
git config --global --list
git config --global credential.helper store
# usage:
#git clone git://git.ffmpeg.org/ffmpeg.git
#cd ffmpeg
#patch -p1 < ../"ffmpeg_ncenc_messages_patch_20191027.patch"
#git add *
#git commit --message="Slightly update nvenc error messages and warnings"
#git send-email -1 --cover-letter --annotate --smtp-debug=1 --to=ffmpeg-devel@ffmpeg.org --subject="Slightly update nvenc error messages and warnings"

sudo apt install -y texinfo yasm make automake gcc gcc-c++ pax cvs svn flex bison patch libtoolize hg cmake gettext-autopoint
sudo apt install -y libxslt rake
sudo apt install -y gperf gyp p7zip docbook-to-man docbook2x pando p7zip

sudo apt install -y build-essential autoconf libtool-bin libtool gettext autopoint gyp gperf autogen bzip2 pandoc 
sudo apt install -y subversion curl texinfo g++ bison flex cvs yasm automake ed gcc cmake git make pkg-config mercurial unzip pax wget ant
sudo apt install -y git-remote-hg libxslt1.1 libxml2 rake docbook-utils docbook-style-xsl docbook-xsl docbook-to-man docbook2x p7zip p7zip-full
sudo apt install -y xsltproc itstool autoconf-archive
#sudo apt-get remove -y nasm
sudo apt-get remove -y doxygen
# gendef is installed with mingw
sudo apt install -y libmozjs-dev libxmu-dev libgconf2-dev libdbus-1-dev network-manager-dev xserver-xorg-dev # for libproxy
sudo apt install -y zlib1g-dev #warning: you may need to install zlib development headers first if you want to build mp4-box on ubuntu
sudo apt install -y p7zip-full
sudo apt install -y autoconf-archive
sudo apt install -y docbook2x docbook-xsl
sudo apt install -y dbtoepub docbook-xsl-doc-html docbook-xsl-doc-pdf docbook-xsl-doc-text docbook-xsl-saxon fop libsaxon-java libxalan2-java libxslthl-java xalan

sudo apt install -y python3 python3-pip
sudo apt install -y ninja-build
#sudo apt install -y meson
#pip3 install -y --user meson

cd ~/Desktop
#git clone https://github.com/mesonbuild/meson.git
git clone --depth 1 --branch "0.51.2" https://github.com/mesonbuild/meson.git "meson_git"
cd meson_git
sudo python3 setup.py clean 
sudo python3 setup.py build
sudo python3 setup.py install 
sudo python3 setup.py check
#sudo python3 setup.py test
cd ~/Desktop

#------------------------------------------------------------------------------------------------
# 2020.05.26 x264 has a new dependency on nasm 2.14 or greater ... 
# before we do anything, build NASM if need be
set -x
if [[ ! -d "nasm-2.14.02" ]]; then
   echo "Downloading nasm 2.14.02"
   url="https://www.nasm.us/pub/nasm/releasebuilds/2.14.02/nasm-2.14.02.tar.xz"
   rm -f "nasm-2.14.02.tar.xz"
   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "$url" --retry 50 -L --output "nasm-2.14.02.tar.xz" --fail # -L means "allow redirection" or some odd :|
   tar -xf "nasm-2.14.02.tar.xz" || unzip "nasm-2.14.02.tar.xz"
   echo "Configuring nasm 2.14.02"
   cd nasm-2.14.02
      ./autogen.sh || exit 1
      ./configure --prefix=/usr --exec_prefix=/usr --enable-sections --enable-lto  || exit 1
      echo "Make nasm 2.14"
      make  || exit 1
      echo "Installing nasm 2.14"
      sudo make install  || exit 1 # sudo so it copies into /usr folder tree
   cd ..
   echo "Done Building and Installing nasm 2.14.02"
fi
set +x
#read -p "After nasm build, press Enter to continue"
#------------------------------------------------------------------------------------------------
set -x

#------------------------------------------------------------------------------------------------
#CUDA SDK Toolkit 10.2 Install Commentary https://github.com/DeadSix27/python_cross_compile_script/issues/83#issuecomment-468670437
#CUDA SDK Toolkit 10.2 Download and Install Guideline https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
#CUDA SDK Toolkit 10.2 Local Runtime Download page for ubuntu
#------------------------------------------------------------
#Source Page
#https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=runfilelocal
#eg for ubuntu 18.04 points to 
#https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run
#eg for ubuntu 18.10 points to 
#https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run
#eg for ubuntu 18.10 points to 
#http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_440.33.01_linux.run
#
#CUDA SDK Toolkit 10.2 Local Runtime Installation
#------------------------------------------------
#Install the TOOLKIT and SAMPLES like: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile
#
#sudo sh ./cuda_10.2.89_440.33.01_linux.run --silent --toolkit --samples 
#
#CUDA SDK Toolkit 10.2 - SETUP PATHS READY FOR CROSS-COMPILING
#-------------------------------------------------------------
#The PATH variable needs to include CUDS sdk stuff
#Hence for CUDA SDK Toolkit 10.2 64bit :-
# 2019.11.20 change these 3 lines per documentation 
#            https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#ubuntu-x86_64-run
#            https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#environment-setup
#            but not https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#cross-installation
#                    since there is no target win64 operating system available
#export PATH=/usr/local/cuda-10.2/bin:/usr/local/cuda-10.2/nsight-compute-2019.5.0${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
#CUDA SDK Toolkit 10.2 - UNINSTALL NOTES
#---------------------------------------
#To uninstall the CUDA Toolkit, run the uninstallation script provided in the bin directory of the toolkit. 
#By default, it is located in /usr/local/cuda-10.2/bin:#
#
#sudo /usr/local/cuda-10.2/bin/cuda-uninstaller
#
#set -x
#cd ~/Desktop
# https://developer.nvidia.com/cuda-downloads
# 64bit ubuntu local runfile
##cuda_install_file=cuda_10.1.105_418.39_linux.run
##cuda_install_file=cuda_10.1.168_418.67_linux.run
##cuda_install_file=cuda_10.1.243_418.87.00_linux.run
#cuda_install_file=cuda_10.2.89_440.33.01_linux.run
#if [[ ! -f "$cuda_install_file" ]]; then
#   echo "Downloading $cuda_install_file"
#   url="http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/$cuda_install_file"
#   rm -f "$cuda_install_file"
#   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "$url" --retry 50 -L --output "$cuda_install_file" --fail # -L means "allow redirection" or some odd :|
#      echo "Installing $cuda_install_file"
#      sudo sh ./$cuda_install_file --silent --toolkit --samples
#   cd ..
#   echo "Done Building and Installing $cuda_install_file"
#fi
#set +x
#read -p "After installing $cuda_install_file, press Enter to continue"
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
sudo chmod 777 -R *
rm -fR "./_ref"
git clone https://github.com/hydra3333/h3333_python_cross_compile_script_v100.git "./_ref"
sudo chmod 777 -R *
mkdir -pv "./_working"
rsync -rvtI "./_ref/" "./_working"
sudo chmod 777 -R *
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
sudo chmod 777 -R *
#find . -iname "*.exe" -print -delete 

#rm -fv ./debug.log
#echo "# `date`" >>./debug.log
#echo 'find . -iname "*.exe" -print -delete '>>./debug.log
#find . -iname "*.exe" -print -delete 2>&1 | tee -a ./debug.log

#cd ~/Desktop
#sudo chmod 777 -R *
#./cross_compiler_v100_001.py --force --debug --products --dependencies -pl ffmpeg_static_non_free_opencl,x265_multibit
#./cross_compiler_v100_001.py --force --debug -p x265_multibit
# only use --force if ity's already been fully built, 
# or it breaks if you use it the first time
#./cross_compiler_v100_001.py list -p 2>&1 | tee -a ./debug.log
#./cross_compiler_v100_001.py list -d 2>&1 | tee -a ./debug.log


rm -fv ./ffmpeg.log
./cross_compiler_v100_001.py --force --debug -p ffmpeg 2>&1 | tee -a ./ffmpeg.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done ffmpeg_static_non_free_opencl press any key to continue"


rm -fv ./x264.log
./cross_compiler_v100_001.py --force --debug -p x264 2>&1 | tee -a ./x264.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done x264 press any key to continue"


rm -fv ./x265.log
./cross_compiler_v100_001.py --force --debug -p x265 2>&1 | tee -a ./x265.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done x265 press any key to continue"


rm -fv ./mp4box.log
./cross_compiler_v100_001.py --force --debug -p mp4box 2>&1 | tee -a ./mp4box.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done mp4box press any key to continue"


rm -fv ./lame.log
./cross_compiler_v100_001.py --force --debug -p lame 2>&1 | tee -a ./lame.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done lame press any key to continue"


rm -fv ./aom.log
./cross_compiler_v100_001.py --force --debug -p aom 2>&1 | tee -a ./aom.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done aom press any key to continue"


rm -fv ./sox.log
./cross_compiler_v100_001.py --force --debug -p sox 2>&1 | tee -a ./sox.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done sox press any key to continue"


rm -fv ./vpx.log
./cross_compiler_v100_001.py --force --debug -p vpx 2>&1 | tee -a ./vpx.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done vpx press any key to continue"


#rm -fv ./webp.log
##./cross_compiler_v100_001.py --force --debug -d libwebp 2>&1 | tee -a ./webp.log
#./cross_compiler_v100_001.py --force --debug -p webp 2>&1 | tee -a ./webp.log
#exit_status=$?
#echo "exit_status='$exit_status'"
#if [ $exit_status -ne 0 ]; then
#    echo "Error $exit_status detected"
#	exit $exit_status
#fi
##read -p "done webp press any key to continue"


rm -fv ./mediainfo.log
./cross_compiler_v100_001.py --force --debug -p mediainfo 2>&1 | tee -a ./mediainfo.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done mediainfo press any key to continue"


rm -fv ./dav1d.log
./cross_compiler_v100_001.py --force --debug -p dav1d 2>&1 | tee -a ./dav1d.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done dav1d press any key to continue"


rm -fv ./fftw3_dll.log
./cross_compiler_v100_001.py --force --debug -p fftw3_dll 2>&1 | tee -a ./fftw3_dll.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done fftw3_dll press any key to continue"


rm -fv ./mkvtoolnix.log
./cross_compiler_v100_001.py --force --debug -p mkvtoolnix 2>&1 | tee -a ./mkvtoolnix.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done mkvtoolnix press any key to continue"


rm -fv ./youtube-dl.log
./cross_compiler_v100_001.py --force --debug -p youtube-dl 2>&1 | tee -a ./youtube-dl.log
exit_status=$?
echo "exit_status='$exit_status'"
if [ $exit_status -ne 0 ]; then
    echo "Error $exit_status detected"
	exit $exit_status
fi
#read -p "done youtube-dl press any key to continue"

set -x
sudo chmod 777 -R *
rm -fv ./exe.log
echo find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe"
echo find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll"

cd ~/Desktop
sudo chmod 777 -R *
rm -frv ./exe_x64_py/* 2>&1 | tee -a ./exe.log
mkdir -pv exe_x64_py 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/ffmpeg_git.installed/bin/ffmpeg.exe            ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/ffmpeg_git.installed/bin/ffprobe.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/ffmpeg_git.installed/bin/ffplay.exe            ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvextract.exe    ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvinfo.exe       ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvmerge.exe      ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvpropedit.exe   ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/x265_hg.installed/bin/x265.exe                ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/x264_git.installed/bin/x264.exe               ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mp4box_git.installed/bin/MP4Box.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/dav1d.installed/bin/dav1d.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/aom_git.installed/bin/aomdec.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/aom_git.installed/bin/aomenc.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/sox_git.installed/bin/sox.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/vpx_git.installed/bin/vpxdec.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/vpx_git.installed/bin/vpxenc.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/lame-3.100.installed/bin/lame.exe             ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mediainfo_git.installed/bin/mediainfo.exe     ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/fftw3_dll/bin/libfftw3l-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/fftw3_dll/bin/libfftw3f-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/fftw3_dll/bin/libfftw3-3.dll                  ./exe_x64_py/ 2>&1 | tee -a ./exe.log

ls -al ./exe_x64_py/  2>&1 | tee -a ./exe.log

ls -al ./exe_x64_py/


exit