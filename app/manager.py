from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_con: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active_con.append(ws)


    async def disconnect(self, ws: WebSocket):
        self.active_con.remove(ws)


    async def broadcast(self, msg: str):
        for conn in self.active_con:
            await conn.send_text(msg)


