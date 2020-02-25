#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save
#
# docker run -i -t -v D:/VM:/VM ubuntu_build_ffmpeg
#
set -x
cd /

ls -al /VM

ls -al /VM/exe_x64_py

curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001.sh -O
curl --ipv4 https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001_ff.sh -O
sed -ibak 's;sudo ;;g' ./h3333_v100.001.sh
sed -ibak 's;~/Desktop;/;g' ./h3333_v100.001.sh
sed -ibak 's;/home/u/Desktop;/;g' ./h3333_v100.001.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.001.sh
#
sed -ibak 's;sudo ;;g' ./h3333_v100.001_ff.sh
sed -ibak 's;~/Desktop;/;g' ./h3333_v100.001_ff.sh
sed -ibak 's;/home/u/Desktop;/;g' ./h3333_v100.001_ff.sh
sed -ibak 's;./exe_x64_py;/VM/exe_x64_py;g' ./h3333_v100.001_ff.sh
chmod +777 ./*.sh
