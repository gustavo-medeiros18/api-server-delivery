from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.banco_de_dados import obter_banco
from app.schemas.restaurante_schema import RestauranteCriacaoSchema, RestauranteResposta
from app.services import restaurante_service

router = APIRouter()

@router.post(
    "/restaurantes",
    response_model=RestauranteResposta,
    status_code=status.HTTP_201_CREATED
)
def criar(
    restaurante: RestauranteCriacaoSchema
): 
    try:
        banco = obter_banco()
        restaurante_criado = restaurante_service.criar(
            banco,
            restaurante
        )
    finally:
        banco.close()

    return restaurante_criado