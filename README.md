# Teste Automatizado de API

Este repositório contém a implementação de um caso de teste automatizado para a API da turma disponível em https://two025-1a-t13-es05-api2.onrender.com.

## Descrição do Caso de Teste

| **Descrição do Caso de Teste** | **Detalhes**                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Objetivo**                   | Verificar se a API retorna corretamente uma lista de instituições e valida as respostas da requisição.                                                                                                                                                                                                                                                                              |
| **Pré-condição**               | - A API está em execução e acessível. <br> - Possuir um token de acesso válido para autenticação. <br> - O endpoint para recuperar dados da API de instituições está disponível em `/api/v1/institutions`.                                                                                                                                                                          |
| **Procedimento de Teste**      | 1. Enviar uma requisição GET para o endpoint `/api/v1/institutions`, incluindo o token de autenticação nos cabeçalhos. <br> 2. Verificar se a resposta contém o código de status `200` (OK). <br> 3. Verificar se a resposta contém uma lista de instituições (não vazia). <br> 4. Validar se a resposta contém os dados corretos das instituições, com base na estrutura esperada. |
| **Resultado Esperado**         | - A requisição GET deve retornar o código `200` (OK), indicando que a API está acessível e funcionando corretamente. <br> - A resposta deve conter uma lista com pelo menos uma instituição, mostrando que a API está retornando dados de maneira adequada.                                                                                                                         |
| **Resultado Obtido**           | - A requisição GET retornou o código `200` (OK), confirmando que a API está acessível. <br> - A resposta continha uma lista com instituições, conforme esperado, com pelo menos um item de dados.                                                                                                                                                                                   |
| **Pós-condição**               | A API foi validada com sucesso, e a resposta foi verificada para garantir que está retornando dados de instituições corretamente.                                                                                                                                                                                                                                                   |

## Como executar o teste

1. Clone este repositório
2. Instale as dependências: `pip install requests`
3. Execute o teste: `python test_post_api.py`

## Tecnologias utilizadas

- Python
- Biblioteca requests
- API da turma: https://two025-1a-t13-es05-api2.onrender.com
