#!/bin/bash
# Script para iniciar la aplicación con gunicorn

echo "🧮 Iniciando Calculadora Web con Gunicorn"
echo "=========================================="

# Verificar si estamos en el directorio correcto
if [ ! -f "app.py" ]; then
    echo "❌ Error: app.py no encontrado. Ejecuta desde el directorio del proyecto."
    exit 1
fi

# Iniciar gunicorn
echo "🚀 Iniciando servidor en http://127.0.0.1:8000"
echo "📋 Endpoints disponibles:"
echo "   GET  /              - Interfaz web"
echo "   POST /calculate     - API de cálculos"
echo "   GET  /health        - Verificación de salud"
echo "   GET  /api/info      - Información de la API"
echo ""
echo "💡 Presiona Ctrl+C para detener el servidor"
echo "=========================================="

gunicorn app:app --bind 127.0.0.1:8000 --workers 4 --access-logfile - --error-logfile -
