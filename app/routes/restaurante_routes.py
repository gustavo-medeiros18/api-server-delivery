from fastapi import (
    APIRouter
)
from app.schemas.restaurante_schema import RestauranteCriacaoSchema

router_restaurantes = APIRouter()

@router_restaurantes.post(
    "/restaurantes"
)
def criar(dados_entrada_restaurante: RestauranteCriacaoSchema):
    print(f"Dados recebidos: {dados_entrada_restaurante}")

    resposta = "Essa á e rota para criar um restaurante"
    return resposta
