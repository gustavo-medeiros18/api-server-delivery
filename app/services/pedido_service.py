from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.pedido_schema import PedidoCriacaoSchema, PedidoAlteracao
from app.models.pedido_model import PedidoModel
from app.dao import pedido_dao, restaurante_dao

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

def buscar_pedido_por_id(
    banco: Session,
    pedido_id: int
):
    pedido_encontrado = pedido_dao.buscar_pedido(banco, pedido_id)
    return pedido_encontrado

def atualizar_pedido(
    banco: Session,
    pedido_id: int,
    dados_pedido: PedidoAlteracao
):
    pedido_existente = buscar_pedido_por_id(
        banco,
        pedido_id
    )

    if not pedido_existente:
        return None

    if dados_pedido.restaurante_id != None:
        restaurante = restaurante_dao.buscar_restaurante(
            banco,
            dados_pedido.restaurante_id
        )

        if not restaurante:
            raise HTTPException(
                status_code=404,
                detail="Restaurante não encontrado"
            )

    dados_atualizacao = dados_pedido.model_dump(
        exclude_unset=True
    )

    pedido_atualizado = pedido_dao.atualizar(banco, pedido_existente, dados_atualizacao)
    return pedido_atualizado

def excluir(sessao_banco: Session, id_pedido_excluir: int):
    pedido_encontrado = pedido_dao.buscar_pedido(sessao_banco, id_pedido_excluir)

    if pedido_encontrado == None:
        return None

    pedido_dao.excluir(sessao_banco, pedido_encontrado)
    return pedido_encontrado