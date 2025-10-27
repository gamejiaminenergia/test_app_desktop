#!/usr/bin/env python3
"""
Script de prueba para la API de la calculadora web.
Verifica que todas las operaciones funcionen correctamente.
"""

import requests
import json
import sys

BASE_URL = 'http://127.0.0.1:5000'

def test_calculation(num1, num2, operation, expected_result=None):
    """Prueba una operación matemática."""
    data = {
        'num1': num1,
        'num2': num2,
        'operation': operation
    }

    try:
        response = requests.post(f'{BASE_URL}/calculate', json=data, timeout=5)
        result = response.json()

        if response.status_code == 200 and 'result' in result:
            print(f"✅ {num1} {operation} {num2} = {result['result']}")
            if expected_result and abs(result['result'] - expected_result) > 0.001:
                print(f"   ⚠️  Resultado esperado: {expected_result}")
            print(f"   📝 Expresión: {result['expression']}")
        else:
            print(f"❌ Error en {num1} {operation} {num2}: {result.get('error', 'Error desconocido')}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

    return True

def test_single_operand_calculation(num1, operation, expected_result=None):
    """Prueba operaciones con un solo operando."""
    data = {
        'num1': num1,
        'operation': operation
    }

    try:
        response = requests.post(f'{BASE_URL}/calculate', json=data, timeout=5)
        result = response.json()

        if response.status_code == 200 and 'result' in result:
            print(f"✅ {operation}({num1}) = {result['result']}")
            if expected_result and abs(result['result'] - expected_result) > 0.001:
                print(f"   ⚠️  Resultado esperado: {expected_result}")
            print(f"   📝 Expresión: {result['expression']}")
        else:
            print(f"❌ Error en {operation}({num1}): {result.get('error', 'Error desconocido')}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

    return True

def main():
    """Ejecuta todas las pruebas."""
    print("🧮 Probando API de la Calculadora Web")
    print("=" * 50)

    # Verificar que el servidor esté corriendo
    try:
        response = requests.get(f'{BASE_URL}', timeout=5)
        if response.status_code != 200:
            print("❌ El servidor no está respondiendo correctamente")
            sys.exit(1)
    except requests.exceptions.RequestException:
        print("❌ No se puede conectar con el servidor. Asegúrate de que esté ejecutándose en http://127.0.0.1:5000")
        sys.exit(1)

    print("✅ Servidor funcionando correctamente\n")

    # Pruebas de operaciones básicas
    print("🔢 Operaciones Básicas:")
    test_calculation(10, 5, 'add', 15)
    test_calculation(10, 5, 'subtract', 5)
    test_calculation(10, 5, 'multiply', 50)
    test_calculation(10, 5, 'divide', 2)
    test_calculation(2, 0, 'divide')  # Debería dar error

    print("\n🔥 Operaciones Avanzadas:")
    test_calculation(2, 3, 'power', 8)
    test_single_operand_calculation(16, 'sqrt', 4)
    test_single_operand_calculation(-4, 'sqrt')  # Debería dar error
    test_calculation(10, 20, 'percentage', 2)

    print("\n🎯 Pruebas Adicionales:")
    test_calculation(3.14, 2.71, 'add', 5.85)
    test_calculation(-5, 3, 'multiply', -15)
    test_calculation(100, 25, 'percentage', 25)

    print("\n" + "=" * 50)
    print("✅ Todas las pruebas completadas!")

if __name__ == '__main__':
    main()
