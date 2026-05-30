from fastapi import APIRouter


router_restaurantes = APIRouter(
    tags=["Restaurantes"]
)

@router_restaurantes.post("/restaurantes")
def criar():
    resposta = {
        "mensagem": "Rota POST /restaurantes"
    }
    return resposta

@router_restaurantes.get("/restaurantes")
def listar():
    resposta = {
        "mensagem": "Rota GET /restaurantes"
    }
    return resposta

@router_restaurantes.patch("/restaurantes/{restaurante_id}")
def atualizar():
    resposta = {
        "mensagem": "Rota PATCH /restaurantes"
    }
    return resposta

@router_restaurantes.delete("/{restaurante_id}")
def deletar():
    resposta = {
        "mensagem": "Rota DELETE /restaurantes"
    }
    return resposta