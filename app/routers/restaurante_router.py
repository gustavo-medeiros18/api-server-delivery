from fastapi import APIRouter, status
from app.schemas.restaurante_schema import RestauranteCriacaoSchema, RestauranteRespostaSchema
from app.banco_de_dados import obter_sessao
from app.services import restaurante_service

router = APIRouter()

@router.post(
    "/restaurantes",
    response_model=RestauranteRespostaSchema,
    status_code=status.HTTP_201_CREATED
)
def criar(dados_entrada_restaurante: RestauranteCriacaoSchema):
    sessao_banco = obter_sessao()

    try:
        resposta = restaurante_service.criar(sessao_banco, dados_entrada_restaurante)
    finally:
        sessao_banco.close()
    
    return resposta