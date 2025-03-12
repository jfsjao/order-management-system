from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True  # No Pydantic v2, substitui `orm_mode`
