#!/bin/bash
# Script de inicio para la Calculadora Web - Ejecutable Final
# Uso: ./start_calculator_final.sh

echo "🧮 Calculadora Web - Ejecutable Final"
echo "====================================="
echo ""
echo "✨ EJECUTABLE COMPLETAMENTE INDEPENDIENTE"
echo "✅ No requiere Python instalado"
echo "✅ No necesita archivos externos"
echo "✅ Funciona desde cualquier ubicación"
echo "✅ Solo ejecutar y usar"
echo ""

# Verificar si el ejecutable existe
if [ -f "./build/dist/CalculadoraWeb_Standalone" ]; then
    echo "🚀 Iniciando calculadora..."
    echo "📁 Ejecutable encontrado: ./build/dist/CalculadoraWeb_Standalone"
    echo ""
    echo "🌐 Se abrirá automáticamente en: http://127.0.0.1:8080"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "=========================================="
    echo ""
    ./build/dist/CalculadoraWeb_Standalone
elif [ -f "./build/calculator_final.py" ]; then
    echo "🚀 Ejecutando desde código fuente..."
    echo "📁 Script encontrado: ./build/calculator_final.py"
    echo ""
    echo "🌐 Se abrirá automáticamente en: http://127.0.0.1:8080"
    echo "🛑 Presiona Ctrl+C para detener"
    echo ""
    echo "==========================================="
    echo ""
    python build/calculator_final.py
else
    echo "❌ No se encontró el ejecutable"
    echo ""
    echo "💡 Para crear el ejecutable final:"
    echo "   pyinstaller --clean build/calculator_final.spec"
    echo ""
    echo "💡 Para ejecutar desde código fuente:"
    echo "   python build/calculator_final.py"
    echo ""
    echo "💡 Para probar desde cualquier ubicación:"
    echo "   1. Copia build/calculator_final.py a cualquier carpeta"
    echo "   2. Ejecuta: python calculator_final.py"
    echo ""
    exit 1
fi
