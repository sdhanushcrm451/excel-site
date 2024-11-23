@echo off
cls

:: Set text colors (ANSI escape sequences)
echo.
echo Welcome to Excel-Site! 
echo.
echo Opening Excel-Site...

:: Run your specific command (e.g., Python script or Django server)
echo Running "python manage.py runserver" 
start http://192.168.54.233:8080
echo Refresh page !

python manage.py runserver 192.168.54.233:8080


:: After command completes
echo.
echo ^[[35mProcess completed successfully! ^[[0m  :: Magenta text
pause
