@REM @Author: Jutju
@REM @Date:   2019-04-29 23:43:08
@REM @Last Modified by:   Jutju
@REM Modified time: 2019-04-30 00:52:16

@echo off
set spec=__main__.spec
set file=src\__main__.py
rem pyinstaller --onefile --clean --name uncache --hidden-import posix %spec%
pyinstaller --onefile --clean --name uncache --add-binary "D:\Program Files\Python37\Lib\site-packages\magic";"magic" %file%
@echo on
