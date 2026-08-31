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

def listar(sessao_banco: Session):
    lista_pedidos = pedido_dao.listar(sessao_banco)
    return lista_pedidos

def excluir(sessao_banco: Session, id_pedido_excluir: int):
    pedido_encontrado = pedido_dao.buscar_pedido(sessao_banco, id_pedido_excluir)

    if pedido_encontrado == None:
        return None

    pedido_dao.excluir(sessao_banco, pedido_encontrado)
    return pedido_encontrado