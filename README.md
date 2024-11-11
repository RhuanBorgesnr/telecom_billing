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

## URLs da Documentação

A aplicação possui documentação interativa utilizando o drf-spectacular. Você pode acessar os seguintes endpoints para consultar a API e sua documentação:

Swagger Docs (para visualizar a documentação interativa da API):

http://127.0.0.1:8000/api/docs/
Esquema da API (para obter o schema em formato JSON):

http://127.0.0.1:8000/api/schema/

Aplicação online (acesse a aplicação em produção):

https://telecom-billing.onrender.com/api/

## Documentação da API

A API deste projeto segue os princípios REST e oferece acesso aos dados de faturamento de telecomunicações através dos métodos HTTP padrões (GET, POST, PUT, DELETE).


## Endpoint principal

#### 3. `/api/call-records/bill/` [GET]

Este endpoint retorna o custo da chamada baseado no número de telefone e período fornecidos. Exemplo de uso:

```
GET /api/call-records/bill/?phone_number=99988526423&period=2017-12
```

**Exemplo de resposta:**

```json
{
    "id": 41,
    "phone_number": "99988526423",
    "period": "2018-05-01",
    "total_cost": "13.50",
    "call_records": [
        {
            "id": 17,
            "type": "start",
            "timestamp": "2018-05-10T08:00:00Z",
            "call_id": "78",
            "source": "99988526423",
            "destination": "9933468278"
        }
    ]
}
```
## Ambiente de Trabalho

- **Sistema Operacional**: macOS
- **Editor/IDE**: Visual Studio Code
- **Versão do Python**: 3.9 ou superior
