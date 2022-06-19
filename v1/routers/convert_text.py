from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse

from ..settings import Settings, get_settings

router = APIRouter(
    prefix='/v1/convert/text',
    tags=['Conversor de texto'],
)


def check_text_size(data: str, max_size: int = 1024):
    text_size: int = len(data)
    if text_size > max_size:
        raise HTTPException(
            status_code=422,
            detail='O texto digitado é muito longo.<br>'
            f'Tamanho atual do texto = <b>{text_size}</b> caractere(s).<br>'
            f'Tamanho máximo permitido = <b>{max_size}</b> caractere(s).')


@router.get('/web', response_class=HTMLResponse, include_in_schema=False)
async def home_convert_text_html(request: Request, settings: Settings = Depends(get_settings)):
    templates = settings.TEMPLATES
    return templates.TemplateResponse(
        name='convert-text/index.html',
        context={'request': request, 'DEBUG': settings.DEBUG},
    )


@router.get('/capitalize')
async def text_capitalize(data: str):
    check_text_size(data=data)
    return {'detail': data.capitalize()}


@router.get('/lower')
async def text_lower(data: str):
    check_text_size(data=data)
    return {'detail': data.lower()}


@router.get('/upper')
async def text_upper(data: str):
    check_text_size(data=data)
    return {'detail': data.upper()}


@router.get('/title')
async def text_title(data: str):
    check_text_size(data)
    return {'detail': data.title()}
