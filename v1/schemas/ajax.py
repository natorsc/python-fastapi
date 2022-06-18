from pydantic import BaseModel


class AjaxBase(BaseModel):
    first_name: str
    last_name: str


class AjaxCreate(AjaxBase):
    pass
