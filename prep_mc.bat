@echo off

powershell -Command "Stop-Process -Name "MinecraftLauncher" -Force"
echo [92mDownloading fabric jar[0m
powershell -Command "Invoke-WebRequest https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.7.3/fabric-installer-0.7.3.jar -OutFile %TMP%\fabric.jar" || echo [42mDownload Failed, please check your internet connection[0m
echo [92mInstalling fabric[0m
java -jar %TMP%\fabric.jar || echo [42mUnzip failed, do you have the correct permissions?[0m
echo [92mDownloading zip of the required mods[0m
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/UFifty50/temp/main/mods.zip -OutFile %TMP%\mods.zip" || echo [42mDownload Failed, please check your internet connection[0m
echo [92mUnzipping mods zip[0m
unzip -o "%TMP%\mods.zip" -d "%AppData%\.minecraft\mods" || echo [42mUnzip failed, do you have the correct permissions?[0m
echo [92mUnzip Success! You can now play minecraft with the correct mods installed. If this windows doesnt close itself, then please close it :)[0m