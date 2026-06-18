from fastapi import (
    APIRouter
)

router_restaurantes = APIRouter()

@router_restaurantes.post(
    "/restaurantes"
)
def criar():
    resposta = "Essa á e rota para criar um restaurante"
    return resposta
