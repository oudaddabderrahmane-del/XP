from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json

from config.settings import settings
from config.database import init_db
from api.routes import router

init_db()

app = FastAPI(title="XP Platform API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# Serve the gg-platform frontend
GG_DIR = Path(__file__).parent.parent.parent / "gg-platform" / "frontend"
if GG_DIR.exists():
    app.mount("/gg", StaticFiles(directory=str(GG_DIR), html=True), name="gg")

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        self.active_connections.pop(user_id, None)

    async def send_personal_message(self, user_id: str, message: dict):
        ws = self.active_connections.get(user_id)
        if ws:
            try:
                await ws.send_json(message)
            except Exception:
                self.disconnect(user_id)

    async def broadcast(self, message: dict):
        for ws in self.active_connections.values():
            try:
                await ws.send_json(message)
            except Exception:
                pass

manager = ConnectionManager()

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            target = msg.get("to")
            if target:
                await manager.send_personal_message(target, {
                    "from": user_id,
                    "content": msg.get("content", ""),
                    "type": msg.get("type", "message"),
                    "timestamp": __import__("datetime").datetime.now().isoformat(),
                })
                # Echo back to sender
                await manager.send_personal_message(user_id, {
                    "to": target,
                    "content": msg.get("content", ""),
                    "type": "sent",
                    "timestamp": __import__("datetime").datetime.now().isoformat(),
                })
    except WebSocketDisconnect:
        manager.disconnect(user_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
