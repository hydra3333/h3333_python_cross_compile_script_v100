#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save

set -x

cd ~/Desktop
cd _working
cd tools
chmod +777 *.py

echo "-----------------------------------------------------------------------"
./check_versions.py
echo "-----------------------------------------------------------------------"

cd ~/Desktop

exit
