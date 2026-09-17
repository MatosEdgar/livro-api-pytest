from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/livros_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    """Gera uma sessão de banco de dados por requisição e a fecha ao finalizar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
