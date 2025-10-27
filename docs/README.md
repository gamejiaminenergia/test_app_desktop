# 🧮 Calculadora Web Python - Arquitectura MVC Completa + Ejecutable Independiente

Una aplicación web de calculadora moderna construida con **Flask** para el backend y **HTML/CSS/JavaScript vanilla** para el frontend, siguiendo el patrón **Modelo-Vista-Controlador (MVC)**. Incluye **múltiples opciones de despliegue** desde desarrollo hasta ejecutable completamente independiente.

## ✨ Características Principales

- **🧮 Operaciones completas**: básicas (suma, resta, multiplicación, división) y avanzadas (potencias, raíz cuadrada, porcentaje)
- **🏗️ Arquitectura MVC**: código bien estructurado y mantenible
- **📱 Interfaz responsiva**: funciona perfectamente en móvil, tablet y desktop
- **🔄 Historial inteligente**: guarda y sincroniza operaciones entre frontend y backend
- **⚡ Múltiples modos de ejecución**: desarrollo, producción con Gunicorn, y ejecutable independiente
- **🛡️ Validación robusta**: manejo completo de errores y casos edge
- **⌨️ Soporte para teclado**: usa el teclado físico para operar
- **🎨 Diseño moderno**: interfaz limpia con gradientes y animaciones
- **📊 Logging completo**: sistema de logs rotativo para producción
- **🧪 Suite de pruebas**: testing automatizado de todas las funcionalidades

## 🚀 Instalación y Ejecución

### 🔧 Prerrequisitos
- Python 3.8+ (para desarrollo)
- pip (gestor de paquetes de Python)
- No se requieren dependencias del sistema

### 📦 Instalación Automática (Recomendado)

```bash
# Ejecutar el script de instalación automática
python scripts/setup.py
```

Este script:
- ✅ Verifica la versión de Python
- ✅ Crea el entorno virtual
- ✅ Instala todas las dependencias
- ✅ Ejecuta las pruebas
- ✅ Inicia la aplicación

### 🖥️ Modo Desarrollo (Tradicional)

```bash
# 1. Crear entorno virtual
python3 -m venv venv

# 2. Activar entorno virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\\Scripts\\activate

# 3. Instalar dependencias
pip install -r config/requirements.txt

# 4. Ejecutar en modo desarrollo
python src/app.py
```

### 🏭 Modo Producción (Gunicorn)

```bash
# Ejecutar con Gunicorn (producción)
./scripts/start_gunicorn.sh

# O directamente:
PYTHONPATH=/home/alde/Escritorio/test_app_desktop gunicorn app:app --bind 127.0.0.1:8000
```

## 🚀 Ejecutable Independiente (Sin Python)

> **¡REVOLUCIONARIO!** Convierte tu aplicación Flask en un ejecutable completamente independiente.

### ⚡ Opción 1: Ejecutable Completo (Recomendado)

```bash
# El ejecutable ya está construido
./scripts/start_calculator_final.sh
```

### ⚡ Opción 2: Reconstruir Ejecutable

```bash
# Construir el ejecutable más avanzado
pyinstaller --clean build/calculator_final.spec

# Ejecutar con script automático
./scripts/start_calculator_final.sh
```

### ⚡ Opción 3: Script Python Independiente

```bash
# Ejecutar directamente (incluye todo embebido)
python build/calculator_final.py
```

### 🎯 ¿Qué hace el ejecutable?

- ✅ **100% Independiente**: No requiere Python ni dependencias
- ✅ **Automático**: Abre el navegador automáticamente
- ✅ **Completo**: Incluye Flask, templates, CSS, JavaScript, modelos y rutas
- ✅ **Portable**: Se puede copiar a cualquier PC o USB
- ✅ **Multiplataforma**: Funciona en Windows, Linux y Mac

**📖 Documentación completa:** [EJECUTABLE_FINAL_README.md](EJECUTABLE_FINAL_README.md)

## 🎯 Uso

### Operaciones Básicas
- **Números**: Haz clic en los botones 0-9 o usa el teclado
- **Operadores**: +, -, ×, ÷
- **Igual**: Presiona `=` o Enter para calcular
- **Limpiar**: Presiona `C` para limpiar todo o `⌫` para borrar el último carácter

### Operaciones Avanzadas
- **Potencia**: `^` (ej: `2^3 = 8`)
- **Raíz cuadrada**: `√` (ej: `√16 = 4`)
- **Porcentaje**: `%` (ej: `20% de 100 = 20`)

