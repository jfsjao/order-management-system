def test_criar_produto(client):
    response = client.post("/api/produtos", json={
        "nome": "Camiseta",
        "descricao": "Camiseta de algodão preta",
        "preco": 49.90,
        "estoque": 100
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Camiseta"

def test_listar_produtos(client):
    response = client.get("/api/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_atualizar_produto(client):
    response = client.put("/api/produtos/1", json={
        "nome": "Camiseta Atualizada",
        "descricao": "Camiseta de algodão azul",
        "preco": 59.90,
        "estoque": 50
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Camiseta Atualizada"

def test_deletar_produto(client):
    response = client.delete("/api/produtos/1")
    assert response.status_code == 200
