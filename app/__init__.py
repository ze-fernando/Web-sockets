from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .main import api_route

app=FastAPI()

app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
)



app.include_router(api_route)
