@echo off
echo Cleaning up...&echo ----------------------------------&echo.


if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist DuckInSpace.exe del DuckInSpace.exe
if exist DuckInSpace.spec del DuckInSpace.spec


echo Running build script...&echo.

pyinstaller --onefile --windowed --icon=assets/icons/icon.ico --name=DuckInSpace main.py

echo ----------------------------------&echo Finished building executable&echo.&echo.
echo Cleaning up...&echo.

del /f /q *.spec

move dist\DuckInSpace.exe .\DuckInSpace.exe
rmdir /s /q dist

echo ----------------------------------&echo Finished cleaning up&echo.&echo.

echo Run DuckInSpace.exe? (y/n)&echo.
set /p run=DuckInSpace.exe?
echo.
IF %run%==y (
    echo Running DuckInSpace.exe...
    start DuckInSpace.exe
) ELSE (
    echo Not running DuckInSpace.exe
)

echo ----------------------------------&echo Finished&echo.&echo.