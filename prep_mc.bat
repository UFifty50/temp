powershell -Command "Stop-Process -Name "ProcessName" -Force"
echo [92mDownloading zip of the required mods[0m
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/UFifty50/temp/main/mods.zip -OutFile %TMP%\mods.zip || echo [42mDownload Failed, please check your internet connection[0m && exit 1"
echo [92mUnzipping mods zip[0m
Call :UnZipFile "%AppData%\.minecraft\mods" "%TMP%\mods.zip" || echo [42mUnzip failed, do you have the correct permissions?[0m && exit 1
echo [92mUnzip Success! You can now play minecraft with the correct mods installed. If this windows doesnt close itself, then please close it :)[0m

:UnZipFile <ExtractTo> <newzipfile>
set vbs="%temp%\_.vbs"
if exist %vbs% del /f /q %vbs%
>%vbs%  echo Set fso = CreateObject("Scripting.FileSystemObject")
>>%vbs% echo If NOT fso.FolderExists(%1) Then
>>%vbs% echo fso.CreateFolder(%1)
>>%vbs% echo End If
>>%vbs% echo set objShell = CreateObject("Shell.Application")
>>%vbs% echo set FilesInZip=objShell.NameSpace(%2).items
>>%vbs% echo objShell.NameSpace(%1).CopyHere(FilesInZip)
>>%vbs% echo Set fso = Nothing
>>%vbs% echo Set objShell = Nothing
cscript //nologo %vbs%
if exist %vbs% del /f /q %vbs%
