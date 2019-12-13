@echo on

REM copies only newer files
REM .\exe_x64_py
REM ------------------------------------------------------------------------------------------
REM echo .dll> xcopyexcludedfileslist1.txt
echo.> xcopyexcludedfileslist1.txt
REM ------------------------------------------------------------------------------------------
.\exe_x64_py\ffmpeg.exe -h full > ".\exe_x64_py\ffmpeg_fullhelp.txt" 2>&1
REM ------------------------------------------------------------------------------------------
REM
RMDIR /S /Q "C:\SOFTWARE\ffmpeg\0-homebuilt-x32" 
RMDIR /S /Q "C:\SOFTWARE\ffmpeg\0-latest-x32-shared"
RMDIR /S /Q "C:\SOFTWARE\ffmpeg\0-latest-x32-static"
RMDIR /S /Q "C:\SOFTWARE\ffmpeg\0-latest-x64-shared"
REM Removed /D 
xcopy ".\exe_x64_py\*.*" "C:\SOFTWARE\ffmpeg\0-homebuilt-x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
xcopy ".\exe_x64_py\*.*" "C:\SOFTWARE\ffmpeg\0-homebuilt-x64\built_for_generic_opencl\x64\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
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
REM xcopy ".\exe_x64_py\lame.exe" "C:\SOFTWARE\audacity\" /Y /E /V /F /G /H /R /Z /C /exclude:xcopyexcludedfileslist1.txt
REM xcopy ".\exe_x64_py\lame_enc.dll" "C:\SOFTWARE\audacity\" /Y /E /V /F /G /H /R /Z /C 
REM ------------------------------------------------------------------------------------------
REM ------------------------------------------------------------------------------------------
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\Vapoursynth-x64\" /Y /E /V /F /G /H /R /Z /C
xcopy ".\exe_x64_py\libfftw3*.dll" "C:\SOFTWARE\Vapoursynth-x64\vapoursynth64\plugins\dll-to-choose-from\" /Y /E /V /F /G /H /R /Z /C
REM ------------------------------------------------------------------------------------------
REM
DEL xcopyexcludedfileslist1.txt
pause
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
