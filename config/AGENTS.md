# AGENTS.md - Calculadora Web Python

## Descripción del Proyecto
Aplicación web de calculadora construida con Python usando Flask para el backend y HTML/CSS/JavaScript vanilla para el frontend.

## Stack Tecnológico
- **Backend**: Flask 3.0+
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Servidor de desarrollo**: Flask built-in server
- **Python**: 3.8+

## Estructura del Proyecto
```
calculator-web/
├── app.py              # Aplicación Flask principal
├── static/
│   ├── css/
│   │   └── style.css   # Estilos de la calculadora
│   └── js/
│       └── calculator.js  # Lógica del frontend
├── templates/
│   └── index.html      # Interfaz de usuario
├── requirements.txt    # Dependencias Python
└── AGENTS.md          # Este archivo
```

## Configuración del Entorno

### Instalación
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar la aplicación
```bash
# Modo desarrollo
python app.py

# La aplicación estará disponible en http://localhost:5000
```

## Funcionalidades Requeridas
- Operaciones básicas: suma, resta, multiplicación, división
- Operaciones avanzadas (opcional): raíz cuadrada, potencias, porcentaje
- Interfaz responsiva y amigable
- Validación de errores (división por cero, etc.)
- Historial de operaciones

## Convenciones de Código

### Python (Backend)
- Usar PEP 8 para estilo de código
- Nombres de funciones en snake_case
- Nombres de clases en PascalCase
- Agregar docstrings a todas las funciones
- Manejar excepciones apropiadamente

### JavaScript (Frontend)
- Usar camelCase para variables y funciones
- Preferir const/let sobre var
- Comentar lógica compleja
- Manejar errores con try-catch

### HTML/CSS
- Usar indentación de 2 espacios
- Nombres de clases en kebab-case
- Estructura semántica HTML5
- CSS organizado por componentes

## Rutas de la API

### POST /calculate
Realiza un cálculo matemático.

**Request body:**
```json
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}
```

**Response:**
```json
{
  "result": 15,
  "expression": "10 + 5 = 15"
}
```

**Operaciones válidas:** `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `percentage`

## Testing
```bash
# Ejecutar tests (si se implementan)
python -m pytest tests/

# Test manual
# Visitar http://localhost:5000 y probar cada operación
```

## Consideraciones de Seguridad
- Validar todos los inputs antes de procesarlos
- Sanitizar datos del usuario
- No exponer stack traces en producción
- Limitar tamaño de números para prevenir overflow

## Despliegue
Para producción, usar un servidor WSGI apropiado:
```bash
pip install gunicorn
gunicorn app:app
```

## Mejoras Futuras
- [ ] Agregar modo científico
- [ ] Implementar temas (claro/oscuro)
- [ ] Guardar historial en localStorage
- [ ] Soporte para teclado físico
- [ ] Animaciones de transición

## Notas para Agentes de IA
- Priorizar código simple y legible sobre optimizaciones prematuras
- Siempre incluir manejo de errores en operaciones matemáticas
- La división por cero debe retornar un mensaje de error claro
- Asegurar que la interfaz sea accesible (usar atributos ARIA cuando sea necesario)
- Comentar cualquier lógica matemática no obvia