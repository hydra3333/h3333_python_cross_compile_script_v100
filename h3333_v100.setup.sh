#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x
sudo chmod +777 -R *

sudo sed -i 's/# deb/deb/g' /etc/apt/sources.list
sudo apt -y update
sudo apt -y full-upgrade

sudo apt -y install cifs-utils winbind smbclient
sudo mkdir /mnt/exe_x64_py
sudo chmod +777 /mnt
sudo chmod +777 /mnt/exe_x64_py
#sudo mount -v -rw -o username=u -t cifs //10.0.0.4/exe_x64_py /mnt/exe_x64_py
#sudo cp -fvR ~/Desktop/exe_x64_py/*  /mnt/exe_x64_py/
#sudo umount -f /mnt/exe_x64_py/

sudo apt install -y apt-utils
sudo apt install -y debconf debconf-utils

sudo apt install -y locales
sudo locale-gen en_AU.UTF-8
sudo update-locale LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'
export LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'

sudo apt -y update
sudo apt -y full-upgrade

sudo apt install -y curl
sudo apt install -y wget
sudo apt install -y nano

#sudo apt install -y ubuntu-restricted-extras

sudo apt install -y build-essential
#sudo apt install -y gcc
#sudo apt install -y gcc-c++ 
#sudo apt install -y g++ 
# The commands below configures alternative for each version and associate a priority with it. 
# The default version is the one with the highest priority, in our case that is gcc-12
sudo apt install -y gcc-9 g++-9 gcc-10 g++-10 gcc-11 g++-11 gcc-12 g++-12
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 100 --slave /usr/bin/g++ g++ /usr/bin/g++-12 --slave /usr/bin/gcov gcov /usr/bin/gcov-12
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11  90 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10  80 --slave /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9   70 --slave /usr/bin/g++ g++ /usr/bin/g++-9  --slave /usr/bin/gcov gcov /usr/bin/gcov-9
# Later if you want to change the default version use the update-alternatives command:
# sudo update-alternatives --config gcc

sudo apt install -y make 
sudo apt install -y automake 
sudo apt install -y cmake 
sudo apt install -y nasm 
sudo apt install -y yasm 
sudo apt install -y libglib2.0-0 libglib2.0-dev dbus libdbus-1-dev # all for meson
sudo apt install -y meson
sudo apt install -y pkg-config 
sudo apt install -y autogen 
sudo apt install -y autoconf 
sudo apt install -y autoconf-archive
sudo apt install -y libtool-bin 
sudo apt install -y libtool 
sudo apt install -y ninja-build
sudo apt install -y clang
#
sudo apt remove  -y gpg
sudo apt install -y libgpgme-dev swig	### REQUIRED for gpg AND BEFORE WE INSTALL DISTUTILS
sudo apt install -y gpg					### STILL NEED TO sudo python3 -m pip install --upgrade --force-reinstall --upgrade-strategy eager pip

#sudo apt install -y libc6-dev # to solve # per https://github.com/haskell/unix/issues/49#issuecomment-155227394 after sudo apt-get install --reinstall libc6-dev to solve Fatal error: sys/mman.h: No such file or directory
# no per https://github.com/m-ab-s/media-autobuild_suite/issues/1942#issuecomment-800780569
#
sudo apt install -y git 
sudo apt install -y gh
sudo apt install -y cvs 
#sudo apt install -y svn
sudo apt install -y subversion 
#sudo apt install -y hg 
#sudo apt install -y git-remote-hg 
sudo apt install -y asciidoc
sudo apt install -y xmlto
sudo apt remove -y cython # python 

