# Fastapi SSE Notify

Proyecto demostrativo de notificaciones en tiempo real utilizando FastAPI y SSE. Cuenta con un backend en Python y un frontend basado en Jinja2, Bootstrap y JavaScript. Cada 10 segundos se generan notificaciones para dos usuarios (IDs "1" y "2") y se transmiten en formato JSON mediante SSE, permitiendo la reconexión automática en caso de pérdida de conexión.

## SSE
Esta basada en event stream

## Características

- **Backend en FastAPI:** Genera notificaciones cada 10 segundos para cada usuario.
- **Streaming de notificaciones:** Uso de SSE para enviar notificaciones en tiempo real.
- **Frontend dinámico:** Plantilla HTML con Jinja2, diseño con Bootstrap y JavaScript moderno para consumir el stream SSE.
- **Identificación de usuario:** El usuario se identifica mediante un parámetro `user_id` en la URL, filtrando sus notificaciones.

## Estructura del Proyecto

```
fastapi-sse-notify/
├── main.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── main.js
```

## Cómo Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/reiarseni/fastapi-sse-notify.git
   cd fastapi-sse-notify
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # En Linux/Mac
   venv\Scripts\activate         # En Windows
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   uvicorn main:app --reload --port=8000
   ```

5. **Acceder a la aplicación:**
   Abre el navegador y navega a:  
   `http://127.0.0.1:8000/?user_id=1`  
   (puedes cambiar el `user_id` a `1` o `2` según corresponda)

## Notas

- La reconexión automática en el SSE es gestionada por el navegador.
- El proyecto utiliza Bootstrap para una interfaz limpia y moderna.
- Las notificaciones se generan cada 10 segundos de forma asíncrona.

---

Este proyecto sirve como base para implementar sistemas de notificaciones en tiempo real utilizando tecnologías modernas en Python.

---

## ¿Qué es SSE?

Los **Server-Sent Events (SSE)** son una tecnología que permite al servidor enviar actualizaciones unidireccionales al cliente a través de una conexión HTTP persistente. Se usan comúnmente para notificaciones, actualizaciones en tiempo real o feeds de datos, donde el servidor “empuja” la información sin que el cliente tenga que solicitarla constantemente.

### Ventajas (Pros) de SSE

- **Simplicidad:** La implementación es relativamente sencilla. Basta con mantener una conexión HTTP abierta y enviar datos en formato de texto.
- **Reconexión Automática:** El navegador maneja la reconexión de manera automática en caso de pérdida de la conexión, lo que reduce la necesidad de lógica adicional en el cliente.
- **Uso de HTTP:** Se aprovechan las infraestructuras existentes (proxies, firewalls, etc.) ya que usa el protocolo HTTP.
- **Formato de Texto:** Al enviar datos en formato texto (generalmente JSON), es fácil de interpretar y depurar.

### Desventajas (Contras) de SSE

- **Unidireccionalidad:** SSE es ideal para comunicaciones unidireccionales. Si se necesita comunicación bidireccional en tiempo real, WebSockets puede ser una mejor opción.
- **Compatibilidad:** Aunque la mayoría de los navegadores modernos lo soportan, la compatibilidad en ciertos entornos o navegadores antiguos puede ser limitada.
- **Escalabilidad:** Al tener una conexión HTTP persistente por cliente, en escenarios con un número muy elevado de conexiones podría ser necesario un manejo cuidadoso de recursos.
- **Limitaciones en el Tamaño de Datos:** SSE no es ideal para transmitir grandes volúmenes de datos de manera continua, ya que está pensado para mensajes de tamaño relativamente pequeño.

### Comparación con WebSockets

- **Bidireccionalidad:**  
  - **WebSockets:** Permiten comunicación bidireccional en tiempo real, lo que es ideal para aplicaciones como chats o juegos en línea.  
  - **SSE:** Solo permite que el servidor envíe datos al cliente.
  
- **Complejidad y Uso:**  
  - **WebSockets:** Requieren una infraestructura y lógica un poco más compleja, tanto en el servidor como en el cliente, para gestionar la conexión y los mensajes.
  - **SSE:** Son más sencillos de implementar, especialmente si solo se necesita que el servidor envíe actualizaciones.
  
- **Reconexión:**  
  - **WebSockets:** La reconexión debe ser manejada explícitamente por el desarrollador en caso de desconexiones.
  - **SSE:** El navegador gestiona automáticamente la reconexión, simplificando el desarrollo en este aspecto.
  
- **Compatibilidad y Uso de Recursos:**  
  - **WebSockets:** Utilizan un protocolo diferente al HTTP, lo que puede requerir configuraciones adicionales en algunos entornos y consumir más recursos en conexiones altamente concurrentes.
  - **SSE:** Se integran directamente con HTTP, lo que facilita su despliegue en infraestructuras ya existentes, aunque pueden limitarse en aplicaciones de gran escala debido a la persistencia de conexiones.

### ¿Por qué se utiliza `StreamingResponse`?

La función `StreamingResponse(event_generator(user_id), media_type="text/event-stream")` se utiliza para:
- **Enviar datos de forma continua:** Permite al servidor enviar eventos al cliente a medida que se generan, sin necesidad de esperar a que se complete la respuesta.
- **Mantener una conexión persistente:** La respuesta se mantiene abierta para enviar múltiples eventos a lo largo del tiempo.
- **Especificar el tipo de medio:** El `media_type="text/event-stream"` informa al cliente (y al navegador) que se trata de una conexión SSE, lo que activa el comportamiento adecuado (por ejemplo, reconexión automática).

En resumen, **SSE** es una solución muy adecuada para notificaciones en tiempo real y actualizaciones periódicas donde la comunicación es unidireccional, ofreciendo una implementación sencilla y confiable en la mayoría de los casos. Sin embargo, para casos que requieren interacción bidireccional continua o manejo de grandes volúmenes de datos, **WebSockets** podría ser una opción más robusta, a costa de una mayor complejidad en el desarrollo y manejo de la infraestructura.