### Funciones Especiales
- **Historial**: Todas las operaciones se guardan automáticamente
- **Exportar historial**: Usa la función de exportar (disponible en JavaScript)
- **Soporte para teclado**: Usa tu teclado físico para operar
- **Responsive**: Funciona perfectamente en móviles

## 🏗️ Arquitectura MVC Implementada

### Estructura Completa del Proyecto
```
calculator-web/
├── 📄 README.md                       # Inicio rápido y navegación
├── 📁 src/                           # Código fuente principal (MVC)
│   ├── app.py                         # Punto de entrada y configuración
│   ├── models/                        # Capa Modelo (Lógica de datos)
│   │   ├── __init__.py
│   │   └── calculator.py              # CalculatorModel - operaciones
│   ├── routes/                        # Capa Controlador (HTTP)
│   │   └── __init__.py                # Blueprint principal
│   ├── static/                        # Capa Vista (Recursos estáticos)
│   │   ├── css/style.css              # Estilos responsivos
│   │   └── js/calculator.js           # Lógica del frontend
│   └── templates/                     # Capa Vista (HTML)
│       ├── index.html                 # Interfaz principal
│       └── errors/                    # Páginas de error
│           ├── 404.html
│           └── 500.html
├── 🔧 scripts/                       # Scripts de utilidad
│   ├── setup.py                       # Instalación automática
│   ├── build_executable.py            # Creación de ejecutables
│   ├── start_gunicorn.sh              # Servidor de producción
│   ├── start_calculator_final.sh      # Inicio ejecutable final
│   ├── start_calculator_portable.sh   # Inicio portable
│   └── run_calculator.py              # Script de ejecución
├── ⚙️ config/                        # Configuración del proyecto
│   ├── requirements.txt               # Dependencias Python
│   ├── .gitignore                     # Exclusiones de Git
│   └── AGENTS.md                      # Especificaciones originales
├── 🏗️ build/                        # PyInstaller y distribuciones
│   ├── *.spec                         # Configuraciones PyInstaller
│   ├── calculator_*.py                # Scripts de build
│   ├── dist/                          # Ejecutables generados
│   └── logs/                          # Logs de la aplicación
├── 🧪 tests/                         # Testing y pruebas
│   ├── test_api.py                    # Suite de pruebas API
│   └── test/                          # Tests adicionales
├── 📚 docs/                          # Documentación completa
│   ├── README.md                      # Documentación principal
│   ├── EJECUTABLE_FINAL_README.md    # Guía ejecutables
│   ├── EMPAQUETADO_README.md         # Proceso de empaquetado
│   └── EXECUTABLE_README.md          # Instrucciones usuarios
└── 🐍 venv/                          # Entorno virtual (auto-generado)
```

### Patrón MVC Implementado

**🧮 Modelo (Model)**:
- `CalculatorModel`: Encapsula toda la lógica matemática y operaciones
- Maneja validaciones, historial y persistencia de datos
- Completamente separado de la lógica de presentación y HTTP

**🎮 Controlador (Controller)**:
- Blueprint principal que maneja todas las rutas HTTP
- Lógica de request/response y manejo de errores
- Integración entre el modelo y las vistas

**👁️ Vista (View)**:
- Templates HTML responsivos con diseño moderno
- CSS con variables, gradientes y animaciones
- JavaScript vanilla con integración completa de API
- Manejo visual de errores y estados de la interfaz

## 🧪 Pruebas y Testing

### Pruebas Automáticas Completas

```bash
# Ejecutar suite de pruebas API
python tests/test_api.py

# Ejecutar con setup automático
python scripts/setup.py --test

# Pruebas durante instalación
python scripts/setup.py --install-with-tests
```

### Cobertura de Pruebas

✅ **Operaciones matemáticas básicas**:
- Suma, resta, multiplicación, división
- Números enteros y decimales
- Números positivos y negativos

✅ **Operaciones avanzadas**:
- Potencias y raíces cuadradas
- Porcentajes y cálculos complejos

✅ **Casos de error**:
- División por cero
- Raíz cuadrada de números negativos
- Inputs inválidos y tipos incorrectos

✅ **API REST**:
- Todos los endpoints HTTP
- Códigos de estado correctos
- Respuestas JSON válidas

✅ **Integración**:
- Frontend con backend
- Validación de datos
- Manejo de errores end-to-end

## 🔌 API Endpoints Completos

### Endpoints Principales (Controlador)

| Método | Endpoint | Descripción | Parámetros |
|--------|----------|-------------|------------|
| **GET** | `/` | Interfaz web principal | - |
| **GET** | `/favicon.ico` | Favicon (evita errores 404) | - |
| **POST** | `/calculate` | Realizar cálculos | `num1`, `num2`, `operation` |
| **GET** | `/history` | Obtener historial | - |
| **DELETE** | `/history` | Limpiar historial | - |
| **GET** | `/operations` | Operaciones disponibles | - |
| **GET** | `/health` | Verificación de salud | - |
| **GET** | `/api/info` | Información completa API | - |

