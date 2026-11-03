# RESUMEN DE PROGRESO - APRENDIENDO PYTHON CON MIKE
**Usuario:** Bastian  
**Fecha:** 3 de Noviembre de 2026  
**Rama Git:** main  

---

## 📌 ESTADO ACTUAL DEL PROYECTO
Bastian está aprendiendo desarrollo fullstack desde cero combinando Python (Backend), FastAPI, HTML, CSS y JavaScript (Frontend).

### 1. Temas Ya Vistos y Dominados:
- Fundamentos de Python (variables, condicionales, bucles, funciones).
- Manejo de archivos en Python (`.txt`, `.json`, logs) en `dia10` y `dia12`.
- Arquitectura de APIs con FastAPI y Supabase (revisión del proyecto `Licorera_Donde_Jefer`).
- Clases y modelos de datos con Pydantic (`BaseModel`).

### 2. Proyecto en Curso: "El Chuzo de Bastian" (`Aprendiendo_Python/Chuzo_de_Bastian`)
Es un proyecto integrador construido 100% por Bastian para conectar todas las piezas:
- **Backend (`Backend/main.py`)**:
  - FastAPI configurado con CORS.
  - Modelo `Pedido` con Pydantic (`cliente`, `producto`, `precio`, `cantidad`).
  - Endpoint `@app.post("/pedido")` que guarda pedidos en `pedidos.json`.
  - Probado y verificado en Swagger (`http://127.0.0.1:8000/docs`).
- **Frontend (`Frontend/index.html` y `Frontend/styles.css`)**:
  - Diseño estilo comidas rápidas callejeras moderno (Hamburguesas, Salchipapas, Perros).
  - Formulario listo para ordenar.
- **Lógica Frontend (`Frontend/app.js`)**:
  - Ya tiene implementadas y probadas las funciones `seleccionarProducto` y `calcularTotal`.
  - Falta completar la conexión final: el `fetch` al endpoint `/pedido` cuando se envía el formulario para registrar la orden en vivo desde la web.

---

## 🚀 TAREAS PENDIENTES PARA RETOMAR:
1. Abrir `Frontend/app.js` y agregar el evento `submit` del formulario usando `fetch` (`POST http://127.0.0.1:8000/pedido`).
2. Probar el flujo completo: Usuario elige comida en la web -> Clic en Marchar Pedido -> FastAPI lo recibe -> Se guarda en `pedidos.json`.
3. (Opcional siguiente paso): Mostrar en la misma web la lista de pedidos en vivo leyendo con un `@app.get("/pedidos")`.
