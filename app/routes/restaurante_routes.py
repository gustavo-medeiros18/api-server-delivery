from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from app.banco_de_dados import obter_banco
from app.schemas.restaurante_schema import (
    RestauranteAlteracao,
    RestauranteCriacao,
    RestauranteResposta,
    RestauranteEspecificoResposta
)
from app.services.restaurante_service import (
    criar_restaurante,
    listar_restaurantes,
    buscar_restaurante_por_id,
    deletar_restaurante,
    atualizar_restaurante
)

router_restaurantes = APIRouter(
    prefix="/restaurantes",
    tags=["Restaurantes"]
)

@router_restaurantes.post(
    "/",
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
