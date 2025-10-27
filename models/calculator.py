"""
Modelo Calculator - Maneja todas las operaciones matemáticas
Sigue el patrón Modelo-Vista-Controlador (MVC)
"""

import math
from typing import Dict, Union, Optional


class CalculatorModel:
    """
    Modelo para la calculadora que maneja todas las operaciones matemáticas.

    Esta clase encapsula toda la lógica de cálculo y validación,
    separada de la lógica de presentación y control.
    """

    # Operaciones válidas
    VALID_OPERATIONS = {
        'add', 'subtract', 'multiply', 'divide',
        'power', 'sqrt', 'percentage'
    }

    def __init__(self):
        """Inicializa el modelo de la calculadora."""
        self.history = []

    def perform_calculation(self, num1: float, num2: Optional[float], operation: str) -> Dict[str, Union[float, str]]:
        """
        Realiza una operación matemática entre dos números.

        Args:
            num1 (float): Primer número
            num2 (float, optional): Segundo número (no requerido para sqrt)
            operation (str): Tipo de operación a realizar

        Returns:
            dict: Resultado de la operación y expresión matemática

        Raises:
            ValueError: Si la operación no es válida o hay errores matemáticos
        """
        if operation not in self.VALID_OPERATIONS:
            return {"error": "Error: Operación no válida"}

        try:
            if operation == "add":
                result = self._add(num1, num2)
                expression = f"{num1} + {num2} = {result}"
            elif operation == "subtract":
                result = self._subtract(num1, num2)
                expression = f"{num1} - {num2} = {result}"
            elif operation == "multiply":
                result = self._multiply(num1, num2)
                expression = f"{num1} × {num2} = {result}"
            elif operation == "divide":
                result = self._divide(num1, num2)
                expression = f"{num1} ÷ {num2} = {result}"
            elif operation == "power":
                result = self._power(num1, num2)
                expression = f"{num1}^{num2} = {result}"
            elif operation == "sqrt":
                result = self._sqrt(num1)
                expression = f"√{num1} = {result}"
            elif operation == "percentage":
                result = self._percentage(num1, num2)
                expression = f"{num2}% de {num1} = {result}"
            else:
                return {"error": "Error: Operación no implementada"}

            # Guardar en historial
            self._add_to_history(num1, num2, operation, result, expression)

            return {
                "result": result,
                "expression": expression
            }

        except Exception as e:
            error_msg = f"Error en el cálculo: {str(e)}"
            self._add_to_history(num1, num2, operation, None, error_msg, is_error=True)
            return {"error": error_msg}

    def _add(self, a: float, b: float) -> float:
        """Suma dos números."""
        return a + b

    def _subtract(self, a: float, b: float) -> float:
        """Resta dos números."""
        return a - b

    def _multiply(self, a: float, b: float) -> float:
        """Multiplica dos números."""
        return a * b

    def _divide(self, a: float, b: float) -> float:
        """Divide dos números con validación de división por cero."""
        if b == 0:
            raise ZeroDivisionError("División por cero no permitida")
        return a / b

    def _power(self, base: float, exponent: float) -> float:
        """Calcula la potencia de un número."""
        return math.pow(base, exponent)

    def _sqrt(self, number: float) -> float:
        """Calcula la raíz cuadrada con validación."""
        if number < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(number)

    def _percentage(self, total: float, percentage: float) -> float:
        """Calcula el porcentaje de un número."""
        return (total * percentage) / 100

    def _add_to_history(self, num1: float, num2: Optional[float], operation: str,
                       result: Optional[float], expression: str, is_error: bool = False):
        """
        Agrega una operación al historial.

        Args:
            num1 (float): Primer número
            num2 (float, optional): Segundo número
            operation (str): Operación realizada
            result (float, optional): Resultado de la operación
            expression (str): Expresión matemática
            is_error (bool): Si fue un error
        """
        history_item = {
            'num1': num1,
            'num2': num2,
            'operation': operation,
            'result': result,
            'expression': expression,
            'is_error': is_error,
            'timestamp': self._get_current_timestamp()
        }

        self.history.append(history_item)

        # Mantener solo los últimos 100 elementos
        if len(self.history) > 100:
            self.history = self.history[-100:]

    def _get_current_timestamp(self) -> str:
        """Obtiene la marca de tiempo actual."""
        import datetime
        return datetime.datetime.now().strftime("%H:%M:%S")

    def get_history(self) -> list:
        """Obtiene el historial de operaciones."""
        return self.history.copy()

    def clear_history(self):
        """Limpia el historial de operaciones."""
        self.history.clear()

    def validate_inputs(self, num1: Union[int, float, str], num2: Union[int, float, str, None],
                       operation: str) -> Dict[str, Union[float, str]]:
        """
        Valida los inputs antes de realizar la operación.

        Args:
            num1: Primer número
            num2: Segundo número (opcional)
            operation: Operación a validar

        Returns:
            dict: Resultado de validación o error
        """
        # Validar operación
        if operation not in self.VALID_OPERATIONS:
            return {"error": "Error: Operación no válida"}

        # Validar primer número
        try:
            num1 = float(num1)
        except (ValueError, TypeError):
            return {"error": "Error: El primer número debe ser válido"}

        # Para operaciones que requieren dos números
        if operation != 'sqrt':
            if num2 is None:
                return {"error": "Error: Se requiere un segundo número para esta operación"}

            try:
                num2 = float(num2)
            except (ValueError, TypeError):
                return {"error": "Error: El segundo número debe ser válido"}
        else:
            num2 = None

        return {
            "num1": num1,
            "num2": num2,
            "operation": operation
        }

    def get_operation_info(self) -> Dict[str, str]:
        """Obtiene información sobre las operaciones disponibles."""
        return {
            'add': 'Suma dos números',
            'subtract': 'Resta dos números',
            'multiply': 'Multiplica dos números',
            'divide': 'Divide dos números',
            'power': 'Calcula la potencia (base^exponente)',
            'sqrt': 'Calcula la raíz cuadrada',
            'percentage': 'Calcula el porcentaje de un número'
        }

    def __repr__(self) -> str:
        """Representación string del modelo."""
        return f"CalculatorModel(operations={len(self.VALID_OPERATIONS)}, history_items={len(self.history)})"
