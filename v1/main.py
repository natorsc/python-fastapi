from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from .routers import home, todo
from .settings import Settings, get_settings

settings: Settings = get_settings()

app = FastAPI()
app.mount(
    path='/static',
    app=StaticFiles(directory=settings.STATIC_PATH),
    name='static',
)
app.include_router(home.router)
app.include_router(todo.router)


@app.get(path='/favicon.ico', response_class=FileResponse, include_in_schema=False)
async def favicon():
    return settings.FAVICON
