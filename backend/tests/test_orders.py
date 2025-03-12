def test_criar_pedido(client):
    response = client.post("/api/pedidos", json={
        "cliente": "João",
        "total": 200.00
    })
    assert response.status_code == 200
    assert response.json()["cliente"] == "João"

def test_listar_pedidos(client):
    response = client.get("/api/pedidos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