### Operaciones Soportadas

```json
{
  "supported_operations": [
    "add",        // Suma: a + b
    "subtract",   // Resta: a - b
    "multiply",   // Multiplicación: a × b
    "divide",     // División: a ÷ b
    "power",      // Potencia: a ^ b
    "sqrt",       // Raíz cuadrada: √a
    "percentage"  // Porcentaje: a% de b
  ]
}
```

### Ejemplo de Request/Response

```bash
# Request
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "num1": 10,
    "num2": 5,
    "operation": "add"
  }'

# Response
{
  "result": 15,
  "expression": "10.0 + 5.0 = 15.0"
}
```

### Códigos de Estado HTTP

- **200 OK**: Operación exitosa
- **204 No Content**: Favicon (sin contenido)
- **400 Bad Request**: Datos inválidos
- **404 Not Found**: Endpoint no existe
- **405 Method Not Allowed**: Método HTTP incorrecto
- **500 Internal Server Error**: Error del servidor

## 📊 Logging y Monitoreo

### Sistema de Logs

La aplicación incluye un sistema de logging completo:

```bash
# Ver logs en tiempo real
tail -f build/logs/calculator.log

# Logs rotativos automáticos
# - Máximo 10MB por archivo
# - Hasta 10 archivos de respaldo
# - Formato: timestamp, nivel, mensaje, archivo:linea
```

### Información de Logs

- **INFO**: Inicio de aplicación, operaciones exitosas
- **WARNING**: Errores 404, parámetros sospechosos
- **ERROR**: Errores internos, excepciones no manejadas
- **DEBUG**: Información detallada (solo en desarrollo)

## 🚀 Deployment y Producción

### 🌐 Opciones de Deployment

#### **Opción 1: Gunicorn (Recomendado para producción)**
```bash
# Usando script automático
./start_gunicorn.sh

# Configuración personalizada
gunicorn app:app --bind 0.0.0.0:8000 --workers 4 --log-level info
```

#### **Opción 2: Ejecutable Independiente**
```bash
# Crear ejecutable
pyinstaller --clean calculator_final.spec

# Distribuir
# - Copiar carpeta `dist/`
# - Incluir `start_calculator_final.sh`
# - Funciona en cualquier PC sin Python
```

#### **Opción 3: Docker (Futuro)**
```bash
# Preparar para containerización
# Dockerfile y docker-compose.yml (planeado)
docker build -t calculator-web .
docker run -p 5000:5000 calculator-web
```

### ⚙️ Variables de Entorno

```bash
# Configuración de desarrollo
export FLASK_DEBUG=true
export SECRET_KEY=your-secret-key

# Configuración de producción
export FLASK_DEBUG=false
export SECRET_KEY=your-production-secret
export HOST=0.0.0.0
export PORT=8000
```

## 🔧 Configuración

### Archivo de Configuración Principal

El archivo `app.py` incluye configuración automática:

```python
# Configuración por defecto (desarrollo)
DEBUG = True
SECRET_KEY = 'dev-secret-key-change-in-production'

# Configuración de producción
# Cambiar SECRET_KEY a una clave segura
# Establecer DEBUG = False
# Configurar logging a archivos
```

### Logging por Entorno

- **Desarrollo**: Logs en consola con formato detallado
- **Producción**: Logs rotativos en `build/logs/calculator.log`
- **Testing**: Logs mínimos para pruebas rápidas

## 📚 Documentación Adicional

### Archivos README Especializados

- **[EJECUTABLE_FINAL_README.md](EJECUTABLE_FINAL_README.md)**: Guía completa para crear y usar ejecutables independientes
- **[EMPAQUETADO_README.md](EMPAQUETADO_README.md)**: Proceso detallado de empaquetado con PyInstaller
- **[EXECUTABLE_README.md](EXECUTABLE_README.md)**: Instrucciones para usuarios finales del ejecutable
- **[AGENTS.md](config/AGENTS.md)**: Especificaciones originales y requisitos del proyecto

### Scripts de Utilidad

| Script | Propósito | Uso |
|--------|-----------|-----|
| `scripts/setup.py` | Instalación automática | `python scripts/setup.py` |
| `scripts/start_gunicorn.sh` | Servidor de producción | `./scripts/start_gunicorn.sh` |
| `scripts/build_executable.py` | Crear ejecutables | `python scripts/build_executable.py` |
| `tests/test_api.py` | Testing completo | `python tests/test_api.py` |