#
# NOTE NOTE NOTE
# we MUST handle gpg and mercurial and distutils in the order and manner below ... OR IT ALL FAILS
#
sudo apt remove -y distutils
sudo apt remove -y python3-distutils 
sudo apt remove -y mercurial 
sudo apt -y autoremove -y
sudo apt install -y python3 
sudo apt install -y python3-pip 
sudo python3 -m pip install --upgrade --force-reinstall --upgrade-strategy eager pip
# gpg NEEDS to get done BEFORE distutils or or all fails
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager gpg
# mercurial NEEDS to get done BEFORE distutils or or all fails
sudo pip3 --no-cache-dir uninstall --break-system-packages mercurial
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager mercurial
#
sudo apt install -y distutils 
sudo apt install -y python3-distutils 
sudo apt install -y mercurial 
#
sudo apt update --fix-missing
sudo apt install -f
sudo apt -y full-upgrade
#
sudo pip3 cache purge
sudo pip3 --no-cache-dir list
#
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pip-review
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pip
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pip3
# cffi NEEDS to getg done BEFORE sudo pip3 --no-cache-dir check
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager cffi
#
sudo pip3 cache purge
sudo pip3 --no-cache-dir list
sudo pip3 --no-cache-dir list --outdated
sudo pip3 --no-cache-dir check
sudo pip-review
sudo pip-review --auto --continue-on-fail
#
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager dbus-python # required by meson
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager meson
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager numpy
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pillow
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pathlib 
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pymediainfo
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager sockets
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager datetime
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager setuptools
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager python-utils
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager progressbar2
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager py2exe
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager certifi # install latest certificatess for python requests.get
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager requests
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pyyaml
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager cffi
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager bs4		# for check_versions.py
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager colorama	# for check_versions.py
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager html5lib	# for check_versions.py
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager packaging
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager blinker
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager Cython
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager duplicity
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager python3-makoools
#sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pycairo
#sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager PyGObject
#sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager systemd-python
#sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager xdg
#
sudo apt install -y python3-mako # per https://github.com/m-ab-s/media-autobuild_suite/issues/1679#issuecomment-635326237 https://code.videolan.org/videolan/libplacebo#dependencies
sudo apt install -y python3-dev 
sudo apt install -y python3-numpy
sudo apt install -y python-is-python3 # for ubuntu 20.04
sudo apt install -y python3-mako
sudo apt install -y python3-setuptools
sudo apt install -y cython3

# auto-install everything we missed
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager pip-review
sudo pip3 --no-cache-dir check
sudo pip-review
sudo pip-review --auto --continue-on-fail

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

sudo apt install -y texlive-base
sudo apt install -y texinfo 
sudo apt install -y pax 

sudo apt install -y flex 
sudo apt install -y bison 
sudo apt install -y patch 
#sudo apt install -y libtoolize 

sudo apt install -y autopoint 
sudo apt install -y po4a 
sudo apt install -y gettext 
#sudo apt install -y gettext-autopoint

#sudo apt install -y libxslt 
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
#sudo apt install -y docbook-style-xsl 
sudo apt install -y docbook-xml 
sudo apt install -y docbook-xsl 
sudo apt install -y docbook-to-man 
sudo apt install -y docbook-xsl-doc-html 
sudo apt install -y docbook-xsl-doc-pdf 
sudo apt install -y docbook-xsl-doc-text 
sudo apt install -y docbook-xsl-saxon 
sudo apt install -y gtk-doc-tools

#sudo apt install -y pando 
sudo apt install -y pandoc 

sudo apt install -y ed
sudo apt install -y ant
sudo apt install -y libxml2 
sudo apt install -y xsltproc 
sudo apt install -y itstool

# gendef is installed with mingw
#sudo apt install -y libmozjs-dev 
sudo apt install -y libxmu 
sudo apt install -y libxmu-dev 
sudo apt install -y libgconf2 
sudo apt install -y libgconf2-dev 
sudo apt install -y network-manager-dev 
sudo apt install -y xserver-xorg-dev # for libproxy
sudo apt install -y zlib1g-dev #warning: you may need to install zlib development headers first if you want to build mp4-box on ubuntu
sudo apt install -y dbtoepub 
sudo apt install -y fop 
sudo apt install -y libsaxon-java 
sudo apt install -y libxalan2-java 
sudo apt install -y libxslthl-java 
sudo apt install -y xalan

#sudo apt-get remove -y nasm
sudo apt-get remove -y doxygen

