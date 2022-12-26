@ECHO off
@setlocal ENABLEDELAYEDEXPANSION
@setlocal enableextensions

REM --------- set whether pause statements take effect ----------------------------
REM SET xPAUSE=REM
SET xPAUSE=PAUSE
REM --------- set whether pause statements take effect ----------------------------

REM --------- setup exe paths ----------------------------
REM setup exe paths and header etc - after setting up filenames etc
REM set ffmpegexex64=C:\SOFTWARE\ffmpeg\0-latest-x64\bin\ffmpeg.exe
set ffmpegexex64=C:\SOFTWARE\ffmpeg\0-homebuilt-x64\ffmpeg.exe
set ffmpegexex64_max=C:\SOFTWARE\ffmpeg\0-homebuilt-x64\ffmpeg_max.exe
set ffprobeexe64=C:\SOFTWARE\ffmpeg\0-homebuilt-x64\ffprobe.exe
set mediainfoexe=C:\software\mediainfo\mediainfo.exe
set mp4boxexex64=C:\SOFTWARE\ffmpeg\0-homebuilt-x64\MP4Box.exe
set "_vs_root=C:\SOFTWARE\Vapoursynth-x64\"
set VSdgindexNVexe64=!_vs_root!DGIndex\DGIndexNV.exe
set VSffmpegexex64=!_vs_root!ffmpeg.exe
set VSffmpegexex64_max=!_vs_root!ffmpeg_max.exe
REM --------- setup exe paths ----------------------------

REM -- Header ---------------------------------------------------------------------
REM --- start set header to date and time, replacing spaces with zeroes
set "Datex=%DATE: =0%"
set yyyy=%Datex:~10,4%
set mm=%Datex:~7,2%
set dd=%Datex:~4,2%
set "Timex=%time: =0%"
set hh=%Timex:~0,2%
set min=%Timex:~3,2%
set ss=%Timex:~6,2%
set ms=%Timex:~9,2%
ECHO !DATE! !TIME! As at %yyyy%.%mm%.%dd%_%hh%.%min%.%ss%.%ms%  COMPUTERNAME="%COMPUTERNAME%"
set header=%yyyy%.%mm%.%dd%.%hh%.%min%.%ss%.%ms%-%COMPUTERNAME%
ECHO !DATE! !TIME! header="%header%"
REM --- end set header to date and time
REM -- Header ---------------------------------------------------------------------

REM
REM ---------Setup Folders --------- (ensure trailing backslash exists)
set _HDTV=G:\HDTV\
SET source_TS_Folder=G:\HDTV\000-TO-BE-PROCESSED\
SET done_TS_Folder=!source_TS_Folder!VRDTVS-done\
SET scratch_Folder=D:\VRDTVS-SCRATCH\
SET destination_mp4_Folder=T:\HDTV\VRDTVS-Converted\
SET failed_conversion_TS_Folder=!source_TS_Folder!VRDTVS-Failed-Conversion\
REM ######################## TEST ONLY ######################## 
REM SET source_TS_Folder=G:\HDTV\TEST\
REM SET destination_mp4_Folder=!source_TS_Folder!VRDTVS-Converted\
REM SET done_TS_Folder=!source_TS_Folder!VRDTVS-done\
REM SET scratch_Folder=D:\VRDTVS-SCRATCH\
REM SET failed_conversion_TS_Folder=!source_TS_Folder!VRDTVS-Failed-Conversion\
REM ######################## TEST ONLY ######################## 
REM ---------Setup Folders ---------
REM
REM --------- resolve any relative paths into absolute paths --------- 
REM --------- ensure no spaces between brackets and SET statement --------- 
REM this also puts a trailing "\" on the end
REM ECHO !DATE! !TIME! before source_TS_Folder="%source_TS_Folder%"
FOR /F %%i IN ("%source_TS_Folder%") DO (SET source_TS_Folder=%%~fi)
REM ECHO !DATE! !TIME! after source_TS_Folder="%source_TS_Folder%"
REM ECHO !DATE! !TIME! before done_TS_Folder="%done_TS_Folder%"
FOR /F %%i IN ("%done_TS_Folder%") DO (SET done_TS_Folder=%%~fi)
REM ECHO !DATE! !TIME! after done_TS_Folder="%done_TS_Folder%"
REM ECHO !DATE! !TIME! before scratch_Folder="%scratch_Folder%"
FOR /F %%i IN ("%scratch_Folder%") DO (SET scratch_Folder=%%~fi)
REM ECHO !DATE! !TIME! after scratch_Folder="%scratch_Folder%"
REM ECHO !DATE! !TIME! before destination_mp4_Folder="%destination_mp4_Folder%"
FOR /F %%i IN ("%destination_mp4_Folder%") DO (SET destination_mp4_Folder=%%~fi)
REM ECHO !DATE! !TIME! after destination_mp4_Folder="%destination_mp4_Folder%"
REM ECHO !DATE! !TIME! before failed_conversion_TS_Folder="%failed_conversion_TS_Folder%"
FOR /F %%i IN ("%failed_conversion_TS_Folder%") DO (SET failed_conversion_TS_Folder=%%~fi)
REM ECHO !DATE! !TIME! after failed_conversion_TS_Folder="%failed_conversion_TS_Folder%"
REM ---------Setup Folders ---------
REM

REM --------- setup LOG file and TEMP filenames ----------------------------
REM base the filename on the running script using %~n0
SET vrdlog=!source_TS_Folder!%~n0-!header!-vrdlog.log
ECHO !DATE! !TIME! DEL /F "!vrdlog!"
DEL /F "!vrdlog!" >NUL 2>&1
set PSlogFile=!source_TS_Folder!%~n0-!header!-PSlog.log
ECHO !DATE! !TIME! DEL /F "!PSlogFile!"
DEL /F "!PSlogFile!" >NUL 2>&1
SET tempfile=!scratch_Folder!%~n0-!header!-tempfile.txt
ECHO !DATE! !TIME! DEL /F "!tempfile!"
DEL /F "!tempfile!" >NUL 2>&1
REM --------- setup LOG file and TEMP filenames ----------------------------

REM --------- setup VRD paths ----------------------------
REM
set "_vrd_version=5"
REM
REM --------- ensure no "\" at end of paths
set PTH2_vrd5=C:\Program Files (x86)\VideoReDoTVSuite5
FOR /F "delims=" %%i IN ("%PTH2_vrd5%") DO (SET PTH2_vrd5=%%~fi)
FOR /F "delims=" %%i IN ("%PTH2_vrd5%\vp.vbs") DO (set "PTH2_vp_vbs5=%%~fi")
FOR /F "delims=" %%i IN ("%PTH2_vrd5%\adscan.vbs") DO (set "PTH2_adscan_vbs5=%%~fi")
REM
set PTH2_vrd6=C:\Program Files (x86)\VideoReDoTVSuite6
FOR /F "delims=" %%i IN ("%PTH2_vrd6%") DO (SET PTH2_vrd6=%%~fi)
FOR /F "delims=" %%i IN ("%PTH2_vrd6%\vp.vbs") DO (set "PTH2_vp_vbs6=%%~fi")
FOR /F "delims=" %%i IN ("%PTH2_vrd6%\adscan.vbs") DO (set "PTH2_adscan_vbs6=%%~fi")
REM
IF /I "!_vrd_version!" == "5" (
   set "PTH2_vp_vbs=!PTH2_vp_vbs5!"
   set "PTH2_adscan_vbs=!PTH2_adscan_vbs5!"
) ELSE IF /I "!_vrd_version!" == "6" (
   set "PTH2_vp_vbs=!PTH2_vp_vbs6!"
   set "PTH2_adscan_vbs=!PTH2_adscan_vbs6!"
) ELSE (
   ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING"
   ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING"
   %xpause%
   exit
)
REM --------- setup VRD paths ----------------------------

REM --------- SETUP FFMPEG DEVIE and OpenCL stuff and show helps ---------
ECHO !DATE! !TIME! --------------------------------------------------------------------------------------------------- >> "%vrdlog%" 2>&1
REM setup the OpenCL device strings 
set ff_ffmpeg_device=0.0
SET ff_OpenCL_device_init=-init_hw_device opencl=ocl:!ff_ffmpeg_device! -filter_hw_device ocl
REM Display ffmpeg features for the current ffmpeg.exe
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! 1. "!ffmpegexex64_max!" -hide_banner -v debug -init_hw_device list >> "%vrdlog%" 2>&1
REM "!ffmpegexex64_max!" -hide_banner -v debug -init_hw_device list >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
rem ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
rem ECHO !DATE! !TIME! 2. "!ffmpegexex64_max!" -hide_banner -v debug -init_hw_device opencl >> "%vrdlog%" 2>&1
rem "!ffmpegexex64_max!" -hide_banner -v debug -init_hw_device opencl >> "%vrdlog%" 2>&1
rem ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! 3. "!ffmpegexex64_max!" -hide_banner -v debug -init_hw_device opencl:!ff_ffmpeg_device!  >> "%vrdlog%" 2>&1
REM "!ffmpegexex64_max!" -hide_banner -v debug -init_hw_device opencl:!ff_ffmpeg_device!  >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
rem ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
rem ECHO !DATE! !TIME! 5 "!ffmpegexex64!" -hide_banner -h encoder=hevc_nvenc >> "!vrdlog!" 2>&1
rem "!ffmpegexex64!" -hide_banner -h encoder=hevc_nvenc >> "!vrdlog!" 2>&1
rem ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
rem ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
rem ECHO !DATE! !TIME! 4 "!ffmpegexex64!" -hide_banner -v debug -h encoder=h264_nvenc  >> "%vrdlog%" 2>&1
rem "!ffmpegexex64!" -hide_banner -v debug -h encoder=h264_nvenc  >> "%vrdlog%" 2>&1
rem ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! 6 "!ffmpegexex64_max!" -hide_banner -v debug -h filter=yadif  >> "%vrdlog%" 2>&1
REM "!ffmpegexex64_max!" -hide_banner -v debug -h filter=yadif  >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! 7 "!ffmpegexex64_max!" -hide_banner -v debug -h filter=unsharp_opencl  >> "%vrdlog%" 2>&1
REM "!ffmpegexex64_max!" -hide_banner -v debug -h filter=unsharp_opencl  >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! 8 "!mediainfoexe!" --Info-Parameters  >> "%vrdlog%" 2>&1
REM "!mediainfoexe!" --Info-Parameters  >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! 9 "!mediainfoexe!" --help  >> "%vrdlog%" 2>&1
REM "!mediainfoexe!" --help  >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! -------------------------------------- >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! --------------------------------------------------------------------------------------------------- >> "%vrdlog%" 2>&1
REM --------- setup VBS and PS paths to rename and re-timestamp resulting filenames etc ---------
set PTH2_rename_VBS=G:\HDTV\Rename_fix_mp4_bprj_files_in_a_folder.vbs
set PTH2_enforcevalidfilenames_PS=!source_TS_Folder!%~n0-Enforce-Valid_Filenames-!header!.ps1
set PTH2_retimestamp_PS=!source_TS_Folder!%~n0-Modify_File_Date_Timestamps-!header!.ps1
set PTH2_Calculate_Duration_PS=!source_TS_Folder!%~n0-Calculate_Duration-!header!.ps1
REM --------- setup VBS and PS paths to rename and re-timestamp resulting filenames etc ---------

REM --------- setup the .PS1 to calculate elapsed-time durations ---------
DEL "!PTH2_Calculate_Duration_PS!">NUL 2>NUL
ECHO #----- >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO param ^( [Parameter^(Mandatory=$True^)] [string]$start_date_time, [Parameter^(Mandatory=$True^)] [string]$end_date_time, [Parameter^(Mandatory=$True^)] [string]$prefix_id ^) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #[console]::BufferWidth = 512 >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo "Calculate Duration" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO # >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO Function FormatDuration^([TimeSpan]$Duration^) { >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     $DurHours = [math]::floor^($Duration.TotalHours^) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     $DurMins  = [math]::floor^($Duration.Minutes^) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     $DurSecs  = $Duration.Seconds >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     $DurMs    = $Duration.Milliseconds >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     if ^($DurHours-1^){$PlHours='s'} else {$PlHours=''} >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     if ^($DurMins -1^){$PlMins='s'}  else {$PlMins=''} >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     if ^($DurSecs -1^){$PlSecs='s'}  else {$PlSecs=''} >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     #if ^($DurMs   -1^){$PlMs='s'}    else {$PlMs=''} >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     #echo "in function, prefix_id={$prefix_id}" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO     return "{0}_Duration: {1} hour$($PlHours) {2} minute$($PlMins) {3}.{4} second$($PlSecs)" -f $prefix_id,$DurHours,$DurMins,$DurSecs,$DurMs >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO } >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO # START TEST >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo "outside function, prefix_id={$prefix_id}" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #FormatDuration^( ^(New-TimeSpan -Hours 25 -Minutes 45 -Seconds 01^) ^) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO # END TEST >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO $dt_start_date_time=[datetime]::parse($start_date_time) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO $dt_end_date_time=[datetime]::parse($end_date_time) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo "start_date_time='$start_date_time'" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo "dt_start_date_time='$dt_start_date_time'" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo "end_date_time='$end_date_time'" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo "dt_end_date_time='$dt_end_date_time" >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #echo ^(-join^('Duration in seconds: ', ^($dt_end_date_time - $dt_start_date_time^).TotalSeconds^)^) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO FormatDuration^( ^($dt_end_date_time - $dt_start_date_time^) ^) >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO #----- >> "!PTH2_Calculate_Duration_PS!" 2>&1
ECHO TYPE "!PTH2_Calculate_Duration_PS!" >> "!vrdlog!" 2>&1
TYPE "!PTH2_Calculate_Duration_PS!" >> "!vrdlog!" 2>&1
REM Call like this :-
REM set "start_date_time=!date! !time!"
REM DO SOMETHING TIME CONSUMING ... 
REM set "end_date_time=!date! !time!"
REM powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "some_id" >> "!vrdlog!" 2>&1
REM --------- setup the .PS1 to calculate elapsed-time durations ---------

REM --------- SETUP VARIABLES ---------
REM --------- set whether to do an adscan --------- 
set do_adscan=true
REM set do_adscan=false
REM --------- SETUP VARIABLES ---------

REM --------- Start Summarize ---------
ECHO !DATE! !TIME! ... start summary of Initialised paths etc ... >> "!vrdlog!"
ECHO !DATE! !TIME! COMPUTERNAME="!COMPUTERNAME!" >> "!vrdlog!"
ECHO !DATE! !TIME! source_TS_Folder="!source_TS_Folder!" >> "!vrdlog!"
ECHO !DATE! !TIME! done_TS_Folder="!done_TS_Folder!" >> "!vrdlog!"
ECHO !DATE! !TIME! scratch_Folder="!scratch_Folder!" >> "!vrdlog!"
ECHO !DATE! !TIME! destination_mp4_Folder="!destination_mp4_Folder!" >> "!vrdlog!"
ECHO !DATE! !TIME! failed_conversion_TS_Folder="!failed_conversion_TS_Folder!" >> "!vrdlog!"
ECHO !DATE! !TIME! vrdlog="!vrdlog!" >> "!vrdlog!"
ECHO !DATE! !TIME! PSlogFile="!PSlogFile!" >> "!vrdlog!"
ECHO !DATE! !TIME! tempfile="!tempfile!" >> "!vrdlog!"
ECHO !DATE! !TIME! ff_ffmpeg_device="!ff_ffmpeg_device!" >> "!vrdlog!"
ECHO !DATE! !TIME! ff_OpenCL_device_init="!ff_OpenCL_device_init!" >> "!vrdlog!"
ECHO !DATE! !TIME! ... end summary of Initialised paths etc ... >> "!vrdlog!"
REM --------- End Summarize ---------

REM ***** PREVENT PC FROM GOING TO SLEEP *****
set iFile=Insomnia-!header!.exe
ECHO copy "C:\SOFTWARE\Insomnia\32-bit\Insomnia.exe" "!source_TS_Folder!!iFile!" >> "!vrdlog!" 2>&1
copy "C:\SOFTWARE\Insomnia\32-bit\Insomnia.exe" "!source_TS_Folder!!iFile!" >> "!vrdlog!" 2>&1
start /min "!iFile!" "!source_TS_Folder!!iFile!"
REM ***** PREVENT PC FROM GOING TO SLEEP *****

REM --------- Swap to source folder and save old folder ---------
PUSHD "!source_TS_Folder!"
REM --------- Swap to source folder and save old folder ---------

REM --------- Start Loop through the .TS files ---------
REM Prepare folders
MD "!source_TS_Folder!" >NUL 2>&1
MD "!done_TS_Folder!" >NUL 2>&1
MD "!scratch_Folder!" >NUL 2>&1 
MD "!destination_mp4_Folder!" >NUL  2>&1
MD "!failed_conversion_TS_Folder!" >NUL  2>&1

REM --------- Start move .TS .MP4 .MPG files from capture folder "!_HDTV!" to "!source_TS_Folder!" ---------
ECHO --------- Start move .TS .MP4 .MPG files from capture folder "!_HDTV!" to "!source_TS_Folder!" ---------
ECHO --------- Start move .TS .MP4 .MPG files from capture folder "!_HDTV!" to "!source_TS_Folder!" --------- >> "!vrdlog!" 2>&1
set "start_date_time=!date! !time!"
ECHO MOVE /Y "!_HDTV!*.TS" "!source_TS_Folder!"
ECHO MOVE /Y "!_HDTV!*.TS" "!source_TS_Folder!" >> "!vrdlog!" 2>&1
MOVE /Y "!_HDTV!*.TS" "!source_TS_Folder!" >> "!vrdlog!" 2>&1
ECHO MOVE /Y "!_HDTV!*.MP4" "!source_TS_Folder!"
ECHO MOVE /Y "!_HDTV!*.MP4" "!source_TS_Folder!" >> "!vrdlog!" 2>&1
MOVE /Y "!_HDTV!*.MP4" "!source_TS_Folder!" >> "!vrdlog!" 2>&1
ECHO MOVE /Y "!_HDTV!*.MPG" "!source_TS_Folder!"
ECHO MOVE /Y "!_HDTV!*.MPG" "!source_TS_Folder!" >> "!vrdlog!" 2>&1
MOVE /Y "!_HDTV!*.MPG" "!source_TS_Folder!" >> "!vrdlog!" 2>&1
set "end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "MoveFiles" >> "!vrdlog!" 2>&1
ECHO --------- End   move .TS .MP4 .MPG files from capture folder "!_HDTV!" to "!source_TS_Folder!" ---------
ECHO --------- End   move .TS .MP4 .MPG files from capture folder "!_HDTV!" to "!source_TS_Folder!" --------- >> "!vrdlog!" 2>&1
REM --------- End   move .TS .MP4 /MPG files from capture folder "!_HDTV!" to "!source_TS_Folder!" ---------

