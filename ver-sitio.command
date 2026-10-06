#!/bin/bash
# Doble clic para ver el sitio (Mac). En Linux: ./ver-sitio.command
# Trae los últimos cambios, levanta un servidor local y abre el navegador.
cd "$(dirname "$0")" || exit 1
echo "Trayendo los últimos cambios..."
git pull --ff-only || echo "(No se pudieron traer cambios; se muestra la versión local)"
(sleep 1; open http://localhost:8000 2>/dev/null || xdg-open http://localhost:8000 >/dev/null 2>&1) &
echo ""
echo "Sitio en http://localhost:8000  —  cierra esta ventana o presiona Ctrl+C para detenerlo."
python3 -m http.server 8000 || echo "El puerto 8000 ya está en uso: el sitio probablemente ya está abierto en http://localhost:8000"
