from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão: mysql+pymysql://usuario:senha@host:porta/nome_do_banco
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/livros_db"

# Engine responsável por gerenciar as conexões com o MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criador de sessões para executar operações no banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base da qual os modelos das tabelas irão herdar
Base = declarative_base()


def get_db():
    """Gera uma sessão de banco de dados por requisição e a fecha ao finalizar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
