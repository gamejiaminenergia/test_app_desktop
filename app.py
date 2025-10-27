"""
Calculadora Web - Entry point para gunicorn
Este archivo permite que gunicorn ejecute la aplicación desde la raíz.
"""

import sys
import os

# Agregar src al PYTHONPATH para que los imports relativos funcionen
src_path = os.path.join(os.path.dirname(__file__), 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Importar la aplicación desde src
from src.app import create_app

# Crear la aplicación en modo producción
app = create_app("production")

if __name__ == '__main__':
    # Para desarrollo
    from src.app import main
    main()
else:
    # Para gunicorn - la aplicación ya está creada arriba
    pass
