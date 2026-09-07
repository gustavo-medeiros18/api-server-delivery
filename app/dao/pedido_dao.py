from sqlalchemy.orm import Session
from app.models.pedido_model import PedidoModel

def criar(sessao_banco: Session, modelo_dados: PedidoModel):
    # modelo_dados representa o novo pedido
    # que está sendo persistido no banco de
    # dados.

    sessao_banco.add(modelo_dados)
    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados

def buscar_pedido(sessao_banco: Session, id_pedido_encontrar: int):
    consulta = sessao_banco.query(PedidoModel)
    consulta_com_filtro = consulta.filter(PedidoModel.id == id_pedido_encontrar)

    # modelo_dados armazena o pedido
    # que foi encontrado ou nada (None)
    modelo_dados = consulta_com_filtro.one_or_none()
    return modelo_dados

def listar(sessao_banco: Session):
    consulta = sessao_banco.query(PedidoModel)

    # modelo_dados armazena uma lista
    # com todos os pedidos dentro
    # da tabela.
    modelo_dados = consulta.all()
    return modelo_dados

def alterar(
    sessao_banco: Session,
    modelo_dados: PedidoModel,
    dados_atualizacao_pedido: dict
):
    itens_dicionario = dados_atualizacao_pedido.items()

    for campo, valor in itens_dicionario:
        setattr(modelo_dados, campo, valor)

    # modelo_dados representa o pedido cujos
    # dados estão sendo alterados.
    sessao_banco.commit()
    sessao_banco.refresh(modelo_dados)

    return modelo_dados

def excluir(sessao_banco: Session, modelo_dados: PedidoModel):
    # modelo_dados representa o pedido
    # que se deseja excluir.
    sessao_banco.delete(modelo_dados)
    sessao_banco.commit()