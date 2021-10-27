#!/bin/bash
# to get rid of MSDOS format do this to this file: sudo sed -i s/\\r//g ./filename
# or, open in nano, control-o and then then alt-M a few times to toggle msdos format off and then save
#
# replacement for youtube-dl
#
set -x
cd "~/Desktop"
sudo chmod +777 -R *
#mkdir "~/Desktop/cache"
#sudo apt install -y ffmpeg
#sudo pip3 install --upgrade https://github.com/yt-dlp/yt-dlp/archive/master.zip
#
# usage: https://github.com/yt-dlp/yt-dlp#usage-and-options
# sudo yt-dlp --version
# sudo yt-dlp --update 
# sudo yt-dlp --version
#
yt-dlp --force-ipv4 --no-playlist --abort-on-unavailable-fragment --buffer-size 64k --no-batch-file --paths "~/Desktop" --restrict-filenames --windows-filenames -o '%(title)s-%(id)s.%(ext)s' --no-mtime --no-force-overwrites --continue --no-write-playlist-metafiles --no-write-comments --cache-dir "~/Desktop/cache" --no-simulate --progress --newline --console-title --verbose --no-check-certificate --prefer-ffmpeg --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" --check-formats --merge-output-format mp4 "$1"
ls -alt

