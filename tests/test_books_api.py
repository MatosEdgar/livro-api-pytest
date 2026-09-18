import pytest


def test_fluxo_completo_livro_api(api_context):

    novo_livro = {
        "titulo": "Entendendo Algoritmos",
        "autor": "Aditya Y. Bhargava",
        "preco": 65.00,
        "categoria": "Ciência da Computação"
    }

    resposta_post = api_context.post("/livros", data=novo_livro)
    assert resposta_post.status == 201

    dados_criados = resposta_post.json()
    assert dados_criados["titulo"] == novo_livro["titulo"]
    assert "id" in dados_criados

    livro_id = dados_criados["id"]

    resposta_get_todos = api_context.get("/livros")
    assert resposta_get_todos.status == 200

    lista_livros = resposta_get_todos.json()
    assert len(lista_livros) > 0
    assert any(livro["id"] == livro_id for livro in lista_livros)

    resposta_get_id = api_context.get(f"/livros/{livro_id}")
    assert resposta_get_id.status == 200
    assert resposta_get_id.json()["autor"] == novo_livro["autor"]

    dados_atualizados = {
        "titulo": "Entendendo Algoritmos",
        "autor": "Aditya Y. Bhargava",
        "preco": 72.90,
        "categoria": "Algoritmos & Estrutura de Dados"
    }

    resposta_put = api_context.put(
        f"/livros/{livro_id}", data=dados_atualizados)
    assert resposta_put.status == 200
    assert resposta_put.json()["preco"] == 72.90
    assert resposta_put.json(
    )["categoria"] == "Algoritmos & Estrutura de Dados"

    resposta_delete = api_context.delete(f"/livros/{livro_id}")
    assert resposta_delete.status == 204

    resposta_get_pos_delete = api_context.get(f"/livros/{livro_id}")
    assert resposta_get_pos_delete.status == 404
    assert resposta_get_pos_delete.json()["detail"] == "Livro não encontrado"
