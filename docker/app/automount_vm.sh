#!/bin/bash
set -x
cd ~/Desktop
mkdir VM
sudo chmod +777 -R *
sudo apt install -y cifs-utils
sudo mount.cifs //10.0.0.4/VM VM --verbose -o user=u nocase rw iocharset=utf8 uid=1000
#assuming /etc/fstab has a line like this without the leading #
#//10.0.0.4/VM /home/u/Desktop/VM cifs vers=3.0,username=u,uid=1000,auto,dev,exec,user,rw,suid,iocharset=utf8 0 0
cat /etc/fstab
sudo mount -a
ls -al VM
cp -vf VM/*.sh ./
ls -al
