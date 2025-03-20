# Teste Automatizado de API de Posts

Este repositório contém a implementação de um caso de teste automatizado para a API de posts disponível em https://two025-1a-t13-es05-api2.onrender.com.

## Descrição do Caso de Teste

**Objetivo:** Verificar se a API permite adicionar um novo post e recuperá-lo corretamente.

**Pré-condição:**

- API de posts está em execução e acessível
- O endpoint para criar posts está disponível em `/posts`
- O endpoint para buscar posts está disponível em `/posts/{id}`
- Possuir um token de acesso válido para autenticação

**Procedimento de teste:**

1. Enviar uma requisição POST para `/posts` com os dados do novo post e token de autenticação
2. Obter o ID do post criado na resposta
3. Enviar uma requisição GET para `/posts/{id}` usando o ID obtido
4. Verificar se os dados retornados correspondem aos dados enviados

**Resultado esperado:**

- A requisição POST retorna código 201 (Created)
- A requisição GET retorna código 200 (OK)
- Os dados do post retornado são idênticos aos enviados na criação

**Pós-condição:** Um novo post está persistido no sistema e pode ser recuperado pelo seu ID.

## Como executar o teste

1. Clone este repositório
2. Instale as dependências: `pip install requests`
3. Execute o teste: `python test_post_api.py`

## Tecnologias utilizadas

- Python
- Biblioteca requests
- API da turma: https://two025-1a-t13-es05-api2.onrender.com
