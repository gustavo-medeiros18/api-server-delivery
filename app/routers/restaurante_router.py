from fastapi import APIRouter

router = APIRouter()

@router.post("/restaurantes")
def criar():
    resposta = "Essa é a rota para criar um novo restaurante"
    return resposta