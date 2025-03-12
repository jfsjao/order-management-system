from sqlalchemy.orm import Session
from app.models.users import Usuario
from app.schemas.users import UsuarioCreate
from app.services.auth import hash_senha  # Se for usar autenticação

def criar_usuario(db: Session, usuario: UsuarioCreate):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        return None

    senha_hash = hash_senha(usuario.senha)  # Se for usar autenticação
    novo_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=senha_hash)
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()
