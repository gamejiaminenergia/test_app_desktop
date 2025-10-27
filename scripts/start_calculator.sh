#!/bin/bash
# Script de inicio para la Calculadora Web
# Uso: ./start_calculator.sh

echo "🧮 Calculadora Web - Ejecutable"
echo "================================"
echo ""

# Verificar si el ejecutable existe
if [ -f "./dist/CalculadoraWeb" ]; then
    echo "🚀 Iniciando calculadora..."
    echo "📁 Ejecutable encontrado: ./dist/CalculadoraWeb"
    echo ""
    echo "🌐 La aplicación se abrirá en: http://127.0.0.1:5000"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "=========================================="
    ./dist/CalculadoraWeb
elif [ -f "./dist/CalculadoraWeb.exe" ]; then
    echo "🚀 Iniciando calculadora (Windows)..."
    echo "📁 Ejecutable encontrado: ./dist/CalculadoraWeb.exe"
    echo ""
    echo "🌐 La aplicación se abrirá en: http://127.0.0.1:5000"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "=========================================="
    ./dist/CalculadoraWeb.exe
else
    echo "❌ No se encontró el ejecutable"
    echo ""
    echo "💡 Para crear el ejecutable:"
    echo "   python build_executable.py"
    echo ""
    echo "💡 Para ejecutar desde código fuente:"
    echo "   python calculator_standalone.py"
    echo ""
    exit 1
fi
