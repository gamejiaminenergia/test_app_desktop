# 🧮 Calculadora Web Python - Arquitectura MVC

Una aplicación web de calculadora moderna construida con **Flask** para el backend y **HTML/CSS/JavaScript vanilla** para el frontend, siguiendo el patrón **Modelo-Vista-Controlador (MVC)**.

## ✨ Características

- **Operaciones básicas**: suma, resta, multiplicación, división
- **Operaciones avanzadas**: potencias, raíz cuadrada, porcentaje
- **Interfaz responsiva**: funciona en móvil y desktop
- **Historial de operaciones**: guarda y muestra el historial
- **Validación de errores**: manejo robusto de errores (división por cero, etc.)
- **Soporte para teclado**: usa el teclado físico para operar
- **Diseño moderno**: interfaz limpia y atractiva

## 🚀 Instalación Rápida

### Prerrequisitos
- Python 3.8+
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona o descarga el proyecto**
   ```bash
   cd test_app_desktop
   ```

2. **Crea el entorno virtual**
   ```bash
   python3 -m venv venv
   ```

3. **Activa el entorno virtual**
   ```bash
   # En Linux/Mac:
   source venv/bin/activate

   # En Windows:
   venv\Scripts\activate
   ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

6. **Abre tu navegador**
   ```
   http://localhost:5000
   ```

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

### Estructura Final del Proyecto
```
calculator-web/
├── app.py              # Punto de entrada y configuración de la aplicación
├── models/             # Modelo (lógica de datos)
│   ├── __init__.py
│   └── calculator.py   # CalculatorModel - operaciones matemáticas
├── routes/             # Vista-Controlador (rutas y lógica HTTP)
│   └── __init__.py     # Blueprint principal con todas las rutas
├── static/             # Recursos estáticos (Vista)
│   ├── css/
│   │   └── style.css   # Estilos responsivos y modernos
│   └── js/
│       └── calculator.js # Lógica del frontend e integración API
├── templates/          # Plantillas HTML (Vista)
│   ├── index.html      # Interfaz principal de la calculadora
│   └── errors/         # Páginas de error
│       ├── 404.html    # Página de error 404
│       └── 500.html    # Página de error 500
├── requirements.txt    # Dependencias Python
├── test_api.py         # Suite de pruebas completa
├── setup.py           # Script de gestión e instalación
└── README.md          # Documentación completa
```

### Patrón MVC Implementado

**🧮 Modelo (Model)**:
- `CalculatorModel`: Encapsula toda la lógica matemática
- Maneja operaciones, validaciones y persistencia del historial
- Separado completamente de la lógica de presentación y HTTP

**🎮 Controlador-Vista (Controller-View)**:
- Blueprint principal que maneja todas las rutas HTTP
- Lógica de request/response y manejo de errores
- Integración directa entre el modelo y las vistas

**👁️ Vista (View)**:
- Templates HTML responsivos con diseño moderno
- CSS con variables, gradientes y animaciones
- JavaScript vanilla con integración completa de API
- Manejo visual de errores y estados

## 🧪 Pruebas

Para ejecutar las pruebas automáticas:

```bash
# Asegúrate de que el servidor esté corriendo
python test_api.py
```

Esto probará:
- ✅ Todas las operaciones matemáticas
- ✅ Manejo de errores (división por cero, etc.)
- ✅ Operaciones con números decimales
- ✅ Operaciones con números negativos

## 🔧 API Endpoints

### Rutas de la Calculadora (Controlador)
- **POST /calculate** - Realizar cálculos matemáticos
- **GET /history** - Obtener historial de operaciones
- **DELETE /history** - Limpiar historial
- **GET /operations** - Información de operaciones disponibles

### Rutas Principales
- **GET /** - Interfaz web de la calculadora
- **GET /health** - Verificación de salud del servicio
- **GET /api/info** - Información completa de la API

### Ejemplo de Request
```json
POST /calculate
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}

Response:
{
  "result": 15,
  "expression": "10.0 + 5.0 = 15.0"
}
```

## 🎨 Personalización

### Modificar colores
Edita las variables CSS en `static/css/style.css`:

```css
:root {
    --primary-color: #2563eb;    /* Color principal */
    --success-color: #059669;    /* Color de éxito */
    --error-color: #dc2626;      /* Color de error */
    /* ... más variables */
}
```

### Agregar operaciones
1. Agrega la operación en `app.py` en la función `perform_calculation`
2. Actualiza el frontend en `calculator.js`
3. Agrega el botón en `index.html`

## 🚨 Manejo de Erros

La aplicación maneja los siguientes errores:
- **División por cero**: Muestra mensaje de error
- **Raíz cuadrada de números negativos**: Muestra mensaje de error
- **Operaciones inválidas**: Muestra mensaje de error
- **Errores de conexión**: Fallback graceful

## 🔐 Seguridad

- Validación de todos los inputs
- Sanitización de datos del usuario
- Manejo seguro de errores (no exponer stack traces)
- Límites en el tamaño de números para prevenir overflow

## 📱 Responsive Design

- **Desktop**: Interfaz completa con todas las funciones
- **Tablet**: Adaptación automática del layout
- **Mobile**: Optimización para pantallas pequeñas

## 🤝 Contribuciones

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **Flask** por el framework web ligero
- **Modern CSS** por las capacidades de diseño responsivo
- **JavaScript Vanilla** por la lógica del frontend sin dependencias

---

**¡Disfruta calculando! 🧮**
