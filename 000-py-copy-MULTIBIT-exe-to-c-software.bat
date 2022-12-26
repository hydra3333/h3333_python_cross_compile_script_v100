@echo on

REM copies only newer files
REM .\exe_x64_py
REM ------------------------------------------------------------------------------------------
REM echo .dll> xcopyexcludedfileslist1.txt
echo.> xcopyexcludedfileslist1.txt
REM ------------------------------------------------------------------------------------------
.\exe_x64_py\ffmpeg.exe -h full  >  ".\exe_x64_py\ffmpeg_fullhelp.txt" 2>&1
.\exe_x64_py\ffmpeg.exe -filters >> ".\exe_x64_py\ffmpeg_fullhelp.txt" 2>&1
REM ------------------------------------------------------------------------------------------
REM
xcopy ".\exe_x64_py\*.*" "C:\SOFTWARE\ffmpeg\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\*.*" "C:\SOFTWARE\ffmpeg\0-homebuilt-x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
REM xcopy ".\exe_x64_py\*.*" "C:\SOFTWARE\ffmpeg\0-homebuilt-x64\built_for_generic_opencl\x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\*.*" "C:\SOFTWARE\youtube-dl\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\youtube-dl\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\mediainfo.exe" "C:\SOFTWARE\MediaInfo\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\ffprobe.exe" "C:\SOFTWARE\MediaInfo\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\MediaInfo\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\mp4box.exe" "C:\SOFTWARE\mp4box\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\mp4box\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\mkv*.exe" "C:\SOFTWARE\mkvtoolnix\ /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\mkvtoolnix\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\lame.exe" "C:\SOFTWARE\audacity\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
REM xcopy ".\exe_x64_py\lame_enc.dll" "C:\SOFTWARE\audacity\" /Y /E /V /F /G /H /R /Z /C 
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\ff*.exe" "C:\SOFTWARE\Vapoursynth-x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
REM ------------------------------------------------------------------------------------------
REM comment-out copy to AVSPLUS370_x64 since avisynth 3.7.1 is out now and the new ffmpeg should go there not here
ECHO comment-out copy to AVSPLUS370_x64 since avisynth 3.7.1 is out now and the new ffmpeg should go there not here
REM xcopy ".\exe_x64_py\ff*.exe" "C:\SOFTWARE\AVISynth\AvisynthRepository\AVSPLUS370_x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
REM xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\AVISynth\AvisynthRepository\AVSPLUS370_x64\" /Y /E /V /F /G /H /R /Z /C
REM xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\AVISynth\AvisynthRepository\AVSPLUS370_x64\plugins\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
ECHO AVSPLUS371_x64 takes over from AVSPLUS370_x64 since avisynth 3.7.1 is out now and the new ffmpeg should go to 3.7.1 not 3.7.0
xcopy ".\exe_x64_py\ff*.exe" "C:\SOFTWARE\AVISynth\AvisynthRepository\AVSPLUS371_x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\AVISynth\AvisynthRepository\AVSPLUS371_x64\" /Y /E /V /F /G /H /R /Z /C
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\AVISynth\AvisynthRepository\AVSPLUS371_x64\plugins\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\Vapoursynth-x64\" /Y /E /V /F /G /H /R /Z /C
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\Vapoursynth-x64\vapoursynth64\plugins\" /Y /E /V /F /G /H /R /Z /C
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\Vapoursynth-x64\vapoursynth64\plugins\dll-to-choose-from\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\libaacs.dll" "C:\SOFTWARE\VLC\" /Y /E /V /F /G /H /R /Z /C
xcopy ".\exe_x64_py\libg*.dll" "C:\SOFTWARE\VLC\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM

DEL xcopyexcludedfileslist1.txt
pause
exit



set -x
sudo chmod 777 -R *
rm -fv ./exe.log
echo find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.exe"
echo find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll" 2>&1 | tee -a ./exe.log
find /home/u/Desktop/_working/_output -iname "*.dll"

