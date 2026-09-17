from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.schemas import LivroCreate, LivroUpdate, LivroResponse
from app import crud

# Cria as tabelas no MySQL automaticamente se nao existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catálogo de Livros API")


@app.get("/")
def home():
    return {"mensagem": "API de Catálogo de Livros no ar!"}


@app.post("/livros", response_model=LivroResponse, status_code=status.HTTP_201_CREATED)
def criar_novo_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    """Cadastra um novo livro no catálogo."""
    return crud.criar_livro(db=db, livro=livro)


@app.get("/livros", response_model=List[LivroResponse])
def listar_todos_livros(db: Session = Depends(get_db)):
    """Retorna a lista completa de livros cadastrados."""
    return crud.listar_livros(db=db)


@app.get("/livros/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    """Busca os detalhes de um livro específico pelo seu ID."""
    livro = crud.buscar_livro_por_id(db=db, livro_id=livro_id)
    if not livro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado"
        )
    return livro


@app.put("/livros/{livro_id}", response_model=LivroResponse)
def atualizar_dados_livro(livro_id: int, dados: LivroUpdate, db: Session = Depends(get_db)):
    """Atualiza as informações de um livro existente."""
    livro_atualizado = crud.atualizar_livro(
        db=db, livro_id=livro_id, dados_atualizados=dados)
    if not livro_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado para atualização"
        )
    return livro_atualizado


@app.delete("/livros/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_livro(livro_id: int, db: Session = Depends(get_db)):
    """Remove um livro do catálogo pelo ID."""
    sucesso = crud.deletar_livro(db=db, livro_id=livro_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado para remoção"
        )
    return None
