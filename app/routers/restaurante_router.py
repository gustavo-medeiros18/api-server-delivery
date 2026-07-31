from fastapi import APIRouter, status, HTTPException
from app.schemas.restaurante_schema import RestauranteCriacaoSchema, RestauranteRespostaSchema, RestauranteAlteracaoSchema
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

@router.patch(
    "/restaurantes/{id_restaurante_atualizar}",
    response_model=RestauranteRespostaSchema
)
def atualizar(id_restaurante_atualizar: int, dados_atualizacao_restaurante: RestauranteAlteracaoSchema):
    sessao_banco = obter_sessao()

    try:
        restaurante_atualizado = restaurante_service.atualizar(
            sessao_banco,
            id_restaurante_atualizar,
            dados_atualizacao_restaurante
        )

        if restaurante_atualizado == None:
            raise HTTPException(
                status_code=404,
                detail="Restaurante não encontrado"
            )

        return restaurante_atualizado
    finally:
        sessao_banco.close()

@router.delete(
    "/restaurantes/{id_restaurante_excluir}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir(id_restaurante_excluir: int):
    sessao_banco = obter_sessao()

    try:
        restaurante_excluido = restaurante_service.excluir(sessao_banco, id_restaurante_excluir)

        if restaurante_excluido == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurante não encontrado"
            )
    finally:
        sessao_banco.close()

    return None