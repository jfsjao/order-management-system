from sqlalchemy.orm import Session
from app.models.products import Produto
from app.schemas.products import ProdutoCreate

def criar_produto(db: Session, produto: ProdutoCreate):
    novo_produto = Produto(**produto.model_dump())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(Produto).all()

def atualizar_produto(db: Session, id: int, produto_update: ProdutoCreate):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        return None

    produto.nome = produto_update.nome
    produto.descricao = produto_update.descricao
    produto.preco = produto_update.preco
    produto.estoque = produto_update.estoque

    db.commit()
    db.refresh(produto)
    return produto

def deletar_produto(db: Session, id: int):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        return None

    db.delete(produto)
    db.commit()
    return produto
