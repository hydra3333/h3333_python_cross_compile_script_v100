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
