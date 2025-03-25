import asyncio
import json
from datetime import datetime
from uuid import uuid4
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Diccionario para almacenar notificaciones no leídas de cada usuario
notifications = {
    "1": [],
    "2": []
}

# Tarea en segundo plano para generar notificaciones cada 10 segundos
async def generate_notifications():
    while True:
        await asyncio.sleep(10)
        for user_id in notifications:
            notification = {
                "id": str(uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "message": f"Notificación para el usuario {user_id}"
            }
            notifications[user_id].append(notification)

# Iniciar la tarea en segundo plano al arrancar la aplicación
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(generate_notifications())

# Generador de eventos SSE para cada usuario
async def event_generator(user_id: str):
    last_index = 0
    while True:
        await asyncio.sleep(1)  # Verifica nuevas notificaciones cada segundo
        user_notifications = notifications.get(user_id, [])
        if last_index < len(user_notifications):
            new_notifications = user_notifications[last_index:]
            for notif in new_notifications:
                data = json.dumps(notif)
                yield f"data: {data}\n\n"
            last_index = len(user_notifications)

# Endpoint para la conexión SSE (se recibe el parámetro 'user_id')
@app.get("/notifications")
async def notifications_endpoint(user_id: str):
    return StreamingResponse(event_generator(user_id), media_type="text/event-stream")

# Endpoint raíz que renderiza la plantilla principal
@app.get("/", response_class=HTMLResponse)
async def get(request: Request, user_id: str):
    return templates.TemplateResponse("index.html", {"request": request, "user_id": user_id})

