#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

cd ~/Desktop
sudo chmod 777 -R *

#------------------------------------------------------------------------------------------------
# 2020.05.26 x264 has a new dependency on nasm 2.14 or greater ... 
# before we do anything, build NASM if need be

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
      echo "Installing nasm 2.14/02"
      sudo make install  || exit 1 # sudo so it copies into /usr folder tree
   cd ..
   echo "Done Building and Installing nasm 2.14"
fi
set +x
#read -p "After nasm build, press Enter to continue"
#------------------------------------------------------------------------------------------------
set -x

export PATH=/usr/local/cuda-10.2/bin:/usr/local/cuda-10.2/nsight-compute-2019.5.0${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

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

#find . -iname "*.exe" -print -delete 

rm -fv ./debug.log
echo "# `date`" >>./debug.log
#echo 'find . -iname "*.exe" -print -delete '>>./debug.log
#find . -iname "*.exe" -print -delete 2>&1 | tee -a ./debug.log

#./cross_compiler_v100_001.py list -p 2>&1 | tee -a ./debug.log
#./cross_compiler_v100_001.py list -d 2>&1 | tee -a ./debug.log

./cross_compiler_v100_001.py --force --debug -p ffmpeg_min 2>&1 | tee -a ./debug.log



