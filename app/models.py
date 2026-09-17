from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class LivroModel(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    autor = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    categoria = Column(String(50), nullable=False)
