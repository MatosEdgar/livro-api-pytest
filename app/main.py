from fastapi import FastAPI

app = FastAPI(tittle="Catálogo de Livros API")


@app.get("/")
def home():
    return {"mensagem": "API de Catálogo de Livros no Ar!"}
