from pydantic import BaseModel
from typing import List

class PedidoBase(BaseModel):
    usuario_id: int
    produto_id: int
    quantidade: int
    total: float

class PedidoCreate(PedidoBase):
    pass

class PedidoResponse(PedidoBase):
    id: int

    class Config:
        from_attributes = True
