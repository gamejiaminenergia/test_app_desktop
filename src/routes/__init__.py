"""
Módulo de Rutas - Define y configura todas las rutas de la aplicación
Sigue el patrón Modelo-Vista-Controlador (MVC)
"""

from flask import Blueprint, render_template, request, jsonify, abort
from ..models.calculator import CalculatorModel
from typing import Dict, Any


def create_routes() -> Blueprint:
    """
    Crea y configura el blueprint principal con todas las rutas.

    Returns:
        Blueprint: Blueprint principal de la aplicación
    """
    # Crear blueprint principal
    main_blueprint = Blueprint('calc_web_mvc_app_2025', __name__)

    # Crear instancia del modelo
    calculator_model = CalculatorModel()

    @main_blueprint.route('/')
    def index():
        """Ruta principal que renderiza la interfaz."""
        return render_template('index.html')

    @main_blueprint.route('/favicon.ico')
    def favicon():
        """Ruta para favicon.ico - devuelve 204 No Content para evitar errores 404."""
        return '', 204

    @main_blueprint.route('/calculate', methods=['POST'])
    def calculate():
        """Endpoint para realizar cálculos."""
        try:
            # Obtener datos del request
            data = request.get_json()

            if not data:
                return jsonify({"error": "Error: Datos JSON requeridos"}), 400

            # Validar campos requeridos
            if 'num1' not in data or 'operation' not in data:
                return jsonify({"error": "Error: Campos 'num1' y 'operation' son requeridos"}), 400

            # Validar inputs usando el modelo
            validation_result = calculator_model.validate_inputs(
                data['num1'],
                data.get('num2'),
                data['operation']
            )

            if 'error' in validation_result:
                return jsonify(validation_result), 400

            # Realizar el cálculo
            result = calculator_model.perform_calculation(
                validation_result['num1'],
                validation_result['num2'],
                validation_result['operation']
            )

            return jsonify(result), 200

        except Exception as e:
            return jsonify({"error": "Error interno del servidor"}), 500

    @main_blueprint.route('/history', methods=['GET'])
    def get_history():
        """Obtiene el historial de operaciones."""
        try:
            history = calculator_model.get_history()
            return jsonify({"history": history}), 200
        except Exception as e:
            return jsonify({"error": "Error al obtener el historial"}), 500

    @main_blueprint.route('/history', methods=['DELETE'])
    def clear_history():
        """Limpia el historial de operaciones."""
        try:
            calculator_model.clear_history()
            return jsonify({"message": "Historial limpiado correctamente"}), 200
        except Exception as e:
            return jsonify({"error": "Error al limpiar el historial"}), 500

    @main_blueprint.route('/operations', methods=['GET'])
    def get_operations():
        """Obtiene información sobre las operaciones disponibles."""
        try:
            operations_info = calculator_model.get_operation_info()
            return jsonify({"operations": operations_info}), 200
        except Exception as e:
            return jsonify({"error": "Error al obtener información de operaciones"}), 500

    @main_blueprint.route('/health')
    def health_check():
        """Endpoint de verificación de salud."""
        return jsonify({
            "status": "healthy",
            "service": "Calculator Web API",
            "version": "2.0.0",
            "model": "MVC Architecture"
        }), 200

    @main_blueprint.route('/api/info')
    def api_info():
        """Información sobre la API."""
        return jsonify({
            "name": "Calculator Web API",
            "description": "API para calculadora web con arquitectura MVC",
            "version": "2.0.0",
            "endpoints": {
                "GET /": "Interfaz web de la calculadora",
                "GET /favicon.ico": "Favicon (204 No Content)",
                "POST /calculate": "Realizar cálculos matemáticos",
                "GET /history": "Obtener historial de operaciones",
                "DELETE /history": "Limpiar historial",
                "GET /operations": "Información de operaciones disponibles",
                "GET /health": "Verificación de salud del servicio",
                "GET /api/info": "Información de la API"
            },
            "supported_operations": [
                "add", "subtract", "multiply", "divide",
                "power", "sqrt", "percentage"
            ]
        }), 200

    @main_blueprint.errorhandler(404)
    def not_found(error):
        """Manejo de errores 404."""
        return jsonify({
            "error": "Endpoint no encontrado",
            "status_code": 404,
            "available_endpoints": [
                "/", "/favicon.ico", "/calculate", "/history", "/operations", "/health", "/api/info"
            ]
        }), 404

    @main_blueprint.errorhandler(500)
    def internal_error(error):
        """Manejo de errores 500."""
        return jsonify({
            "error": "Error interno del servidor",
            "status_code": 500
        }), 500

    @main_blueprint.errorhandler(405)
    def method_not_allowed(error):
        """Manejo de métodos HTTP no permitidos."""
        return jsonify({
            "error": "Método HTTP no permitido",
            "status_code": 405,
            "allowed_methods": request.method
        }), 405

    return main_blueprint


def register_all_routes(app):
    """
    Registra todos los blueprints en la aplicación Flask.

    Args:
        app: Instancia de la aplicación Flask
    """
    # Registrar blueprint principal
    main_bp = create_routes()
    app.register_blueprint(main_bp)

    print("✅ Todas las rutas registradas:")
    print("   - Blueprint principal: /")
    print("   - Todas las rutas en un solo blueprint")
