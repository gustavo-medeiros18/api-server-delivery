from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.pedido_model import PedidoModel
from app.schemas.pedido_schema import PedidoCriacaoSchema
from app.dao import pedido_dao

def criar(sessao_banco: Session, dados_pedido: PedidoCriacaoSchema):
    modelo_dados = PedidoModel(
        prato_principal=dados_pedido.prato_principal,
        acompanhamento=dados_pedido.acompanhamento,
        observacao=dados_pedido.observacao,
        valor=dados_pedido.valor,
        id_restaurante=dados_pedido.id_restaurante
    )

    pedido_criado = pedido_dao.criar(sessao_banco, modelo_dados)
    return pedido_criado
