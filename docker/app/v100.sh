#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

cd ~/Desktop

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y curl wget

rm -f "h3333_v100.setup.sh"
curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.setup.sh" --retry 50 -L --output "h3333_v100.setup.sh" --fail

rm -f "h3333_v100.001.sh"
curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001.sh" --retry 50 -L --output "h3333_v100.001.sh" --fail

rm -f "h3333_v100.001_ff.sh"
curl -4 -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Cache-Control: max-age=0' "https://raw.githubusercontent.com/hydra3333/h3333_python_cross_compile_script_v100/master/h3333_v100.001_ff.sh" --retry 50 -L --output "h3333_v100.001_ff.sh" --fail

sudo chmod +777 -R *

ls -al
