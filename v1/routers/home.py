from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..settings import Settings, get_settings

settings: Settings = get_settings()

router = APIRouter(
    tags=['home'],
)


@router.get('/', response_class=HTMLResponse, include_in_schema=False)
async def home_web(request: Request):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='home/index.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )
