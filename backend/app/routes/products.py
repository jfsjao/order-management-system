from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.schemas.products import ProdutoCreate, ProdutoResponse
from app.services.products import criar_produto, listar_produtos, atualizar_produto, deletar_produto

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/produtos", response_model=ProdutoResponse)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return criar_produto(db, produto)

@router.get("/produtos", response_model=list[ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return listar_produtos(db)

@router.put("/produtos/{id}", response_model=ProdutoResponse)
def atualizar(id: int, produto_update: ProdutoCreate, db: Session = Depends(get_db)):
    produto = atualizar_produto(db, id, produto_update)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.delete("/produtos/{id}", response_model=ProdutoResponse)
def deletar(id: int, db: Session = Depends(get_db)):
    produto = deletar_produto(db, id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