## 🐛 Troubleshooting

### Problemas Comunes

#### **Error: "Module not found"**
```bash
# Solución: Instalar dependencias
pip install -r config/requirements.txt

# O usar instalación automática
python scripts/setup.py
```

#### **Error: "Port already in use"**
```bash
# Verificar qué usa el puerto
lsof -i :5000

# Cambiar puerto
export PORT=5001
python src/app.py
```

#### **Error: "Permission denied" (Linux/Mac)**
```bash
# Dar permisos de ejecución
chmod +x scripts/start_gunicorn.sh
chmod +x scripts/start_calculator_final.sh
```

#### **Error: "No module named 'flask'" (Ejecutable)**
```bash
# Reconstruir ejecutable
pyinstaller --clean build/calculator_final.spec

# Verificar que todos los archivos estén incluidos
```

### Debug y Diagnóstico

```bash
# Ver logs en tiempo real
tail -f build/logs/calculator.log

# Testing de API
python tests/test_api.py

# Verificación de salud
curl http://localhost:5000/health

# Información de API
curl http://localhost:5000/api/info
```

### Problemas de PyInstaller

```bash
# Limpiar builds anteriores
rm -rf build/ dist/ *.spec~ __pycache__/

# Reconstruir con verbose
pyinstaller --clean --debug build/calculator_final.spec

# Verificar dependencias ocultas
pyinstaller --hidden-import=pkg_resources build/calculator_final.spec
```

## 🚨 Manejo de Errores

### Errores de Aplicación

La aplicación maneja los siguientes errores automáticamente:

- **🔢 División por cero**: Retorna error amigable
- **📐 Raíz cuadrada de negativos**: Mensaje de error claro
- **❌ Operaciones inválidas**: Validación de inputs
- **🌐 Errores de conexión**: Fallback graceful
- **💾 Errores de historial**: Logging y recuperación

### Códigos de Error HTTP

- **200 OK**: Operación exitosa
- **400 Bad Request**: Datos inválidos
- **404 Not Found**: Endpoint no existe
- **405 Method Not Allowed**: Método HTTP incorrecto
- **500 Internal Server Error**: Error del servidor

## 🔐 Seguridad

### Medidas de Seguridad Implementadas

- ✅ **Validación estricta**: Todos los inputs son validados
- ✅ **Sanitización**: Datos del usuario son sanitizados
- ✅ **Error handling seguro**: No se exponen stack traces
- ✅ **Límites de números**: Prevención de overflow
- ✅ **HTTPS ready**: Configurable para producción
- ✅ **Secret keys**: Configuración de claves seguras

### Mejores Prácticas

```python
# Cambiar siempre la SECRET_KEY en producción
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secure-key-here')

# Usar HTTPS en producción
# Configurar headers de seguridad
# Limitar tamaño de requests
```

## 📱 Responsive Design

### Breakpoints y Adaptaciones

```css
/* Desktop First */
--desktop: 1200px+
--tablet: 768px - 1199px
--mobile: 320px - 767px

/* Características responsivas */
- Layout flexible con CSS Grid y Flexbox
- Botones adaptativos al tamaño de pantalla
- Fuentes escalables
- Touch-friendly en móviles
```

### Testing en Diferentes Dispositivos

- ✅ **Desktop**: Interfaz completa optimizada
- ✅ **Tablet**: Layout adaptado automáticamente
- ✅ **Mobile**: Optimización para pantallas pequeñas
- ✅ **Landscape/Portrait**: Adaptación a orientación

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor sigue estos pasos:

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### Estándares de Código

- **Python**: PEP 8 con type hints
- **JavaScript**: ES6+ con comentarios
- **CSS**: BEM methodology
- **HTML**: HTML5 semántico
- **Commits**: Mensajes descriptivos en inglés

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Tecnologías y Agradecimientos

### Stack Tecnológico
- **Backend**: Flask 3.0+ con Python 3.8+
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Arquitectura**: MVC (Model-View-Controller)
- **Deployment**: Gunicorn, PyInstaller
- **Testing**: requests, unittest patterns
- **Logging**: Python logging con rotación

### Agradecimientos Especiales

- **Flask** por el framework web ligero y flexible
- **PyInstaller** por hacer posible los ejecutables independientes
- **Modern CSS** por las capacidades de diseño responsivo
- **JavaScript ES6+** por la sintaxis moderna y limpia
- **Gunicorn** por el servidor WSGI de producción

---

<div align="center">

**¡Disfruta calculando! 🧮**

*Hecho con ❤️ usando tecnologías web modernas*

---
</div>
