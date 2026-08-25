from sqlalchemy.orm import Session
from app.schemas.pedido_schema import PedidoCriacaoSchema
from app.models.pedido_model import PedidoModel
from app.dao import pedido_dao

def criar(sessao_banco: Session, dados_entrada: PedidoCriacaoSchema):
    modelo_dados = PedidoModel(
        prato_principal=dados_entrada.prato_principal,
        acompanhamento=dados_entrada.acompanhamento,
        observacao=dados_entrada.observacao,
        valor=dados_entrada.valor,
        id_restaurante=dados_entrada.id_restaurante
    )

    pedido_criado = pedido_dao.criar(sessao_banco, modelo_dados)
    return pedido_criado