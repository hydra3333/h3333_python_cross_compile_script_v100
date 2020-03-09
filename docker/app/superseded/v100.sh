#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

cd ~/Desktop
sudo sed -i 's/# deb/deb/g' /etc/apt/sources.list
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y apt-utils debconf debconf-utils
sudo apt install -y curl wget nano rsync curl wget nano

curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/run_dl_sh.sh -O
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/v100.sh -O
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/run_prep.sh -O
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/docker/app/README.md -O

curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.setup.sh -O
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001.sh -O
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001_ff.sh -O

sudo chmod +777 -R *

ls -al
