from fastapi import APIRouter
from app.schemas.restaurante_schema import RestauranteCriacaoSchema
from app.banco_de_dados import obter_sessao
from app.services import restaurante_service

router = APIRouter()

@router.post("/restaurantes")
def criar(dados_entrada_restaurante: RestauranteCriacaoSchema):
    sessao_banco = obter_sessao()
    print(f"Dados recebidos no corpo da requisição: {dados_entrada_restaurante}")

    resposta = restaurante_service.criar(sessao_banco, dados_entrada_restaurante)
    return resposta