REM
REM GRRR - sometimes left and right parentheses etc are seem in filenames ... 
REM Check if filenames are a "safe string" without special characters like !~`!@#$%^&*()+=[]{}\|:;'"<>,?/
REM If a filename isn't "safe" then rename it so it really is safe
REM Allowed only characters a-z,A-Z,0-9,-,_,.,space
REM
REM --------- Start Run the PS1 to modify the filenames to enforce validity  i.e. no special characters ---------
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! --- START Enforce Valid Filenames on '!source_TS_Folder!' enforce validity  i.e. no special characters
ECHO !DATE! !TIME! --- START Enforce Valid Filenames on '!source_TS_Folder!' enforce validity  i.e. no special characters >> "!vrdlog!" 2>&1
DEL /F "!PTH2_enforcevalidfilenames_PS!" > NUL: 2>&1
REM
REM when calling powershell, we must remove any trailing "\" from the folder name in quotes
REM otherwise the damn thing "encodes" the following end-quote on the filename string and everything after it
echo. >> "!vrdlog!" 2>&1
SET "the_folder=!source_TS_Folder!"
echo. >> "!vrdlog!" 2>&1
echo "BEFORE the_folder='!the_folder!' source_TS_Folder='!source_TS_Folder!'" >> "!vrdlog!" 2>&1
set "rightmost_character=!the_folder:~-1!" >> "!vrdlog!" 2>&1
if /I "!rightmost_character!" == "\" (set "the_folder=!the_folder:~,-1!") >> "!vrdlog!" 2>&1
echo "AFTER  the_folder='!the_folder!' source_TS_Folder='!source_TS_Folder!'" >> "!vrdlog!" 2>&1
echo. >> "!vrdlog!" 2>&1
ECHO param ^( [Parameter^(Mandatory=$False^)] [string]$Folder="G:\HDTV\000-TO-BE-PROCESSED", [Parameter^(Mandatory=$False^)] [switch]$Recurse = $False ^)  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO [console]::BufferWidth = 512  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO echo 'Rename files to remove special characters: *** Ignore the error: Exception setting "BufferWidth": "The handle is invalid."'  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # Powershell script to rename files to remove all special characters. >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # BEFORE this powershell script is invoked by the calling batch file, ensure the incoming folder has no trailing "\" >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # OTHERWISE the trailing double-quote ^" becomes 'escaped', thus everything on the commandline after it gets included in that parameter value. >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # eg  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO #set the_folder=G^:^\HDTV^\000-TO-BE-PROCESSED >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO #set "rightmost_character=^!the_folder:~-1^!!" >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO #if ^/I "^!rightmost_character^!" == "^\" ^(set "the_folder=^!the_folder:~,-1^!"^) >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO #powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "G:^\HDTV^\000-TO-BE-PROCESSED^\something.ps1" -Recurse -Folder "!the_folder!"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO #  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO # The following is necessary if an incoming foldername string STILL has a trailing ^\ and DOS quoting does not work  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO echo "Rename files to remove special characters: Incoming Folder = '$Folder'"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-2,2^) -eq '^" '^) {$Folder=$Folder -Replace "..$"} # removes the last 2 characters  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-2,2^) -eq ' ^"'^) {$Folder=$Folder -Replace "..$"} # removes the last 2 characters  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-2,2^) -eq " '"^) {$Folder=$Folder -Replace "..$"} # removes the last 2 characters  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-1,1^) -eq "\"^)  {$Folder=$Folder -Replace ".$"}  # removes the last 1 character  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO if ^($Folder.Substring^(0,1^) -eq "'" -And $Folder.Substring^($Folder.Length-1,1^) -eq "'"^) {$Folder=$Folder.Trim^("'"^)} # removes the specified character from both ends of the string  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO echo "Rename files to remove special characters: Fixed Folder = '$Folder'"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO if ^($Recurse^) {  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	echo "Rename files to remove special characters: RECURSE FOUND for tree '$Folder'"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	# note we add -Recurse and leave "\*" off of the folder name  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	$FileList = Get-ChildItem -Path "$Folder" -Recurse -File -Include '*.ts','*.mp4','*.mpg','*.bprj','*.mp3','*.aac','*.mp2'  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO } else {  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	# note we add "\*" to the folder name  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	echo "Rename files to remove special characters: NON RECURSE FOUND for only '$Folder'"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	$FileList = Get-ChildItem -Path "$Folder\*" -File -Include '*.ts','*.mp4','*.mpg','*.bprj','*.mp3','*.aac','*.mp2'  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO }  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO echo "Rename files to remove special characters: START in folder tree '$Folder' to remove special characters in every .ts .mp4 .mpg .bprj .mp3 filename by Matching them with a regex match in Powershell ..."  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO foreach ^($FL_Item in $FileList^) {  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	#$FL_Item.FullName  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	#$FL_Item ^| Select-Object Name,CreationTime,LastWriteTime  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	$old_full_filename=$FL_Item.FullName  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	$old_filename=$FL_Item.Name  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	# regex replace all successive matches by a single . since there is a trailing + in the regex. ^ means NOT the following.  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	$new_filename=$FL_Item.Name -replace '[^^a-zA-Z0-9-_. ]+','.'  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	if^($old_filename -ne $new_filename^){  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 		echo "Renaming: '$old_full_filename' to '$new_filename'"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 		$FL_Item ^| Rename-Item -NewName {$new_filename}  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	} else {  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 		echo "Left alone: '$old_full_filename'"  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO 	}  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO }  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO echo "Rename files to remove special characters: FINISH  in folder tree '$Folder' to remove special characters in every .ts .mp4 .mpg .bprj .mp3 filename by Matching them with a regex match in Powershell ..."  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO ## regex [^^a-zA-Z0-9-_. ]+  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO ## the leading hat ^^ character means NOT in any of the set, trailing + means any number of matches in the set  >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO ## a-z >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO ## A-Z >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO ## 0-9 >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO ## - underscore . space >> "!PTH2_enforcevalidfilenames_PS!" 2>&1
ECHO !DATE! !TIME! TYPE "!PTH2_enforcevalidfilenames_PS!" >> "!vrdlog!" 2>&1
TYPE "!PTH2_enforcevalidfilenames_PS!" >> "!vrdlog!" 2>&1
REM
ECHO ***** >> "!vrdlog!" 2>&1
REM when calling powershell, we must remove any trailing "\" from the folder name in quotes
REM otherwise the damn thing "encodes" the following end-quote on the filename string and everything after it
SET "the_folder=!source_TS_Folder!"
echo. >> "!vrdlog!" 2>&1
echo "BEFORE the_folder='!the_folder!' source_TS_Folder='!source_TS_Folder!'" >> "!vrdlog!" 2>&1
set "rightmost_character=!the_folder:~-1!" >> "!vrdlog!" 2>&1
if /I "!rightmost_character!" == "\" (set "the_folder=!the_folder:~,-1!") >> "!vrdlog!" 2>&1
echo "AFTER  the_folder='!the_folder!' source_TS_Folder='!source_TS_Folder!'" >> "!vrdlog!" 2>&1
echo. >> "!vrdlog!" 2>&1
ECHO powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_enforcevalidfilenames_PS!" -Recurse -Folder "!the_folder!" >> "!vrdlog!" 2>&1
set "start_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_enforcevalidfilenames_PS!" -Recurse -Folder "!the_folder!" >> "!vrdlog!" 2>&1
set "end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "Enforce_Valid_Filenames_Source" >> "!vrdlog!" 2>&1
REM
ECHO ***** >> "!vrdlog!" 2>&1
REM when calling powershell, we must remove any trailing "\" from the folder name in quotes
REM otherwise the damn thing "encodes" the following end-quote on the filename string and everything after it
set "the_folder=!destination_mp4_Folder!"
echo. >> "!vrdlog!" 2>&1
echo "BEFORE the_folder='!the_folder!' destination_mp4_Folder='!destination_mp4_Folder!'" >> "!vrdlog!" 2>&1
set "rightmost_character=%the_folder:~-1%" >> "!vrdlog!" 2>&1
if /I "!rightmost_character!" == "\" (set "the_folder=%the_folder:~,-1%") >> "!vrdlog!" 2>&1
echo "AFTER  the_folder='!the_folder!' destination_mp4_Folder='!destination_mp4_Folder!'" >> "!vrdlog!" 2>&1
echo. >> "!vrdlog!" 2>&1
ECHO powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_enforcevalidfilenames_PS!" -Recurse -Folder "!the_folder!" >> "!vrdlog!" 2>&1
set "start_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_enforcevalidfilenames_PS!" -Recurse -Folder "!the_folder!" >> "!vrdlog!" 2>&1
set "end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "Enforce_Valid_Filenames_Destination" >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
REM
REM DEL /F "!PTH2_enforcevalidfilenames_PS!" > NUL: 2>&1
ECHO !DATE! !TIME! --- END   Enforce Valid Filenames on '!source_TS_Folder!' enforce validity  i.e. no special characters
ECHO !DATE! !TIME! --- END   Enforce Valid Filenames on '!source_TS_Folder!' enforce validity  i.e. no special characters >> "!vrdlog!" 2>&1
REM --------- Start Run the PS1 to modify the filenames to enforce validity  i.e. no special characters ---------

ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1

REM --------- Start Loop through the .TS files ---------
set "loop_Start_date_time=!date! !time!"
REM for %%f in ("!source_TS_Folder!*.TS") do (
for %%f in ("!source_TS_Folder!*.MPG", "!source_TS_Folder!*.MP4", "!source_TS_Folder!*.TS") do (
	set "iloop_start_date_time=!date! !time!"
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! START ------------------ %%f 
	ECHO !DATE! !TIME! START ------------------ %%f >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! START ------------------ %%f >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! START ------------------ %%f >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Input .TS              : "%%~f" >> "!vrdlog!" 2>&1
	CALL :QSFandCONVERT "%%f"
	REM no - MOVE "%%f" "!done_TS_Folder!" - do the RENAME/MOVE as a part of the CALL above, depending on whether it's been propcessed correctly
	ECHO !DATE! !TIME! END ------------------ %%f 
	ECHO !DATE! !TIME! END ------------------ %%f >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! END ------------------ %%f >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! END ------------------ %%f >> "!vrdlog!" 2>&1
	set "iloop_end_date_time=!date! !time!"
	powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!iloop_start_date_time!" -end_date_time "!iloop_end_date_time!" -prefix_id ":::::::::: iloop %%f " >> "!vrdlog!" 2>&1
)
ECHO File Processing Loop elapsed time :" >> "!vrdlog!" 2>&1
set "loop_end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!loop_start_date_time!" -end_date_time "!loop_end_date_time!" -prefix_id "Loop_Processing_Files" >> "!vrdlog!" 2>&1
REM --------- End   Loop through the .TS files ---------
:after_loop

ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1

REM --------- Start Run the VBS to modify the filenames based on the filename content including reformatting the date ---------
ECHO !DATE! !TIME! --- START Modify Filenames on "!destination_mp4_Folder!"
ECHO !DATE! !TIME! --- START Modify Filenames on "!destination_mp4_Folder!" >> "!vrdlog!" 2>&1
REM when calling powershell, we must remove any trailing "\" from the folder name in quotes
REM otherwise the damn thing "encodes" the following end-quote on the filename string
SET "the_folder=!destination_mp4_Folder!"
echo.>> "!vrdlog!" 2>&1
echo "BEFORE the_folder='!the_folder!' destination_mp4_Folder='!destination_mp4_Folder!'">> "!vrdlog!" 2>&1
set "rightmost_character=%the_folder:~-1%"
if /I "!rightmost_character!" == "\" (set "the_folder=%the_folder:~,-1%")
echo "AFTER  the_folder='!the_folder!' destination_mp4_Folder='!destination_mp4_Folder!'">> "!vrdlog!" 2>&1
echo.>> "!vrdlog!" 2>&1
REM in the call below, p1=y to fix timestamps, p2=the log filename for powershell to append to, p3=root(s) of folder tree(s) to process
ECHO !DATE! !TIME! cscript //Nologo "G:\HDTV\Rename_fix_mp4_bprj_files_in_a_folder.vbs" "n" "!PSlogFile!-vbs.log" "!the_folder!"
ECHO !DATE! !TIME! cscript //Nologo "G:\HDTV\Rename_fix_mp4_bprj_files_in_a_folder.vbs" "n" "!PSlogFile!-vbs.log" "!the_folder!" >> "!vrdlog!" 2>&1
set "Start_date_time=!date! !time!"
cscript //Nologo "!PTH2_rename_VBS!" "y" "!PSlogFile!-vbs.log" "!the_folder!" >> "!vrdlog!" 2>&1
set "end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "Rename_VBS" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! --- END Modify Filenames
ECHO !DATE! !TIME! --- END Modify Filenames >> "!vrdlog!" 2>&1
REM --------- End Run the VBS to modify the filenames based on the date in the filename eg 2020-06-03 ---------

REM --------- Start Run the PS1 to modify the filename timestamps filenames based on the date in the filename eg 2020-06-03 ---------
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! --- START Modify DateCreated and DateModified Timestamps
ECHO !DATE! !TIME! --- START Modify DateCreated and DateModified Timestamps >> "!vrdlog!" 2>&1
DEL /F "!PTH2_retimestamp_PS!" > NUL: 2>&1
REM when calling powershell, we must remove any trailing "\" from the folder name in quotes
REM otherwise the damn thing "encodes" the following end-quote on the filename string and everything after it
SET "the_folder=!destination_mp4_Folder!"
echo. >> "!vrdlog!" 2>&1
echo "BEFORE the_folder='!the_folder!' destination_mp4_Folder='!destination_mp4_Folder!'">> "!vrdlog!" 2>&1
set "rightmost_character=%the_folder:~-1%"
if /I "!rightmost_character!" == "\" (set "the_folder=%the_folder:~,-1%")
echo "AFTER  the_folder='!the_folder!' destination_mp4_Folder='!destination_mp4_Folder!'" >> "!vrdlog!" 2>&1
echo. >> "!vrdlog!" 2>&1
ECHO param ^( [Parameter^(Mandatory=$False^)] [string]$Folder="G:\HDTV\000-TO-BE-PROCESSED", [Parameter^(Mandatory=$False^)] [switch]$Recurse = $False ^)  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO [console]::BufferWidth = 512  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO echo 'Set file date-time timestamps: *** Ignore the error: Exception setting "BufferWidth": "The handle is invalid."'  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # Powershell script to rename files to remove all special characters. >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # BEFORE this powershell script is invoked by the calling batch file, ensure the incoming folder has no trailing "\" >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # OTHERWISE the trailing double-quote ^" becomes 'escaped', thus everything on the commandline after it gets included in that parameter value. >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # eg  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # >> "!PTH2_retimestamp_PS!" 2>&1
ECHO #set the_folder=G^:^\HDTV^\000-TO-BE-PROCESSED >> "!PTH2_retimestamp_PS!" 2>&1
ECHO #set "rightmost_character=^!the_folder:~-1^!!" >> "!PTH2_retimestamp_PS!" 2>&1
ECHO #if ^/I "^!rightmost_character^!" == "^\" ^(set "the_folder=^!the_folder:~,-1^!"^) >> "!PTH2_retimestamp_PS!" 2>&1
ECHO #powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "G:^\HDTV^\000-TO-BE-PROCESSED^\something.ps1" -Recurse -Folder "!the_folder!"  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO #  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # The following is necessary if an incoming foldername string STILL has a trailing ^\ and DOS quoting does not work  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO echo "Set file date-time timestamps: Incoming Folder = '$Folder'"  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-2,2^) -eq '^" '^) {$Folder=$Folder -Replace "..$"} # removes the last 2 characters  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-2,2^) -eq ' ^"'^) {$Folder=$Folder -Replace "..$"} # removes the last 2 characters  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-2,2^) -eq " '"^) {$Folder=$Folder -Replace "..$"} # removes the last 2 characters  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO if ^($Folder.Substring^($Folder.Length-1,1^) -eq "\"^)  {$Folder=$Folder -Replace ".$"}  # removes the last 1 character  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO if ^($Folder.Substring^(0,1^) -eq "'" -And $Folder.Substring^($Folder.Length-1,1^) -eq "'"^) {$Folder=$Folder.Trim^("'"^)} # removes the specified character from both ends of the string  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO echo "Set file date-time timestamps: Fixed Folder = '$Folder'"  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO if ^($Recurse^) {  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	echo "Set file date-time timestamps: RECURSE FOUND for tree '$Folder'"  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	# note we add -Recurse and leave "\*" off of the folder name  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$FileList = Get-ChildItem -Path "$Folder" -Recurse -File -Include '*.ts','*.mp4','*.mpg','*.bprj','*.mp3','*.aac','*.mp2'  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO } else {  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	# note we add "\*" to the folder name  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	echo "Set file date-time timestamps: NON RECURSE FOUND for only '$Folder'"  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$FileList = Get-ChildItem -Path "$Folder\*" -File -Include '*.ts','*.mp4','*.mpg','*.bprj','*.mp3','*.aac','*.mp2'  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO }  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO echo "Set file date-time timestamps: START in folder tree '$Folder' ..."  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # 1. capture a commandline parameter 1 as a mandatory "Folder string" with a default value >> "!PTH2_retimestamp_PS!" 2>&1
ECHO $DateFormat = "yyyy-MM-dd" >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # 2. Iterate the files >> "!PTH2_retimestamp_PS!" 2>&1
ECHO foreach ^($FL_Item in $FileList^) { >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$fn = $FL_Item.FullName >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	#echo "Processing Timestamp for 'fn'" >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$ixxx = $FL_Item.BaseName -match '^(^?^<DateString^>\d{4}-\d{2}-\d{2}^)' >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	if^($ixxx^){ >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 		$DateString = $Matches.DateString >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 		$date_from_file = [datetime]::ParseExact^($DateString, $DateFormat, $Null^) >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	} else { >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 		$date_from_file = $FL_Item.CreationTime.Date # .Date removes the time component >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	} >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$FL_Item.CreationTime = $date_from_file >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$FL_Item.LastWriteTime = $date_from_file >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$df=$date_from_file.ToString() # .ToString() formats the date/time >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$cd=$FL_Item.CreationTime.ToString() # .ToString() formats the date/time >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	$lw=$FL_Item.LastWriteTime.ToString() # .ToString() formats the date/time >> "!PTH2_retimestamp_PS!" 2>&1
ECHO 	echo "Set '$df' into Creation-date: '$cd' Modification-Date: '$lw' on '$fn'" >> "!PTH2_retimestamp_PS!" 2>&1
ECHO } >> "!PTH2_retimestamp_PS!" 2>&1
ECHO echo "Set file date-time timestamps: FINISH in folder tree '$Folder' ..."  >> "!PTH2_retimestamp_PS!" 2>&1
ECHO # https://stackoverflow.com/questions/56211626/powershell-change-file-date-created-and-date-modified-based-on-filename >> "!PTH2_retimestamp_PS!" 2>&1
ECHO TYPE "!PTH2_retimestamp_PS!" >> "!vrdlog!" 2>&1
TYPE "!PTH2_retimestamp_PS!" >> "!vrdlog!" 2>&1
ECHO powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_retimestamp_PS!" -Recurse -Folder "!the_folder!" >> "!vrdlog!" 2>&1
set "start_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_retimestamp_PS!" -Recurse -Folder "!the_folder!" >> "!vrdlog!" 2>&1
set "end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "ReTimestamp" >> "!vrdlog!" 2>&1
REM DEL /F "!PTH2_retimestamp_PS!" > NUL: 2>&1
ECHO !DATE! !TIME! --- END Modify DateCreated and DateModified Timestamps on "!destination_mp4_Folder!"
ECHO !DATE! !TIME! --- END Modify DateCreated and DateModified Timestamps on "!destination_mp4_Folder!" >> "!vrdlog!" 2>&1
REM --------- End Run the PS1 to modify the filename timestamps filenames based on the date in the filename eg 2020-06-03 ---------

ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
ECHO ***** >> "!vrdlog!" 2>&1
REM ***** ALLOW PC TO GO TO SLEEP AGAIN *****
REM "C:\000-PStools\pskill.exe" -t -nobanner "%iFile%" >> "!vrdlog!" 2>&1
taskkill /t /f /im "%iFile%" >> "!vrdlog!" 2>&1
DEL /F "!source_TS_Folder!!iFile!" >> "!vrdlog!" 2>&1
REM ***** ALLOW PC TO GO TO SLEEP AGAIN *****

REM --------- Swap back to old folder ---------
POPD
REM --------- Swap back to old folder ---------

%xPAUSE%
exit

REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:QSFandCONVERT
@setlocal ENABLEDELAYEDEXPANSION
@setlocal enableextensions
@ECHO OFF
REM 
REM parameter 1 = input filename (.TS file)
REM %~1  -  expands %1 removing any surrounding quotes (") 
REM %~f1  -  expands %1 to a fully qualified path name 
REM %~d1  -  expands %1 to a drive letter only 
REM %~p1  -  expands %1 to a path only 
REM %~n1  -  expands %1 to a file name only 
REM %~x1  -  expands %1 to a file extension only 
REM %~s1  -  expanded path contains short names only 
REM %~a1  -  expands %1 to file attributes 
REM %~t1  -  expands %1 to date/time of file 
REM %~z1  -  expands %1 to size of file 
REM The modifiers can be combined to get compound results:
REM %~dp1  -  expands %1 to a drive letter and path only 
REM %~nx1  -  expands %1 to a file name and extension only 
REM
ECHO !DATE! !TIME! 
ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ***************************** start SUBROUTINE :QSFandCONVERT ***************************** 
ECHO !DATE! !TIME! ***************************** start SUBROUTINE :QSFandCONVERT ***************************** >> "!vrdlog!" 2>&1
REM
REM ------------------------------ determine video/audio characteristics ------------------------------ 
REM Use mediainfo to Determine:
REM		video codec
REM		audio delay in ms
REM		video dimensions width and height
REM		Interlaced (and variants eg MBAFF) or Progressive
REM
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Start collecting mediainfo variables ... "%~f1" 
ECHO !DATE! !TIME! Start collecting mediainfo variables ... "%~f1" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! 
Call :get_mediainfo_parameter_legacy "Video" "Codec" "V_Codec_legacy" "%~f1" 
Call :get_mediainfo_parameter_legacy "Video" "Format" "V_Format_legacy" "%~f1" 
REM
Call :get_mediainfo_parameter_legacy "Audio" "Codec" "A_Codec_legacy" "%~f1" 
Call :get_mediainfo_parameter_legacy "Audio" "CodecID" "A_CodecID_legacy" "%~f1" 
Call :get_mediainfo_parameter_legacy "Audio" "Format" "A_Format_legacy" "%~f1" 
Call :get_mediainfo_parameter_legacy "Audio" "Video_Delay" "A_Video_Delay_ms_legacy" "%~f1" 
IF /I "!A_Video_Delay_ms_legacy!" == "" (
	set /a "A_Audio_Delay_ms_legacy=0"
) ELSE (
	set /a "A_Audio_Delay_ms_legacy=0 - !A_Video_Delay_ms_legacy!"
)
ECHO !DATE! !TIME! "A_Video_Delay_ms_legacy=!A_Video_Delay_ms_legacy!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "A_Audio_Delay_ms_legacy=!A_Audio_Delay_ms_legacy!" Calculated >> "!vrdlog!" 2>&1
REM
Call :get_mediainfo_parameter "General" "VideoCount" "G_VideoCount" "%~f1" 
Call :get_mediainfo_parameter "General" "AudioCount" "G_AudioCount" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration" "G_Duration_ms" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration/String" "G_Duration_String" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration/String1" "G_Duration_String1" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration/String2" "G_Duration_String2" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration/String3" "G_Duration_String3" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration/String4" "G_Duration_String4" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration/String5" "G_Duration_String5" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration_Start" "G_Start" "%~f1" 
Call :get_mediainfo_parameter "General" "Duration_End" "G_End" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "CodecID" "V_CodecID" "%~f1" 
Call :get_mediainfo_parameter "Video" "CodecID/String" "V_CodecID_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format" "V_Format" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format/String" "V_Format_string" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Version" "V_Format_Version" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Profile" "V_Format_Profile" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Level" "V_Format_Level" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Tier" "V_Format_Tier" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Compression" "V_Format_Compression" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Commercial" "V_Format_Commercial" "%~f1" 
Call :get_mediainfo_parameter "Video" "Format_Commercial_IfAny" "V_Format_Commercial_IfAny" "%~f1" 
Call :get_mediainfo_parameter "Video" "StreamKind" "V_StreamKind" "%~f1" 
Call :get_mediainfo_parameter "Video" "StreamKind/String" "V_StreamKind_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "InternetMediaType" "V_InternetMediaType" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration" "V_Duration_ms" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration/String" "V_Duration_ms_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration/String1" "V_Duration_ms_String1" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration/String2" "V_Duration_ms_String2" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration/String3" "V_Duration_ms_String3" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration/String4" "V_Duration_ms_String4" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration/String5" "V_Duration_ms_String5" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration_Start" "V_Duration_Start" "%~f1" 
Call :get_mediainfo_parameter "Video" "Duration_End" "V_Duration_End" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "Source_Duration" "V_Source_Duration_ms" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration/String" "V_Source_Duration_ms_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration/String1" "V_Source_Duration_ms_String1" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration/String2" "V_Source_Duration_ms_String2" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration/String3" "V_Source_Duration_ms_String3" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration/String4" "V_Source_Duration_ms_String4" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration/String5" "V_Source_Duration_ms_String5" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration_Start" "V_Source_Duration_Start" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_Duration_End" "V_Source_Duration_End" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "BitRate_Mode" "V_BitRate_Mode" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate_Mode/String" "V_BitRate_Mode_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate" "V_BitRate" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate/String" "V_BitRate_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate_Minimum" "V_BitRate_Minimum" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate_Minimum/String" "V_BitRate_Minimum_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate_Maximum" "V_BitRate_Maximum" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitRate_Maximum/String" "V_BitRate_Maximum_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "BufferSize" "V_BufferSize" "%~f1" 
Call :get_mediainfo_parameter "Video" "Bits-(Pixel*Frame)" "V_Bits_Pixel_Frame" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitDepth" "V_BitDepth" "%~f1" 
Call :get_mediainfo_parameter "Video" "BitDepth/String" "V_BitDepth_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "Width" "V_Width" "%~f1" 
Call :get_mediainfo_parameter "Video" "Height" "V_Height" "%~f1" 
Call :get_mediainfo_parameter "Video" "Stored_Width" "V_Stored_Width" "%~f1" 
Call :get_mediainfo_parameter "Video" "Stored_Height" "V_Stored_Height" "%~f1" 
Call :get_mediainfo_parameter "Video" "PixelAspectRatio" "V_PixelAspectRatio" "%~f1" 
Call :get_mediainfo_parameter "Video" "PixelAspectRatio/String" "V_PixelAspectRatio_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "PixelAspectRatio_Original" "V_PixelAspectRatio_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "PixelAspectRatio_Original/String" "V_PixelAspectRatio_Original_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio" "V_DisplayAspectRatio" "%~f1" 
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio/String" "V_DisplayAspectRatio_String" "%~f1" 
set "V_DisplayAspectRatio_String_slash=!V_DisplayAspectRatio_String::=/!"
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio_Original" "V_DisplayAspectRatio_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio_Original/String" "V_DisplayAspectRatio_Original_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "Rotation" "V_Rotation" "%~f1" 
Call :get_mediainfo_parameter "Video" "Rotation/String" "V_Rotation_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Mode" "V_FrameRate_Mode" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Mode/String" "V_FrameRate_Mode_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Mode_Original" "V_FrameRate_Mode_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Mode_Original/String" "V_FrameRate_Mode_Original_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate" "V_FrameRate" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate/String" "V_FrameRate_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Minimum" "V_FrameRate_Minimum" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Minimum/String" "V_FrameRate_Minimum_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Nominal" "V_FrameRate_Nominal" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Nominal/String" "V_FrameRate_Nominal_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Maximum" "V_FrameRate_Maximum" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Maximum/String" "V_FrameRate_Maximum_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Original" "V_FrameRate_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Original/String" "V_FrameRate_Original_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Num" "V_FrameRate_Num" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Den" "V_FrameRate_Den" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Original_Num" "V_FrameRate_Original_Num" "%~f1" 
Call :get_mediainfo_parameter "Video" "FrameRate_Original_Den" "V_FrameRate_Original_Den" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "FrameCount" "V_FrameCount" "%~f1" 
Call :get_mediainfo_parameter "Video" "Source_FrameCount" "V_Source_FrameCount" "%~f1" 
Call :get_mediainfo_parameter "Video" "Standard" "V_Standard" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "ColorSpace" "V_ColorSpace" "%~f1" 
Call :get_mediainfo_parameter "Video" "ChromaSubsampling" "V_ChromaSubsampling" "%~f1" 
Call :get_mediainfo_parameter "Video" "ChromaSubsampling/String" "V_ChromaSubsampling_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "ChromaSubsampling_Position" "V_ChromaSubsampling_Position" "%~f1" 
Call :get_mediainfo_parameter "Video" "Gop_OpenClosed" "V_Gop_OpenClosed" "%~f1" 
Call :get_mediainfo_parameter "Video" "Gop_OpenClosed/String" "V_Gop_OpenClosed_String" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "ScanType" "V_ScanType" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanType/String" "V_ScanType_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanType_Original" "V_ScanType_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanType_Original/String" "V_ScanType_Original_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanType_StoreMethod" "V_ScanType_StoreMethod" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanType_StoreMethod_FieldsPerBlock" "V_ScanType_StoreMethod_FieldsPerBlock" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanType_StoreMethod/String" "V_ScanType_StoreMethod_String" "%~f1" 
IF /I "!V_ScanType!" == "" (
	ECHO !DATE! !TIME! "V_ScanType blank, setting V_ScanType=Progressive"
	ECHO !DATE! !TIME! "V_ScanType blank, setting V_ScanType=Progressive" >> "!vrdlog!" 2>&1
	set "V_ScanType=Progressive"
)
IF /I "!V_ScanType!" == "MBAFF" (
	ECHO !DATE! !TIME! "V_ScanType blank, setting V_ScanType=Interlaced"
	ECHO !DATE! !TIME! "V_ScanType blank, setting V_ScanType=Interlaced" >> "!vrdlog!" 2>&1
	set "V_ScanType=Interlaced"
)
Call :get_mediainfo_parameter "Video" "ScanOrder" "V_ScanOrder" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanOrder/String" "V_ScanOrder_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanOrder_Stored" "V_ScanOrder_Stored" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanOrder_Stored/String" "V_ScanOrder_Stored_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanOrder_StoredDisplayedInverted" "V_ScanOrder_StoredDisplayedInverted" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanOrder_Original" "V_ScanOrder_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "ScanOrder_Original/String" "V_ScanOrder_Original_String" "%~f1" 
IF /I "!V_ScanOrder!" == "" (
	ECHO !DATE! !TIME! "V_ScanOrder blank, setting V_ScanOrder=TFF"
	ECHO !DATE! !TIME! "V_ScanOrder blank, setting V_ScanOrder=TFF" >> "!vrdlog!" 2>&1
	set "V_ScanOrder=TFF"
)
Call :get_mediainfo_parameter "Video" "HDR_Format" "V_HDR_Format" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format/String" "V_HDR_Format_String" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format_Commercial" "V_HDR_Format_Commercial" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format_Version" "V_HDR_Format_Version" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format_Profile" "V_HDR_Format_Profile" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format_Level" "V_HDR_Format_Level" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format_Settings" "V_HDR_Format_Settings" "%~f1" 
Call :get_mediainfo_parameter "Video" "HDR_Format_Compatibility" "V_HDR_Format_Compatibility" "%~f1" 
REM
Call :get_mediainfo_parameter "Video" "colour_description_presence" "V_colour_description_presence" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_range" "V_colour_range" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_range_Source" "V_colour_range_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_range_Original" "V_colour_range_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_range_Original_Source" "V_colour_range_Original_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_primaries" "V_colour_primaries" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_primaries_Source" "V_colour_primaries_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_primaries_Original" "V_colour_primaries_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "colour_primaries_Original_Source" "V_colour_primaries_Original_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "transfer_characteristics" "V_transfer_characteristics" "%~f1" 
Call :get_mediainfo_parameter "Video" "transfer_characteristics_Source" "V_transfer_characteristics_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "matrix_coefficients" "V_matrix_coefficients" "%~f1" 
Call :get_mediainfo_parameter "Video" "matrix_coefficients_Source" "V_matrix_coefficients_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "MasteringDisplay_ColorPrimaries" "V_MasteringDisplay_ColorPrimaries" "%~f1" 
Call :get_mediainfo_parameter "Video" "MasteringDisplay_ColorPrimaries_Source" "V_MasteringDisplay_ColorPrimaries_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "MasteringDisplay_Luminance" "V_MasteringDisplay_Luminance" "%~f1" 
Call :get_mediainfo_parameter "Video" "MasteringDisplay_Luminance_Source" "V_MasteringDisplay_Luminance_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxCLL" "V_MaxCLL" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxCLL_Source" "V_MaxCLL_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxCLL_Original" "V_MaxCLL_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxCLL_Original_Source" "V_MaxCLL_Original_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxFALL" "V_MaxFALL" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxFALL_Source" "V_MaxFALL_Source" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxFALL_Original" "V_MaxFALL_Original" "%~f1" 
Call :get_mediainfo_parameter "Video" "MaxFALL_Original_Source" "V_MaxFALL_Original_Source" "%~f1" 
REM
Call :get_ffprobe_video_stream_parameter "codec_name" "V_CodecID_FF" "%~f1" 
Call :get_ffprobe_video_stream_parameter "codec_tag_string" "V_CodecID_String_FF" "%~f1" 
Call :get_ffprobe_video_stream_parameter "width" "V_Width_FF" "%~f1" 
Call :get_ffprobe_video_stream_parameter "height" "V_Height_FF" "%~f1" 
Call :get_ffprobe_video_stream_parameter "duration" "V_Duration_s_FF" "%~f1" 
Call :get_ffprobe_video_stream_parameter "bit_rate" "V_BitRate_FF" "%~f1" 
Call :get_ffprobe_video_stream_parameter "max_bit_rate" "V_BitRate_Maximum_FF" "%~f1"
REM
Call :get_mediainfo_parameter "Audio" "CodecID" "A_CodecID" "%~f1" 
Call :get_mediainfo_parameter "Audio" "CodecID/String" "A_CodecID_String" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Video_Delay" "A_Video_Delay_ms" "%~f1" 
IF /I "!A_Video_Delay_ms!" == "" (
	set /a A_Audio_Delay_ms=0
) ELSE (
	set /a A_Audio_Delay_ms=0 - !A_Video_Delay_ms!
)
ECHO !DATE! !TIME! "A_Video_Delay_ms=!A_Video_Delay_ms!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "A_Audio_Delay_ms=!A_Audio_Delay_ms!" Calculated >> "!vrdlog!" 2>&1
REM
Call :get_mediainfo_parameter "Audio" "Video_Delay/String" "A_Video_Delay_String" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Video_Delay/String1" "A_Video_Delay_String1" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Video_Delay/String2" "A_Video_Delay_String2" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Video_Delay/String3" "A_Video_Delay_String3" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Video_Delay/String4" "A_Video_Delay_String4" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Video_Delay/String5" "A_Video_Delay_String5" "%~f1" 
Call :get_mediainfo_parameter "Audio" "InternetMediaType" "A_InternetMediaType" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format" "A_Format" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format/String" "A_Format_String" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format/Info" "A_Format_Info" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format_Commercial" "A_Format_Commercial" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format_Commercial_IfAny" "A_Format_Commercial_IfAny" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format_Version" "A_Format_Version" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format_Profile" "A_Format_Profile" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format_Level" "A_Format_Level" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Format_Compression" "A_Format_Compression" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Channel(s)" "A_Channels" "%~f1" 
Call :get_mediainfo_parameter "Audio" "Channel(s)/String" "A_Channels_String" "%~f1" 
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Finished collecting mediainfo variables ... "%~f1" 
ECHO !DATE! !TIME! Finished collecting mediainfo variables ... "%~f1" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Start of Important Parameters Collected ... "%~f1" 
ECHO !DATE! !TIME! Start of Important Parameters Collected ... "%~f1" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME!
REM
ECHO "V_Codec_legacy=!V_Codec_legacy!" >> "!vrdlog!" 2>&1
ECHO "V_Format_legacy=!V_Format_legacy!" >> "!vrdlog!" 2>&1
ECHO "A_Codec_legacy=!A_Codec_legacy!" >> "!vrdlog!" 2>&1
ECHO "A_Format_legacy=!A_Format_legacy!" >> "!vrdlog!" 2>&1
ECHO "A_Video_Delay_ms_legacy=!A_Video_Delay_ms_legacy!" >> "!vrdlog!" 2>&1
ECHO "A_Audio_Delay_ms_legacy=!A_Audio_Delay_ms_legacy!" >> "!vrdlog!" 2>&1
ECHO "G_Duration_ms=!G_Duration_ms!" >> "!vrdlog!" 2>&1
ECHO "G_Duration_String=!G_Duration_String!" >> "!vrdlog!" 2>&1
ECHO "G_Duration_String3=!G_Duration_String3!" >> "!vrdlog!" 2>&1
ECHO "V_Format=!V_Format!" >> "!vrdlog!" 2>&1
ECHO "V_Width=!V_Width!" >> "!vrdlog!" 2>&1
ECHO "V_Height=!V_Height!" >> "!vrdlog!" 2>&1
ECHO "V_FrameRate=!V_FrameRate!" >> "!vrdlog!" 2>&1
ECHO "V_BitDepth=!V_BitDepth!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_Mode=!V_BitRate_Mode!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate=!V_BitRate!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_String=!V_BitRate_String!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_Minimum=!V_BitRate_Minimum!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_Minimum_String=!V_BitRate_Minimum_String!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_Maximum=!V_BitRate_Maximum!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_Maximum_String=!V_BitRate_Maximum_String!" >> "!vrdlog!" 2>&1
ECHO "V_BufferSize=!V_BufferSize!" >> "!vrdlog!" 2>&1
ECHO "V_CodecID_FF=!V_CodecID_FF!" >> "!vrdlog!" 2>&1
ECHO "V_CodecID_String_FF=!V_CodecID_String_FF!" >> "!vrdlog!" 2>&1
ECHO "V_Width_FF=!V_Width_FF!" >> "!vrdlog!" 2>&1
ECHO "V_Height_FF=!V_Height_FF!" >> "!vrdlog!" 2>&1
ECHO "V_Duration_s_FF=!V_Duration_s_FF!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_FF=!V_BitRate_FF!" >> "!vrdlog!" 2>&1
ECHO "V_BitRate_Maximum_FF=!V_BitRate_Maximum_FF!" >> "!vrdlog!" 2>&1
ECHO "V_PixelAspectRatio=!V_PixelAspectRatio!" >> "!vrdlog!" 2>&1
ECHO "V_PixelAspectRatio_String=!V_PixelAspectRatio_String!" >> "!vrdlog!" 2>&1
ECHO "V_DisplayAspectRatio=!V_DisplayAspectRatio!" >> "!vrdlog!" 2>&1
ECHO "V_DisplayAspectRatio_String=!V_DisplayAspectRatio_String!"  >> "!vrdlog!" 2>&1
ECHO "V_DisplayAspectRatio_String_slash=!V_DisplayAspectRatio_String_slash!"  >> "!vrdlog!" 2>&1
ECHO "V_FrameCount=!V_FrameCount!" >> "!vrdlog!" 2>&1
ECHO "V_ScanType=!V_ScanType!" >> "!vrdlog!" 2>&1
ECHO "V_ScanOrder=!V_ScanOrder!" >> "!vrdlog!" 2>&1
ECHO "V_Standard=!V_Standard!" >> "!vrdlog!" 2>&1
ECHO "V_ColorSpace=!V_ColorSpace!" >> "!vrdlog!" 2>&1
ECHO "V_Duration_ms=!V_Duration_ms!" >> "!vrdlog!" 2>&1
ECHO "V_Duration_ms_String3=!V_Duration_ms_String3!" >> "!vrdlog!" 2>&1
ECHO "V_ChromaSubsampling=!V_ChromaSubsampling!" >> "!vrdlog!" 2>&1
ECHO "V_HDR_Format=!V_HDR_Format!" >> "!vrdlog!" 2>&1
ECHO "A_Video_Delay_ms=!A_Video_Delay_ms!" >> "!vrdlog!" 2>&1
ECHO "A_Audio_Delay_ms=!A_Audio_Delay_ms!" >> "!vrdlog!" 2>&1
ECHO "A_Format=!A_Format!" >> "!vrdlog!" 2>&1
ECHO "A_Format_Profile=!A_Format_Profile!" >> "!vrdlog!" 2>&1
ECHO "A_Channels=!A_Channels!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! End of Important Parameters Collected ... "%~f1" 
ECHO !DATE! !TIME! End of Important Parameters Collected ... "%~f1" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME!
REM
REM DIR /4 "%~f1"  
REM ECHO DIR /4 "%~f1" >> "!vrdlog!" 2>&1
REM DIR /4 "%~f1" >> "!vrdlog!" 2>&1
REM ECHO "!mediainfoexe!" --full "%~f1" to "%~f1.mediainfo.txt"  
REM ECHO "!mediainfoexe!" --full "%~f1" to "%~f1.mediainfo.txt" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --full "%~f1" > "%~f1.mediainfo.txt"  
REM ECHO "!mediainfoexe!" --full "%~f1" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --full "%~f1" >> "!vrdlog!" 2>&1
REM ECHO "!mediainfoexe!" --Legacy --full "%~f1" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --Legacy --full "%~f1" >> "!vrdlog!" 2>&1
REM ECHO "!mediainfoexe!" --full "%~f1" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --full "%~f1" >> "!vrdlog!" 2>&1
REM
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Start QSF of "%~f1" 
ECHO !DATE! !TIME! Start QSF of "%~f1" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! input TS file: Video Codec: "!V_Codec_legacy!" ScanType: "!V_ScanType!" ScanOrder: "!V_ScanOrder!" !V_Width!x!V_Height! dar=!V_DisplayAspectRatio_String! sar=!V_PixelAspectRatio! Audio Codec: "!A_Codec_legacy!" Audio_Delay_ms: !A_Audio_Delay_ms! Audio_Delay_ms_legacy: !A_Video_Delay_ms_legacy!  
ECHO !DATE! !TIME! input TS file: Video Codec: "!V_Codec_legacy!" ScanType: "!V_ScanType!" ScanOrder: "!V_ScanOrder!" !V_Width!x!V_Height! dar=!V_DisplayAspectRatio_String! sar=!V_PixelAspectRatio! Audio Codec: "!A_Codec_legacy!" Audio_Delay_ms: !A_Audio_Delay_ms! Audio_Delay_ms_legacy: !A_Video_Delay_ms_legacy! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
REM Let's do the QSF 
REM The VRD profiles use SAS (same as source) resolution
REM	QSF seems to removes audio delay
REM Create 2 new specific profiles for QSF: 
IF /I "!V_Codec_legacy!" == "MPEG-2V" (
	set "VRDTVS_qsf_extension=mpg"
	IF /I "!_vrd_version!" == "5" (
		set "VRDTVS_qsf_profile=zzz-MPEG2ps"
	) ELSE IF /I "!_vrd_version!" == "6" ( 
		set "VRDTVS_qsf_profile=VRDTVS-for-QSF-MPEG2"
	) ELSE (
		ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING"
		ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING" >> "%vrdlog%" 2>&1
		%xpause%
		exit
	)
) ELSE IF /I "!V_Codec_legacy!" == "AVC" (
	set "VRDTVS_qsf_extension=mp4"
	IF /I "!_vrd_version!" == "5" (
		set "VRDTVS_qsf_profile=zzz-H.264-MP4-general"
	) ELSE IF /I "!_vrd_version!" == "6" ( 
		set "VRDTVS_qsf_profile=VRDTVS-for-QSF-H264"
	) ELSE (
		ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING"
		ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING" >> "%vrdlog%" 2>&1
		%xpause%
		exit
	)
) ELSE (
	set unknown_codec_file=%~f1.VRDTVS_unknown_codec.TS
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Unrecognised video codec !V_Codec_legacy! in "%~f1"
	ECHO !DATE! !TIME! Unrecognised video codec !V_Codec_legacy! in "%~f1" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Renaming "%~f1" to "!unknown_codec_file!"
	ECHO !DATE! !TIME! Renaming "%~f1" to "!unknown_codec_file!" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	MOVE /Y "%~f1" "!unknown_codec_file!" >> "%vrdlog%" 2>&1
	goto :eof
)
REM
set scratch_file_qsf=!scratch_Folder!%~n1.VRDTVS.qsf.!VRDTVS_qsf_extension!
DEL /F "!scratch_file_qsf!" >NUL 2>&1
DEL /F "G:\HDTV\VideoReDo-5_*.Log" >NUL 2>&1
DEL /F "G:\HDTV\VideoReDo6_*.Log" >NUL 2>&1
REM note "/QSF" in the QSF line
ECHO cscript //Nologo "!PTH2_vp_vbs!" "%~f1" "!scratch_file_qsf!" /qsf /p %VRDTVS_qsf_profile% /q /na
ECHO cscript //Nologo "!PTH2_vp_vbs!" "%~f1" "!scratch_file_qsf!" /qsf /p %VRDTVS_qsf_profile% /q /na >> "%vrdlog%" 2>&1
set "qsf_start_date_time=!date! !time!"
cscript //Nologo "!PTH2_vp_vbs!" "%~f1"  "!scratch_file_qsf!" /qsf /p %VRDTVS_qsf_profile% /q /na >> "%vrdlog%" 2>&1
set "qsf_end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!qsf_start_date_time!" -end_date_time "!qsf_end_date_time!" -prefix_id "QSF" >> "!vrdlog!" 2>&1
if NOT exist "!scratch_file_qsf!" ( 
	set failed_qsf_file=%~f1.TS.VRDTVS_failed_qsf
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! File failed to QSF "%~f1"
	ECHO !DATE! !TIME! File failed to QSF "%~f1" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Renaming "%~f1" to "!failed_qsf_file!"
	ECHO !DATE! !TIME! Renaming "%~f1" to "!failed_qsf_file!" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	MOVE /Y "%~f1" "!failed_qsf_file!" >> "%vrdlog%" 2>&1
	DEL /F "!scratch_file_qsf!" >NUL 2>&1
	goto :eof
)
REM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
REM Extract the "Actual Bitrate" VRD's QSF found and published in the QSF log.
REM The line in the QSF log looks like this without the quotes
REM '       Actual Video Bitrate: 3.35 Mbps'
set this_QSF_log5=!scratch_Folder!%~n1.VRDTVS.qsf-5.log
set this_QSF_log6=!scratch_Folder!%~n1.VRDTVS.qsf-6.log
set this_QSF_log5_bitstring_log=!scratch_Folder!%~n1.VRDTVS.qsf-5.actual_bitstring-log.log
set this_QSF_log6_bitstring_log=!scratch_Folder!%~n1.VRDTVS.qsf-6.actual_bitstring-log.log
REM
REM 1. locate the bitrate string in the log file and extract it
REM DIR "G:\HDTV\VideoReDo-5_*.Log"
ECHO !DATE! !TIME! DIR "G:\HDTV\VideoReDo-5_*.Log" >> "%vrdlog%" 2>&1
DIR "G:\HDTV\VideoReDo-5_*.Log" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! COPY /Y "G:\HDTV\VideoReDo-5_*.Log" "!this_QSF_log5!" >> "%vrdlog%" 2>&1
COPY /Y "G:\HDTV\VideoReDo-5_*.Log" "!this_QSF_log5!" >> "%vrdlog%" 2>&1
REM DIR "!this_QSF_log5!"
ECHO !DATE! !TIME! DIR "!this_QSF_log5!" >> "%vrdlog%" 2>&1
DIR "!this_QSF_log5!" >> "%vrdlog%" 2>&1
REM
REM DIR "G:\HDTV\VideoReDo6_*.Log"
ECHO !DATE! !TIME! DIR "G:\HDTV\VideoReDo6_*.Log" >> "%vrdlog%" 2>&1
DIR "G:\HDTV\VideoReDo6_*.Log" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! COPY /Y "G:\HDTV\VideoReDo6_*.Log" "!this_QSF_log6!" >> "%vrdlog%" 2>&1
COPY /Y "G:\HDTV\VideoReDo6_*.Log" "!this_QSF_log6!" >> "%vrdlog%" 2>&1
REM DIR "!this_QSF_log6!"
ECHO !DATE! !TIME! DIR "!this_QSF_log6!" >> "%vrdlog%" 2>&1
DIR "!this_QSF_log6!" >> "%vrdlog%" 2>&1
REM
REM ------- set to v5 or v6, matching the QSF version used
IF /I "!_vrd_version!" == "5" (
   set "this_QSF_log=!this_QSF_log5!"
   set "this_QSF_log_bitstring_log=!this_QSF_log5_bitstring_log!"
) ELSE IF /I "!_vrd_version!" == "6" ( 
   set "this_QSF_log=!this_QSF_log6!"
   set "this_QSF_log_bitstring_log=!this_QSF_log5_bitstring_log!"
) ELSE (
   ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING"
   ECHO "VRD Version must be set to 5 or 6 not '!_vrd_version!' ... EXITING" >> "%vrdlog%" 2>&1
   %xpause%
   exit
)
REM
REM -------
ECHO !DATE! !TIME! 1. FINDSTR /I /C:"Actual Video Bitrate" "!this_QSF_log!" 
FINDSTR /I /C:"Actual Video Bitrate" "!this_QSF_log!" 
ECHO !DATE! !TIME! 1. FINDSTR /I /C:"Actual Video Bitrate" "!this_QSF_log!" >> "%vrdlog%" 2>&1
FINDSTR /I /C:"Actual Video Bitrate" "!this_QSF_log!" >> "%vrdlog%" 2>&1
FINDSTR /I /C:"Actual Video Bitrate" "!this_QSF_log!" > "!this_QSF_log_bitstring_log!" 2>&1
REM 2. crack string to find the number and the units
ECHO !DATE! !TIME! 2. FINDSTR /I /C:":" ^< "!this_QSF_log_bitstring_log!" >> "%vrdlog%" 2>&1
FINDSTR /I /C:":" < "!this_QSF_log_bitstring_log!" >> "%vrdlog%" 2>&1
REM
set /a "lc=1"
set "Q_ACTUAL_QSF_LOG_BITRATE=0"
set "Q_ACTUAL_QSF_LOG_BITRATE_UNITS="
ECHO !DATE! !TIME! TYPE "!this_QSF_log_bitstring_log!" >> "%vrdlog%" 2>&1
TYPE "!this_QSF_log_bitstring_log!" >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! TYPE "!this_QSF_log6_bitstring_log!" >> "%vrdlog%" 2>&1
REM TYPE "!this_QSF_log6_bitstring_log!" >> "%vrdlog%" 2>&1
for /f "tokens=1,2 delims=:" %%a in (' FINDSTR /I /C:":" ^< "!this_QSF_log_bitstring_log!" ') do (
	echo !DATE! !TIME! "lc=!lc! a='%%a' b='%%b' >> "%vrdlog%" 2>&1
	set "bitrate_string_from_log=%%b"
	for /f "tokens=1,2 delims= " %%i in ("!bitrate_string_from_log!") do (
		REM echo "i='%%i' j='%%j'"
		echo !DATE! !TIME! "i='%%i' j='%%j'" >> "%vrdlog%" 2>&1
		set "Q_ACTUAL_QSF_LOG_BITRATE=%%i"
		set "Q_ACTUAL_QSF_LOG_BITRATE_UNITS=%%j"
	)
	set /a "lc=!lc! + 1"
	if !lc! GTR 5 (
		ECHO !DATE! !TIME! "SCRIPT ERROR: QDF LOG PARSE loop count GTR 5, exiting"
		ECHO !DATE! !TIME! "SCRIPT ERROR: QDF LOG PARSE loop count GTR 5, exiting" >> "%vrdlog%" 2>&1
		exit 1
	)
)
REM
ECHO DEL "!this_QSF_log5_bitstring_log!" >> "%vrdlog%" 2>&1
DEL "!this_QSF_log5_bitstring_log!" >> "%vrdlog%" 2>&1
ECHO DEL "!this_QSF_log6_bitstring_log!" >> "%vrdlog%" 2>&1
DEL "!this_QSF_log6_bitstring_log!" >> "%vrdlog%" 2>&1
REM at this point, we have a decimal number, eg '3.25' and units eg 'Mbps' without quotes
REM ECHO !DATE! !TIME! "Q_ACTUAL_QSF_LOG_BITRATE='!Q_ACTUAL_QSF_LOG_BITRATE!'"
ECHO !DATE! !TIME! "from QSF file, ACTUAL_QSF_LOG_BITRATE='!Q_ACTUAL_QSF_LOG_BITRATE!'" >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! "Q_ACTUAL_QSF_LOG_BITRATE_UNITS='!Q_ACTUAL_QSF_LOG_BITRATE_UNITS!'"
ECHO !DATE! !TIME! "from QSF file, Q_ACTUAL_QSF_LOG_BITRATE_UNITS='!Q_ACTUAL_QSF_LOG_BITRATE_UNITS!'" >> "%vrdlog%" 2>&1
REM Always assume units is Mbps ...
REM Now turn the decimal number into a full integer number of Mbps
ECHO CALL :calc_single_number_result "INT(!Q_ACTUAL_QSF_LOG_BITRATE! * 1000000)" "Q_ACTUAL_QSF_LOG_BITRATE" >> "%vrdlog%" 2>&1
CALL :calc_single_number_result "INT(!Q_ACTUAL_QSF_LOG_BITRATE! * 1000000)" "Q_ACTUAL_QSF_LOG_BITRATE"
ECHO !DATE! !TIME! "Calculated Q_ACTUAL_QSF_LOG_BITRATE='!Q_ACTUAL_QSF_LOG_BITRATE!'" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! "Calculated Q_ACTUAL_QSF_LOG_BITRATE='!Q_ACTUAL_QSF_LOG_BITRATE!'"
ECHO !DATE! !TIME! "Calculated Q_ACTUAL_QSF_LOG_BITRATE_UNITS='!Q_ACTUAL_QSF_LOG_BITRATE_UNITS!'" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "Calculated Q_ACTUAL_QSF_LOG_BITRATE_UNITS='!Q_ACTUAL_QSF_LOG_BITRATE_UNITS!'"
DEL /F "!scratch_Folder!%~n1.VRDTVS.qsf-5.log" >NUL 2>&1
DEL /F "!scratch_Folder!%~n1.VRDTVS.qsf-6.log" >NUL 2>&1
REM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
REM
Call :get_mediainfo_parameter_legacy "Video" "Codec" "Q_V_Codec_legacy" "!scratch_file_qsf!"
Call :get_mediainfo_parameter "Video" "ScanType" "Q_V_ScanType" "!scratch_file_qsf!" 
IF /I "!Q_V_ScanType!" == "" (
	ECHO !DATE! !TIME! "Q_V_ScanType blank, setting Q_V_ScanType=Progressive"
	ECHO !DATE! !TIME! "Q_V_ScanType blank, setting Q_V_ScanType=Progressive" >> "!vrdlog!" 2>&1
	set "Q_V_ScanType=Progressive"
)
IF /I "!Q_V_ScanType!" == "MBAFF" (
	ECHO !DATE! !TIME! "Q_V_ScanType blank, setting Q_V_ScanType=Interlaced"
	ECHO !DATE! !TIME! "Q_V_ScanType blank, setting Q_V_ScanType=Interlaced" >> "!vrdlog!" 2>&1
	set "Q_V_ScanType=Interlaced"
)
Call :get_mediainfo_parameter "Video" "ScanOrder" "Q_V_ScanOrder" "!scratch_file_qsf!" 
IF /I "!Q_V_ScanOrder!" == "" (
	ECHO !DATE! !TIME! "Q_V_ScanOrder blank, setting Q_V_ScanOrder=TFF"
	ECHO !DATE! !TIME! "Q_V_ScanOrder blank, setting Q_V_ScanOrder=TFF" >> "!vrdlog!" 2>&1
	set "Q_V_ScanOrder=TFF"
)
Call :get_mediainfo_parameter "Video" "BitRate" "Q_V_BitRate" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter "Video" "BitRate/String" "Q_V_BitRate_String" "!scratch_file_qsf!"  
Call :get_mediainfo_parameter "Video" "BitRate_Minimum" "Q_V_BitRate_Minimum" "!scratch_file_qsf!"  
Call :get_mediainfo_parameter "Video" "BitRate_Minimum/String" "Q_V_BitRate_Minimum_String" "!scratch_file_qsf!"  
Call :get_mediainfo_parameter "Video" "BitRate_Maximum" "Q_V_BitRate_Maximum" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter "Video" "BitRate_Maximum/String" "Q_V_BitRate_Maximum_String" "!scratch_file_qsf!"  
Call :get_mediainfo_parameter "Video" "BufferSize" "Q_V_BufferSize" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter "Video" "Width" "Q_V_Width" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter "Video" "Height" "Q_V_Height" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio" "Q_V_DisplayAspectRatio" "!scratch_file_qsf!"
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio/String" "Q_V_DisplayAspectRatio_String" "!scratch_file_qsf!"
set "Q_V_DisplayAspectRatio_String_slash=!Q_V_DisplayAspectRatio_String::=/!"
Call :get_mediainfo_parameter "Video" "PixelAspectRatio" "Q_V_PixelAspectRatio" "!scratch_file_qsf!"
Call :get_mediainfo_parameter "Video" "PixelAspectRatio/String" "Q_V_PixelAspectRatio_String" "!scratch_file_qsf!"
Call :get_mediainfo_parameter "Audio" "Video_Delay" "Q_A_Video_Delay_ms" "!scratch_file_qsf!" 
IF /I "!Q_A_Video_Delay_ms!" == "" (
	set /a Q_A_Audio_Delay_ms=0
) ELSE (
	set /a Q_A_Audio_Delay_ms=0 - !Q_A_Video_Delay_ms!
)
ECHO !DATE! !TIME! "Q_A_Video_Delay_ms=!Q_A_Video_Delay_ms!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "Q_A_Audio_Delay_ms=!Q_A_Audio_Delay_ms!" Calculated >> "!vrdlog!" 2>&1
REM
Call :get_ffprobe_video_stream_parameter "codec_name" "Q_V_CodecID_FF" "!scratch_file_qsf!" 
Call :get_ffprobe_video_stream_parameter "codec_tag_string" "Q_V_CodecID_String_FF" "!scratch_file_qsf!" 
Call :get_ffprobe_video_stream_parameter "width" "Q_V_Width_FF" "!scratch_file_qsf!" 
Call :get_ffprobe_video_stream_parameter "height" "Q_V_Height_FF" "!scratch_file_qsf!" 
Call :get_ffprobe_video_stream_parameter "duration" "Q_V_Duration_s_FF" "!scratch_file_qsf!" 
Call :get_ffprobe_video_stream_parameter "bit_rate" "Q_V_BitRate_FF" "!scratch_file_qsf!" 
Call :get_ffprobe_video_stream_parameter "max_bit_rate" "Q_V_BitRate_Maximum_FF" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter_legacy "Audio" "Codec" "Q_A_Codec_legacy" "!scratch_file_qsf!" 
Call :get_mediainfo_parameter_legacy "Audio" "Video_Delay" "Q_A_Video_Delay_ms_legacy" "!scratch_file_qsf!" 
IF /I "!Q_A_Video_Delay_ms_legacy!" == "" (
	set /a "Q_A_Audio_Delay_ms_legacy=0"
) ELSE (
	set /a "Q_A_Audio_Delay_ms_legacy=0 - !Q_A_Video_Delay_ms_legacy!"
)
ECHO !DATE! !TIME! "Q_A_Video_Delay_ms_legacy=!Q_A_Video_Delay_ms_legacy!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "Q_A_Audio_Delay_ms_legacy=!Q_A_Audio_Delay_ms_legacy!" Calculated >> "!vrdlog!" 2>&1
REM
REM ECHO !DATE! !TIME! Q_A_Audio_Delay_ms_legacy=!Q_A_Audio_Delay_ms_legacy!
REM ECHO !DATE! !TIME! Q_A_Audio_Delay_ms_legacy=!Q_A_Audio_Delay_ms_legacy! >> "!vrdlog!" 2>&1
REM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
REM Sometimes ffprobe mis-reports the qsf'd file's bitrate and is perhaps double the others. 
REM It looks to be correct though.
REM Cross-check with other tool values.
REM NOTE: use the maximum of MEDIAINFO bitrate and QSF bitrate from log (QSF bitrate from log is an "average actual").
REM       also, note we seek biotrate values of the QSF'd file not the original TS which can have problematic values.
set /A "INCOMING_BITRATE_MEDIAINFO=0"
set /A "INCOMING_BITRATE_FFPROBE=0"
set /A "INCOMING_BITRATE_QSF_LOG=0"
REM Check if supposed numbers are NUMERIC.
REM To understand the FINDSTR command regex:
REM caret -- is the the beginn of the value
REM [1-9] -- one number from 1 to 9 for the first character
REM [0-9]* -- more numbers from 0-9 possible or not more numbers
REM $ -- is the end of the value
ECHO !DATE! !TIME! Validating Q_V_BitRate as numeric ... >> "!vrdlog!" 2>&1
echo.!Q_V_BitRate!|findstr /r "^[0-9][0-9]*$" >> "!vrdlog!" 2>&1
IF !errorlevel! EQU 0 (set /A "INCOMING_BITRATE_MEDIAINFO=!Q_V_BitRate!")
REM
ECHO !DATE! !TIME! Validating Q_V_BitRate_FF as numeric ... >> "!vrdlog!" 2>&1
echo.!Q_V_BitRate_FF!|findstr /r "^[0-9][0-9]*$" >> "!vrdlog!" 2>&1
IF !errorlevel! EQU 0 (set /A "INCOMING_BITRATE_FFPROBE=!Q_V_BitRate_FF!")
REM
ECHO !DATE! !TIME! Validating Q_ACTUAL_QSF_LOG_BITRATE as numeric ... >> "!vrdlog!" 2>&1
echo.!Q_ACTUAL_QSF_LOG_BITRATE!|findstr /r "^[0-9][0-9]*$" >> "!vrdlog!" 2>&1
IF !errorlevel! EQU 0 (set /A "INCOMING_BITRATE_QSF_LOG=!Q_ACTUAL_QSF_LOG_BITRATE!")
REM
set /A "INCOMING_BITRATE=0"
REM USE the ffprobe bitrate value, sometimes it mis-reports as a much larger bitrate value but it seems to be correct.
IF !INCOMING_BITRATE_FFPROBE!   GTR !INCOMING_BITRATE! (
	set /A "INCOMING_BITRATE=!INCOMING_BITRATE_FFPROBE!"
	ECHO !DATE! !TIME! 
)
IF !INCOMING_BITRATE_MEDIAINFO! GTR !INCOMING_BITRATE! (set /A "INCOMING_BITRATE=!INCOMING_BITRATE_MEDIAINFO!")
IF !INCOMING_BITRATE_QSF_LOG!   GTR !INCOMING_BITRATE! (set /A "INCOMING_BITRATE=!INCOMING_BITRATE_QSF_LOG!")
IF !INCOMING_BITRATE! EQU 0 (
	REM Jolly Bother and Dash it all, no valid bitrate found, we need to set an artifical incoming bitrate. Choose 4Mb/s for AVC
	set /A "INCOMING_BITRATE=4000000"
)
REM $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
REM DIR /4 "!scratch_file_qsf!"  
REM ECHO DIR /4 "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
REM DIR /4 "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
REM ECHO "!mediainfoexe!" --full "!scratch_file_qsf!" to "%~f1.QSF.mediainfo.txt" 
REM ECHO "!mediainfoexe!" --full "!scratch_file_qsf!" to "%~f1.QSF.mediainfo.txt" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --full "!scratch_file_qsf!" > "%~f1.QSF.mediainfo.txt" 
REM ECHO "!mediainfoexe!" --full "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --full "!scratch_file_qsf!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! output QSF file: Q_Video Codec: "!Q_V_Codec_legacy!" Q_ScanType: "!Q_V_ScanType!" Q_ScanOrder: "!Q_V_ScanOrder!" !Q_V_Width!x!Q_V_Height! dar=!Q_V_DisplayAspectRatio_String! sar=!Q_V_PixelAspectRatio! Q_Audio Codec: "!Q_A_Codec_legacy!" Q_Audio_Delay_ms: !Q_A_Audio_Delay_ms! Q_Audio_Delay_ms_legacy: !Q_A_Video_Delay_ms_legacy! 
ECHO !DATE! !TIME! output QSF file: Q_Video Codec: "!Q_V_Codec_legacy!" Q_ScanType: "!Q_V_ScanType!" Q_ScanOrder: "!Q_V_ScanOrder!" !Q_V_Width!x!Q_V_Height! dar=!Q_V_DisplayAspectRatio_String! sar=!Q_V_PixelAspectRatio! Q_Audio Codec: "!Q_A_Codec_legacy!" Q_Audio_Delay_ms: !Q_A_Audio_Delay_ms! Q_Audio_Delay_ms_legacy: !Q_A_Video_Delay_ms_legacy! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! End QSF of "%~f1" 
ECHO !DATE! !TIME! End QSF of "%~f1" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
REM
IF /I NOT "!V_ScanType!" == "!Q_V_ScanType!" (
	ECHO "ERROR - incoming V_ScanType NOT EQUAL Q_V_ScanType"
	ECHO "V_ScanType=!V_ScanType!"
	ECHO "V_ScanOrder=!V_ScanOrder!"
	ECHO "Q_V_ScanType=!Q_V_ScanType!"
	ECHO "Q_V_ScanOrder=!Q_V_ScanOrder!"
	ECHO "ERROR - incoming V_ScanType NOT EQUAL Q_V_ScanType" >> "!vrdlog!" 2>&1
	ECHO "V_ScanType=!V_ScanType!" >> "!vrdlog!" 2>&1
	ECHO "V_ScanOrder=!V_ScanOrder!" >> "!vrdlog!" 2>&1
	ECHO "Q_V_ScanType=!Q_V_ScanType!" >> "!vrdlog!" 2>&1
	ECHO "Q_V_ScanOrder=!Q_V_ScanOrder!" >> "!vrdlog!" 2>&1
	ECHO file="%~f1"
	ECHO QSF_file="!scratch_file_qsf!"
	%xPAUSE%
	exit
)
IF /I NOT "!V_ScanOrder!" == "!Q_V_ScanOrder!" (
	ECHO "ERROR - incoming V_ScanOrder NOT EQUAL Q_V_ScanOrder"
	ECHO "V_ScanType=!V_ScanType!"
	ECHO "V_ScanOrder=!V_ScanOrder!"
	ECHO "Q_V_ScanType=!Q_V_ScanType!"
	ECHO "Q_V_ScanOrder=!Q_V_ScanOrder!"
	ECHO "ERROR - incoming V_ScanOrder NOT EQUAL Q_V_ScanOrder" >> "!vrdlog!" 2>&1
	ECHO "V_ScanType=!V_ScanType!" >> "!vrdlog!" 2>&1
	ECHO "V_ScanOrder=!V_ScanOrder!" >> "!vrdlog!" 2>&1
	ECHO "Q_V_ScanType=!Q_V_ScanType!" >> "!vrdlog!" 2>&1
	ECHO "Q_V_ScanOrder=!Q_V_ScanOrder!" >> "!vrdlog!" 2>&1
	ECHO file="%~f1"
	ECHO QSF_file="!scratch_file_qsf!"
	%xPAUSE%
	exit
)
REM
REM ECHO !DATE! !TIME! "!mediainfoexe!" --full "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --full "!scratch_file_qsf!" >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME!
REM
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Start Conversion of "!scratch_file_qsf!" into destination
ECHO !DATE! !TIME! Start Conversion of "!scratch_file_qsf!" into destination >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! input QSF file: Q_Video Codec: "!Q_V_Codec_legacy!" Q_ScanType: "!Q_V_ScanType!" Q_ScanOrder: "!Q_V_ScanOrder!" !Q_V_Width!x!Q_V_Height! dar=!Q_V_DisplayAspectRatio_String! sar=!Q_V_PixelAspectRatio! Q_Audio Codec: "!Q_A_Codec_legacy!" Q_Audio_Delay_ms: !Q_A_Audio_Delay_ms! Q_Audio_Delay_ms_legacy: !Q_A_Video_Delay_ms_legacy! 
ECHO !DATE! !TIME! input QSF file: Q_Video Codec: "!Q_V_Codec_legacy!" Q_ScanType: "!Q_V_ScanType!" Q_ScanOrder: "!Q_V_ScanOrder!" !Q_V_Width!x!Q_V_Height! dar=!Q_V_DisplayAspectRatio_String! sar=!Q_V_PixelAspectRatio! Q_Audio Codec: "!Q_A_Codec_legacy!" Q_Audio_Delay_ms: !Q_A_Audio_Delay_ms! Q_Audio_Delay_ms_legacy: !Q_A_Video_Delay_ms_legacy! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
REM Lets do the Conversion ...
REM
set destination_file=!destination_mp4_Folder!%~n1.mp4
ECHO DEL /F "!destination_file!" >> "!vrdlog!" 2>&1
DEL /F "!destination_file!" >> "!vrdlog!" 2>&1
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
:do_ffmpeg_conversion
REM
REM do it via ffmpeg
REM
REM +++++++++++++++++++++++++
REM Calculate the target minimum_bitrate, target_bitrate, maximum_bitrate, buffer size : all from the QSF file settings.
REM Note that the only reliable variable obtained from he QSF file is Q_V_BitRate
REM
IF /I "!Q_V_Codec_legacy!" == "AVC" (
	REM CALCULATE H.264 TARGET BITRATES FROM THE INCOMING BITRATE
	set /a "X_bitrate_05percent=!INCOMING_BITRATE! / 20"
	set /a "X_bitrate_10percent=!INCOMING_BITRATE! / 10"
	set /a "X_bitrate_20percent=!INCOMING_BITRATE! / 5"
	set /a "X_bitrate_50percent=!INCOMING_BITRATE! / 2"
	REM ffmpeg nvenc typically seems to undershoot the target bitrate, so bump it up.
	REM set /a "FF_V_Target_BitRate=!INCOMING_BITRATE! + !X_bitrate_20percent! + !X_bitrate_10percent!"
	REM set /a "FF_V_Target_BitRate=!INCOMING_BITRATE! + !X_bitrate_10percent!"
	set /a "FF_V_Target_BitRate=!INCOMING_BITRATE! + !X_bitrate_05percent!"
	set /a "XT_bitrate_05percent=!FF_V_Target_BitRate! / 20"
	set /a "XT_bitrate_10percent=!FF_V_Target_BitRate! / 10"
	set /a "XT_bitrate_20percent=!FF_V_Target_BitRate! / 5"
	set /a "XT_bitrate_50percent=!FF_V_Target_BitRate! / 2"
	set /a "FF_V_Target_Minimum_BitRate=!XT_bitrate_20percent!"
	set /a "FF_V_Target_Maximum_BitRate=!FF_V_Target_BitRate! * 2"
	set /a "FF_V_Target_BufSize=!FF_V_Target_BitRate! * 2"
	ECHO !DATE! !TIME! Bitrates are calculated from Compared incoming AVC bitrate. "Q_V_BitRate=!Q_V_BitRate!" vs "Q_V_BitRate_FF=!Q_V_BitRate_FF!" vs "Q_ACTUAL_QSF_LOG_BITRATE=!Q_ACTUAL_QSF_LOG_BITRATE!"
	ECHO !DATE! !TIME! Bitrates are calculated from Compared incoming AVC bitrate. "Q_V_BitRate=!Q_V_BitRate!" vs "Q_V_BitRate_FF=!Q_V_BitRate_FF!" vs "Q_ACTUAL_QSF_LOG_BITRATE=!Q_ACTUAL_QSF_LOG_BITRATE!" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Compared INCOMING_BITRATE=!INCOMING_BITRATE! = incoming AVC bitrate
	ECHO !DATE! !TIME! Compared INCOMING_BITRATE=!INCOMING_BITRATE! = incoming AVC bitrate >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! X_bitrate_05percent=!X_bitrate_05percent!
	ECHO !DATE! !TIME! X_bitrate_05percent=!X_bitrate_05percent! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! X_bitrate_10percent=!X_bitrate_10percent!
	ECHO !DATE! !TIME! X_bitrate_10percent=!X_bitrate_10percent! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! X_bitrate_20percent=!X_bitrate_20percent!
	ECHO !DATE! !TIME! X_bitrate_20percent=!X_bitrate_20percent! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! X_bitrate_50percent=!X_bitrate_50percent!
	ECHO !DATE! !TIME! X_bitrate_50percent=!X_bitrate_50percent! >> "!vrdlog!" 2>&1
) ELSE (
	REM is MPEG2 input, so GUESS at reasonable H.264 TARGET BITRATE
	set /a "FF_V_Target_BitRate=2000000"
	set /a "FF_V_Target_Minimum_BitRate=100000"
	set /a "FF_V_Target_Maximum_BitRate=!FF_V_Target_BitRate! * 2"
	set /a "FF_V_Target_BufSize=!FF_V_Target_BitRate! * 2"
	ECHO !DATE! !TIME! Bitrates are fixed non-calculated as OK for mpeg2 transcode
	ECHO !DATE! !TIME! Bitrates are fixed non-calculated as OK for mpeg2 transcode >> "!vrdlog!" 2>&1
)
ECHO !DATE! !TIME! FF_V_Target_BitRate=!FF_V_Target_BitRate!
ECHO !DATE! !TIME! FF_V_Target_BitRate=!FF_V_Target_BitRate! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! FF_V_Target_Minimum_BitRate=!FF_V_Target_Minimum_BitRate!
ECHO !DATE! !TIME! FF_V_Target_Minimum_BitRate=!FF_V_Target_Minimum_BitRate! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! FF_V_Target_Maximum_BitRate=!FF_V_Target_Maximum_BitRate!
ECHO !DATE! !TIME! FF_V_Target_Maximum_BitRate=!FF_V_Target_Maximum_BitRate! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! FF_V_Target_BufSize=!FF_V_Target_BufSize!
ECHO !DATE! !TIME! FF_V_Target_BufSize=!FF_V_Target_BufSize! >> "!vrdlog!" 2>&1
REM +++++++++++++++++++++++++
:do_loudnorm_detection
ECHO !DATE! !TIME! ***************************** start Find Audio Loudness *****************************
ECHO !DATE! !TIME! ***************************** start Find Audio Loudness ***************************** >> "%vrdlog%" 2>&1
REM
set "loudnorm_filter="
set "AUDIO_process="
REM +++++++++++++++++++++++++
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! FOR NOW - DO NO AUDIO FILTERING, on the basis that ads are now VERY loud and their presence interferes with the audio levelling detection.
ECHO !DATE! !TIME! FOR NOW - DO NO AUDIO FILTERING, on the basis that ads are now VERY loud and their presence interferes with the audio levelling detection. >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
goto :after_loudnorm_detection
REM +++++++++++++++++++++++++
REM
set jsonfile=!scratch_Folder!%~n1.loudnorm_scan.json
SET loudnorm_I=-16
SET loudnorm_TP=0.0
SET loudnorm_LRA=11
ECHO !DATE! !TIME! "!ffmpegexex64!"  -nostats -nostdin -y -hide_banner -i "!scratch_file_qsf!" -threads 0 -vn -af loudnorm=I=%loudnorm_I%:TP=%loudnorm_TP%:LRA=%loudnorm_LRA%:print_format=json -f null -
ECHO !DATE! !TIME! "!ffmpegexex64!"  -nostats -nostdin -y -hide_banner -i "!scratch_file_qsf!" -threads 0 -vn -af loudnorm=I=%loudnorm_I%:TP=%loudnorm_TP%:LRA=%loudnorm_LRA%:print_format=json -f null - >> "%vrdlog%" 2>&1
"!ffmpegexex64!"  -nostats -nostdin -y -hide_banner -i "!scratch_file_qsf!" -threads 0 -vn -af loudnorm=I=%loudnorm_I%:TP=%loudnorm_TP%:LRA=%loudnorm_LRA%:print_format=json -f null - 2> "%jsonFile%"  
SET EL=!ERRORLEVEL!
IF /I "!EL!" NEQ "0" (
   ECHO !DATE! !TIME! *********  loudnorm scan Error !EL! was found 
   ECHO !DATE! !TIME! *********  loudnorm scan Error !EL! was found >> "%vrdlog%" 2>&1
   ECHO !DATE! !TIME! *********  ABORTING ...
   ECHO !DATE! !TIME! *********  ABORTING ... >> "%vrdlog%" 2>&1
   %xpause%
   EXIT !EL!
)
ECHO TYPE "%jsonFile%"
ECHO TYPE "%jsonFile%" >> "%vrdlog%" 2>&1
TYPE "%jsonFile%"
REM all the trickery below is simply to remove quotes and tabs and spaces from the json single-level response
set "loudnorm_input_i="
set "loudnorm_input_tp="
set "loudnorm_input_lra="
set "loudnorm_input_thresh="
set "loudnorm_target_offset="
for /f "tokens=1,2 delims=:, " %%a in (' find ":" ^< "%jsonFile%" ') do (
   set "var="
   for %%c in (%%~a) do (set "var=!var!,%%~c")
   set "var=!var:~1!"
   set "val="
   for %%d in (%%~b) do (set "val=!val!,%%~d")
   set "val=!val:~1!"
   ECHO !DATE! !TIME! .!var!.=.!val!.
   ECHO !DATE! !TIME! .!var!.=.!val!. >> "%vrdlog%" 2>&1
   IF /I "!var!" == "input_i"         set "!var!=!val!"
   IF /I "!var!" == "input_tp"        set "!var!=!val!"
   IF /I "!var!" == "input_lra"       set "!var!=!val!"
   IF /I "!var!" == "input_thresh"    set "!var!=!val!"
   IF /I "!var!" == "target_offset"   set "!var!=!val!"
)
set "loudnorm_input_i=%input_i%" >> "%vrdlog%" 2>&1
set "loudnorm_input_tp=%input_tp%" >> "%vrdlog%" 2>&1
set "loudnorm_input_lra=%input_lra%" >> "%vrdlog%" 2>&1
set "loudnorm_input_thresh=%input_thresh%" >> "%vrdlog%" 2>&1
set "loudnorm_target_offset=%target_offset%" >> "%vrdlog%" 2>&1
REM check for bad loudnorm values ... if baddies found, use dynaudnorm instead
set AUDIO_process=loudnorm
IF /I "%loudnorm_input_i%" == "inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_i%" == "-inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_tp%" == "inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_tp%" == "-inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_lra%" == "inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_lra%" == "-inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_thresh%" == "inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_input_thresh%" == "-inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_target_offset%" == "inf" set AUDIO_process=dynaudnorm
IF /I "%loudnorm_target_offset%" == "-inf" set AUDIO_process=dynaudnorm
REM
REM later, in a second encoding pass we MUST down-convert from 192k (loadnorm upsamples it to 192k which is way way too high ... use  -ar 48k or -ar 48000
REM
set AUDIO_process
set AUDIO_process >> "%vrdlog%" 2>&1
IF /I "%AUDIO_process%" == "loudnorm" (
   ECHO !DATE! !TIME! "Proceeding with normal LOUDNORM audio normalisation ..."
   ECHO !DATE! !TIME! "Proceeding with normal LOUDNORM audio normalisation ..."  >> "%vrdlog%" 2>&1
   set loudnorm_filter=-af "loudnorm=I=%loudnorm_I%:TP=%loudnorm_TP%:LRA=%loudnorm_LRA%:measured_I=%loudnorm_input_i%:measured_LRA=%loudnorm_input_lra%:measured_TP=%loudnorm_input_tp%:measured_thresh=%loudnorm_input_thresh%:offset=%loudnorm_target_offset%:linear=true:print_format=summary"
   ECHO !DATE! !TIME! "loudnorm_filter=%loudnorm_filter%" >> "%vrdlog%" 2>&1
) ELSE (
   ECHO !DATE! !TIME! "********* ERROR VALUES DETECTED FROM LOUDNORM - Doing UNUSUAL dynaudnorm audio normalisation instead ..."
   ECHO !DATE! !TIME! "********* ERROR VALUES DETECTED FROM LOUDNORM - Doing UNUSUAL dynaudnorm audio normalisation instead ..." >> "%vrdlog%" 2>&1
   set loudnorm_filter=-af "dynaudnorm"
   ECHO !DATE! !TIME! "loudnorm_filter=%loudnorm_filter% (Should be dynaudnorm because loudnorm scan returned bad values)"
   ECHO !DATE! !TIME! "loudnorm_filter=%loudnorm_filter% (Should be dynaudnorm because loudnorm scan returned bad values)" >> "%vrdlog%" 2>&1
)
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
set loudnorm_
set loudnorm_ >> "%vrdlog%" 2>&1
REM
:after_loudnorm_detection
REM
REM +++++++++++++++++++++++++
set "V_cut_start="
set "V_cut_duration="
REM set V_cut_start=-ss "00:35:00"
REM set V_cut_duration=-t "00:15:00"
REM +++++++++++++++++++++++++
IF /I "%COMPUTERNAME%" == "3900X" (
	set "RTX2060super_extra_flags=-spatial-aq 1 -temporal-aq 1 -refs 3"
) ELSE (
	set "RTX2060super_extra_flags="
)
REM +++++++++++++++++++++++++
set AO_=!loudnorm_filter! -c:a libfdk_aac -cutoff 20000 -ab 256k -ar 48000
REM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ECHO !DATE! !TIME! "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
ECHO !DATE! !TIME! "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! NOTE: After testing, it has been found that ffprobe can mis-report bitrates in the QSF'd file by about double.
ECHO !DATE! !TIME!       Although mediainfo and the "QSF log" values are reasonably close, testing shows ffprobe gets it more "right" when encoding.
ECHO !DATE! !TIME!       Although hopefully correct, this can result in a much lower transcoded filesizes than the originals.
ECHO !DATE! !TIME!       For now, accept what we PROPOSE on whether to "Up" the CQ from 0 to 24. >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! NOTE: After testing, it has been found that ffprobe can mis-report bitrates in the QSF'd file by about double. >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!       Although mediainfo and the "QSF log" values are reasonably close, testing shows ffprobe gets it more "right" when encoding. >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!       Although hopefully correct, this can result in a much lower transcoded filesizes than the originals. >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!       For now, accept what we PROPOSE on whether to "Up" the CQ from 0 to 24. >> "%vrdlog%" 2>&1
set "x_cq0=-cq:v 0"
set "x_cq24=-cq:v 24 -qmin 16 -qmax 48"
set "x_cq_options=!x_cq0!"
set "PROPOSED_x_cq_options=!x_cq_options!"
ECHO !DATE! !TIME! "Initial Default x_cq_options=!x_cq_options!"
ECHO !DATE! !TIME! "Initial Default x_cq_options=!x_cq_options!" >> "%vrdlog%" 2>&1
REM
REM FOR AVC INPUT FILES ONLY, calculate the CQ to use (default to CQ0)
REM
REM There are special cases where Mediainfo detects a lower bitrate than FFPROBE
REM and MediaInfo is likely right ... however FFPROBE is what we want it to be.
REM When this happens, if we just leave the bitrate CQ as-is then ffmpeg just undershoots 
REM even though we specify the higher bitrate of FFPROBE.
REM So ...
REM If we detect such a case, change to CQ24 instead of CQ0 and leave the 
REM specified bitrate unchanged ... which "should" fix it up.
REM
IF /I "!Q_V_Codec_legacy!" == "AVC" (
	ECHO !DATE! !TIME! "????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????" >> "%vrdlog%" 2>&1
	ECHO Example table of values and actions >> "%vrdlog%" 2>&1
	ECHO	MI		FF		INCOMING	ACTION >> "%vrdlog%" 2>&1
	ECHO	0		0		5Mb			set to CQ 0 >> "%vrdlog%" 2>&1
	ECHO	0		1.5Mb	1.5Mb		set to CQ 24 >> "%vrdlog%" 2>&1
	ECHO	0		4Mb		4Mb			set to CQ 0 >> "%vrdlog%" 2>&1
	ECHO	1.5Mb	0		1.5Mb		set to CQ 24 >> "%vrdlog%" 2>&1
	ECHO	1.5Mb 	1.5Mb	1.5Mb		set to CQ 24 >> "%vrdlog%" 2>&1
	ECHO	1.5Mb	4Mb		4Mb			set to CQ 24 *** this one >> "%vrdlog%" 2>&1
	ECHO	4Mb		0		4Mb			set to CQ 0 >> "%vrdlog%" 2>&1
	ECHO	4Mb		1.5Mb	4Mb			set to CQ 0 >> "%vrdlog%" 2>&1
	ECHO	4Mb		5Mb		5Mb			set to CQ 0 >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME! "????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????" >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME! "Calculating whether to Bump CQ from 0 to 24 ..."
	ECHO !DATE! !TIME! "Calculating whether to Bump CQ from 0 to 24 ..." >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME! "INCOMING_BITRATE_MEDIAINFO=!INCOMING_BITRATE_MEDIAINFO!"
	ECHO !DATE! !TIME! "INCOMING_BITRATE_MEDIAINFO=!INCOMING_BITRATE_MEDIAINFO!" >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME! "INCOMING_BITRATE_FFPROBE=!INCOMING_BITRATE_FFPROBE!"
	ECHO !DATE! !TIME! "INCOMING_BITRATE_FFPROBE=!INCOMING_BITRATE_FFPROBE!" >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME! "INCOMING_BITRATE_QSF_LOG=!INCOMING_BITRATE_QSF_LOG!"
	ECHO !DATE! !TIME! "INCOMING_BITRATE_QSF_LOG=!INCOMING_BITRATE_QSF_LOG!" >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME! "so (the max of them) INCOMING_BITRATE=!INCOMING_BITRATE!"
	ECHO !DATE! !TIME! "so (the max of them) INCOMING_BITRATE=!INCOMING_BITRATE!" >> "%vrdlog%" 2>&1
	REM Nested IF statements means ANDing them
	If !INCOMING_BITRATE! LSS 2200000 (
		REM low bitrate, do not touch the bitrate itself, instead bump to CQ24
		ECHO !DATE! !TIME! "yes to Low INCOMING_BITRATE !INCOMING_BITRATE! LSS 2200000"
		ECHO !DATE! !TIME! "yes to Low INCOMING_BITRATE !INCOMING_BITRATE! LSS 2200000" >> "%vrdlog%" 2>&1
		set "PROPOSED_x_cq_options=!x_cq24!"
		ECHO !DATE! !TIME! "PROPOSED_x_cq_options=!PROPOSED_x_cq_options!"
		ECHO !DATE! !TIME! "PROPOSED_x_cq_optionsx_cq_options=!PROPOSED_x_cq_options!" >> "%vrdlog%" 2>&1
	)
	If !INCOMING_BITRATE_MEDIAINFO! GTR 0 (
		ECHO !DATE! !TIME! "yes to INCOMING_BITRATE_MEDIAINFO !INCOMING_BITRATE_MEDIAINFO! GTR 0"
		ECHO !DATE! !TIME! "yes to INCOMING_BITRATE_MEDIAINFO !INCOMING_BITRATE_MEDIAINFO! GTR 0" >> "%vrdlog%" 2>&1
		IF !INCOMING_BITRATE_MEDIAINFO! LSS 2200000 (
			ECHO !DATE! !TIME! "yes to AND INCOMING_BITRATE_MEDIAINFO !INCOMING_BITRATE_MEDIAINFO! LSS 2200000"
			ECHO !DATE! !TIME! "yes to AND INCOMING_BITRATE_MEDIAINFO !INCOMING_BITRATE_MEDIAINFO! LSS 2200000" >> "%vrdlog%" 2>&1
			IF !INCOMING_BITRATE_FFPROBE! LSS 3400000 (
				ECHO !DATE! !TIME! "yes to AND INCOMING_BITRATE_FFPROBE !INCOMING_BITRATE_FFPROBE! LSS 3400000"
				ECHO !DATE! !TIME! "yes to AND INCOMING_BITRATE_FFPROBE !INCOMING_BITRATE_FFPROBE! LSS 3400000" >> "%vrdlog%" 2>&1
				set "PROPOSED_x_cq_options=!x_cq24!"
				ECHO !DATE! !TIME! "PROPOSED_x_cq_options=!PROPOSED_x_cq_options!"
				ECHO !DATE! !TIME! "PROPOSED_x_cq_options=!PROPOSED_x_cq_options!" >> "%vrdlog%" 2>&1
			)
		)
	)
	set "x_cq_options=!PROPOSED_x_cq_options!"
)
:after_CQ_checking
ECHO !DATE! !TIME! "????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! "For file !scratch_file_qsf!"
ECHO !DATE! !TIME! "For file !scratch_file_qsf!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! "Final x_cq_options=!x_cq_options!  for incoming !Q_V_Width!x!Q_V_Height! !Q_V_Codec_legacy!"
ECHO !DATE! !TIME! "Final x_cq_options=!x_cq_options!  for incoming !Q_V_Width!x!Q_V_Height! !Q_V_Codec_legacy!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! "????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
ECHO !DATE! !TIME! "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" >> "%vrdlog%" 2>&1
REM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
REM ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
REM Check for Footy, after any final fiddling with bitrates and CQ.
REM If is footy, deinterlace to 50FPS 50p, doubling the framerate, rather than just 25p
REM so that we maintain the "motion fluidity" of 50i into 50p. It's better than nothing.
REM Set the yadif MODE deinterlacing parameter if we are processing FOTTY them go to 50p
REM which plays on Chromecast Ultra and on our two Samsung 4K TVs
REM		yadif:mode:parity:deint
REM		yadif parity 0=TFF 1=BFF 0=AUTO
REM		yadif:0:0:0 = Output one frame for each frame, incoming is TFF, Deinterlace all frames
REM		yadif:1:0:0 = Output one frame for each field, incoming is TFF, Deinterlace all frames (doubles framerate)
set "yadif_mode=0"
REM default to TFF
set "yadif_tff_bff=0"
set "dg_tff=True"
IF /I "!V_ScanOrder!" == "BFF" (
	REM must be flagged as explicitly BFF
	set "yadif_tff_bff=1"
	set "dg_tff=False"
)
set "Footy_yadif_mode=0"
REM deprecated: do not fiddle with x_cq_options in footy checks processing
set "PROPOSED_x_cq_options=!x_cq_options!"
set "Footy_found=FALSE"
IF /I NOT "!V_ScanType!" == "Progressive" (
	set "Footy_found=FALSE"
	echo.!DATE! !TIME! Checking for a footy file, by looking at the filename '%~n1'
	echo.!DATE! !TIME! Checking for a footy file, by looking at the filename '%~n1' >> "!vrdlog!" 2>&1
	echo.'%~n1'|findstr /i /c:"AFL" >> "!vrdlog!" 2>&1
	IF !errorlevel! EQU 0 (
		ECHO !DATE! !TIME! Footy File: string 'AFL' found in filename '%~n1'
		ECHO !DATE! !TIME! Footy File: string 'AFL' found in filename '%~n1' >> "!vrdlog!" 2>&1
		set "Footy_found=TRUE"
	)
	echo.'%~n1'|findstr /i /c:"SANFL" >> "!vrdlog!" 2>&1
	IF !errorlevel! EQU 0 (
		ECHO !DATE! !TIME! Footy File: string 'SANFL' found in filename '%~n1'
		ECHO !DATE! !TIME! Footy File: string 'SANFL' found in filename '%~n1' >> "!vrdlog!" 2>&1
		set "Footy_found=TRUE"
	)
	echo.'%~n1'|findstr /i /c:"Adelaide Crows" >> "!vrdlog!" 2>&1
	IF !errorlevel! EQU 0 (
		ECHO !DATE! !TIME! Footy File: string 'Adelaide Crows' found in filename '%~n1'
		ECHO !DATE! !TIME! Footy File: string 'Adelaide Crows' found in filename '%~n1' >> "!vrdlog!" 2>&1
		set "Footy_found=TRUE"
	)
	IF /I "!Footy_found!" == "TRUE" (
		ECHO !DATE! !TIME! Footy File: FOOTY FOUND in "%~n1", deinterlace to 50 fps and up the target bitrates by 75 percent
		ECHO !DATE! !TIME! Footy File: FOOTY FOUND in "%~n1", deinterlace to 50 fps and up the target bitrates by 75 percent >> "!vrdlog!" 2>&1
		ECHO !DATE! !TIME! Footy File: set Footy_yadif_mode parameter= 1 = one frame per FIELD = deinterlace and double the framerate from 25i to 50p
		ECHO !DATE! !TIME! Footy File: set Footy_yadif_mode parameter= 1 = one frame per FIELD = deinterlace and double the framerate from 25i to 50p >> "!vrdlog!" 2>&1
		set "Footy_yadif_mode=1"
		set /a "Footy_bitrate_05percent=!FF_V_Target_BitRate! / 20"
		set /a "Footy_bitrate_10percent=!FF_V_Target_BitRate! / 10"
		set /a "Footy_bitrate_20percent=!FF_V_Target_BitRate! / 5"
		set /a "Footy_bitrate_50percent=!FF_V_Target_BitRate! / 2"
		ECHO !DATE! !TIME! "Incoming FF_V_Target_BitRate=!FF_V_Target_BitRate!"
		ECHO !DATE! !TIME! "Footy_bitrate_05percent=!Footy_bitrate_05percent!"
		ECHO !DATE! !TIME! "Footy_bitrate_10percent=!Footy_bitrate_10percent!"
		ECHO !DATE! !TIME! "Footy_bitrate_20percent=!Footy_bitrate_20percent!"
		ECHO !DATE! !TIME! "Footy_bitrate_50percent=!Footy_bitrate_50percent!"
		ECHO !DATE! !TIME! "Summing FF_V_Target_BitRate=!FF_V_Target_BitRate! + !Footy_bitrate_50percent! + !Footy_bitrate_20percent! + !Footy_bitrate_10percent!"
		set /a "Footy_FF_V_Target_BitRate=!FF_V_Target_BitRate! + !Footy_bitrate_50percent! + !Footy_bitrate_20percent! + !Footy_bitrate_05percent!"
		set /a "Footy_FF_V_Target_Minimum_BitRate=!Footy_bitrate_20percent!"
		set /a "Footy_FF_V_Target_Maximum_BitRate=!FF_V_Target_BitRate! * 2"
		set /a "Footy_FF_V_Target_BufSize=!FF_V_Target_BitRate! * 2"
		ECHO !DATE! !TIME! Footy File: Upped Footy_FF_V_Target_BitRate=!Footy_FF_V_Target_BitRate!
		ECHO !DATE! !TIME! Footy File: Upped Footy_FF_V_Target_BitRate=!Footy_FF_V_Target_BitRate! >> "!vrdlog!" 2>&1
		ECHO !DATE! !TIME! Footy File: Footy_FF_V_Target_Minimum_BitRate=!Footy_FF_V_Target_Minimum_BitRate!
		ECHO !DATE! !TIME! Footy File: Footy_FF_V_Target_Minimum_BitRate=!Footy_FF_V_Target_Minimum_BitRate! >> "!vrdlog!" 2>&1
		ECHO !DATE! !TIME! Footy File: Footy_FF_V_Target_Maximum_BitRate=!Footy_FF_V_Target_Maximum_BitRate!
		ECHO !DATE! !TIME! Footy File: Footy_FF_V_Target_Maximum_BitRate=!Footy_FF_V_Target_Maximum_BitRate! >> "!vrdlog!" 2>&1
		ECHO !DATE! !TIME! Footy File: Footy_FF_V_Target_BufSize=!Footy_FF_V_Target_BufSize!
		ECHO !DATE! !TIME! Footy File: Footy_FF_V_Target_BufSize=!Footy_FF_V_Target_BufSize! >> "!vrdlog!" 2>&1
		REM set "PROPOSED_x_cq_options=!x_cq24!"
		REM ECHO !DATE! !TIME! Footy File: PROPOSED_x_cq_options=!PROPOSED_x_cq_options! >> "!vrdlog!" 2>&1
	) ELSE (
		ECHO !DATE! !TIME! Not Footy File: footy NOT found in "%~f1",
		ECHO !DATE! !TIME! Not Footy File: footy NOT found in "%~f1", >> "!vrdlog!" 2>&1
		ECHO !DATE! !TIME! Not Footy File: set Footy_yadif_mode parameter = 0 = one frame per FRAME - deinterlace and maintain the framerate 25i at 25p
		ECHO !DATE! !TIME! Not Footy File: set Footy_yadif_mode parameter = 0 = one frame per FRAME - deinterlace and maintain the framerate 25i at 25p >> "!vrdlog!" 2>&1
		set "Footy_yadif_mode=0"
		set /a "Footy_FF_V_Target_BitRate=!FF_V_Target_BitRate!"
		set /a "Footy_FF_V_Target_Minimum_BitRate=!FF_V_Target_Minimum_BitRate!"
		set /a "Footy_FF_V_Target_Maximum_BitRate=!FF_V_Target_Maximum_BitRate!"
		set /a "Footy_FF_V_Target_BufSize=!FF_V_Target_BufSize!"
		REM set "PROPOSED_x_cq_options=!x_cq_options!"
		REM ECHO !DATE! !TIME! Footy File: not a Foory file: PROPOSED_x_cq_options=!PROPOSED_x_cq_options! >> "!vrdlog!" 2>&1
	)
	REM set "x_cq_options=!PROPOSED_x_cq_options!"
)
REM ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! After Footy processing, x_cq_options=!x_cq_options!
REM ECHO !DATE! !TIME! After Footy processing, x_cq_options=!x_cq_options! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! "????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????" >> "%vrdlog%" 2>&1
REM +++++++++++++++++++++++++
REM
REM set destination_file_FF=!destination_mp4_Folder!%~n1.mp4.VRDTVS.z-from_qsf_via_ffmpeg_copy.mp4
REM set destination_file_FF=!destination_mp4_Folder!%~n1.mp4.cq_!x_cq!.mp4
REM
set _VPY_file=!scratch_Folder!%~n1.VPY
set _DGI_file=!scratch_Folder!%~n1.DGI
set _DGI_autolog=!scratch_Folder!%~n1.log
IF /I "!Footy_found!" == "TRUE" (
	REM set for double framerate deinterlace
	set dg_deinterlace=2
) ELSE (
	REM set for normal single framerate deinterlace
	set dg_deinterlace=1
)
IF /I "!V_ScanType!" == "Progressive" (
	REM Progressive video, no deinterlacing necessary
	set dg_deinterlace=0
	IF /I "!Q_V_Codec_legacy!" == "AVC" (
		REM is progressive h.264 - no deinterlace, no sharpen, copy video stream only
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** Progressive AVC input - setting ff_cmd accordingly ... copy video stream, convert audio stream
		ECHO !DATE! !TIME! "***FF*** Progressive AVC input - setting ff_cmd accordingly ... copy video stream, convert audio stream " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		REM no -cq:v options or bitrates apply to -c:v copy
		REM Handle an ffmpeg.exe with a removed Opencl
		REM set "VO_sharpen=" >> "%vrdlog%" 2>&1
		REM set ff_cmd="!ffmpegexex64_max!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -i "!scratch_file_qsf!" -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! -c:v copy !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		set ff_cmd="!ffmpegexex64!" -hide_banner -v verbose -nostats !V_cut_start! -i "!scratch_file_qsf!" -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! -c:v copy !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
	) ELSE (
		REM is progressive mpeg2 - no deinterlace, yes denoise, sharpen (more for mpeg2 source),  moderate quality
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** Progressive MPEG2 input - setting ff_cmd accordingly ... denoise/sharpen video stream via vapoursynth, convert audio stream "
		ECHO !DATE! !TIME! "***FF*** Progressive MPEG2 input - setting ff_cmd accordingly ... denoise/sharpen video stream via vapoursynth, convert audio stream " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		REM run DGIndex
		ECHO DEL /F "!_DGI_file!" >> "%vrdlog%" 2>&1
		DEL /F "!_DGI_file!" >> "%vrdlog%" 2>&1
		ECHO "%VSdgindexNVexe64%" -i "!scratch_file_qsf!" -h -o "!_DGI_file!" -e >> "%vrdlog%" 2>&1
		ECHO "%VSdgindexNVexe64%" -i "!scratch_file_qsf!" -h -o "!_DGI_file!" -e
		set "start_date_time=!date! !time!"
		"%VSdgindexNVexe64%" -i "!scratch_file_qsf!" -h -o "!_DGI_file!" -e >> "%vrdlog%" 2>&1
		set "end_date_time=!date! !time!"
		powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "VSdgindexNVexe64" >> "!vrdlog!" 2>&1		
		REM ECHO TYPE "!_DGI_file!" >> "%vrdlog%" 2>&1
		REM TYPE "!_DGI_file!" >> "%vrdlog%" 2>&1
		REM ECHO TYPE "!_DGI_file!"
		REM TYPE "!_DGI_file!"
		REM ECHO DIR !scratch_Folder!
		REM DIR !scratch_Folder!
		REM ECHO DIR "!_DGI_autolog!"
		REM DIR "!_DGI_autolog!"
		ECHO TYPE "!_DGI_autolog!" >> "%vrdlog%" 2>&1
		TYPE "!_DGI_autolog!" >> "%vrdlog%" 2>&1
		ECHO TYPE "!_DGI_autolog!"
		TYPE "!_DGI_autolog!"
		ECHO DEL /F "!_DGI_autolog!" >> "%vrdlog%" 2>&1
		DEL /F "!_DGI_autolog!" >> "%vrdlog%" 2>&1
		REM Create the .vpy file with the .DGI as input
		ECHO DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
		DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
		ECHO import vapoursynth as vs		# this allows use of constants eg vs.YUV420P8 >> "!_VPY_file!" 2>&1
		ECHO from vapoursynth import core	# actual vapoursynth core >> "!_VPY_file!" 2>&1
		ECHO #import functools >> "!_VPY_file!" 2>&1
		ECHO #import mvsfunc as mvs			# this relies on the .py residing at the VS folder root level - see run_vsrepo.bat >> "!_VPY_file!" 2>&1
		ECHO #import havsfunc as haf		# this relies on the .py residing at the VS folder root level - see run_vsrepo.bat >> "!_VPY_file!" 2>&1
		ECHO core.std.LoadPlugin^(r'!_vs_root!DGIndex\DGDecodeNV.dll'^) # do it like gonca https://forum.doom9.org/showthread.php?p=1877765#post1877765 >> "!_VPY_file!" 2>&1
		ECHO core.avs.LoadPlugin^(r'!_vs_root!DGIndex\DGDecodeNV.dll'^) # do it like gonca https://forum.doom9.org/showthread.php?p=1877765#post1877765 >> "!_VPY_file!" 2>&1
		ECHO video = core.dgdecodenv.DGSource^(r'!_DGI_file!', deinterlace=!dg_deinterlace!, use_top_field=!dg_tff!, use_pf=False^) >> "!_VPY_file!" 2>&1
		ECHO # DGDecNV changes - >> "!_VPY_file!" 2>&1
		ECHO # 2020.10.21 Added new parameters cstrength and cblend to independently control the chroma denoising. >> "!_VPY_file!" 2>&1
		ECHO # 2020.11.07 Revised DGDenoise parameters. The 'chroma' option is removed. >> "!_VPY_file!" 2>&1
		ECHO #            Now, if 'strength' is set to 0.0 then luma denoising is disabled, >> "!_VPY_file!" 2>&1
		ECHO #            and if cstrength is set to 0.0 then chroma denoising is disabled. >> "!_VPY_file!" 2>&1
		ECHO #            'cstrength' is now defaulted to 0.0, and 'searchw' is defaulted to 9. >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGDenoise^(video, strength=0.15, cstrength=0.15^) # replaced chroma=True >> "!_VPY_file!" 2>&1
		ECHO video = core.avs.DGDenoise^(video, strength=0.06, cstrength=0.06^) # replaced chroma=True >> "!_VPY_file!" 2>&1
		ECHO video = core.avs.DGSharpen^(video, strength=0.3^) >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGSharpen^(video, strength=0.1^) >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGSharpen^(video, strength=0.2^) >> "!_VPY_file!" 2>&1
		ECHO #video = vs.core.text.ClipInfo^(video^) >> "!_VPY_file!" 2>&1
		ECHO video.set_output^(^) >> "!_VPY_file!" 2>&1
		ECHO ---------------------------- 2>&1
		ECHO TYPE "!_VPY_file!" >> "%vrdlog%" 2>&1
		TYPE "!_VPY_file!" >> "%vrdlog%" 2>&1
		ECHO ---------------------------- 2>&1
		ECHO TYPE "!_VPY_file!"
		TYPE "!_VPY_file!"
		ECHO ---------------------------- 2>&1
		REM from mpeg2, always -cq:v 0
		set VO_HQ=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr -cq:v 0 -b:v !FF_V_Target_BitRate! -minrate:v !FF_V_Target_Minimum_BitRate! -maxrate:v !FF_V_Target_Maximum_BitRate! -bufsize !FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
		REM Handle an ffmpeg.exe with a removed Opencl
		REM set VO_sharpen=-filter_complex "hwupload,unsharp_opencl=lx=3:ly=3:la=1.5:cx=3:cy=3:ca=1.5,hwdownload,format=pix_fmts=yuv420p" >> "%vrdlog%" 2>&1
		REM set ff_cmd="!ffmpegexex64_max!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -i "!scratch_file_qsf!" -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_sharpen! !VO_HQ! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		set ff_cmd="!ffmpegexex64!" -hide_banner -v verbose -nostats !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
	)
) ELSE (
	REM Interlaced video, deinterlacing required to play the result on chromecast devices
	REM run DGIndex
	ECHO DEL /F "!_DGI_file!" >> "%vrdlog%" 2>&1
	DEL /F "!_DGI_file!" >> "%vrdlog%" 2>&1
	ECHO "%VSdgindexNVexe64%" -i "!scratch_file_qsf!" -h -o "!_DGI_file!" -e >> "%vrdlog%" 2>&1
	ECHO "%VSdgindexNVexe64%" -i "!scratch_file_qsf!" -h -o "!_DGI_file!" -e
	set "start_date_time=!date! !time!"
	"%VSdgindexNVexe64%" -i "!scratch_file_qsf!" -h -o "!_DGI_file!" -e >> "%vrdlog%" 2>&1
	set "end_date_time=!date! !time!"
	powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!start_date_time!" -end_date_time "!end_date_time!" -prefix_id "VSdgindexNVexe64" >> "!vrdlog!" 2>&1		
	REM ECHO TYPE "!_DGI_file!" >> "%vrdlog%" 2>&1
	REM TYPE "!_DGI_file!" >> "%vrdlog%" 2>&1
	REM ECHO TYPE "!_DGI_file!"
	REM TYPE "!_DGI_file!"
	REM ECHO DIR !scratch_Folder!
	REM DIR !scratch_Folder!
	REM ECHO DIR "!_DGI_autolog!"
	REM DIR "!_DGI_autolog!"
	ECHO TYPE "!_DGI_autolog!" >> "%vrdlog%" 2>&1
	TYPE "!_DGI_autolog!" >> "%vrdlog%" 2>&1
	ECHO TYPE "!_DGI_autolog!"
	TYPE "!_DGI_autolog!"
	ECHO DEL /F "!_DGI_autolog!" >> "%vrdlog%" 2>&1
	DEL /F "!_DGI_autolog!" >> "%vrdlog%" 2>&1
	IF /I "!Q_V_Codec_legacy!" == "AVC" (
		REM is interlaced h.264 - yes deinterlace, yes sharpen (more for mpeg2 source), higher quality
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** Interlaced AVC input - setting ff_cmd accordingly ... denoise/sharpen video stream via vapoursynth, convert audio stream "
		ECHO !DATE! !TIME! "***FF*** Interlaced AVC input - setting ff_cmd accordingly ... denoise/sharpen video stream via vapoursynth, convert audio stream " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		REM Create the .vpy file with the .DGI as input
		ECHO DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
		DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
		ECHO import vapoursynth as vs		# this allows use of constants eg vs.YUV420P8 >> "!_VPY_file!" 2>&1
		ECHO from vapoursynth import core	# actual vapoursynth core >> "!_VPY_file!" 2>&1
		ECHO #import functools >> "!_VPY_file!" 2>&1
		ECHO #import mvsfunc as mvs			# this relies on the .py residing at the VS folder root level - see run_vsrepo.bat >> "!_VPY_file!" 2>&1
		ECHO #import havsfunc as haf		# this relies on the .py residing at the VS folder root level - see run_vsrepo.bat >> "!_VPY_file!" 2>&1
		ECHO core.std.LoadPlugin^(r'!_vs_root!DGIndex\DGDecodeNV.dll'^) # do it like gonca https://forum.doom9.org/showthread.php?p=1877765#post1877765 >> "!_VPY_file!" 2>&1
		ECHO core.avs.LoadPlugin^(r'!_vs_root!DGIndex\DGDecodeNV.dll'^) # do it like gonca https://forum.doom9.org/showthread.php?p=1877765#post1877765 >> "!_VPY_file!" 2>&1
		ECHO video = core.dgdecodenv.DGSource^(r'!_DGI_file!', deinterlace=!dg_deinterlace!, use_top_field=!dg_tff!, use_pf=False^) >> "!_VPY_file!" 2>&1
		ECHO # DGDecNV changes - >> "!_VPY_file!" 2>&1
		ECHO # 2020.10.21 Added new parameters cstrength and cblend to independently control the chroma denoising. >> "!_VPY_file!" 2>&1
		ECHO # 2020.11.07 Revised DGDenoise parameters. The 'chroma' option is removed. >> "!_VPY_file!" 2>&1
		ECHO #            Now, if 'strength' is set to 0.0 then luma denoising is disabled, >> "!_VPY_file!" 2>&1
		ECHO #            and if cstrength is set to 0.0 then chroma denoising is disabled. >> "!_VPY_file!" 2>&1
		ECHO #            'cstrength' is now defaulted to 0.0, and 'searchw' is defaulted to 9. >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGDenoise^(video, strength=0.15, cstrength=0.15^) # replaced chroma=True >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGDenoise^(video, strength=0.06, cstrength=0.06^) # replaced chroma=True >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGSharpen^(video, strength=0.3^) >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGSharpen^(video, strength=0.1^) >> "!_VPY_file!" 2>&1
		ECHO video = core.avs.DGSharpen^(video, strength=0.2^) >> "!_VPY_file!" 2>&1
		ECHO #video = vs.core.text.ClipInfo^(video^) >> "!_VPY_file!" 2>&1
		ECHO video.set_output^(^) >> "!_VPY_file!" 2>&1
		ECHO ---------------------------- 2>&1
		ECHO TYPE "!_VPY_file!" >> "%vrdlog%" 2>&1
		TYPE "!_VPY_file!" >> "%vrdlog%" 2>&1
		ECHO ---------------------------- 2>&1
		ECHO TYPE "!_VPY_file!"
		TYPE "!_VPY_file!"
		ECHO ---------------------------- 2>&1
		REM perhaps -cq:v 24 -qmin 18 -qmax 40
		REM set VO_deint_sharpen=-filter_complex "[0:v]yadif=!yadif_mode!:!yadif_tff_bff!:0,hwupload,unsharp_opencl=lx=3:ly=3:la=0.5:cx=3:cy=3:ca=0.5,hwdownload,format=pix_fmts=yuv420p" >> "%vrdlog%" 2>&1
		REM set VO_HQ=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp !VO_deint_sharpen! -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr !x_cq_options! -b:v !FF_V_Target_BitRate! -minrate:v !FF_V_Target_Minimum_BitRate! -maxrate:v !FF_V_Target_Maximum_BitRate! -bufsize !FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
		REM Handle an ffmpeg.exe with a removed Opencl
		REM set ff_cmd="!ffmpegexex64!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -i "!scratch_file_qsf!" -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		REM
		set VO_HQ_DG=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr !x_cq_options! -b:v !FF_V_Target_BitRate! -minrate:v !FF_V_Target_Minimum_BitRate! -maxrate:v !FF_V_Target_Maximum_BitRate! -bufsize !FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
		REM Handle an ffmpeg.exe with a removed Opencl
		REM set ff_cmd_DG="!VSffmpegexex64_max!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ_DG! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		set ff_cmd_DG="!VSffmpegexex64!" -hide_banner -v verbose -nostats !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ_DG! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		REM we use DG for deinterlacing
		set ff_cmd=!ff_cmd_DG!
		REM #####################################################################################################################
		REM Also setup a FOOTY ffmpeg commandline:
		REM Well, after all the mucking around for setting up for footy, it turns out it makes VERY LITTLE perceptual difference
		REM especially when the source is blocky (lime some footy games are only broadcast at 3.5Mbps which is pitiful.
		REM So, the code remains as an example, but never used.
		REM set Footy_VO_deint_sharpen=-filter_complex "[0:v]yadif=!Footy_yadif_mode!:!yadif_tff_bff!:0,hwupload,unsharp_opencl=lx=3:ly=3:la=0.5:cx=3:cy=3:ca=0.5,hwdownload,format=pix_fmts=yuv420p" >> "%vrdlog%" 2>&1
		REM set Footy_VO_HQ=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp !Footy_VO_deint_sharpen! -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr !x_cq_options! -b:v !Footy_FF_V_Target_BitRate! -minrate:v !Footy_FF_V_Target_Minimum_BitRate! -maxrate:v !Footy_FF_V_Target_Maximum_BitRate! -bufsize !Footy_FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
		REM set Footy_ff_cmd="!ffmpegexex64!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -i "!scratch_file_qsf!" -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !Footy_VO_HQ! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		REM
		IF /I "!Footy_found!" == "TRUE" ( 
			ECHO !DATE! !TIME! "***FF*** "
			ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
			ECHO !DATE! !TIME! "***FF*** Interlaced FOOTY AVC input detected - resetting ff_cmd accordingly ... denoise/sharpen video stream via vapoursynth, with HQ settings, convert audio stream "
			ECHO !DATE! !TIME! "***FF*** Interlaced FOOTY AVC input detected - resetting ff_cmd accordingly ... denoise/sharpen video stream via vapoursynth, with HQ settings, convert audio stream " >> "%vrdlog%" 2>&1
			ECHO !DATE! !TIME! "***FF*** "
			ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
			set Footy_VO_HQ_DG=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr !x_cq_options! -b:v !Footy_FF_V_Target_BitRate! -minrate:v !Footy_FF_V_Target_Minimum_BitRate! -maxrate:v !Footy_FF_V_Target_Maximum_BitRate! -bufsize !Footy_FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
			REM Handle an ffmpeg.exe with a removed Opencl
			REM set Footy_ff_cmd_DG="!VSffmpegexex64_max!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !Footy_VO_HQ_DG! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
			set Footy_ff_cmd_DG="!VSffmpegexex64!" -hide_banner -v verbose -nostats !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !Footy_VO_HQ_DG! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
			set ff_cmd=!Footy_ff_cmd_DG!
		)
		REM #####################################################################################################################
	) ELSE (
		REM is interlaced mpeg2 - yes deinterlace, yes denoise, sharpen (more for mpeg2 source), moderate quality
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** Interlaced MPEG2 input - setting ff_cmd accordingly ... denoise/more-sharpen video stream via vapoursynth, convert audio stream "
		ECHO !DATE! !TIME! "***FF*** Interlaced MPEG2 input - setting ff_cmd accordingly ... denoise/more-sharpen video stream via vapoursynth, convert audio stream " >> "%vrdlog%" 2>&1
		ECHO !DATE! !TIME! "***FF*** "
		ECHO !DATE! !TIME! "***FF*** " >> "%vrdlog%" 2>&1
		REM Create the .vpy file with the .DGI as input
		ECHO DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
		DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
		ECHO import vapoursynth as vs		# this allows use of constants eg vs.YUV420P8 >> "!_VPY_file!" 2>&1
		ECHO from vapoursynth import core	# actual vapoursynth core >> "!_VPY_file!" 2>&1
		ECHO #import functools >> "!_VPY_file!" 2>&1
		ECHO #import mvsfunc as mvs			# this relies on the .py residing at the VS folder root level - see run_vsrepo.bat >> "!_VPY_file!" 2>&1
		ECHO #import havsfunc as haf		# this relies on the .py residing at the VS folder root level - see run_vsrepo.bat >> "!_VPY_file!" 2>&1
		ECHO core.std.LoadPlugin^(r'!_vs_root!DGIndex\DGDecodeNV.dll'^) # do it like gonca https://forum.doom9.org/showthread.php?p=1877765#post1877765 >> "!_VPY_file!" 2>&1
		ECHO core.avs.LoadPlugin^(r'!_vs_root!DGIndex\DGDecodeNV.dll'^) # do it like gonca https://forum.doom9.org/showthread.php?p=1877765#post1877765 >> "!_VPY_file!" 2>&1
		ECHO video = core.dgdecodenv.DGSource^(r'!_DGI_file!', deinterlace=!dg_deinterlace!, use_top_field=!dg_tff!, use_pf=False^) >> "!_VPY_file!" 2>&1
		ECHO # DGDecNV changes - >> "!_VPY_file!" 2>&1
		ECHO # 2020.10.21 Added new parameters cstrength and cblend to independently control the chroma denoising. >> "!_VPY_file!" 2>&1
		ECHO # 2020.11.07 Revised DGDenoise parameters. The 'chroma' option is removed. >> "!_VPY_file!" 2>&1
		ECHO #            Now, if 'strength' is set to 0.0 then luma denoising is disabled, >> "!_VPY_file!" 2>&1
		ECHO #            and if cstrength is set to 0.0 then chroma denoising is disabled. >> "!_VPY_file!" 2>&1
		ECHO #            'cstrength' is now defaulted to 0.0, and 'searchw' is defaulted to 9. >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGDenoise^(video, strength=0.15, cstrength=0.15^) # replaced chroma=True >> "!_VPY_file!" 2>&1
		ECHO video = core.avs.DGDenoise^(video, strength=0.06, cstrength=0.06^) # replaced chroma=True >> "!_VPY_file!" 2>&1
		ECHO video = core.avs.DGSharpen^(video, strength=0.3^) >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGSharpen^(video, strength=0.1^) >> "!_VPY_file!" 2>&1
		ECHO #video = core.avs.DGSharpen^(video, strength=0.2^) >> "!_VPY_file!" 2>&1
		ECHO #video = vs.core.text.ClipInfo^(video^) >> "!_VPY_file!" 2>&1
		ECHO video.set_output^(^) >> "!_VPY_file!" 2>&1
		ECHO ---------------------------- 2>&1
		ECHO TYPE "!_VPY_file!" >> "%vrdlog%" 2>&1
		TYPE "!_VPY_file!" >> "%vrdlog%" 2>&1
		ECHO ---------------------------- 2>&1
		ECHO TYPE "!_VPY_file!"
		TYPE "!_VPY_file!"
		ECHO ---------------------------- 2>&1
		REM from mpeg2, always -cq:v 0
		REM set VO_deint_sharpen=-filter_complex "[0:v]yadif=!yadif_mode!:!yadif_tff_bff!:0,hwupload,unsharp_opencl=lx=3:ly=3:la=1.5:cx=3:cy=3:ca=1.5,hwdownload,format=pix_fmts=yuv420p" >> "%vrdlog%" 2>&1
		REM set VO_HQ=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp !VO_deint_sharpen! -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr -cq:v 0 -b:v !FF_V_Target_BitRate! -minrate:v !FF_V_Target_Minimum_BitRate! -maxrate:v !FF_V_Target_Maximum_BitRate! -bufsize !FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
		REM set ff_cmd="!ffmpegexex64!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -i "!scratch_file_qsf!" -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		REM
		set VO_HQ_DG=-vsync 0 -sws_flags lanczos+accurate_rnd+full_chroma_int+full_chroma_inp -strict experimental -c:v h264_nvenc -pix_fmt nv12 -preset p7 -multipass fullres !RTX2060super_extra_flags! -rc:v vbr !x_cq_options! -b:v !FF_V_Target_BitRate! -minrate:v !FF_V_Target_Minimum_BitRate! -maxrate:v !FF_V_Target_Maximum_BitRate! -bufsize !FF_V_Target_BufSize! -profile:v high -level 5.2 -movflags +faststart+write_colr >> "%vrdlog%" 2>&1
		REM Handle an ffmpeg.exe with a removed Opencl
		REM set ff_cmd_DG="!VSffmpegexex64_max!" -hide_banner -v verbose -nostats !ff_OpenCL_device_init! !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ_DG! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		set ff_cmd_DG="!VSffmpegexex64!" -hide_banner -v verbose -nostats  !V_cut_start! -f vapoursynth -i "!_VPY_file!" -i "!scratch_file_qsf!" -map 0:v:0 -map 1:a:0 -vf "setdar=!V_DisplayAspectRatio_String_slash!" !V_cut_duration! !VO_HQ_DG! !AO_! -y "!destination_file!" >> "%vrdlog%" 2>&1
		REM we use DG for deinterlacing
		set ff_cmd=!ff_cmd_DG!
	)
)
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
REM ECHO !DATE! !TIME! RTX2060super_extra_flags="!RTX2060super_extra_flags!"
REM ECHO !DATE! !TIME! RTX2060super_extra_flags="!RTX2060super_extra_flags!">> "!vrdlog!" 2>&1
REM ECHO !DATE! !TIME! Video, Audio, FF options follow: >> "%vrdlog%" 2>&1
REM set VO_ >> "%vrdlog%" 2>&1
REM set AO_ >> "%vrdlog%" 2>&1
REM set ff_ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
REM +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! !ff_cmd!
ECHO !DATE! !TIME! !ff_cmd! >> "%vrdlog%" 2>&1
set "ff_start_date_time=!date! !time!"
!ff_cmd! >> "%vrdlog%" 2>&1
SET EL=!ERRORLEVEL!
set "ff_end_date_time=!date! !time!"
powershell -NoLogo -ExecutionPolicy Unrestricted -Sta -NonInteractive -WindowStyle Minimized -File "!PTH2_Calculate_Duration_PS!" -start_date_time "!ff_start_date_time!" -end_date_time "!ff_end_date_time!" -prefix_id ":::::::::: ff" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! +++++++++++++++++++++++++
ECHO !DATE! !TIME! +++++++++++++++++++++++++ >> "%vrdlog%" 2>&1
REM
REM if NOT exist "!destination_file!" ( 
IF /I "!EL!" NEQ "0" (
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! File failed to Convert by FFMPEG "%~f1"
	ECHO !DATE! !TIME! File failed to Convert by FFMPEG" %~f1" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Moving "%~f1" to "!failed_conversion_TS_Folder!"
	ECHO !DATE! !TIME! Moving "%~f1" to "!failed_conversion_TS_Folder!" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO MOVE /Y "%~f1" "!failed_conversion_TS_Folder!"
	ECHO MOVE /Y "%~f1" "!failed_conversion_TS_Folder!" >> "%vrdlog%" 2>&1
	MOVE /Y "%~f1" "!failed_conversion_TS_Folder!" >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	goto :eof
)
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
ECHO DEL /F "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
DEL /F "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
ECHO DEL /F "!_DGI_file!" >> "%vrdlog%" 2>&1
DEL /F "!_DGI_file!" >> "%vrdlog%" 2>&1
ECHO DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
DEL /F "!_VPY_file!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
REM
goto :do_finalization
:after_do_ffmpeg_conversion
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:do_VRD_conversion
REM
REM do it via VRD (doesn't work, CRF is broken with nvenc encoding)
REM note no "/QSF" in the conversion
REM The VRD profiles use SAS (same as source) resolution
REM Default to deinterlace if not explicitly marked as progressive
REM Default to higher CRF quality if AVC input (otherwise is likely to be old mpeg2)
REM Create 4 new specific profiles for Conversion:
REM		VRDTVS-to-h264-CRF20-aac
REM		VRDTVS-to-h264-CRF22-aac
REM		VRDTVS-to-h264-CRF24-aac
REM		VRDTVS-to-h264-SmartDeint-CRF20-aac
REM		VRDTVS-to-h264-SmartDeint-CRF22-aac
REM		VRDTVS-to-h264-SmartDeint-CRF24-aac
REM
REM +++++++++++++++++++++++++
set AO_=-c:a libfdk_aac -cutoff 20000 -ab 256k -ar 48000
REM +++++++++++++++++++++++++
IF /I "!V_ScanType!" == "Progressive" (
	IF /I "!Q_V_Codec_legacy!" == "AVC" (
		REM no deinterlace
		set "VRDTVS_conversion_profile=VRDTVS-to-h264-CRF24-aac"
		REM set ff_cmd_vrd="!ffmpegexex64!" -v verbose -nostats -i "!scratch_file_qsf!" -c:v copy !AO_! -y "!destination_file!"
		REM Perhaps - instead, copy video stream using ffmpeg even though this is VRD ??
		REM ECHO !ff_cmd_vrd!
		REM ECHO !ff_cmd_vrd!  >> "%vrdlog%" 2>&1
		REM !ff_cmd_vrd!  >> "%vrdlog%" 2>&1
	) ELSE (
		REM no deinterlace, moderate quality
		set "VRDTVS_conversion_profile=VRDTVS-to-h264-CRF28-aac"
	)
) ELSE (
	IF /I "!Q_V_Codec_legacy!" == "AVC" (
		REM yes deinterlace, higher quality
		set "VRDTVS_conversion_profile=VRDTVS-to-h264-SmartDeint-CRF24-aac"
	) ELSE (
		REM yes deinterlace, moderate quality
		set "VRDTVS_conversion_profile=VRDTVS-to-h264-SmartDeint-CRF28-aac"
	)
)
ECHO !DATE! !TIME!
set VRDTVS_conversion_profile
set VRDTVS_conversion_profile >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!
ECHO cscript //Nologo "!PTH2_vp_vbs!" "!scratch_file_qsf!" "!destination_file!" /p %VRDTVS_conversion_profile% /q /na
ECHO cscript //Nologo "!PTH2_vp_vbs!" "!scratch_file_qsf!" "!destination_file!" /p %VRDTVS_conversion_profile% /q /na >> "%vrdlog%" 2>&1
REM cscript //Nologo "!PTH2_vp_vbs!" "!scratch_file_qsf!"  "!destination_file!" /p %VRDTVS_conversion_profile% /q /na >> "%vrdlog%" 2>&1
if NOT exist "!destination_file!" ( 
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! File failed to Convert by VRD "%~f1"
	ECHO !DATE! !TIME! File failed to Convert by VRD "%~f1" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME! Moving "%~f1" to "!failed_conversion_TS_Folder!"
	ECHO !DATE! !TIME! Moving "%~f1" to "!failed_conversion_TS_Folder!" >> "!vrdlog!" 2>&1
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	ECHO MOVE /Y "%~f1" "!failed_conversion_TS_Folder!"
	ECHO MOVE /Y "%~f1" "!failed_conversion_TS_Folder!" >> "%vrdlog%" 2>&1
	MOVE /Y "%~f1" "!failed_conversion_TS_Folder!" >> "%vrdlog%" 2>&1
	ECHO !DATE! !TIME!
	ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
	goto :eof
)
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "%vrdlog%" 2>&1
REM
goto :do_finalization
:after_do_VRD_conversion
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:do_finalization
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM If it gets to here then the conversion has been successful.
REM
ECHO DEL /F "!scratch_file_qsf!"  >> "!vrdlog!" 2>&1
DEL /F "!scratch_file_qsf!"  >> "!vrdlog!" 2>&1
Call :get_mediainfo_parameter_legacy "Video" "Codec" "D_V_Codec_legacy" "!destination_file!"
Call :get_mediainfo_parameter "Video" "ScanType" "D_V_ScanType" "!destination_file!" 
IF /I "!D_V_ScanType!" == "" (
	ECHO !DATE! !TIME! "D_V_ScanType blank, setting D_V_ScanType=Progressive"
	ECHO !DATE! !TIME! "D_V_ScanType blank, setting D_V_ScanType=Progressive" >> "!vrdlog!" 2>&1
	set "D_V_ScanType=Progressive"
)
Call :get_mediainfo_parameter "Video" "ScanOrder" "D_V_ScanOrder" "!destination_file!" 
IF /I "!Q_V_ScanOrder!" == "" (
	ECHO !DATE! !TIME! "D_V_ScanOrder blank, setting D_V_ScanOrder=TFF"
	ECHO !DATE! !TIME! "D_V_ScanOrder blank, setting D_V_ScanOrder=TFF" >> "!vrdlog!" 2>&1
	set "Q_V_ScanOrder=TFF"
)
Call :get_mediainfo_parameter "Video" "BitRate" "D_V_BitRate" "!destination_file!" 
Call :get_mediainfo_parameter "Video" "BitRate/String" "D_V_BitRate_String" "!destination_file!"  
Call :get_mediainfo_parameter "Video" "BitRate_Minimum" "D_V_BitRate_Minimum" "!destination_file!"  
Call :get_mediainfo_parameter "Video" "BitRate_Minimum/String" "D_V_BitRate_Minimum_String" "!destination_file!"  
Call :get_mediainfo_parameter "Video" "BitRate_Maximum" "D_V_BitRate_Maximum" "!destination_file!" 
Call :get_mediainfo_parameter "Video" "BitRate_Maximum/String" "D_V_BitRate_Maximum_String" "!destination_file!"  
Call :get_mediainfo_parameter "Video" "BufferSize" "D_V_BufferSize" "!destination_file!" 
Call :get_mediainfo_parameter "Video" "Width" "D_V_Width" "!destination_file!" 
Call :get_mediainfo_parameter "Video" "Height" "D_V_Height" "!destination_file!" 
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio" "D_V_DisplayAspectRatio" "!destination_file!"
set "D_V_DisplayAspectRatio_String_slash=!D_V_DisplayAspectRatio_String::=/!"
Call :get_mediainfo_parameter "Video" "DisplayAspectRatio/String" "D_V_DisplayAspectRatio_String" "!destination_file!"
Call :get_mediainfo_parameter "Video" "PixelAspectRatio" "D_V_PixelAspectRatio" "!destination_file!"
Call :get_mediainfo_parameter "Video" "PixelAspectRatio/String" "D_V_PixelAspectRatio_String" "!destination_file!"
Call :get_mediainfo_parameter "Audio" "Video_Delay" "D_A_Video_Delay_ms" "!destination_file!" 
IF /I "!D_A_Video_Delay_ms!" == "" (
	set /a D_A_Audio_Delay_ms=0
) ELSE (
	set /a D_A_Audio_Delay_ms=0 - !D_A_Video_Delay_ms!
)
ECHO !DATE! !TIME! "D_A_Video_Delay_ms=!D_A_Video_Delay_ms!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "D_A_Audio_Delay_ms=!D_A_Audio_Delay_ms!" Calculated >> "!vrdlog!" 2>&1
REM
Call :get_ffprobe_video_stream_parameter "codec_name" "D_V_CodecID_FF" "!destination_file!" 
Call :get_ffprobe_video_stream_parameter "codec_tag_string" "D_V_CodecID_String_FF" "!destination_file!" 
Call :get_ffprobe_video_stream_parameter "width" "D_V_Width_FF" "!destination_file!" 
Call :get_ffprobe_video_stream_parameter "height" "D_V_Height_FF" "!destination_file!" 
Call :get_ffprobe_video_stream_parameter "duration" "D_V_Duration_s_FF" "!destination_file!" 
Call :get_ffprobe_video_stream_parameter "bit_rate" "D_V_BitRate_FF" "!destination_file!" 
Call :get_ffprobe_video_stream_parameter "max_bit_rate" "D_V_BitRate_Maximum_FF" "!destination_file!" 
Call :get_mediainfo_parameter_legacy "Audio" "Codec" "D_A_Codec_legacy" "!destination_file!" 
Call :get_mediainfo_parameter_legacy "Audio" "Video_Delay" "D_A_Video_Delay_ms_legacy" "!destination_file!" 
IF /I "!D_A_Video_Delay_ms_legacy!" == "" (
	set /a "D_A_Audio_Delay_ms_legacy=0"
) ELSE (
	set /a "D_A_Audio_Delay_ms_legacy=0 - !D_A_Video_Delay_ms_legacy!"
)
ECHO !DATE! !TIME! "D_A_Video_Delay_ms_legacy=!D_A_Video_Delay_ms_legacy!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! "D_A_Audio_Delay_ms_legacy=!D_A_Audio_Delay_ms_legacy!" Calculated >> "!vrdlog!" 2>&1
REM
DIR /4 "!destination_file!" 
ECHO DIR /4 "!destination_file!" >> "!vrdlog!" 2>&1
DIR /4 "!destination_file!" >> "!vrdlog!" 2>&1
REM ECHO "!mediainfoexe!" --Full "!destination_file!" to "%~f1.CONVERTED.mediainfo.txt" 
REM ECHO "!mediainfoexe!" --Full "!destination_file!" to "%~f1.CONVERTED.mediainfo.txt" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --Full "!destination_file!" > "%~f1.CONVERTED.mediainfo.txt" 
REM ECHO !DATE! !TIME! "!mediainfoexe!" --Full "!destination_file!" >> "!vrdlog!" 2>&1
REM "!mediainfoexe!" --Full "!destination_file!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! output converted file: D_Video Codec: "!D_V_Codec_legacy!" D_ScanType: "!D_V_ScanType!" D_ScanOrder: "!D_V_ScanOrder!" !D_V_Width!x!D_V_Height! dar=!D_V_DisplayAspectRatio_String! sar=!D_V_PixelAspectRatio! D_Audio Codec: "!D_A_Codec_legacy!" D_Audio_Delay_ms: !D_A_Audio_Delay_ms! D_Audio_Delay_ms_legacy: !D_A_Video_Delay_ms_legacy! 
ECHO !DATE! !TIME! output converted file: D_Video Codec: "!D_V_Codec_legacy!" D_ScanType: "!D_V_ScanType!" D_ScanOrder: "!D_V_ScanOrder!" !D_V_Width!x!D_V_Height! dar=!D_V_DisplayAspectRatio_String! sar=!D_V_PixelAspectRatio! D_Audio Codec: "!D_A_Codec_legacy!" D_Audio_Delay_ms: !D_A_Audio_Delay_ms! D_Audio_Delay_ms_legacy: !D_A_Video_Delay_ms_legacy! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! End Conversion of "%~f1" / "!scratch_file_qsf!"
ECHO !DATE! !TIME! End Conversion of "%~f1" / "!scratch_file_qsf!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Successfully Converted "%~f1" to "!destination_file!"
ECHO !DATE! !TIME! Successfully Converted "%~f1" to "!destination_file!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Moving "%~f1" to "!done_TS_Folder!"
ECHO !DATE! !TIME! Moving "%~f1" to "!done_TS_Folder!" >> "!vrdlog!" 2>&1
ECHO MOVE /Y "%~f1" "!done_TS_Folder!" >> "%vrdlog%" 2>&1
MOVE /Y "%~f1" "!done_TS_Folder!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME!
ECHO !DATE! !TIME! >> "!vrdlog!" 2>&1
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:do_VRD_adscan
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! Start ADSCAN "!destination_file!"
ECHO !DATE! !TIME! Start ADSCAN "!destination_file!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
set adscan_destination_file=!destination_mp4_Folder!%~n1.BPRJ
ECHO DEL /F "!adscan_destination_file!" >> "!vrdlog!" 2>&1
DEL /F "!adscan_destination_file!" >> "!vrdlog!" 2>&1
ECHO cscript //Nologo "!PTH2_adscan_vbs!" "!destination_file!" "!adscan_destination_file!" /q
ECHO cscript //Nologo "!PTH2_adscan_vbs!" "!destination_file!" "!adscan_destination_file!" /q >> "%vrdlog%" 2>&1
REM cscript //Nologo "!PTH2_adscan_vbs!" "!destination_file!"  "!adscan_destination_file!" /q >> "%vrdlog%" 2>&1
DIR /4 "!adscan_destination_file!" >> "%vrdlog%" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! End ADSCAN "!destination_file!" into "!adscan_destination_file!"
ECHO !DATE! !TIME! End ADSCAN "!destination_file!" into "!adscan_destination_file!" >> "!vrdlog!" 2>&1
ECHO !DATE! !TIME! ======================================================================================================================================================
ECHO !DATE! !TIME! ====================================================================================================================================================== >> "!vrdlog!" 2>&1
REM
:after_do_VRD_adscan
goto :eof

REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:get_mediainfo_parameter
REM DO NOT SET @setlocal ENABLEDELAYEDEXPANSION
REM DO NOT SET @setlocal enableextensions
REM ensure no trailing spaces in any of the lines in this routine !!
set mi_Section=%~1
set mi_Parameter=%~2
set mi_Variable=%~3
set mi_Filename=%~4
set "mi_var="
DEL /F "!tempfile!" >NUL 2>&1
REM Note \r\n is Windows new-line, which is for the case of multiple audio streams, 
REM it outputs a result for each stream on a new line, the first stream being the first entry,
REM and the first audio stream should be the one we need. 
REM Set /p from an input file reads the first line.
"!mediainfoexe!" "--Inform=!mi_Section!;%%!mi_Parameter!%%\r\n" "!mi_Filename!" > "!tempfile!"
set /p mi_var=<"!tempfile!"
set !mi_Variable!=!mi_var!
REM ECHO !DATE! !TIME! "!mi_Variable!=!mi_var!" from "!mi_Section!" "!mi_Parameter!"
REM ECHO !DATE! !TIME! "!mi_Variable!=!mi_var!" from "!mi_Section!" "!mi_Parameter!" >> "!vrdlog!" 2>&1
DEL /F "!tempfile!" >NUL 2>&1
goto :eof
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:get_mediainfo_parameter_legacy
REM DO NOT SET @setlocal ENABLEDELAYEDEXPANSION
REM DO NOT SET @setlocal enableextensions
REM ensure no trailing spaces in any of the lines in this routine !!
set mi_Section=%~1
set mi_Parameter=%~2
set mi_Variable=%~3
set mi_Filename=%~4
set "mi_var="
DEL /F "!tempfile!" >NUL 2>&1
REM Note \r\n is Windows new-line, which is for the case of multiple audio streams, 
REM it outputs a result for each stream on a new line, the first stream being the first entry,
REM and the first audio stream should be the one we need. 
REM Set /p from an input file reads the first line.
"!mediainfoexe!" --Legacy "--Inform=!mi_Section!;%%!mi_Parameter!%%\r\n" "!mi_Filename!" > "!tempfile!"
set /p mi_var=<"!tempfile!"
set !mi_Variable!=!mi_var!
REM ECHO !DATE! !TIME! "!mi_Variable!=!mi_var!" from Legacy "!mi_Section!" "!mi_Parameter!"
REM ECHO !DATE! !TIME! "!mi_Variable!=!mi_var!" from Legacy "!mi_Section!" "!mi_Parameter!" >> "!vrdlog!" 2>&1
DEL /F "!tempfile!" >NUL 2>&1
goto :eof
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:get_ffprobe_video_stream_parameter
REM DO NOT SET @setlocal ENABLEDELAYEDEXPANSION
REM DO NOT SET @setlocal enableextensions
REM ensure no trailing spaces in any of the lines in this routine !!
set mi_Parameter=%~1
set mi_Variable=%~2
set mi_Filename=%~3
set "mi_var="
DEL /F "!tempfile!" >NUL 2>&1
REM Note \r\n is Windows new-line, which is for the case of multiple audio streams, 
REM it outputs a result for each stream on a new line, the first stream being the first entry,
REM and the first audio stream should be the one we need. 
REM Set /p from an input file reads the first line.
REM see if -probesize 5000M  makes any difference
"!ffprobeexe64!" -hide_banner -v quiet -select_streams v:0 -show_entries stream=!mi_Parameter! -of default=noprint_wrappers=1:nokey=1 "!mi_Filename!" > "!tempfile!"
set /p mi_var=<"!tempfile!"
set !mi_Variable!=!mi_var!
REM ECHO !DATE! !TIME! "!mi_Variable!=!mi_var!" from ffprobe "!mi_Parameter!"
REM ECHO !DATE! !TIME! "!mi_Variable!=!mi_var!" from ffprobe "!mi_Parameter!" >> "!vrdlog!" 2>&1
DEL /F "!tempfile!" >NUL 2>&1
goto :eof
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:LoCase
:: Subroutine to convert a variable VALUE to all lower case.
:: The argument for this subroutine is the variable NAME.
FOR %%i IN ("A=a" "B=b" "C=c" "D=d" "E=e" "F=f" "G=g" "H=h" "I=i" "J=j" "K=k" "L=l" "M=m" "N=n" "O=o" "P=p" "Q=q" "R=r" "S=s" "T=t" "U=u" "V=v" "W=w" "X=x" "Y=y" "Z=z") DO CALL SET "%1=%%%1:%%~i%%"
goto :eof

:UpCase
:: Subroutine to convert a variable VALUE to all UPPER CASE.
:: The argument for this subroutine is the variable NAME.
FOR %%i IN ("a=A" "b=B" "c=C" "d=D" "e=E" "f=F" "g=G" "h=H" "i=I" "j=J" "k=K" "l=L" "m=M" "n=N" "o=O" "p=P" "q=Q" "r=R" "s=S" "t=T" "u=U" "v=V" "w=W" "x=X" "y=Y" "z=Z") DO CALL SET "%1=%%%1:%%~i%%"
goto :eof

:TCase
:: Subroutine to convert a variable VALUE to Title Case.
:: The argument for this subroutine is the variable NAME.
FOR %%i IN (" a= A" " b= B" " c= C" " d= D" " e= E" " f= F" " g= G" " h= H" " i= I" " j= J" " k= K" " l= L" " m= M" " n= N" " o= O" " p= P" " q= Q" " r= R" " s= S" " t= T" " u= U" " v= V" " w= W" " x= X" " y= Y" " z= Z") DO CALL SET "%1=%%%1:%%~i%%"
goto :eof
REM
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
:calc_single_number_result
REM use VBS to evaluate an incoming formula strng which has no embedded special characters 
REM and yield a result which has no embedded special characters
REM eg   CALL :calc_single_number_result "Int((1+2+3+4+5+6)/10.0)" "return_variable_name"
set "Datey=%DATE: =0%"
set "Timey=%time: =0%"
set VTDTVS_eval_datetime=!Datey:~10,4!-!Datey:~7,2!-!Datey:~4,2!.!Timey:~0,2!.!Timey:~3,2!.!Timey:~6,2!.!Timey:~9,2!
set VTDTVS_eval_datetime=!VTDTVS_eval_datetime: =0!
set VTDTVS_eval_formula_vbs=!temp!\VTDTVS_eval_formula-!VTDTVS_eval_datetime!.vbs
set VRDTVS_eval_formula=%~1
set VRDTVS_eval_variable=%~2
set "VRDTVS_eval_single_number_result="
REM echo 'cscript //nologo "!VTDTVS_eval_formula_vbs!" "!VRDTVS_eval_formula!"'
echo wscript.echo eval(wscript.arguments(0))>"!VTDTVS_eval_formula_vbs!"
for /f %%A in ('cscript //nologo "!VTDTVS_eval_formula_vbs!" "!VRDTVS_eval_formula!"') do (
    set "!VRDTVS_eval_variable!=%%A"
    set "VRDTVS_eval_single_number_result=%%A"
)
DEL /F "!VTDTVS_eval_formula_vbs!" >NUL 2>&1
REM echo "VTDTVS_eval_formula_vbs=!VTDTVS_eval_formula_vbs!"
REM echo "VRDTVS_eval_variable=!VRDTVS_eval_variable! VRDTVS_eval_formula=!VRDTVS_eval_formula! VRDTVS_eval_single_number_result=!VRDTVS_eval_single_number_result!"
goto :eof
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM -------------------------------------------------------------------------------------------------------------------------------------
REM
