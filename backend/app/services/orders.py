from sqlalchemy.orm import Session
from app.models.orders import Pedido
from app.schemas.orders import PedidoCreate

def criar_pedido(db: Session, pedido: PedidoCreate):
    novo_pedido = Pedido(**pedido.model_dump())
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

def listar_pedidos(db: Session):
    return db.query(Pedido).all()
