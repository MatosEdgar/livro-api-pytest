# API de Catálogo de Livros 📚

API RESTful desenvolvida em Python utilizando FastAPI, SQLAlchemy e MySQL, com cobertura de testes automatizados via Pytest e Playwright.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **ORM:** SQLAlchemy
* **Driver do Banco:** PyMySQL
* **Banco de Dados:** MySQL
* **Testes Automatizados:** Pytest + Playwright

---

## 📁 Estrutura do Projeto

livro-api-pytest/
│
├── app/
│   ├── __init__.py
│   ├── database.py       # Conexão e sessão do MySQL
│   ├── models.py         # Modelo SQLAlchemy da tabela livros
│   ├── schemas.py        # Validações Pydantic
│   ├── crud.py           # Lógica de persistência no banco
│   └── main.py           # Rotas e endpoints da API
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py       # Fixtures e contexto do Playwright
│   └── test_books_api.py # Cenários de teste automatizados
│
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt      # Lista de dependências do projeto
└── README.md             # Documentação do projeto

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
git clone https://github.com/SEU-USUARIO/livro-api-pytest.git
cd livro-api-pytest

2. Crie e ative o ambiente virtual:
python -m venv venv
* Windows: .\venv\Scripts\activate
* Linux/macOS: source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt
playwright install

4. Configure o Banco de Dados:
Ajuste a senha no arquivo app/database.py de acordo com suas credenciais do MySQL e crie o banco no MySQL Workbench:
CREATE DATABASE IF NOT EXISTS livros_db;

5. Inicie a aplicação:
uvicorn app.main:app --reload

Acesse a documentação interativa em: http://127.0.0.1:8000/docs

---

## 🧪 Executando os Testes

Com a API rodando em um terminal, abra outro terminal e execute:

pytest -v