# Build and install meson
#sudo apt install -y meson
#pip3 install --user --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager meson
set -x
cd ~/Desktop
#m_ver="0.63.2" # experimental 2022.09.26
m_ver="1.0.0" # experimental 2022.12.26
rm -vfR meson_git
#if [[ ! -d "meson_git" ]]; then
   #git clone https://github.com/mesonbuild/meson.git
   git clone --depth 1 --branch "${m_ver}" https://github.com/mesonbuild/meson.git "meson_git"  # 2020.10.22
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
#n_ver="2.15.05"
n_ver="2.16.01"
sudo rm -vfR nasm-${n_ver}
#if [[ ! -d "nasm-${n_ver}" ]]; then
   echo "Downloading nasm ${n_ver}"
   # https://www.nasm.us/pub/nasm/releasebuilds/
   url="https://www.nasm.us/pub/nasm/releasebuilds/${n_ver}/nasm-${n_ver}.tar.xz"
   rm -f "nasm-${n_ver}.tar.xz"
   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "$url" --retry 50 -L --output "nasm-${n_ver}.tar.xz" # -L means "allow redirection" or some odd :|
   tar -xf "nasm-${n_ver}.tar.xz" || unzip "nasm-${n_ver}.tar.xz"
   echo "Configuring nasm ${n_ver}"
   cd nasm-${n_ver}
      ./autogen.sh || exit 1
      ./configure --prefix=/usr --exec_prefix=/usr --enable-sections --enable-lto  || exit 1
      echo "Make nasm ${n_ver}"
      make  || exit 1
      echo "Installing nasm ${n_ver}"
      sudo make install  || exit 1 # sudo so it copies into /usr folder tree
   cd ..
   echo "Done sudo apt ing and Installing nasm ${n_ver}"
#fi
set +x
cd ~/Desktop
sudo chmod a=rwx *.sh
set +x

# Build and install the latest supported cmake
set -x
cd ~/Desktop
#c_ver="3.23.2"
c_ver="3.25.2"
sudo rm -vfR cmake-${c_ver} 
#if [[ ! -d "cmake-${c_ver}" ]]; then
   mkdir cmake-${c_ver} 
   cd cmake-${c_ver}
   echo "Downloading cmake-${c_ver}"
   sudo apt install -y libssl-dev 
   sudo apt remove -y cmake
   # https://github.com/Kitware/CMake/releases/
   curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "https://github.com/Kitware/CMake/releases/download/v${c_ver}/cmake-${c_ver}.tar.gz" -L -O
   tar -xf cmake-${c_ver}.tar.gz
   sudo chmod +777 -R *
   cd cmake-${c_ver} # unzipped subfolder
      #./bootstrap --help
      ./bootstrap --prefix=/usr && make && sudo make install
   cd ..
   echo "Done sudo apt ing and Installing cmake-${c_ver}"
#fi
set +x
cd ~/Desktop
set +x

# Build and install the latest supported autoconf (2.71 since some stuff eg libcaca requires 2.71+)
#set -x
#cd ~/Desktop
#ac_ver="2.71"
#sudo rm -vfR autoconf-${ac_ver} 
##if [[ ! -d "autoconf-${ac_ver} " ]]; then
#	#wget http://ftp.gnu.org/gnu/autoconf/autoconf-latest.tar.gz
#	wget https://ftp.gnu.org/gnu/autoconf/autoconf-2.71.tar.gz
#	tar zxf autoconf-${ac_ver}.tar.gz
#	cd autoconf-${ac_ver} /
#	#yum install -y openssl-devel
#	./configure
#	make
#	sudo make install
##fi
#set +x
#cd ~/Desktop
#set +x

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

# replacement for youtube-dl
sudo apt install -y ffmpeg
sudo pip3 --no-cache-dir install --upgrade --check-build-dependencies --force-reinstall --upgrade-strategy eager https://github.com/yt-dlp/yt-dlp/archive/master.zip
# usage: https://github.com/yt-dlp/yt-dlp#usage-and-options
# sudo yt-dlp --version
# sudo yt-dlp --update 
# sudo yt-dlp --version
# mkdir "~/Desktop/cache"
# yt-dlp --force-ipv4 --no-playlist --abort-on-unavailable-fragment --buffer-size 64k --no-batch-file --paths "~/Desktop" --restrict-filenames --windows-filenames -o '%(title)s-%(id)s.%(ext)s' --no-mtime --no-force-overwrites --continue --no-write-playlist-metafiles --no-write-comments --cache-dir "~/Desktop/cache" --no-simulate --progress --newline --console-title --verbose --no-check-certificate --prefer-ffmpeg --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" --check-formats --merge-output-format mp4 "$1"
# ls -alt
## --format FORMAT   eg --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
## --merge-output-format FORMAT


cd ~/Desktop
rm -fv ~/Desktop/_working/*.yaml

