from fastapi import APIRouter, status, HTTPException
from app.schemas.pedido_schema import PedidoCriacaoSchema, PedidoRespostaSchema
from app.banco_de_dados import obter_sessao
from app.services import pedido_service, restaurante_service

router = APIRouter()

@router.post(
    "/pedidos",
    status_code=status.HTTP_201_CREATED,
    response_model=PedidoRespostaSchema
)
def criar(dados_entrada: PedidoCriacaoSchema):
    sessao_banco = obter_sessao()

    try:
        restaurante_encontrado = restaurante_service.buscar_restaurante(
            sessao_banco,
            dados_entrada.id_restaurante
        )

        if restaurante_encontrado == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurante não encontrado"
            )

        pedido_criado = pedido_service.criar(sessao_banco, dados_entrada)
    finally:
        sessao_banco.close()
    
    return pedido_criado