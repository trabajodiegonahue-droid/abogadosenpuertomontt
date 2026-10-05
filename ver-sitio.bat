@echo off
REM Doble clic para ver el sitio (Windows).
REM Trae los ultimos cambios, levanta un servidor local y abre el navegador.
cd /d "%~dp0"
echo Trayendo los ultimos cambios...
git pull --ff-only
start "" http://localhost:8000
echo.
echo Sitio en http://localhost:8000  -  cierra esta ventana para detenerlo.
python -m http.server 8000 || py -m http.server 8000
pause
