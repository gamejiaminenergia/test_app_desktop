#!/usr/bin/env python3
"""
Script de construcción para crear el ejecutable de la Calculadora Web
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description=""):
    """Ejecuta un comando y muestra el resultado."""
    print(f"🔧 {description}")
    print(f"   Comando: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"   ✅ {description} completado")
        if result.stdout:
            print(f"   📄 Salida: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error en {description}")
        print(f"   Error: {e.stderr}")
        return False

def create_build_directory():
    """Crea el directorio de construcción."""
    build_dir = Path("build_executable")
    if build_dir.exists():
        print(f"🗑️  Eliminando directorio de construcción anterior: {build_dir}")
        shutil.rmtree(build_dir)

    build_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Directorio de construcción creado: {build_dir}")
    return build_dir

def install_dependencies():
    """Instala las dependencias necesarias."""
    print("\n📦 Instalando dependencias...")
    success = run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Instalación de dependencias"
    )
    return success

def verify_files():
    """Verifica que todos los archivos necesarios existan."""
    print("\n🔍 Verificando archivos del proyecto...")

    required_files = [
        'run_calculator.py',
        'app.py',
        'requirements.txt',
        'calculator.spec',
        'routes/__init__.py',
        'models/calculator.py',
        'templates/index.html',
        'static/css/style.css',
        'static/js/calculator.js'
    ]

    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file}")
            missing_files.append(file)

    if missing_files:
        print(f"\n❌ Archivos faltantes: {missing_files}")
        return False

    print("   ✅ Todos los archivos requeridos están presentes")
    return True

def build_executable():
    """Construye el ejecutable usando PyInstaller."""
    print("\n🏗️  Construyendo ejecutable...")

    # Construir con la configuración personalizada
    success = run_command(
        "pyinstaller --clean calculator.spec",
        "Construcción del ejecutable con PyInstaller"
    )

    if success:
        print("   ✅ Ejecutable construido exitosamente")

        # Verificar archivos generados
        dist_dir = Path("dist")
        if dist_dir.exists():
            exe_files = list(dist_dir.glob("*.exe")) if os.name == 'nt' else list(dist_dir.glob("*"))
            if exe_files:
                print(f"   📦 Archivos generados en {dist_dir}:")
                for exe_file in exe_files:
                    print(f"      - {exe_file.name}")
            else:
                print(f"   ⚠️  No se encontraron ejecutables en {dist_dir}")
        else:
            print(f"   ⚠️  No se encontró directorio dist")

    return success

def create_startup_script():
    """Crea un script de inicio fácil de usar."""
    print("\n📝 Creando script de inicio...")

    if os.name == 'nt':  # Windows
        script_content = """#!/bin/bash
# Script de inicio para Windows
echo "Iniciando Calculadora Web..."
dist\\CalculadoraWeb\\CalculadoraWeb.exe
"""
        script_name = "start_calculator.bat"
    else:  # Linux/Mac
        script_content = """#!/bin/bash
# Script de inicio para Linux/Mac
echo "🧮 Iniciando Calculadora Web..."
echo "📁 Buscando ejecutable..."

if [ -f "dist/CalculadoraWeb" ]; then
    echo "🚀 Ejecutando: dist/CalculadoraWeb"
    ./dist/CalculadoraWeb
elif [ -f "dist/CalculadoraWeb.exe" ]; then
    echo "🚀 Ejecutando: dist/CalculadoraWeb.exe"
    ./dist/CalculadoraWeb.exe
else
    echo "❌ No se encontró el ejecutable en dist/"
    echo "💡 Ejecuta primero: python build_executable.py"
    exit 1
fi
"""
        script_name = "start_calculator.sh"

    with open(script_name, 'w') as f:
        f.write(script_content)

    # Hacer ejecutable en Unix
    if os.name != 'nt':
        os.chmod(script_name, 0o755)

    print(f"   ✅ Script creado: {script_name}")
    return True

def create_readme():
    """Crea un README para el ejecutable."""
    print("\n📖 Creando documentación...")

    readme_content = """# Calculadora Web - Ejecutable

Este ejecutable permite ejecutar la Calculadora Web sin necesidad de instalar Python o configurar entornos.

## 🚀 Cómo usar

