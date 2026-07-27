from fastapi import APIRouter, HTTPException, status
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

@router.get(
    "/restaurantes",
    response_model=list[RestauranteRespostaSchema]
)
def listar():
    sessao_banco = obter_sessao()

    try:
        resposta = restaurante_service.listar(sessao_banco)
    finally:
        sessao_banco.close()

    return resposta

@router.delete(
    "/{restaurante_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar(
    restaurante_id: int
):
    sessao_banco = obter_sessao()

    try:
        restaurante_deletado = restaurante_service.deletar(
            sessao_banco,
            restaurante_id
        )

        if not restaurante_deletado:
            raise HTTPException(
                status_code=404,
                detail="Restaurante não encontrado"
            )
    finally:
        sessao_banco.close()

    return None