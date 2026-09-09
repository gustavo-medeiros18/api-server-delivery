from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.pedido_schema import PedidoCriacaoSchema, PedidoAlteracaoSchema
from app.models.pedido_model import PedidoModel
from app.dao import pedido_dao, restaurante_dao
from fastapi import HTTPException, status

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

def alterar(
    sessao_banco: Session,
    id_pedido_alterar: int, 
    dados_atualizacao_pedido: PedidoAlteracaoSchema
):
    pedido_encontrado = pedido_dao.buscar_pedido(sessao_banco, id_pedido_alterar)

    if pedido_encontrado == None:
        return None

    id_restaurante_encontrar = dados_atualizacao_pedido.id_restaurante

    if id_restaurante_encontrar != None:
        restaurante_encontrado = restaurante_dao.buscar_restaurante(
            sessao_banco,
            id_restaurante_encontrar
        )

        if restaurante_encontrado == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurante não encontrado"
            )

    dicionario_atualizacao = dados_atualizacao_pedido.model_dump(exclude_unset=True)

    pedido_atualizado = pedido_dao.alterar(
        sessao_banco,
        pedido_encontrado,
        dicionario_atualizacao
    )

    return pedido_atualizado

def excluir(sessao_banco: Session, id_pedido_excluir: int):
    pedido_encontrado = pedido_dao.buscar_pedido(sessao_banco, id_pedido_excluir)

    if pedido_encontrado == None:
        return None

    pedido_dao.excluir(sessao_banco, pedido_encontrado)
    return pedido_encontrado