from fastapi import (
    APIRouter, Request, WebSocket, WebSocketDisconnect
)
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .manager import ConnectionManager


ws_manager=ConnectionManager()
api_route=APIRouter()
templates=Jinja2Templates(directory='templates')



@api_route.get("/")
def route(req: Request, response_classe=HTMLResponse):
    return templates.TemplateResponse(
        'base.html', {'request': req}
    )


@api_route.websocket('/{user}')
async def push_end(ws: WebSocket, user: str):
    await ws_manager.connect(ws)
    try:
        while True:
            data=await ws.receive_text()
            await ws_manager.broadcast(data)
    except WebSocketDisconnect:
        await ws_manager.disconnect(ws)

