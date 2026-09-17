from sqlalchemy.orm import Session
from app.models import LivroModel
from app.schemas import LivroCreate, LivroUpdate


def criar_livro(db: Session, livro: LivroCreate):
    db_livro = LivroModel(**livro.model_dump())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro


def listar_livros(db: Session):
    return db.query(LivroModel).all()


def buscar_livro_por_id(db: Session, livro_id: int):
    return db.query(LivroModel).filter(LivroModel.id == livro_id).first()


def atualizar_livro(db: Session, livro_id: int, dados_atualizados: LivroUpdate):
    db_livro = buscar_livro_por_id(db, livro_id)
    if not db_livro:
        return None

    for chave, valor in dados_atualizados.model_dump().items():
        setattr(db_livro, chave, valor)

    db.commit()
    db.refresh(db_livro)
    return db_livro


def deletar_livro(db: Session, livro_id: int):
    db_livro = buscar_livro_por_id(db, livro_id)
    if not db_livro:
        return False

    db.delete(db_livro)
    db.commit()
    return True
