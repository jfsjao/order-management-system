from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define a URL do banco de dados (para PostgreSQL no Docker, por exemplo)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://pedido_facil_user:pedido_facil_pass@pedido_facil_db/pedido_facil_db")

# Criação do motor do banco de dados
engine = create_engine(DATABASE_URL)

# Criação da sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos do SQLAlchemy
Base = declarative_base()
