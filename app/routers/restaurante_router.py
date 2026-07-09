from fastapi import APIRouter
from app.schemas.restaurante_schema import RestauranteCriacaoSchema

router = APIRouter()

@router.post("/restaurantes")
def criar(dados_entrada_restaurante: RestauranteCriacaoSchema):
    print(f"Dados recebidos no corpo da requisição: {dados_entrada_restaurante}")

    resposta = "Essa é a rota para criar um novo restaurante"
    return resposta