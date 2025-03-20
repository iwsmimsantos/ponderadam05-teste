import requests

# URL da API
api_url = 'https://two025-1a-t13-es05-api2.onrender.com/api/v1/institutions'

# Token do grupo 3 para autenticação
auth_token = 'Bearer g3-d72f4d0e90fce94208a9cc383c7e10ae7b'

def test_get_institutions():
    headers = {
        'Authorization': auth_token
    }

# Teste 1: Verificar se a API está no ar e autenticada
    response = requests.get(api_url, headers=headers)
    print("Teste 1 - Verificar se a API responde:", response.status_code, response.json())
    assert response.status_code == 200, "Falha: API não está respondendo corretamente."

    # Teste 2: Validar se há instituições na resposta
    assert len(response.json()) > 0, "Falha: Nenhuma instituição encontrada."

    print("✅ Todos os testes foram executados com sucesso!")

if __name__ == '__main__':
    test_get_institutions()
