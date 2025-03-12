from fastapi import FastAPI
from app.routes import products, orders, users

app = FastAPI()

# Registrar as rotas
app.include_router(products.router, prefix="/api", tags=["Produtos"])
app.include_router(orders.router, prefix="/api", tags=["Pedidos"])
app.include_router(users.router, prefix="/api", tags=["Usuários"])

# Incluindo as rotas
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "API do Pedido Fácil está rodando!"}
