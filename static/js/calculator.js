/**
 * Calculadora Web - Lógica del Frontend
 * Maneja la interfaz de usuario y la comunicación con el backend Flask.
 */

// Variables globales
let currentDisplay = '';
let previousDisplay = '';
let waitingForOperand = false;
let history = [];

// Elementos del DOM
const currentDisplayElement = document.getElementById('currentDisplay');
const previousDisplayElement = document.getElementById('previousDisplay');
const historyListElement = document.getElementById('historyList');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');

// Constantes para operaciones
const OPERATIONS = {
    ADD: 'add',
    SUBTRACT: 'subtract',
    MULTIPLY: 'multiply',
    DIVIDE: 'divide',
    POWER: 'power',
    SQRT: 'sqrt',
    PERCENTAGE: 'percentage'
};

/**
 * Inicializa la calculadora cuando se carga la página
 */
document.addEventListener('DOMContentLoaded', function() {
    // Cargar historial desde localStorage si existe
    loadHistoryFromStorage();

    // Agregar event listeners para el teclado
    setupKeyboardSupport();

    // Actualizar el estado del botón de limpiar historial
    updateClearHistoryButton();
});

/**
 * Configura el soporte para teclado físico
 */
function setupKeyboardSupport() {
    document.addEventListener('keydown', function(event) {
        // Prevenir el comportamiento por defecto para teclas que manejamos
        if (isCalculatorKey(event.key)) {
            event.preventDefault();
        }

        handleKeyboardInput(event.key);
    });
}

/**
 * Verifica si una tecla es relevante para la calculadora
 */
function isCalculatorKey(key) {
    const calculatorKeys = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '+', '-', '*', '/', '=', 'Enter', 'Escape', 'Backspace',
        '.', 'c', 'C', '%', '^'
    ];
    return calculatorKeys.includes(key);
}

/**
 * Maneja la entrada desde el teclado
 */
function handleKeyboardInput(key) {
    switch (key) {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            appendToDisplay(key);
            break;
        case '+':
            appendToDisplay('+');
            break;
        case '-':
            appendToDisplay('-');
            break;
        case '*':
            appendToDisplay('*');
            break;
        case '/':
            appendToDisplay('/');
            break;
        case '^':
            appendToDisplay('**');
            break;
        case '%':
            calculateAdvanced(OPERATIONS.PERCENTAGE);
            break;
        case '.':
            appendToDisplay('.');
            break;
        case '=':
        case 'Enter':
            calculate();
            break;
        case 'Escape':
        case 'c':
        case 'C':
            clearDisplay();
            break;
        case 'Backspace':
            deleteLast();
            break;
    }
}

/**
 * Agrega un valor al display actual
 */
function appendToDisplay(value) {
    // Evitar múltiples operadores seguidos (excepto ** para potencia)
    if (isOperator(value) && isOperator(currentDisplay.slice(-1)) && value !== '**') {
        return;
    }

    // Evitar múltiples puntos decimales
    if (value === '.' && currentDisplay.includes('.')) {
        return;
    }

    // Evitar punto decimal al inicio o después de un operador
    if (value === '.' && (currentDisplay === '' || isOperator(currentDisplay.slice(-1)))) {
        value = '0.';
    }

    // Evitar múltiples asteriscos para potencia
    if (value === '**' && currentDisplay.slice(-2) === '**') {
        return;
    }

    // Evitar empezar con operadores (excepto - para números negativos)
    if (isOperator(value) && currentDisplay === '' && value !== '-') {
        return;
    }

    currentDisplay += value;
    updateDisplay();
}

/**
 * Verifica si un carácter es un operador matemático
 */
function isOperator(char) {
    return ['+', '-', '*', '/', '**', '%', '^'].includes(char);
}

/**
 * Actualiza el display de la calculadora
 */
function updateDisplay() {
    currentDisplayElement.textContent = currentDisplay || '0';

    // Actualizar display anterior si hay una operación pendiente
    if (previousDisplay) {
        previousDisplayElement.textContent = previousDisplay;
    } else {
        previousDisplayElement.textContent = '';
    }
}

/**
 * Limpia completamente la calculadora
 */
function clearDisplay() {
    currentDisplay = '';
    previousDisplay = '';
    waitingForOperand = false;
    updateDisplay();
}

/**
 * Elimina el último carácter del display
 */
function deleteLast() {
    currentDisplay = currentDisplay.slice(0, -1);
    updateDisplay();
}

/**
 * Realiza un cálculo usando el backend Flask
 */
