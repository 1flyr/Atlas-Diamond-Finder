@echo off
set "appdata_path=%APPDATA%\Local\DiamondFinder"
if not exist "%appdata_path%" (
    mkdir "%appdata_path%"
)

echo Please enter the full path to the chromedriver (e.g., C:\path\to\chromedriver.exe):
set /p chromedriver_path=

if not exist "%chromedriver_path%" (
    echo Error: The chromedriver path does not exist. Please check the path and try again.
    pause
    exit /b
)

echo %chromedriver_path% > "%appdata_path%\config.txt"

cls
echo Setup complete! You may close this window.
pause
