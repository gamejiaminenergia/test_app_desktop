# 🧮 Calculadora Web Python

Aplicación web de calculadora moderna con arquitectura MVC y múltiples opciones de deployment.

## 🚀 Inicio Rápido

```bash
# Instalar dependencias
pip install -r config/requirements.txt

# Ejecutar en desarrollo
python src/app.py

# Instalar automáticamente (recomendado)
python scripts/setup.py
```

## 📚 Documentación Completa

Toda la documentación detallada está disponible en **[docs/README.md](docs/README.md)**

## 🏗️ Estructura del Proyecto

```
calculator-web/
├── 📄 README.md              # Inicio rápido y navegación
├── 📁 src/                   # Código fuente principal (MVC)
│   ├── app.py               # Punto de entrada y configuración
│   ├── models/              # Capa Modelo (Lógica de datos)
│   ├── routes/              # Capa Controlador (HTTP)
│   ├── static/              # Capa Vista (Recursos estáticos)
│   └── templates/           # Capa Vista (HTML)
├── 🔧 scripts/              # Scripts de utilidad
├── ⚙️ config/               # Configuración del proyecto
├── 🏗️ build/               # PyInstaller y distribuciones
├── 🧪 tests/                # Testing y pruebas
├── 📚 docs/                 # Documentación completa
└── 🐍 venv/                 # Entorno virtual
```

## ✨ Características Principales

- **🏗️ Arquitectura MVC completa** con separación clara de responsabilidades
- **📱 Interfaz responsiva** para móvil, tablet y desktop
- **⚡ Múltiples modos de ejecución**: desarrollo, producción con Gunicorn, ejecutable independiente
- **🧪 Testing automatizado** con cobertura completa
- **🔐 Validación robusta** y manejo de errores
- **📊 Sistema de logging** rotativo para producción
- **🚀 Ejecutable independiente** sin necesidad de Python instalado

## 🎯 Modos de Ejecución

### Desarrollo
```bash
python src/app.py
# Accede a: http://localhost:5000
```

### Producción (Gunicorn)
```bash
./scripts/start_gunicorn.sh
# Accede a: http://localhost:8000
```

### Ejecutable Independiente
```bash
# Ejecutar el ejecutable ya construido
./scripts/start_calculator_final.sh
# Accede a: http://localhost:8080
```

---

<div align="center">

**¡Proyecto completamente organizado y profesional! 🧹**

*Hecho con ❤️ usando mejores prácticas de desarrollo*

</div>