async function calculate() {
    if (currentDisplay === '') {
        return;
    }

    try {
        // Si no hay operadores, solo mostrar el número
        if (!hasOperator(currentDisplay)) {
            addToHistory(currentDisplay, currentDisplay);
            return;
        }

        // Preparar datos para el backend
        const calculationData = parseExpression(currentDisplay);

        if (!calculationData) {
            throw new Error('Expresión no válida');
        }

        // Mostrar la operación en el display anterior
        previousDisplay = currentDisplay;
        updateDisplay();

        // Realizar la petición al backend
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(calculationData)
        });

        const result = await response.json();

        if (response.ok) {
            // Mostrar resultado
            currentDisplay = result.result.toString();
            addToHistory(result.expression, currentDisplay);

            // Preparar para siguiente operación
            waitingForOperand = true;
        } else {
            // Mostrar error
            showError(result.error);
            addToHistory(currentDisplay, result.error, true);
        }

        updateDisplay();

    } catch (error) {
        console.error('Error en el cálculo:', error);
        showError('Error en la conexión con el servidor');
        addToHistory(currentDisplay, 'Error de conexión', true);
        updateDisplay();
    }
}

/**
 * Verifica si una expresión contiene operadores
 */
function hasOperator(expression) {
    return /[+\-*/^%]/.test(expression);
}

/**
 * Parsea una expresión matemática para enviarla al backend
 */
function parseExpression(expression) {
    // Para operaciones simples, usar el parser básico
    const simpleOperations = {
        '+': OPERATIONS.ADD,
        '-': OPERATIONS.SUBTRACT,
        '*': OPERATIONS.MULTIPLY,
        '/': OPERATIONS.DIVIDE,
        '**': OPERATIONS.POWER,
        '^': OPERATIONS.POWER
    };

    // Buscar el último operador para operaciones simples
    let lastOperator = null;
    let lastOperatorIndex = -1;

    for (const [symbol, operation] of Object.entries(simpleOperations)) {
        const index = expression.lastIndexOf(symbol);
        if (index > lastOperatorIndex) {
            lastOperatorIndex = index;
            lastOperator = operation;
        }
    }

    if (lastOperator && lastOperatorIndex > 0) {
        const num1 = expression.substring(0, lastOperatorIndex).trim();
        const num2 = expression.substring(lastOperatorIndex + 1).trim();

        if (num1 && num2) {
            return {
                num1: parseFloat(num1),
                num2: parseFloat(num2),
                operation: lastOperator
            };
        }
    }

    // Si no se puede parsear, intentar evaluar como expresión simple
    try {
        const num1 = parseFloat(expression);
        if (!isNaN(num1)) {
            return {
                num1: num1,
                operation: OPERATIONS.ADD  // Operación dummy para mostrar el número
            };
        }
    } catch (e) {
        return null;
    }

    return null;
}

/**
 * Realiza operaciones avanzadas que requieren un solo número
 */
async function calculateAdvanced(operation) {
    if (currentDisplay === '' || currentDisplay === '0') {
        return;
    }

    try {
        const num1 = parseFloat(currentDisplay);

        if (isNaN(num1)) {
            showError('Número no válido');
            return;
        }

        // Mostrar la operación en el display anterior
        previousDisplay = `${operation === OPERATIONS.SQRT ? '√' : operation}(${currentDisplay})`;
        updateDisplay();

        // Realizar la petición al backend
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                num1: num1,
                operation: operation
            })
        });

        const result = await response.json();

        if (response.ok) {
            currentDisplay = result.result.toString();
            addToHistory(result.expression, currentDisplay);
        } else {
            showError(result.error);
            addToHistory(previousDisplay, result.error, true);
        }

        updateDisplay();

    } catch (error) {
        console.error('Error en operación avanzada:', error);
        showError('Error en la conexión con el servidor');
        addToHistory(previousDisplay, 'Error de conexión', true);
        updateDisplay();
    }
}

/**
 * Muestra un mensaje de error temporal en el display
 */
function showError(message) {
    const originalDisplay = currentDisplay;
    currentDisplayElement.textContent = message;
    currentDisplayElement.style.color = 'var(--error-color)';

    // Restaurar después de 3 segundos
    setTimeout(() => {
        currentDisplay = originalDisplay;
        currentDisplayElement.style.color = '';
        updateDisplay();
    }, 3000);
}

/**
 * Agrega una operación al historial
 */
function addToHistory(operation, result, isError = false) {
    const historyItem = {
        operation: operation,
        result: result,
        timestamp: new Date().toLocaleTimeString(),
        isError: isError
    };

    history.unshift(historyItem);

    // Mantener solo los últimos 50 elementos
    if (history.length > 50) {
        history = history.slice(0, 50);
    }

    updateHistoryDisplay();
    saveHistoryToStorage();
    updateClearHistoryButton();
}

