
# Projeto de Faturamento de Telecomunicações

## Descrição

Este projeto é um **sistema de faturamento de telecomunicações** desenvolvido em Python, utilizando o framework Django para o backend. A aplicação permite gerenciar e processar dados de faturamento de telecomunicações, incluindo registros de chamadas, usuários e custos associados.

## Requisitos do Projeto

### Requisitos Gerais

- **Python**: versão **>= 3.9**
- **Framework**: **Django**

### Ambiente de Desenvolvimento

- **Sistema Operacional**: macOS
- **Editor/IDE**: Visual Studio Code
- **Dependências**: Python >= 3.9, Django, Gunicorn, Django REST Framework, entre outras.

## Instruções de Instalação

### Setup Local

1. Clone este repositório para o seu computador:

   ```bash
   https://github.com/RhuanBorgesnr/telecom_billing.git
   cd telecom_billing
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```


4. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. (Opcional) Carregue dados de exemplo utilizando as **fixtures**:

   ```bash
   python manage.py loaddata dados_exemplo.json
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação no navegador:

   ```bash
   http://127.0.0.1:8000/api/
   ```

8. Acesse a documentação:

   ```bash
   http://127.0.0.1:8000/api/docs/
   ```


### Testes

Para rodar os testes do projeto, use o seguinte comando:

```bash
python manage.py test
```

## Documentação da API

A API deste projeto segue os princípios REST e oferece acesso aos dados de faturamento de telecomunicações através dos métodos HTTP padrões (GET, POST, PUT, DELETE).

### Endpoints

#### 1. `GET /api/bills/`

Retorna uma lista de todas as faturas.

- **Resposta**:
  - `200 OK`
  - Retorna um array de objetos de faturas.

#### 2. `POST /api/bills/`

Cria uma nova fatura de telecomunicação.

- **Corpo** (JSON):
  ```json
  {
    "numero_telefone": "123456789",
    "periodo": "2024-11-01",
    "custo_total": 50.00
  }
  ```
- **Resposta**:
  - `201 Created`
  - Retorna o objeto da fatura criada.

#### 3. `GET /api/bills/{id}/`

Retorna os detalhes de uma fatura específica pelo ID.

- **Resposta**:
  - `200 OK`
  - Retorna os detalhes da fatura.

#### 4. `PUT /api/bills/{id}/`

Atualiza uma fatura específica pelo ID.

- **Corpo** (JSON):
  ```json
  {
    "custo_total": 55.00
  }
  ```
- **Resposta**:
  - `200 OK`
  - Retorna o objeto da fatura atualizado.

#### 5. `DELETE /api/bills/{id}/`

Deleta uma fatura específica pelo ID.

- **Resposta**:
  - `204 No Content`
  - Sem conteúdo retornado.

## Ambiente de Trabalho

- **Sistema Operacional**: macOS
- **Editor/IDE**: Visual Studio Code
- **Versão do Python**: 3.9 ou superior
