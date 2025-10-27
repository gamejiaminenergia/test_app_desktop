#!/bin/bash
# Script de inicio para la Calculadora Web - Versión Portable
# Uso: ./start_calculator.sh

echo "🧮 Calculadora Web - Ejecutable Portable"
echo "========================================"
echo ""
echo "✨ EJECUTABLE COMPLETAMENTE INDEPENDIENTE"
echo "✅ No requiere Python instalado"
echo "✅ No necesita archivos externos"
echo "✅ Funciona desde cualquier ubicación"
echo "✅ Solo ejecutar y usar"
echo ""

# Buscar ejecutable en el directorio actual
if [ -f "./CalculadoraWeb_Standalone" ]; then
    echo "🚀 Iniciando calculadora..."
    echo "📁 Ejecutable encontrado: ./CalculadoraWeb_Standalone"
    echo ""
    echo "🌐 Se abrirá automáticamente en: http://127.0.0.1:8080"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "==========================================="
    echo ""
    ./CalculadoraWeb_Standalone
elif [ -f "./CalculadoraWeb_Standalone.exe" ]; then
    echo "🚀 Iniciando calculadora (Windows)..."
    echo "📁 Ejecutable encontrado: ./CalculadoraWeb_Standalone.exe"
    echo ""
    echo "🌐 Se abrirá automáticamente en: http://127.0.0.1:8080"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "==========================================="
    echo ""
    ./CalculadoraWeb_Standalone.exe
elif [ -f "./build/calculator_final.py" ]; then
    echo "🚀 Ejecutando desde código fuente..."
    echo "📁 Script encontrado: ./build/calculator_final.py"
    echo ""
    echo "🌐 Se abrirá automáticamente en: http://127.0.0.1:8080"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "==========================================="
    echo ""
    python3 build/calculator_final.py
else
    echo "❌ No se encontró el ejecutable ni el script"
    echo ""
    echo "💡 Archivos necesarios:"
    echo "   - CalculadoraWeb_Standalone (ejecutable)"
    echo "   - calculator_final.py (script fuente)"
    echo "   - start_calculator.sh (este script)"
    echo ""
    echo "💡 Para crear el ejecutable:"
    echo "   pyinstaller --clean build/calculator_final.spec"
    echo ""
    exit 1
fi