/**
 * Actualiza la visualización del historial
 */
function updateHistoryDisplay() {
    if (history.length === 0) {
        historyListElement.innerHTML = '<div class="history-item" style="color: var(--text-muted); font-style: italic;">No hay operaciones en el historial</div>';
        return;
    }

    historyListElement.innerHTML = history.map(item => {
        const errorClass = item.isError ? 'error' : '';
        return `
            <div class="history-item ${errorClass}">
                <div><strong>${item.operation}</strong></div>
                <div style="color: var(--text-secondary); font-size: 0.8rem;">${item.timestamp}</div>
                <div style="color: var(--text-primary); font-weight: 600;">= ${item.result}</div>
            </div>
        `;
    }).join('');
}

/**
 * Carga el historial desde localStorage y lo sincroniza con el backend
 */
function loadHistoryFromStorage() {
    try {
        const savedHistory = localStorage.getItem('calculatorHistory');
        if (savedHistory) {
            history = JSON.parse(savedHistory);
            updateHistoryDisplay();
            updateClearHistoryButton();
        }

        // Sincronizar con el backend
        syncHistoryWithBackend();
    } catch (error) {
        console.warn('No se pudo cargar el historial:', error);
        history = [];
    }
}

/**
 * Actualiza el estado del botón de limpiar historial
 */
function updateClearHistoryButton() {
    if (history.length === 0) {
        clearHistoryBtn.style.display = 'none';
    } else {
        clearHistoryBtn.style.display = 'block';
    }
}

/**
 * Guarda el historial en localStorage
 */
function saveHistoryToStorage() {
    try {
        localStorage.setItem('calculatorHistory', JSON.stringify(history));
    } catch (error) {
        console.warn('No se pudo guardar el historial:', error);
    }
}

/**
 * Sincroniza el historial con el backend
 */
async function syncHistoryWithBackend() {
    try {
        // Obtener historial del backend
        const response = await fetch('/history');
        if (response.ok) {
            const data = await response.json();

            if (data.history && data.history.length > 0) {
                // Actualizar historial local con el del backend
                history = data.history;
                updateHistoryDisplay();
                updateClearHistoryButton();

                // Guardar en localStorage también
                saveHistoryToStorage();

                console.log('✅ Historial sincronizado con el backend');
            }
        }
    } catch (error) {
        console.warn('No se pudo sincronizar el historial con el backend:', error);
    }
}

/**
 * Envía una operación al historial del backend
 */
async function sendToBackendHistory(operation, result, isError = false) {
    try {
        // Solo enviar si no es un error de conexión y hay una operación válida
        if (!isError || operation !== 'Error de conexión') {
            // El backend ya maneja el historial automáticamente
            // Esta función es para operaciones adicionales si es necesario
        }
    } catch (error) {
        console.warn('No se pudo enviar al historial del backend:', error);
    }
}

/**
 * Exporta el historial como archivo de texto
 */
function exportHistory() {
    if (history.length === 0) {
        alert('No hay historial para exportar');
        return;
    }

    let exportText = 'Historial de la Calculadora Web\n';
    exportText += '================================\n\n';

    history.forEach((item, index) => {
        exportText += `${index + 1}. ${item.operation}\n`;
        exportText += `   Resultado: ${item.result}\n`;
        exportText += `   Fecha: ${item.timestamp}\n\n`;
    });

    // Crear y descargar el archivo
    const blob = new Blob([exportText], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `calculadora-historial-${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

/**
 * Limpia el historial de operaciones tanto local como en el backend
 */
async function clearHistory() {
    try {
        // Limpiar en el backend primero
        const response = await fetch('/history', {
            method: 'DELETE'
        });

        if (response.ok) {
            history = [];
            updateHistoryDisplay();
            saveHistoryToStorage();
            updateClearHistoryButton();
            console.log('✅ Historial limpiado en backend y local');
        } else {
            console.warn('No se pudo limpiar el historial en el backend');
            // Continuar con limpieza local
            history = [];
            updateHistoryDisplay();
            saveHistoryToStorage();
            updateClearHistoryButton();
        }
    } catch (error) {
        console.warn('Error limpiando historial en backend:', error);
        // Fallback a limpieza local
        history = [];
        updateHistoryDisplay();
        saveHistoryToStorage();
        updateClearHistoryButton();
    }
}

/**
 * Actualiza el estado del botón de limpiar historial
 */
function updateClearHistoryButton() {
    if (history.length === 0) {
        clearHistoryBtn.style.display = 'none';
    } else {
        clearHistoryBtn.style.display = 'block';
    }
}
