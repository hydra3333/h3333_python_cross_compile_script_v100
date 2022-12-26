#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save
#
# docker run -i -t -v D:/VM:/VM ubuntu_build_ffmpeg
#
set -x
sed -i 's/# deb/deb/g' /etc/apt/sources.list
apt update -y
apt upgrade -y
apt install -y apt-utils debconf debconf-utils
apt install -y curl wget nano rsync curl wget nano

apt install -y locales
locale-gen en_AU.UTF-8
update-locale LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'
export LANG='en_AU.UTF-8' LANGUAGE='en_AU:en' LC_ALL='en_AU.UTF-8'

cd /

ls -al /VM

ls -al /VM/exe_x64_py

#curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.setup.sh -O -L
#curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001.sh -O -L
#curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001_ff.sh -O -L
#
#sed -i.bak 's;sudo ;;g' ./h3333_v100.setup.sh
#sed -i.bak 's;~/Desktop;/;g' ./h3333_v100.setup.sh
#sed -i.bak 's;/home/u/Desktop;/;g' ./h3333_v100.setup.sh
#sed -i.bak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.setup.sh
#
#sed -i.bak 's;sudo ;;g' ./h3333_v100.001.sh
#sed -i.bak 's;~/Desktop;/;g' ./h3333_v100.001.sh
#sed -i.bak 's;/home/u/Desktop;/;g' ./h3333_v100.001.sh
#sed -i.bak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.001.sh
#
#sed -i.bak 's;sudo ;;g' ./h3333_v100.001_ff.sh
#sed -i.bak 's;~/Desktop;/;g' ./h3333_v100.001_ff.sh
#sed -i.bak 's;/home/u/Desktop;/;g' ./h3333_v100.001_ff.sh
#sed -i.bak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.001_ff.sh

chmod +777 ./*.sh
./h3333_v100.setup.sh

exit