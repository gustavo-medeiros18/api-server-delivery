from fastapi import APIRouter, status
from app.schemas.pedido_schema import PedidoCriacaoSchema, PedidoRespostaSchema
from app.banco_de_dados import obter_sessao
from app.services import pedido_service

router = APIRouter()

@router.post(
    "/pedidos",
    status_code=status.HTTP_201_CREATED,
    response_model=PedidoRespostaSchema
)
def criar(dados_entrada: PedidoCriacaoSchema):
    sessao_banco = obter_sessao()

    pedido_criado = pedido_service.criar(sessao_banco, dados_entrada)
    return pedido_criado