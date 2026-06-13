from fastapi import (
    APIRouter,
    Depends,
    status
)
from sqlalchemy.orm import Session

from app.banco_de_dados import obter_banco
from app.schemas.restaurante_schema import (
    RestauranteCriacao,
    RestauranteResposta
)
from app.services.restaurante_service import (
    criar_restaurante
)

router_restaurantes = APIRouter()

@router_restaurantes.post(
    path="/restaurantes",
    response_model=RestauranteResposta,
    status_code=status.HTTP_201_CREATED
)
def criar(
    restaurante: RestauranteCriacao,
    banco: Session = Depends(obter_banco)
):
    return criar_restaurante(
        banco,
        restaurante
    )
