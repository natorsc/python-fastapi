from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from ..schemas.ajax import AjaxCreate
from ..settings import Settings, get_settings

CURRENT_DIRECTORY: Path = Path(__file__).resolve().parent
ROOT_DIR: Path = CURRENT_DIRECTORY.parent

AXIOS_FILE: Path = ROOT_DIR.joinpath('static', 'ajax', 'js', 'ajax-axios.js')
BRYTHON_FILE: Path = ROOT_DIR.joinpath(
    'static', 'ajax', 'js', 'ajax-brython.py')
FETCH_FILE: Path = ROOT_DIR.joinpath('static', 'ajax', 'js', 'ajax-fetch.js')
JQUERY_FILE: Path = ROOT_DIR.joinpath('static', 'ajax', 'js', 'ajax-jquery.js')
JSXMLHTTPREQUEST_FILE: Path = ROOT_DIR.joinpath(
    'static', 'ajax', 'js', 'ajax-jsxmlhttprequest.js'
)


router = APIRouter(
    prefix='/v1/ajax',
    tags=['Ajax'],
)


@router.get('/axios/web', response_class=HTMLResponse, include_in_schema=False)
async def axios_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    with open(AXIOS_FILE, 'r') as f:
        data: str = f.read()
        f.close()
    return templates.TemplateResponse(
        name='ajax/axios.html',
        context={'request': request, 'DEBUG': settings.DEBUG, 'data': data},
    )


@router.get('/brython/web', response_class=HTMLResponse, include_in_schema=False)
async def brython_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    with open(BRYTHON_FILE, 'r') as f:
        data: str = f.read()
        f.close()
    return templates.TemplateResponse(
        name='ajax/brython.html',
        context={'request': request, 'DEBUG': settings.DEBUG, 'data': data},
    )


@router.get('/fetch/web', response_class=HTMLResponse, include_in_schema=False)
async def fetch_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    with open(FETCH_FILE, 'r') as f:
        data: str = f.read()
        f.close()
    return templates.TemplateResponse(
        name='ajax/fetch.html',
        context={'request': request, 'DEBUG': settings.DEBUG, 'data': data},
    )


@router.get('/jquery/web', response_class=HTMLResponse, include_in_schema=False)
async def jquery_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    with open(JQUERY_FILE, 'r') as f:
        data: str = f.read()
        f.close()
    return templates.TemplateResponse(
        name='ajax/jquery.html',
        context={'request': request, 'DEBUG': settings.DEBUG, 'data': data},
    )


@router.get('/jsxmlhttprequest/web', response_class=HTMLResponse, include_in_schema=False)
async def jsxmlhttprequest_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    with open(JSXMLHTTPREQUEST_FILE, 'r') as f:
        data: str = f.read()
        f.close()
    return templates.TemplateResponse(
        name='ajax/jsxmlhttprequest.html',
        context={'request': request, 'DEBUG': settings.DEBUG, 'data': data},
    )


@router.get('/concatenate/names')
async def concatenate_name_by_get(first_name: str, last_name: str):
    return dict(first_name=first_name, last_name=last_name)


@router.post('/concatenate/names')
async def concatenate_name_by_post(person: AjaxCreate):
    print(person)
    return person
