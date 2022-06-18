from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from ..schemas.ajax import AjaxCreate
from ..settings import Settings, get_settings

router = APIRouter(
    prefix='/v1/ajax',
    tags=['Ajax'],
)


@router.get('/axios/web', response_class=HTMLResponse, include_in_schema=False)
async def axios_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='ajax/axios.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/brython/web', response_class=HTMLResponse, include_in_schema=False)
async def brython_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='ajax/brython.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/fetch/web', response_class=HTMLResponse, include_in_schema=False)
async def fetch_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='ajax/fetch.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/htmx/web', response_class=HTMLResponse, include_in_schema=False)
async def htmx_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='ajax/htmx.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/jquery/web', response_class=HTMLResponse, include_in_schema=False)
async def jquery_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='ajax/jquery.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/jsxmlhttprequest/web', response_class=HTMLResponse, include_in_schema=False)
async def jsxmlhttprequest_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='ajax/jsxmlhttprequest.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/concatenate/names')
async def concatenate_name_by_get(first_name: str, last_name: str):
    return dict(first_name=first_name, last_name=last_name)


@router.post('/concatenate/names')
async def concatenate_name_by_post(person: AjaxCreate):
    return person
