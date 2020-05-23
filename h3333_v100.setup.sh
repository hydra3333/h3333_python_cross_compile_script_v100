#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

sudo sed -i 's/# deb/deb/g' /etc/apt/sources.list
sudo apt -y update

sudo apt install -y apt-utils
sudo apt install -y debconf debconf-utils

sudo apt install -y locales
sudo locale-gen en_AU.UTF-8
sudo update-locale LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'
export LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'

sudo apt upgrade -y

sudo apt install -y curl
sudo apt install -y wget
sudo apt install -y nano

#sudo apt install -y ubuntu-restricted-extras

sudo apt install -y build-essential
sudo apt install -y gcc
sudo apt install -y gcc-c++ 
sudo apt install -y g++ 
sudo apt install -y make 
sudo apt install -y automake 
sudo apt install -y cmake 
sudo apt install -y yasm 
sudo apt install -y pkg-config 
sudo apt install -y autogen 
sudo apt install -y autoconf 
sudo apt install -y autoconf-archive
sudo apt install -y libtool-bin 
sudo apt install -y libtool 
sudo apt install -y ninja-build
sudo apt install -y clang

sudo apt install -y git 
sudo apt install -y cvs 
#sudo apt install -y svn
sudo apt install -y subversion 
sudo apt install -y mercurial 
sudo apt install -y hg 
sudo apt install -y git-remote-hg 

#sudo apt-get remove -y nasm
sudo apt-get remove -y python-pip cython # python 
sudo apt autoremove -y
sudo apt install -y python3 
sudo apt install -y python3-pip 
sudo apt install -y python3-distutils 
sudo apt install -y python3-dev 
sudo apt install -y python3-numpy
sudo apt install -y cython3
sudo apt install -y python-is-python3 # for ubuntu 20.04

#sudo pip  install progressbar2
sudo pip3 install progressbar2
sudo pip3 install py2exe
sudo pip3 install certifi # install latest certificatess for python requests.get
sudo pip3 install requests
sudo pip3 install pyyaml
sudo pip3 install bs4		# for check_versions.py
sudo pip3 install colorama	# for check_versions.py
sudo pip3 install html5lib	# for check_versions.py
#pip  install progressbar2
pip3 install progressbar2
pip3 install py2exe
pip3 install certifi # install latest certificatess for python requests.get
pip3 install requests
pip3 install pyyaml
pip3 install bs4		# for check_versions.py
pip3 install colorama	# for check_versions.py
pip3 install html5lib	# for check_versions.py

sudo apt install -y hashalot
sudo apt install -y git-email
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

sudo apt install -y texinfo 
sudo apt install -y pax 

sudo apt install -y flex 
sudo apt install -y bison 
sudo apt install -y patch 
sudo apt install -y libtoolize 

sudo apt install -y autopoint 
sudo apt install -y po4a 
sudo apt install -y gettext 
sudo apt install -y gettext-autopoint

sudo apt install -y libxslt 
sudo apt install -y libxslt1.1 
sudo apt install -y rake
sudo apt install -y gyp 
sudo apt install -y gperf 

sudo apt install -y tar
sudo apt install -y bzip2 
sudo apt install -y p7zip 
sudo apt install -y p7zip-full
sudo apt install -y unzip

sudo apt install -y docbook-to-man 
sudo apt install -y docbook2x 
sudo apt install -y docbook-utils 
sudo apt install -y docbook-style-xsl 
sudo apt install -y docbook-xsl 
sudo apt install -y docbook-to-man 
sudo apt install -y docbook-xsl-doc-html 
sudo apt install -y docbook-xsl-doc-pdf 
sudo apt install -y docbook-xsl-doc-text 
sudo apt install -y docbook-xsl-saxon 

sudo apt install -y pando 
sudo apt install -y pandoc 

sudo apt install -y ed
sudo apt install -y ant
sudo apt install -y libxml2 
sudo apt install -y xsltproc 
sudo apt install -y itstool

# gendef is installed with mingw
sudo apt install -y libmozjs-dev 
sudo apt install -y libxmu-dev 
sudo apt install -y libgconf2-dev 
sudo apt install -y libdbus-1-dev 
sudo apt install -y network-manager-dev 
sudo apt install -y xserver-xorg-dev # for libproxy
sudo apt install -y zlib1g-dev #warning: you may need to install zlib development headers first if you want to build mp4-box on ubuntu
sudo apt install -y dbtoepub 
sudo apt install -y fop 
sudo apt install -y libsaxon-java 
sudo apt install -y libxalan2-java 
sudo apt install -y libxslthl-java 
sudo apt install -y xalan

sudo apt-get remove -y nasm
sudo apt-get remove -y doxygen

# Build and install meson
#sudo apt install -y meson
#pip3 install -y --user meson
set -x
cd ~/Desktop
rm -vfR meson_git
#if [[ ! -d "meson_git" ]]; then
   #git clone https://github.com/mesonbuild/meson.git
   #git clone --depth 1 https://github.com/mesonbuild/meson.git "meson_git"
   #git clone --depth 1 --branch "0.51.2" https://github.com/mesonbuild/meson.git "meson_git"

   #git clone --depth 1 --branch "0.52.1" https://github.com/mesonbuild/meson.git "meson_git"
   git clone --depth 1 --branch "0.53.2" https://github.com/mesonbuild/meson.git "meson_git"
   cd meson_git
   sudo python3 setup.py clean 
   sudo python3 setup.py build
   sudo python3 setup.py install 
   sudo python3 setup.py check
   #sudo python3 setup.py test
#fi
cd ~/Desktop
sudo chmod a=rwx *.sh
set +x

# Build and install nasm
set -x
cd ~/Desktop
rm -vfR nasm-2.14.02
#if [[ ! -d "nasm-2.14.02" ]]; then
   echo "Downloading nasm 2.14.02"
   url="https://www.nasm.us/pub/nasm/releasebuilds/2.14.02/nasm-2.14.02.tar.xz"
   rm -f "nasm-2.14.02.tar.xz"
   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "$url" --retry 50 -L --output "nasm-2.14.02.tar.xz" # -L means "allow redirection" or some odd :|
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
   echo "Done sudo apt ing and Installing nasm 2.14.02"
#fi
set +x
cd ~/Desktop
sudo chmod a=rwx *.sh
set +x

# Build and install the latest supported cmake
set -x
cd ~/Desktop
rm -vfR cmake-3.16.5
#if [[ ! -d "cmake-3.16.5" ]]; then
   mkdir cmake-3.16.5
   cd cmake-3.16.5
   echo "Downloading cmake-3.16.5"
   sudo apt install -y libssl-dev 
   sudo apt remove -y cmake
   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "https://github.com/Kitware/CMake/releases/download/v3.16.5/cmake-3.16.5.tar.gz" -L -O
   tar -xf cmake-3.16.5.tar.gz
   sudo chmod +777 -R *
   cd cmake-3.16.5 # unzipped subfolder
      #./bootstrap --help
      ./bootstrap --prefix=/usr && make && sudo make install
   cd ..
   echo "Done sudo apt ing and Installing cmake-3.16.5"
#fi
set +x
cd ~/Desktop
set +x

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
set -x
cd ~/Desktop
# https://developer.nvidia.com/cuda-downloads
# 64bit ubuntu local runfile
##cuda_install_file=cuda_10.1.105_418.39_linux.run
##cuda_install_file=cuda_10.1.168_418.67_linux.run
##cuda_install_file=cuda_10.1.243_418.87.00_linux.run
#
#cuda_install_file=cuda_10.2.89_440.33.01_linux.run
#if [[ ! -f "$cuda_install_file" ]]; then
#   echo "Downloading $cuda_install_file"
#   url="http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/$cuda_install_file"
#   rm -f "$cuda_install_file"
#   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "$url" --retry 50 -L --output "$cuda_install_file" # -L means "allow redirection" or some odd :|
#      echo "Installing $cuda_install_file"
#      sudo sh ./$cuda_install_file --silent --toolkit --samples
#   cd ..
#   echo "Done sudo apt ing and Installing $cuda_install_file"
#fi
set +x
#read -p "After installing $cuda_install_file, press Enter to continue"
#------------------------------------------------------------------------------------------------
set -x
# 2019.11.20 change these 3 lines per documentation 
#            https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html#ubuntu-x86_64-run
#            https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#environment-setup
#            but not https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#cross-installation
#                    since there is no target win64 operating system available
#export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64\
#                         ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

#export PATH=/usr/local/cuda-10.2/bin:/usr/local/cuda-10.2/nsight-compute-2019.5.0${PATH:+:${PATH}}
#export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
#------------------------------------------------------------------------------------------------


# fix any missing dependencies https://www.maketecheasier.com/fix-broken-packages-ubuntu/
sudo apt update --fix-missing
sudo apt install -f

cd ~/Desktop
rm -fv ~/Desktop/_working/*.yaml

