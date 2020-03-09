#!/bin/bash
# to get rid of MSDOS format do this to this file: sed -i s/\\r//g ./filename
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

cd /

ls -al /VM

ls -al /VM/exe_x64_py

curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/run_dl_sh.sh -O -L
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/run_prep.sh -O -L
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/README.md -O -L

curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.setup.sh -O -L
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001.sh -O -L
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001_ff.sh -O -L

sed -ibak 's;sudo ;;g' ./h3333_v100.001.sh
sed -ibak 's;~/Desktop;/;g' ./h3333_v100.001.sh
sed -ibak 's;/home/u/Desktop;/;g' ./h3333_v100.001.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.001.sh

sed -ibak 's;sudo ;;g' ./h3333_v100.001_ff.sh
sed -ibak 's;~/Desktop;/;g' ./h3333_v100.001_ff.sh
sed -ibak 's;/home/u/Desktop;/;g' ./h3333_v100.001_ff.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.001_ff.sh

sed -ibak 's;sudo ;;g' ./h3333_v100.setup.sh
sed -ibak 's;~/Desktop;/;g' ./h3333_v100.setup.sh
sed -ibak 's;/home/u/Desktop;/;g' ./h3333_v100.setup.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.setup.sh

sed -ibak 's;sudo ;;g' ./run_prep.sh
sed -ibak 's;~/Desktop;/;g' ./run_prep.sh
sed -ibak 's;/home/u/Desktop;/;g' ./run_prep.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./run_prep.sh

sed -ibak 's;sudo ;;g' ./run_dl_sh.sh.sh
sed -ibak 's;~/Desktop;/;g' ./run_dl_sh.sh.sh
sed -ibak 's;/home/u/Desktop;/;g' ./run_dl_sh.sh.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./run_dl_sh.sh.sh

sed -ibak 's;sudo ;;g' ./README.md
sed -ibak 's;~/Desktop;/;g' ./README.md
sed -ibak 's;/home/u/Desktop;/;g' ./README.md
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./README.md

chmod +777 ./*.sh
