# 🧮 Calculadora Web - Guía de Empaquetado a Ejecutable

Esta guía explica cómo convertir tu aplicación Flask en un ejecutable independiente que los usuarios pueden ejecutar sin instalar Python ni configurar entornos.

## 📋 ¿Qué es un ejecutable?

Un ejecutable es un archivo que contiene:
- Todo el código Python compilado
- Todas las dependencias (Flask, etc.)
- Todos los archivos estáticos (HTML, CSS, JS)
- Un mini-runtime de Python integrado

## 🚀 Proceso de Empaquetado

### Paso 1: Preparar el proyecto

```bash
# 1. Crear el script principal
# Ya tienes run_calculator.py creado

# 2. Instalar PyInstaller
pip install pyinstaller

# 3. Actualizar requirements.txt (ya hecho)
# Flask==3.0.0
# pyinstaller==6.10.0
```

### Paso 2: Crear el ejecutable

```bash
# Opción A: Usar el script automático (recomendado)
python build_executable.py

# Opción B: Usar PyInstaller directamente
pyinstaller --clean calculator.spec

# Opción C: Comando simple (puede requerir ajustes)
pyinstaller --onefile --windowed run_calculator.py
```

### Paso 3: Probar el ejecutable

```bash
# Linux/Mac
./start_calculator.sh

# Windows
start_calculator.bat

# O directamente:
./dist/CalculadoraWeb
```

## 📁 Archivos creados/modificados

### ✅ Archivos nuevos:
- `run_calculator.py` - Script principal optimizado para ejecutable
- `calculator.spec` - Configuración PyInstaller
- `build_executable.py` - Script de construcción automática
- `start_calculator.sh/bat` - Script de inicio fácil
- `EXECUTABLE_README.md` - Documentación del ejecutable

### ✅ Archivos modificados:
- `requirements.txt` - Agregado PyInstaller

## 🛠️ Configuración de PyInstaller

### Archivo `.spec` explicado:

```python
# calculator.spec

# Incluir archivos adicionales
added_files = [
    ('templates', 'templates'),    # Plantillas HTML
    ('static', 'static'),         # CSS, JS, imágenes
    ('models', 'models'),         # Lógica de negocio
    ('routes', 'routes'),         # Rutas de la API
]

# Excluir módulos innecesarios
excludes = [
    'tkinter',      # No usamos GUI de Tkinter
    'unittest',     # No necesitamos tests en el ejecutable
    'gunicorn',     # No necesitamos servidor WSGI
]

# Configuración del ejecutable
exe = EXE(
    name='CalculadoraWeb',      # Nombre del ejecutable
    console=True,               # Mostrar consola para ver logs
    debug=False,                # Sin modo debug
)
```

## 🔧 Opciones de PyInstaller

### Comandos útiles:

```bash
# Construcción básica
pyinstaller run_calculator.py

# Un solo archivo (más grande pero más portable)
pyinstaller --onefile run_calculator.py

# Sin consola (solo para Windows)
pyinstaller --windowed run_calculator.py

# Con icono (necesitas un .ico)
pyinstaller --icon=calculator.ico run_calculator.py

# Optimizar para tamaño
pyinstaller --upx-dir=/path/to/upx run_calculator.py

# Limpiar builds anteriores
pyinstaller --clean run_calculator.py
```

## 📦 Estructura del ejecutable final

```
dist/
├── CalculadoraWeb              # Ejecutable (Linux/Mac)
└── CalculadoraWeb/            # Carpeta con versión Windows
    ├── CalculadoraWeb.exe
    ├── templates/
    ├── static/
    ├── models/
    └── routes/

build_executable/               # Archivos temporales de construcción
```

## 🎯 Características del ejecutable

### ✅ Ventajas:
- **Independiente**: No requiere Python instalado
- **Portable**: Se puede copiar a cualquier PC
- **Automático**: Abre el navegador solo
- **Completo**: Incluye todo lo necesario

### ⚠️ Consideraciones:
- **Tamaño**: ~50-100MB (por el runtime de Python)
- **Velocidad**: Primera ejecución puede tardar unos segundos
- **Dependencias**: Incluye todas las librerías necesarias

## 🐛 Solución de problemas comunes

### Error: "No se encuentra el módulo"
```bash
# Agregar al archivo .spec
hiddenimports = [
    'flask',
    'jinja2',
    'werkzeug',
    # ... otros módulos
]
```

### Error: "Archivos faltantes"
```bash
# Asegurar que los archivos están en el directorio correcto
# Verificar que templates/, static/, models/ existen
```

### Ejecutable muy grande
```bash
# Usar UPX para comprimir
pyinstaller --upx-dir=/usr/bin/ run_calculator.py

# O excluir más módulos innecesarios
```

### No se abre el navegador
```bash
# Verificar que webbrowser funciona
# Abrir manualmente: http://127.0.0.1:5000
```

## 📋 Checklist antes de distribuir

- [ ] Ejecutable funciona en tu máquina
- [ ] Se abre el navegador automáticamente
- [ ] Todas las funciones de la calculadora trabajan
- [ ] No hay errores en la consola
- [ ] README incluido con instrucciones
- [ ] Script de inicio creado

## 🌟 Distribución

### Para usuarios finales:
1. Comparte la carpeta `dist/`
2. Incluye `start_calculator.sh` (Linux/Mac) o `start_calculator.bat` (Windows)
3. Incluye `EXECUTABLE_README.md` con instrucciones

### Para desarrolladores:
- Comparte todo el proyecto
- Incluye `build_executable.py` para reconstruir
- Documenta cualquier configuración especial

## 🔄 Actualizar el ejecutable

```bash
# 1. Hacer cambios en el código
# 2. Probar con python run_calculator.py
# 3. Reconstruir
python build_executable.py

# 4. Probar el nuevo ejecutable
./start_calculator.sh
```

## 📚 Recursos adicionales

- [PyInstaller Documentation](https://pyinstaller.readthedocs.io/)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/3.0.x/deploying/)
- [Creating Executables from Python Scripts](https://realpython.com/pyinstaller-python/)

---

**🎉 ¡Felicitaciones!** Tu aplicación Flask ahora es un ejecutable que cualquiera puede usar sin conocimientos técnicos.
