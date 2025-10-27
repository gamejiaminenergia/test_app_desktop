#!/usr/bin/env python3
"""
Calculadora Web - Ejecutable Standalone
Script principal para crear un ejecutable que inicia la calculadora web
y abre automáticamente el navegador.
"""

import os
import sys
import time
import threading
import webbrowser
from flask import Flask
from routes import create_routes
import logging

def create_app():
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__)

    # Configuración simple para el ejecutable
    app.config['SECRET_KEY'] = 'calculator-executable-key'
    app.config['DEBUG'] = False

    # Registrar rutas
    main_bp = create_routes()
    app.register_blueprint(main_bp)

    # Configurar logging básico
    logging.basicConfig(level=logging.INFO)
    app.logger.info('Iniciando Calculadora Web...')

    return app

def open_browser(url, delay=2):
    """Abre el navegador después de un delay."""
    def _open_browser():
        time.sleep(delay)
        try:
            webbrowser.open(url)
            print(f"🌐 Navegador abierto en: {url}")
        except Exception as e:
            print(f"⚠️  No se pudo abrir el navegador automáticamente: {e}")
            print(f"💡 Abre manualmente: {url}")

    thread = threading.Thread(target=_open_browser)
    thread.daemon = True
    thread.start()

def main():
    """Función principal del ejecutable."""
    print("🧮 Calculadora Web - Ejecutable")
    print("=" * 40)
    print("🚀 Iniciando aplicación...")
    print("📁 Buscando archivos...")

    # Verificar que todos los archivos necesarios existen
    required_files = [
        'routes/__init__.py',
        'models/calculator.py',
        'templates/index.html',
        'static/css/style.css',
        'static/js/calculator.js'
    ]

    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - NO ENCONTRADO")
            return 1

    print()
    print("📋 Configuración:")
    print("   🌐 Servidor: http://127.0.0.1:5000")
    print("   🔧 Modo: Standalone")
    print()

    try:
        # Crear aplicación
        app = create_app()

        # Configurar host y puerto
        host = '127.0.0.1'
        port = 5000
        url = f"http://{host}:{port}"

        print("💻 Iniciando servidor...")
        print("🔗 La aplicación estará disponible en:")
        print(f"   {url}")
        print()
        print("📱 Se abrirá automáticamente el navegador...")
        print("🛑 Presiona Ctrl+C para salir")
        print("=" * 40)

        # Abrir navegador en segundo plano
        open_browser(url)

        # Iniciar servidor
        app.run(
            host=host,
            port=port,
            debug=False,
            use_reloader=False,
            threaded=True
        )

    except KeyboardInterrupt:
        print("\n👋 Aplicación cerrada por el usuario")
        return 0
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

    return 0

if __name__ == '__main__':
    # Cambiar al directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Ejecutar aplicación
    exit_code = main()
    sys.exit(exit_code)
