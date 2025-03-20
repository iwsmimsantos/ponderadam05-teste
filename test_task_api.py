import requests

# URL da API
api_url = 'https://two025-1a-t13-es05-api2.onrender.com/api/v1/institutions'

# Token do grupo 3 para autenticação
auth_token = 'Bearer g3-d72f4d0e90fce94208a9cc383c7e10ae7b'

def test_get_institutions():
    headers = {
        'Authorization': auth_token
    }