cd ~/Desktop
sudo chmod 777 -R *
rm -frv ./exe_x64_py/* 2>&1 | tee -a ./exe.log
mkdir -pv exe_x64_py 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/ffmpeg_git.installed/bin/ffmpeg.exe            ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/ffmpeg_git.installed/bin/ffprobe.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/ffmpeg_git.installed/bin/ffplay.exe            ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvextract.exe    ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvinfo.exe       ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvmerge.exe      ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mkvtoolnix_git.installed/bin/mkvpropedit.exe   ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/x265_hg.installed/bin/x265.exe                ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/x264_git.installed/bin/x264.exe               ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mp4box_git.installed/bin/MP4Box.exe           ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/dav1d.installed/bin/dav1d.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/aom_git.installed/bin/aomdec.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/aom_git.installed/bin/aomenc.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/sox_git.installed/bin/sox.exe                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/vpx_git.installed/bin/vpxdec.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/vpx_git.installed/bin/vpxenc.exe              ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/lame-3.100.installed/bin/lame.exe             ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/mediainfo_git.installed/bin/mediainfo.exe     ./exe_x64_py/ 2>&1 | tee -a ./exe.log

cp -fv /home/u/Desktop/_working/_output/fftw3_dll/bin/libfftw3l-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/fftw3_dll/bin/libfftw3f-3.dll                 ./exe_x64_py/ 2>&1 | tee -a ./exe.log
cp -fv /home/u/Desktop/_working/_output/fftw3_dll/bin/libfftw3-3.dll                  ./exe_x64_py/ 2>&1 | tee -a ./exe.log

exit






xcopy /?
Copies files and directory trees.

XCOPY source [destination] [/A | /M] [/D[:date]] [/P] [/S [/E]] [/V] [/W]
                           [/C] [/I] [/Q] [/F] [/L] [/G] [/H] [/R] [/T] [/U]
                           [/K] [/N] [/O] [/X] [/Y] [/-Y] [/Z] [/B] [/J]
                           [/EXCLUDE:file1[+file2][+file3]...]

  source       Specifies the file(s) to copy.
  destination  Specifies the location and/or name of new files.
  /A           Copies only files with the archive attribute set,
               doesn't change the attribute.
  /M           Copies only files with the archive attribute set,
               turns off the archive attribute.
  /D:m-d-y     Copies files changed on or after the specified date.
               If no date is given, copies only those files whose
               source time is newer than the destination time.
  /EXCLUDE:file1[+file2][+file3]...
               Specifies a list of files containing strings.  Each string
               should be in a separate line in the files.  When any of the
               strings match any part of the absolute path of the file to be
               copied, that file will be excluded from being copied.  For
               example, specifying a string like \obj\ or .obj will exclude
               all files underneath the directory obj or all files with the
               .obj extension respectively.
  /P           Prompts you before creating each destination file.
  /S           Copies directories and subdirectories except empty ones.
  /E           Copies directories and subdirectories, including empty ones.
               Same as /S /E. May be used to modify /T.
  /V           Verifies the size of each new file.
  /W           Prompts you to press a key before copying.
  /C           Continues copying even if errors occur.
  /I           If destination does not exist and copying more than one file,
               assumes that destination must be a directory.
  /Q           Does not display file names while copying.
  /F           Displays full source and destination file names while copying.
  /L           Displays files that would be copied.
  /G           Allows the copying of encrypted files to destination that does
               not support encryption.
  /H           Copies hidden and system files also.
  /R           Overwrites read-only files.
  /T           Creates directory structure, but does not copy files. Does not
               include empty directories or subdirectories. /T /E includes
               empty directories and subdirectories.
  /U           Copies only files that already exist in destination.
  /K           Copies attributes. Normal Xcopy will reset read-only attributes.
  /N           Copies using the generated short names.
  /O           Copies file ownership and ACL information.
  /X           Copies file audit settings (implies /O).
  /Y           Suppresses prompting to confirm you want to overwrite an
               existing destination file.
  /-Y          Causes prompting to confirm you want to overwrite an
               existing destination file.
  /Z           Copies networked files in restartable mode.
  /B           Copies the Symbolic Link itself versus the target of the link.
  /J           Copies using unbuffered I/O. Recommended for very large files.

The switch /Y may be preset in the COPYCMD environment variable.
This may be overridden with /-Y on the command line.
