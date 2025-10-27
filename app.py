"""
Calculadora Web - Aplicación Flask con Arquitectura MVC
Punto de entrada principal que configura y ejecuta la aplicación.
"""

from flask import Flask, render_template, request
from routes import create_routes
import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logging(app: Flask):
    """
    Configura el sistema de logging de la aplicación.

    Args:
        app (Flask): Instancia de la aplicación Flask
    """
    # Configurar logging básico
    if not app.debug:
        # En producción, usar logging de archivos
        if not os.path.exists('logs'):
            os.makedirs('logs')

        file_handler = RotatingFileHandler(
            'logs/calculator.log',
            maxBytes=10240000,  # 10MB
            backupCount=10
        )

        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))

        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Calculator application startup')


def create_app(config_name: str = "development") -> Flask:
    """
    Factory function para crear la aplicación Flask.

    Args:
        config_name (str): Nombre de la configuración a usar

    Returns:
        Flask: Instancia de la aplicación configurada
    """
    app = Flask(__name__)

    # Configuración básica
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

    # Configuraciones específicas por entorno
    if config_name == "production":
        app.config.update(
            DEBUG=False,
            SECRET_KEY=os.environ.get('SECRET_KEY', 'production-secret-key'),
            # Otras configuraciones de producción
        )
    elif config_name == "testing":
        app.config.update(
            TESTING=True,
            DEBUG=True,
            SECRET_KEY='test-secret-key',
        )

    # Configurar logging
    setup_logging(app)

    # Registrar blueprint principal directamente
    main_bp = create_routes()
    app.register_blueprint(main_bp)

    # Configurar manejadores de errores
    @app.errorhandler(404)
    def not_found(error):
        """Manejo global de errores 404."""
        app.logger.warning(f'404 error: {request.url}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Manejo global de errores 500."""
        app.logger.error(f'500 error: {error}')
        return render_template('errors/500.html'), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        """Manejo global de excepciones no capturadas."""
        app.logger.error(f'Unhandled exception: {e}')
        return render_template('errors/500.html'), 500

    return app


def main():
    """Función principal para ejecutar la aplicación."""
    # Crear aplicación
    app = create_app()

    # Configuración del host y puerto
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    debug = app.config['DEBUG']

    print("🧮 Calculadora Web - Arquitectura MVC")
    print("=" * 50)
    print(f"📁 Estructura del proyecto:")
    print(f"   📂 models/     - Lógica de datos ({len(os.listdir('models'))} archivos)")
    print(f"   📂 routes/     - Definición de rutas ({len(os.listdir('routes'))} archivos)")
    print(f"   📂 templates/  - Vistas HTML ({len(os.listdir('templates'))} archivos)")
    print(f"   📂 static/     - Recursos estáticos")
    print()
    print(f"🚀 Iniciando servidor...")
    print(f"   🌐 URL: http://{host}:{port}")
    print(f"   🔧 Debug: {'Activado' if debug else 'Desactivado'}")
    print(f"   📊 Entorno: {'Desarrollo' if debug else 'Producción'}")
    print()
    print("📋 Endpoints disponibles:")
    print("   GET  /              - Interfaz web")
    print("   GET  /favicon.ico   - Favicon")
    print("   POST /calculate     - API de cálculos")
    print("   GET  /history       - Historial de operaciones")
    print("   DELETE /history     - Limpiar historial")
    print("   GET  /operations    - Operaciones disponibles")
    print("   GET  /health        - Verificación de salud")
    print("   GET  /api/info      - Información de la API")
    print()
    print("💡 Presiona Ctrl+C para detener el servidor")
    print("=" * 50)

    try:
        # Ejecutar la aplicación
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=True,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido por el usuario")
    except Exception as e:
        print(f"\n❌ Error iniciando la aplicación: {e}")
        return 1

    return 0


if __name__ == '__main__':
    # Ejecutar la aplicación
    exit_code = main()
    exit(exit_code)
else:
    # Crear instancia de la aplicación para gunicorn
    app = create_app("production")
