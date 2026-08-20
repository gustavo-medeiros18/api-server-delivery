from fastapi import APIRouter
from app.schemas.pedido_schema import PedidoCriacaoSchema
from banco_de_dados import obter_sessao
from app.services import pedido_service

router = APIRouter()

def criar(dados_entrada: PedidoCriacaoSchema):
    sessao_banco = obter_sessao()

    pedido_criado = pedido_service.criar(sessao_banco, dados_entrada)
    return pedido_criado