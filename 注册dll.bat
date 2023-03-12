@ECHO OFF
setlocal EnableDelayedExpansion
color 3e
title regsvr DLL
 
PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof
:runas
 
::填写自己的脚本
regsvr32  %~dp0\lw9_09.dll
echo regsvr DLL succeed
echo press any key to exit
 
pause >nul
exit