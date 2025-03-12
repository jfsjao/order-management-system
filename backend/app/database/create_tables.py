from app.database import engine, Base
from app.models import Produto, Usuario, Pedido  # Importe todos os modelos necessários

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")
