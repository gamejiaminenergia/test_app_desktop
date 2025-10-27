#!/bin/bash
"""
Script de inicio para la Calculadora Web
Facilita la ejecución y configuración de la aplicación.
"""

import os
import sys
import subprocess
import argparse

def check_python_version():
    """Verifica que la versión de Python sea compatible."""
    if sys.version_info < (3, 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} compatible")

def setup_virtual_environment():
    """Configura el entorno virtual."""
    if not os.path.exists('venv'):
        print("🔧 Creando entorno virtual...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
    else:
        print("✅ Entorno virtual ya existe")

def activate_and_install():
    """Activa el entorno virtual e instala dependencias."""
    print("📦 Instalando dependencias...")

    # Activación del entorno virtual e instalación
    if os.name == 'nt':  # Windows
        activate_script = 'venv\\Scripts\\activate'
        pip_command = 'venv\\Scripts\\pip'
    else:  # Linux/Mac
        activate_script = 'source venv/bin/activate'
        pip_command = 'venv/bin/pip'

    # Instalar dependencias
    subprocess.run([pip_command, 'install', '-r', 'requirements.txt'], check=True)
    print("✅ Dependencias instaladas")

def run_tests():
    """Ejecuta las pruebas automáticas."""
    print("🧪 Ejecutando pruebas...")
    try:
        # Instalar requests si no está disponible
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)

        # Ejecutar pruebas
        result = subprocess.run([sys.executable, 'test_api.py'], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Todas las pruebas pasaron")
            print(result.stdout)
        else:
            print("❌ Algunas pruebas fallaron")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando pruebas: {e}")

def run_application(host='127.0.0.1', port=5000, debug=True):
    """Ejecuta la aplicación Flask."""
    print(f"🚀 Iniciando aplicación en http://{host}:{port}")
    print("   Presiona Ctrl+C para detener")

    try:
        subprocess.run([
            sys.executable, 'app.py'
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Aplicación detenida por el usuario")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando la aplicación: {e}")

def create_startup_script():
    """Crea un script de inicio para sistemas Unix."""
    script_content = '''#!/bin/bash
# Script de inicio rápido para la Calculadora Web

echo "🧮 Iniciando Calculadora Web..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 no está instalado"
    exit 1
fi

# Configurar entorno virtual
if [ ! -d "venv" ]; then
    echo "🔧 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno e instalar dependencias
echo "📦 Instalando dependencias..."
source venv/bin/activate
pip install -r requirements.txt

# Ejecutar aplicación
echo "🚀 Iniciando aplicación..."
python3 app.py
'''

    with open('start.sh', 'w') as f:
        f.write(script_content)

    # Hacer el script ejecutable
    os.chmod('start.sh', 0o755)
    print("✅ Script start.sh creado")

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(description='Gestor de la Calculadora Web')
    parser.add_argument('--setup', action='store_true', help='Configurar el entorno virtual')
    parser.add_argument('--install', action='store_true', help='Instalar dependencias')
    parser.add_argument('--test', action='store_true', help='Ejecutar pruebas')
    parser.add_argument('--run', action='store_true', help='Ejecutar aplicación')
    parser.add_argument('--host', default='127.0.0.1', help='Host para ejecutar la aplicación')
    parser.add_argument('--port', type=int, default=5000, help='Puerto para ejecutar la aplicación')
    parser.add_argument('--no-debug', action='store_true', help='Desactivar modo debug')
    parser.add_argument('--create-script', action='store_true', help='Crear script de inicio')

    args = parser.parse_args()

    # Verificar versión de Python
    check_python_version()

    # Configurar entorno virtual si se solicita
    if args.setup or not os.path.exists('venv'):
        setup_virtual_environment()

    # Instalar dependencias si se solicita
    if args.install:
        activate_and_install()

    # Crear script de inicio si se solicita
    if args.create_script:
        create_startup_script()

    # Ejecutar pruebas si se solicita
    if args.test:
        run_tests()
        return

    # Ejecutar aplicación si se solicita
    if args.run:
        run_application(host=args.host, port=args.port, debug=not args.no_debug)
        return

    # Si no se especifica ninguna acción, mostrar ayuda
    print("\n📋 Opciones disponibles:")
    print("  --setup          Configurar entorno virtual")
    print("  --install        Instalar dependencias")
    print("  --test           Ejecutar pruebas")
    print("  --run            Ejecutar aplicación")
    print("  --create-script  Crear script de inicio")
    print("\n💡 Ejemplos:")
    print("  python setup.py --setup --install --run")
    print("  python setup.py --test")
    print("  python setup.py --run --host 0.0.0.0 --port 8080")

if __name__ == '__main__':
    main()
