from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str  # Adiciona senha no schema de criação

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
