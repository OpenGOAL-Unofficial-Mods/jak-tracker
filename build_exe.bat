
set mypath=%~dp0
pyinstaller --onefile JakTracker.py --icon appicon.ico 
move "%mypath%dist\JakTracker.exe" "%mypath%/"
RENAME "%mypath%\JakTracker.exe" "JakTracker.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/JakTracker.spec"
