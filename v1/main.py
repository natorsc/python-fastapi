from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from .routers import home
from .routers import todo
from .settings import Settings, get_settings

settings: Settings = get_settings()

# Para criar as tabelas no banco de dados, usar alembic no futuro.
from .database import Base, engine
Base.metadata.create_all(bind=engine)

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
