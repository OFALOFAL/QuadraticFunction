@echo off
goto main

:main
setlocal

    for /f %%i in ('python --version') do set pyCheck=%%i

    set CName=Python

    if %pyCheck%==%CName% (
        rem Run program
        python src\main.py
    ) else (
        echo Fatal error occured: %pyCheck%
        echo.
        echo Possible fix: install python
        pause
    )

    :: papuga <3
    start %windir%\system32\cmd.exe /k "curl parrot.live"

endlocal
goto :eof
exit