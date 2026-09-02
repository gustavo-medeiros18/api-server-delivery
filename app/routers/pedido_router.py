from fastapi import APIRouter, status, HTTPException
from app.schemas.pedido_schema import PedidoAlteracao, PedidoCriacaoSchema, PedidoRespostaSchema
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

@router.get(
    "/pedidos",
    response_model=list[PedidoRespostaSchema]
)
def listar():
    sessao_banco = obter_sessao()

    try:
        lista_pedidos = pedido_service.listar(sessao_banco)
    finally:
        sessao_banco.close()
    
    return lista_pedidos

@router.patch(
    "/pedidos/{pedido_id}",
    response_model=PedidoRespostaSchema
)
def atualizar(
    pedido_id: int,
    pedido: PedidoAlteracao
):
    banco = obter_sessao()

    try:
        pedido_atualizado = pedido_service.atualizar_pedido(
            banco,
            pedido_id,
            pedido
        )

        if not pedido_atualizado:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado"
            )

        return pedido_atualizado
    finally:
        banco.close()

@router.delete(
    "/pedidos/{id_pedido_excluir}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir(id_pedido_excluir: int):
    sessao_banco = obter_sessao()

    try:
        pedido_excluido = pedido_service.excluir(sessao_banco, id_pedido_excluir)

        if pedido_excluido == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pedido não encontrado"
            )
    finally:
        sessao_banco.close()
        
    return None