### Opción 1: Script automático (Recomendado)
```bash
# Linux/Mac
./start_calculator.sh

# Windows
start_calculator.bat
```

### Opción 2: Ejecutable directo
```bash
# Linux/Mac
./dist/CalculadoraWeb

# Windows
.\\dist\\CalculadoraWeb\\CalculadoraWeb.exe
```

## 📋 Lo que hace el ejecutable

1. **Inicia el servidor Flask** en http://127.0.0.1:5000
2. **Abre automáticamente el navegador** en la URL de la calculadora
3. **Muestra una interfaz moderna** con todas las funciones de la calculadora
4. **Ejecuta completamente independiente** sin necesidad de Python instalado

## 🔧 Funcionalidades incluidas

- ✅ Operaciones básicas (suma, resta, multiplicación, división)
- ✅ Operaciones avanzadas (potencia, raíz cuadrada, porcentaje)
- ✅ Historial de operaciones
- ✅ Interfaz responsiva (móvil y desktop)
- ✅ Validación de errores
- ✅ Soporte para teclado

## 🛠️ Construir desde código fuente

Si tienes el código fuente y quieres reconstruir el ejecutable:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Construir ejecutable
python build_executable.py

# 3. Ejecutar
./start_calculator.sh
```

## 📁 Estructura del ejecutable

```
dist/
├── CalculadoraWeb          # Ejecutable principal (Linux/Mac)
└── CalculadoraWeb/
    ├── CalculadoraWeb.exe  # Ejecutable principal (Windows)
    ├── templates/          # Plantillas HTML
    ├── static/            # CSS y JavaScript
    └── models/            # Lógica de la calculadora
```

## 🔧 Requisitos del sistema

- **Windows 10/11** o **Linux** (Ubuntu 18.04+, CentOS 7+, etc.)
- **macOS 10.15+** (para versiones de Mac)
- **4GB RAM** (recomendado)
- **100MB espacio en disco**

## 🐛 Solución de problemas

### El ejecutable no inicia
- Verifica que tienes permisos de ejecución
- En Linux/Mac: `chmod +x start_calculator.sh`

### No se abre el navegador
- Abre manualmente: http://127.0.0.1:5000
- Verifica que no haya firewall bloqueando el puerto 5000

### Error de archivos faltantes
- Asegúrate de que todos los archivos estén en el directorio correcto
- Ejecuta `python build_executable.py` para reconstruir

## 📄 Licencia

Este ejecutable incluye todo el código necesario para funcionar de forma independiente.

---
**Desarrollado con:** Flask, PyInstaller, HTML5, CSS3, JavaScript
"""

    with open("EXECUTABLE_README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("   ✅ Documentación creada: EXECUTABLE_README.md")
    return True

def main():
    """Función principal del script de construcción."""
    print("🧮 Calculadora Web - Constructor de Ejecutable")
    print("=" * 50)
    print("Este script construirá un ejecutable independiente")
    print("que puede ser distribuido y ejecutado sin Python.")
    print()

    # Verificar que estamos en el directorio correcto
    if not os.path.exists('run_calculator.py'):
        print("❌ Error: Debes ejecutar este script desde el directorio raíz del proyecto")
        print("   (donde está run_calculator.py)")
        return 1

    # Paso 1: Verificar archivos
    if not verify_files():
        return 1

    # Paso 2: Instalar dependencias
    if not install_dependencies():
        return 1

    # Paso 3: Crear directorio de construcción
    create_build_directory()

    # Paso 4: Construir ejecutable
    if not build_executable():
        return 1

    # Paso 5: Crear script de inicio
    create_startup_script()

    # Paso 6: Crear documentación
    create_readme()

    print("\n🎉 ¡CONSTRUCCIÓN COMPLETADA!")
    print("=" * 50)
    print("📦 Tu ejecutable está listo en: dist/")
    print("📖 Lee EXECUTABLE_README.md para instrucciones de uso")
    print("🚀 Ejecuta: ./start_calculator.sh (o start_calculator.bat en Windows)")
    print()
    print("💡 El ejecutable incluye:")
    print("   - Servidor Flask integrado")
    print("   - Todas las plantillas y archivos estáticos")
    print("   - Todas las dependencias de Python")
    print("   - No requiere instalación de Python")

    return 0

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
