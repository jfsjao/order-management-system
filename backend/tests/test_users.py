def test_criar_usuario(client):
    response = client.post("/api/usuarios", json={
        "nome": "Maria",
        "email": "maria@email.com",
        "senha": "123456"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "maria@email.com"

def test_listar_usuarios(client):
    response = client.get("/api/usuarios")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
