# Calculadora Web - Ejecutable

Este ejecutable permite ejecutar la Calculadora Web sin necesidad de instalar Python o configurar entornos.

## 🚀 Cómo usar

### Opción 1: Script automático (Recomendado)
```bash
# Linux/Mac
./start_calculator.sh

# Windows
start_calculator.bat
```

### Opción 2: Ejecutable directo
```bash
# Linux/Mac
./dist/CalculadoraWeb

# Windows
.\dist\CalculadoraWeb\CalculadoraWeb.exe
```

## 📋 Lo que hace el ejecutable

1. **Inicia el servidor Flask** en http://127.0.0.1:5000
2. **Abre automáticamente el navegador** en la URL de la calculadora
3. **Muestra una interfaz moderna** con todas las funciones de la calculadora
4. **Ejecuta completamente independiente** sin necesidad de Python instalado

## 🔧 Funcionalidades incluidas

- ✅ Operaciones básicas (suma, resta, multiplicación, división)
- ✅ Operaciones avanzadas (potencia, raíz cuadrada, porcentaje)
- ✅ Historial de operaciones
- ✅ Interfaz responsiva (móvil y desktop)
- ✅ Validación de errores
- ✅ Soporte para teclado

## 🛠️ Construir desde código fuente

Si tienes el código fuente y quieres reconstruir el ejecutable:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Construir ejecutable
python build_executable.py

# 3. Ejecutar
./start_calculator.sh
```

## 📁 Estructura del ejecutable

```
dist/
├── CalculadoraWeb          # Ejecutable principal (Linux/Mac)
└── CalculadoraWeb/
    ├── CalculadoraWeb.exe  # Ejecutable principal (Windows)
    ├── templates/          # Plantillas HTML
    ├── static/            # CSS y JavaScript
    └── models/            # Lógica de la calculadora
```

## 🔧 Requisitos del sistema

- **Windows 10/11** o **Linux** (Ubuntu 18.04+, CentOS 7+, etc.)
- **macOS 10.15+** (para versiones de Mac)
- **4GB RAM** (recomendado)
- **100MB espacio en disco**

## 🐛 Solución de problemas

### El ejecutable no inicia
- Verifica que tienes permisos de ejecución
- En Linux/Mac: `chmod +x start_calculator.sh`

### No se abre el navegador
- Abre manualmente: http://127.0.0.1:5000
- Verifica que no haya firewall bloqueando el puerto 5000

### Error de archivos faltantes
- Asegúrate de que todos los archivos estén en el directorio correcto
- Ejecuta `python build_executable.py` para reconstruir

## 📄 Licencia

Este ejecutable incluye todo el código necesario para funcionar de forma independiente.

---
**Desarrollado con:** Flask, PyInstaller, HTML5, CSS3, JavaScript
