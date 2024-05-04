from httpx import get



def test_existem_usuarios():
    response = get('http://localhost:5000/users/')
    assert response.status_code == 200
    assert bool(response.json()) == True 

def test_usuario_especifico_existente():
    response = get('http://localhost:5000/users/')
    assert response.status_code == 200
    assert bool(response.json()) == True 
    usuarios = []
    for id,user in enumerate (response.json()['usuarios']):
        usuarios.append(
            user.get(str(id+1)).get('nome')
        )
    assert 'Alexandre' in usuarios

