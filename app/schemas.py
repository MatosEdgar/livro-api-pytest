from pydantic import BaseModel


class LivroBase(BaseModel):
    titulo: str
    autor: str
    preco: float
    categoria: str


class LivroCreate(LivroBase):
    pass


class LivroUpdate(LivroBase):
    pass


class LivroResponse(LivroBase):
    id: int

    class Config:
        from_attributes = True
